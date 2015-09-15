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

from smartanthill_phc.TokenStreamRewriter import TokenStreamRewriter
from smartanthill_phc.common.visitor import NodeVisitor, visit_node
from smartanthill_phc.root import NonBlockingData


def rewrite_code(compiler, root, token_stream):
    '''
    Rewrites code tree
    '''
    rewriter = TokenStreamRewriter(token_stream)
    visitor = _RewriteVisitor(compiler, rewriter)
    visit_node(visitor, root)

    text = rewriter.getText()

    compiler.check_stage('rewrite')

    return text


class _RewriteVisitor(NodeVisitor):

    '''
    Visitor class for plugin code write
    '''

    def __init__(self, compiler, writer):
        '''
        Constructor
        '''
        self._c = compiler
        self._w = writer
        self._nb = None
        self._txt_lines = []

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._c.report_error(
            node.ctx, "Statement rewrite not supported")

    def _add_line(self, txt_line):
        self._txt_lines.append(txt_line)

    def _rewrite(self, start, stop):
        self._w.replaceTokens(start, stop, u'\n'.join(self._txt_lines))
        self._txt_lines = []

    def _expr(self, expr):
        if expr.has_parenthesis:
            return u"(%s)" % visit_node(self, expr)
        else:
            return visit_node(self, expr)

    def _args(self, arg_list):
        return visit_node(self, arg_list)

    def _type(self, node, name):
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument

        return u"void"

    def visit_RootNode(self, node):
        self._nb = node.get_scope(NonBlockingData)
        visit_node(self, node.child_source)

    def visit_PluginSourceNode(self, node):
        visit_node(self, node.child_declaration_list)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            visit_node(self, each)

    def visit_StateDataStuctDeclarationNode(self, node):

        #        tk = node.ctx.start
        self._add_line(u"struct _sa_state_data_t {")

        for each in self._nb.refs_moved_var_decls:
            start = each.ctx.declarationSpecifier(0).start
            stop = each.ctx.initDeclaratorList().initDeclarator(
                0).declarator().stop

            txt = self._w.tokens.getText((start.tokenIndex, stop.tokenIndex))
            self._add_line(u"%s;" % txt)

        self._add_line(u"};")

        self._rewrite(node.ctx.start, node.ctx.stop)

    def visit_FunctionDeclNode(self, node):
        visit_node(self, node.child_statement_list)
        ctx = node.child_statement_list.ctx
        self._rewrite(ctx.start, ctx.stop)

    def visit_StmtListNode(self, node):

        self._add_line(u"{")
        for each in node.childs_statements:
            visit_node(self, each)
        self._add_line(u"}")

    def visit_NopStmtNode(self, node):
        # pylint: disable=unused-argument
        self._add_line(u";")

    def visit_VariableDeclarationStmtNode(self, node):

        if self._nb.is_moved_var_decl(node):

            decl_list = node.ctx.initDeclaratorList()
            assert decl_list is not None
            assert len(decl_list.initDeclarator()) == 1

            if node.child_initializer is not None:
                self._add_line(  # node.ctx.start,
                    u"_sa_state->%s = %s;" %
                    (node.txt_name, self._expr(node.child_initializer)))
        else:
            self._add_line(  # node.ctx.start,
                u"%s = %s;" %
                (self._type(u"", node.txt_name),
                 self._expr(node.child_initializer)))

    def visit_ExpressionStmtNode(self, node):
        self._add_line(u"%s;" % self._expr(node.child_expression))

    def visit_BlockingCallStmtNode(self, node):
        self._add_line(u"%s;" % self._expr(node.child_expression))

    def visit_ReturnStmtNode(self, node):
        if node.child_expression is not None:
            self._add_line(u"return %s;" %
                           self._expr(node.child_expression))
        else:
            self._add_line(u"return;")

    def visit_IfElseStmtNode(self, node):
        self._add_line(u"if(%s)" % self._expr(node.child_expression))
        visit_node(self, node.child_if_branch)
        if node.child_else_branch is not None:
            self._add_line(u"else")
            visit_node(self, node.child_else_branch)

    def visit_StateMachineStmtNode(self, node):

        assert len(node.childs_states) != 0

        self._add_line(u"switch(_sa_state->_sa_next) {")
        for each in node.childs_states:
            self._add_line(u"case %s:" % each.txt_id)
            visit_node(self, each.child_statement_list)

        self._add_line(u"}")
        self._add_line(u"assert(false);")

    def visit_NextStateStmtNode(self, node):

        txt = 'WAIT' if node.flag_wait else 'NEXT'
        self._add_line(
            u"_sa_state->_sa_next = %s; return %s;" %
            (node.ref_next_state.txt_id, txt))

    def visit_InitStateStmtNode(self, node):
        # pylint: disable=unused-argument
        self._add_line(u"_sa_state->_sa_next = 0;")

    def visit_StateDataCastStmtNode(self, node):
        self._add_line(
            u"_sa_state_data_t* _sa_state = (_sa_state_data_t*)%s;" %
            node.txt_arg)

    def visit_DontCareExprNode(self, node):
        ops = []
        for each in node.childs_expressions:
            ops.append(self._expr(each))

        return u"(op)".join(ops)

    def visit_TypeCastExprNode(self, node):
        return u"(%s)%s" % (self._type(u"", u""),
                            self._expr(node.child_expression))

    def visit_VariableExprNode(self, node):

        if node.ref_decl is not None and\
                self._nb.is_moved_var_decl(node.ref_decl):
            return u"(_sa_state->%s)" % node.txt_name
        else:
            return node.txt_name

    def visit_FunctionCallExprNode(self, node):
        return u"%s(%s)" % (node.txt_name,
                            self._args(node.child_argument_list))

    def visit_NumberLiteralExprNode(self, node):
        # pylint: disable=no-self-use
        return node.txt_literal

    def visit_ArgumentListNode(self, node):

        args = []
        for each in node.childs_arguments:
            args.append(self._expr(each))

        return u','.join(args)
