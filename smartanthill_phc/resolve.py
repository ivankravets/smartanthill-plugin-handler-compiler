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

from smartanthill_phc import pointer
from smartanthill_phc.common import errors, lookup
from smartanthill_phc.common.base import OnDemandResolution,\
    TypeDeclNode
from smartanthill_phc.common.compiler import format_location
from smartanthill_phc.common.lookup import RootScope,\
    StatementListScope, FunctionScope, TypeScope
from smartanthill_phc.common.visitor import CodeVisitor, visit_node,\
    NodeWalker


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
    visit_node(visitor, root)

    compiler.check_stage('resolve')

    walker = _ResolutionCheckWalker()
    walker.walk_node(root)


def report_overload_error(compiler, ctx, first_line, args, decls):

    txt = []
    txt.append(format_location(ctx) + first_line)
    txt.append("Arguments:")

    current = '('
    for i in range(len(args)):
        if i != 0:
            current += ','

        current += args[i].to_string()
    current += ')'
    txt.append(current)

    txt.append("Candidates:")
    for each in decls:
        current = '('
        e = each.argument_decl_list.get().declarations
        for i in range(e.get_size()):
            if i != 0:
                current += ','

            current += e.at(i).get().get_type().to_string()
        current += ')'
        txt.append(current)

    for each in txt:
        print each

    compiler.raise_error()


def overload_filter(compiler, ctx, args, candidates):
    '''
    From a list declarations, returns one that can match the arguments,
    if no candidate is found, reports error an raises
    '''
    exact_match = []
    cast_match = {}
    min_cast = 0
    for current in candidates:
        r = current.can_match_arguments(compiler, ctx, args)

        if r == TypeDeclNode.NO_MATCH:
            pass
        elif r == TypeDeclNode.EXACT_MATCH:
            exact_match.append(current)
        else:
            if r not in cast_match:
                cast_match[r] = []
            cast_match[r].append(current)
            if min_cast == 0 or r < min_cast:
                min_cast = r

    if len(exact_match) == 0:
        if min_cast == 0:
            report_overload_error(
                compiler, ctx, "None of candidates can match the arguments",
                args, candidates)
        elif len(cast_match[min_cast]) == 1:
            return cast_match[min_cast][0]
        else:
            report_overload_error(
                compiler, ctx, "More than a candidate can match the arguments",
                args, candidates)
    elif len(exact_match) == 1:
        return exact_match[0]
    else:
        report_overload_error(
            compiler, ctx, "More than a candidate match the arguments",
            args, candidates)


def expression_type_match(compiler, lhs_type, expr_type, box):
    '''
    Helper function for expression type matching
    If no match possible just returns false
    If exact match returns true
    If can match but needs cast, inserts cast and returns true
    '''

    if expr_type == lhs_type:
        return True
    elif lhs_type.can_cast_from(expr_type):
        lhs_type.insert_cast_from(compiler, expr_type, box)
        return True
    else:
        return False


