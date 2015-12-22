# Copyright (C) 2015 OLogN Technologies AG
#
# This source file is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from smartanthill_phc.common import errors
from smartanthill_phc.common.base import ResolutionHelper,\
    expression_type_match, TypeDeclNode
from smartanthill_phc.common.lookup import lookup_type, RootScope,\
    StatementListScope, ReturnStmtScope, FunctionScope
from smartanthill_phc.common.visitor import CodeVisitor, visit_node,\
    NodeWalker, walk_node_childs


def resolve_tree(compiler, root):
    '''
    Process a syntax tree, doing all lookup tables, resolution,
    and type checks required
    After this function the tree is fully resolved and ready for intermediate
    code generation
    Resolution of the tree may trigger node replacements,
    and other modifications of the tree, as semantic meaning is needed
    '''

    visitor = _ResolveVisitor(compiler)
    visitor.visit(root)

    compiler.check_stage('resolve')

    walker = _ResolutionCheckWalker()
    walker.walk_node(root)


class _ResolutionCheckWalker(NodeWalker):

    '''
    Walker class that will check all reachable nodes do not raise when
    get_type() is called and that something is returned
    '''

    def walk_node(self, node):
        assert node
        try:
            m = getattr(node, 'get_type')
            if m:
                t = m()
                if not t:
                    print type(node)
                    assert False
        except AttributeError:
            pass

        walk_node_childs(self, node)


class _ResolveVisitor(CodeVisitor):
    '''
    Walk and visit the node tree doing resolution
    '''

    def __init__(self, compiler):
        '''
        Constructor
        '''
        super(_ResolveVisitor, self).__init__()
        self._c = compiler
        self._stack = []

        # easier access to common used types
        self._zc_dont_care = None
        self._void = None

    def visit(self, node):
        '''
        Override base visit function, to keep stack of node being resolved, and
        check for resolution loops
        '''
        if node in self._stack:
            raise errors.ResolutionCycleError()

        self._stack.append(node)
        visit_node(self, node)
        self._stack.pop()

    def on_demand_resolve(self, node):
        '''
        Calls to resolve on demand, on some declaration after look up
        This resolution in not result of natural tree order
        '''
        assert isinstance(node, (ResolutionHelper, TypeDeclNode))
        self.visit(node)
        return node.get_type()

    def visit_PluginSourceNode(self, node):
        self.visit(node.child_declaration_list)

    def visit_RootNode(self, node):

        # first built-ins
        self.visit(node.child_builtins)

        sc = node.get_scope(RootScope)
        self._zc_dont_care = sc.get_type('_zc_dont_care')
        self._void = sc.get_type('void')
        assert self._zc_dont_care is not None
        assert self._void is not None

        self.visit(node.child_source)

    def visit_StmtListNode(self, node):
        self.visit_stmt_list(node)

        has_flow_stmt = False
        for each in node.childs_statements:
            # state _StatementsSplitterVisitor needs nice flow statements
            # so no unreachable statements allowed
            if has_flow_stmt:
                self._c.report_error(each.ctx, "Unreachable statement")
            if each.is_closed_stmt():
                has_flow_stmt = True

    def visit_DeclarationListNode(self, node):
        for decl in node.childs_declarations:
            self.visit(decl)

    def visit_ArgumentDeclNode(self, node):
        # pylint: disable=no-self-use
        if node.begin_resolution():
            node.get_scope(FunctionScope).add_argument(
                self._c, node.txt_name, node)

            self.visit(node.child_argument_type)
            node.set_type(node.child_argument_type.get_type())

    def visit_VariableDeclarationStmtNode(self, node):

        if node.begin_resolution():

            node.get_scope(StatementListScope).add_variable(
                self._c, node.txt_name, node)

            self.visit_childs(node)

            node.set_type(node.child_declaration_type.get_type())

    def visit_FunctionDeclNode(self, node):

        if node.begin_resolution():

            node.get_scope(RootScope).add_function(
                self._c, node.txt_name, node)
            self.visit(node.child_return_type)
            self.visit(node.child_argument_decl_list)
            self.visit(node.child_stmt_list)

            node.set_type(node.child_return_type.get_type())

    def visit_TypedefStmtNode(self, node):

        if node.begin_resolution():

            stmt_scope = node.get_scope(StatementListScope)
            if stmt_scope is not None:
                stmt_scope.add_typedef(self._c, node.txt_name, node)
            else:
                node.get_scope(RootScope).add_typedef(
                    self._c, node.txt_name, node)

            self.visit(node.child_type)

            node.set_type(node.child_type.get_type())

    def visit_NopStmtNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        pass

    def visit_ErrorStmtNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        assert False

    def visit_ReturnStmtNode(self, node):

        self.visit_childs(node)

        node.get_scope(ReturnStmtScope).add_return_stmt(node)

    def visit_ExpressionStmtNode(self, node):

        self.visit_childs(node)

    def visit_IfElseStmtNode(self, node):
        self.visit_childs(node)

#         t = self.get_scope(RootScope).lookup_type('_zc_boolean')
#
#         if not expression_type_match(compiler, t, self, 'child_expression'):
#             compiler.report_error(
#                 self.ctx, "Condition can not be evaluated to boolean")
        # no need to raise here

    def visit_FunctionCallStmtNode(self, node):
        self.visit_childs(node)

    def visit_WhileStmtNode(self, node):
        self.visit_childs(node)

    def visit_DoWhileStmtNode(self, node):
        self.visit_childs(node)

    def visit_ForStmtNode(self, node):
        self.visit_childs(node)

    def visit_SimpleTypeNode(self, node):
        # pylint: disable=no-self-use

        root_scope = node.get_scope(RootScope)
        stmt_scope = node.get_scope(StatementListScope)
        t = lookup_type(node.txt_name, root_scope, stmt_scope)
        if t is None:
            t = self._zc_dont_care

        node.set_type(t)

    def visit_InvalidTypeNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        assert False

    def visit_PointerTypeNode(self, node):
        self.visit_childs(node)

        t = node.child_pointed_type.get_type()
        # TODO
        node.set_type(t)

    def visit_PapiFunctionDeclNode(self, node):
        node.get_scope(RootScope).add_function(self._c, node.txt_name, node)

    def visit_TypeDeclNode(self, node):
        node.get_scope(RootScope).add_type(self._c, node.txt_name, node)

    def visit_FunctionCallExprNode(self, node):
        self.visit(node.child_argument_list)

        node.ref_declaration = node.get_scope(
            RootScope).lookup_function(node.txt_name)
#         compiler.report_error(
#             self.ctx, "Unresolved function call '%s'" % self.txt_name)

        node.set_type(self._zc_dont_care)

    def visit_MemberAccessExprNode(self, node):

        self.visit_childs(node)

        t = node.child_expression.get_type()
        m = t.lookup_member(self.txt_member)
        if m is None:
            self._c.report_error(node.ctx, "Member '%s' not found" %
                                 node.txt_member)
            self._c.raise_error()

        node.type_decl = t
        node.member_decl = m

        t = self.on_demand_resolve(node.member_decl)
        node.set_type(t)

    def visit_LiteralExprNode(self, node):
        node.set_type(self._zc_dont_care)

    def visit_NumberLiteralExprNode(self, node):
        # pylint: disable=no-self-use
        t = node.get_scope(RootScope).get_type('_zc_number_literal')
        node.set_type(t)

    def visit_BooleanLiteralExprNode(self, node):
        # pylint: disable=no-self-use
        t = node.get_scope(RootScope).get_type('_zc_boolean_literal')
        node.set_type(t)

    def visit_VariableExprNode(self, node):

        sc = node.get_scope(StatementListScope)
        assert sc is not None
        d = sc.lookup_variable(node.txt_name)
        if d is not None:
            node.ref_declaration = d
            t = self.on_demand_resolve(node.ref_declaration)
        else:
            sc = node.get_scope(FunctionScope)
            assert sc is not None
            d = sc.lookup_argument(node.txt_name)
            if d is not None:
                node.ref_declaration = d
                t = self.on_demand_resolve(node.ref_declaration)
            else:
                t = self._zc_dont_care

        node.set_type(t)

    def visit_AssignmentExprNode(self, node):

        self.visit_childs(node)

        sc = node.get_scope(StatementListScope)
        decl = sc.lookup_variable(node.txt_name)
        if decl is None:
            self._c.report_error(
                node.ctx, "Unresolved variable '%s'" % node.txt_name)
            self._c.raise_error()

        node.ref_declaration = decl
        t = self.on_demand_resolve(node.ref_declaration)

        if not expression_type_match(self._c, t, node, 'child_rhs_expression'):
            self._c.report_error(
                node.ctx, "Type mismatch on assignment of variable '%s'" %
                node.txt_name)
            # no need to raise here

        # don't allow chained assignment
        node.set_type(self._void)

    def visit_OperatorExprNode(self, node):

        self.visit(node.child_argument_list)
        candidates = node.get_scope(
            RootScope).lookup_operator(node.txt_operator)

        if len(candidates) == 0:
            if False:
                self._c.report_error(
                    node.ctx, "Unresolved operator '%s'" % node.txt_operator)
                self._c.raise_error()
            else:
                node.set_type(self._zc_dont_care)
                return

        node.ref_decl = node.child_argument_list.overload_filter(
            self._c, candidates)
        node.child_argument_list.make_match(
            self._c, node.ref_declaration.child_parameter_list)

        node.ref_declaration.static_evaluate(self._c, node,
                                             node.child_argument_list)

        t = self.on_demand_resolve(node.ref_declaration)
        node.set_type(t)

    def visit_DontCareExprNode(self, node):

        self.visit(node.child_argument_list)
        node.set_type(self._zc_dont_care)

    def visit_MemberExprNode(self, node):

        self.visit_childs(node)
        left = node.child_expression.get_type()

        if node.bool_arrow:
            pass
        if left == self._zc_dont_care:
            node.set_type(self._zc_dont_care)
            return

        node.ref_declaration = left.lookup_member(node.txt_name)
        if node.ref_declaration is not None:
            t = self.on_demand_resolve(node.ref_declaration)
        else:
            self._c.report_error(node.ctx, "Member '%s' not found on '%s'" % (
                node.txt_name, t.to_string()))
            t = self._zc_dont_care

        node.set_type(t)

    def visit_CastExprNode(self, node):

        self.visit_childs(node)
        node.set_type(node.child_cast_type.get_type())

    def visit_ArgumentListNode(self, node):
        self.visit_expression_list(node, node.childs_arguments)