class _ResolutionCheckWalker(NodeWalker):

    '''
    Walker class that will check all reachable nodes do not raise when
    get_type() is called and that something is returned
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(_ResolutionCheckWalker, self).__init__()

    def walk_node(self, node, box=None):
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
        except errors.ResolutionCycleError:
            print "ResolutionCycleError"
            print "Node   : %s" % type(node).__name__
#            assert False
        except errors.UnresolvedError:
            print "UnresolvedError"
            print "Node   : %s" % type(node).__name__
#            assert False
        except errors.PreviousResolutionError:
            print "PreviousResolutionError"
            print "Node   : %s" % type(node).__name__
#            assert False

        self.walk_childs(node)


def _get_internal_type(txt_name, node):
    '''
    Type look up at RootScope that is known to success
    '''
    t = node.get_scope(RootScope).types.lookup(txt_name)
    assert t is not None
    return t


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

    def visit(self, box):
        '''
        Override base visit function, to keep stack of node being resolved, and
        check for resolution loops
        '''
        if box.get() in self._stack:
            raise errors.ResolutionCycleError()

        self._stack.append(box.get())
        res = super(_ResolveVisitor, self).visit(box)
        self._stack.pop()
        return res

    def on_demand_resolve(self, node):
        '''
        Calls to resolve on demand, on some declaration after look up
        This resolution in not result of natural tree order
        '''
        assert isinstance(node, (OnDemandResolution, TypeDeclNode))
        visit_node(self, node)
        return node.get_type()

    def visit_RootNode(self, node):

        # first built-ins
        self.visit(node.builtins)
        self.visit(node.manifest)

        if not node.source.is_none():
            self.visit(node.source)

    def visit_PluginSourceNode(self, node):
        self.visit_childs(node)

    def visit_PluginManifestNode(self, node):
        self.visit_childs(node)

    def visit_TypeDeclNode(self, node):

        if node.begin_resolution():
            sc = node.get_parent_scope(TypeScope)
            if sc is None:
                sc = node.get_scope(RootScope)
                assert sc is not None

            sc.types.add(self._c, node.txt_name, node)

            self.visit_childs(node)
            node.set_type(node)

    def visit_OperatorDeclNode(self, node):
        if node.begin_resolution():

            sc = node.get_scope(TypeScope)
            if sc is None:
                sc = node.get_scope(RootScope)
                assert sc is not None

            sc.operators.add(self._c, node.txt_name, node)

            self.visit_childs(node)
            node.set_type(node.return_type.get().get_type())

    def visit_TrivialCastRuleNode(self, node):
        self.visit_childs(node)

    def visit_StmtListNode(self, node):
        self.visit_stmt_list(node)

        has_flow_stmt = False
        for each in node.statements:
            # state _StatementsSplitterVisitor needs nice flow statements
            # so no unreachable statements allowed
            if has_flow_stmt:
                self._c.report_error(each.ctx, "Unreachable statement")
            if each.get().is_closed_stmt():
                has_flow_stmt = True

    def visit_DeclarationListNode(self, node):
        self.visit_childs(node)

    def visit_PreprocessorDirectiveNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        pass

    def visit_ConstantDefineNode(self, node):
        if node.begin_resolution():
            node.get_scope(RootScope).constants.add(
                self._c, node.txt_name, node)

            t = self.visit(node.expression)
            node.set_type(t)

    def visit_ArgumentDeclNode(self, node):
        if node.begin_resolution():
            if node.txt_name is not None:
                sc = node.get_scope(FunctionScope)
                # function declaration without implementation don't have scope
                if sc is not None:
                    sc.arguments.add(self._c, node.txt_name, node)

            self.visit_childs(node)
            node.set_type(node.argument_type.get().get_type())

    def visit_VariableDeclarationStmtNode(self, node):

        if node.begin_resolution():

            node.get_scope(StatementListScope).variables.add(
                self._c, node.txt_name, node)

            self.visit_childs(node)

            node.set_type(node.declaration_type.get().get_type())

    def visit_AttributeDeclarationNode(self, node):

        if node.begin_resolution():

            node.get_scope(TypeScope).attributes.add(
                self._c, node.txt_name, node)

            self.visit_childs(node)

            node.set_type(node.declaration_type.get().get_type())

    def visit_FunctionDefinitionNode(self, node):
        self.visit_childs(node)

    def visit_FunctionDeclNode(self, node):

        if node.begin_resolution():

            node.get_scope(RootScope).functions.add(
                self._c, node.txt_name, node)
            self.visit_childs(node)

            node.set_type(node.return_type.get().get_type())

    def visit_TypedefStmtNode(self, node):

        if node.begin_resolution():

            stmt_scope = node.get_scope(StatementListScope)
            if stmt_scope is not None:
                stmt_scope.typedefs.add(self._c, node.txt_name, node)
            else:
                node.get_scope(RootScope).typedefs.add(
                    self._c, node.txt_name, node)

            self.visit_childs(node)

            node.set_type(node.typedef_type.get().get_type())

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

    def visit_ParserStmtNode(self, node):
        self.visit_childs(node)

    def visit_ComposerStmtNode(self, node):
        self.visit_childs(node)

    def visit_RefTypeNode(self, node):

        # pylint: disable=no-self-use
        assert node.get_type() is not None

    def visit_SimpleTypeNode(self, node):

        root_scope = node.get_scope(RootScope)
        stmt_scope = node.get_scope(StatementListScope)
        t = lookup.lookup_type(node.txt_name, root_scope, stmt_scope)
        if t is None:
            self._c.report_eror(
                node.ctx, "Unresolved type '%s'" % node.txt_name)
            self._c.raise_error()

        node.set_type(t)

    def visit_InvalidTypeNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        assert False

    def visit_PointerTypeNode(self, node):
        self.visit_childs(node)

        t = node.pointed_type.get().get_type()
        ptr = pointer.make_pointer_of(self._c, t)
        d = self.on_demand_resolve(ptr)
        node.set_type(d)

    def visit_FunctionCallExprNode(self, node, box):

        args = self.resolve_ArgumentListNode(node.argument_list.get())

        candidates = node.get_scope(
            RootScope).functions.lookup(node.txt_name)

        if candidates is None or len(candidates) == 0:

            self._c.report_error(
                node.ctx, "Unresolved call '%s'" % node.txt_name)
            self._c.raise_error()

        d = overload_filter(self._c, node.ctx, args, candidates)

        d.make_arguments_match(
            self._c, node.ctx, args, node.argument_list.get().arguments)
        node.ref_declaration = d
        t = self.on_demand_resolve(node.ref_declaration)
        return t

    def visit_IntegerLiteralExprNode(self, node, box):
        # pylint: disable=no-self-use
        t = _get_internal_type('sa_int_literal', node)
        return t

    def visit_BooleanLiteralExprNode(self, node, box):
        # pylint: disable=no-self-use
        t = _get_internal_type('sa_bool_literal', node)
        return t

    def visit_VariableExprNode(self, node, box):

        sc = node.get_scope(StatementListScope)

        d = lookup.lookup_variable(node.txt_name, sc)
        if d is not None:
            node.ref_declaration = d
            t = self.on_demand_resolve(node.ref_declaration)
        else:
            # Try find as function argument
            sc = node.get_scope(FunctionScope)
            d = sc.arguments.lookup(node.txt_name)
            if d is not None:
                node.ref_declaration = d
                t = self.on_demand_resolve(node.ref_declaration)
            else:
                # Try find as global define
                sc = node.get_scope(RootScope)
                d = sc.constants.lookup(node.txt_name)
                if d is not None:
                    node.ref_declaration = d
                    t = self.on_demand_resolve(node.ref_declaration)
                else:
                    self._c.report_error(
                        node.ctx, "Unresolved variable '%s'" % node.txt_name)
                    self._c.raise_error()

        return t

    def visit_AssignmentExprNode(self, node, box):

        t = self.visit(node.left_expression)
        r = self.visit(node.right_expression)

        if not expression_type_match(self._c, t, r, node.right_expression):
            self._c.report_error(node.ctx, "Type mismatch on assignment")

        # allow chained assignment
        return t

    def visit_ConditionalExprNode(self, node, box):

        self.visit(node.condition_expression)
        self.visit(node.true_expression)
        self.visit(node.false_expression)

        return _get_internal_type('_zc_dont_care', node)

    def visit_OperatorExprNode(self, node, box):

        args = self.resolve_ArgumentListNode(node.argument_list.get())
        candidates = node.get_scope(
            RootScope).operators.lookup(node.txt_operator)

        if candidates is None or len(candidates) == 0:
            self._c.report_error(
                node.ctx, "Unresolved operator '%s'" % node.txt_operator)
            self._c.raise_error()

        d = overload_filter(
            self._c, node.ctx, args,
            candidates)
        d.make_arguments_match(
            self._c, node.ctx, args, node.argument_list.get().arguments)
        node.ref_declaration = d
        t = self.on_demand_resolve(node.ref_declaration)
        return t


#         r = d.static_evaluate(self._c, node.child_argument_list)
#         if r is not None:
#             self.replace_expression(r)

    def visit_MemberOperatorExprNode(self, node, box):

        args = self.resolve_ArgumentListNode(node.argument_list.get())

        ref_type = self.visit(node.expression)

        candidates = ref_type.get_scope(
            TypeScope).operators.lookup(node.txt_operator)

        if candidates is None or len(candidates) == 0:
            self._c.report_error(
                node.ctx, "Unresolved operator '%s'" % node.txt_operator)
            self._c.raise_error()

        d = overload_filter(
            self._c, node.ctx, args, candidates)

        d.make_arguments_match(
            self._c, node.ctx, args, node.argument_list.get().arguments)

        node.ref_declaration = d
        t = self.on_demand_resolve(node.ref_declaration)
        return t

    def visit_PointerExprNode(self, node, box):

        ref_type = self.visit(node.expression)
        p = pointer.get_pointed_by(self._c, node.ctx, ref_type)
        return p

    def visit_AddressOfExprNode(self, node, box):

        ref_type = self.visit(node.expression)
        # TODO check valid
        p = pointer.make_pointer_of(self._c, ref_type)
        return p

    def visit_MemberAccessExprNode(self, node, box):

        left = self.visit(node.expression)

        if node.bool_arrow:
            left = pointer.get_pointed_by(self._c, node.ctx, left)

        node.ref_declaration = left.get_scope(
            TypeScope).attributes.lookup(node.txt_name)
        if node.ref_declaration is not None:
            t = self.on_demand_resolve(node.ref_declaration)
        else:
            self._c.report_error(node.ctx, "Member '%s' not found on '%s'" % (
                node.txt_name, left.txt_name))
            self._c.raise_error()

        return t

    def visit_CastExprNode(self, node, box):

        self.visit_childs(node)
        return node.cast_type.get().get_type()

    def resolve_ArgumentListNode(self, node):

        result = []
        for each in node.arguments:
            t = self.visit(each)
            result.append(t)
        return result
