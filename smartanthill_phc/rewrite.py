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
from smartanthill_phc.parser import get_declarator_name
from smartanthill_phc.root import NonBlockingData


def rewrite_code(compiler, root, token_stream):
    '''
    Rewrites code tree
    '''
    rewriter = TokenStreamRewriter(token_stream)
    visitor = RewriteVisitor(compiler, rewriter)
    visit_node(visitor, root)

    text = rewriter.getText()

    compiler.check_stage('rewrite')

    return text


class RewriteVisitor(NodeVisitor):

    '''
    Visitor class for plugin rewrite
    '''

    def __init__(self, compiler, writer):
        '''
        Constructor
        '''
        self._c = compiler
        self._w = writer
        self._nb = None

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._c.report_error(
            node.ctx, "Statement rewrite not supported")

    def _visit_expression(self, expr):
        '''
        Helper method to create an expression visitor an call it
        '''
        visit_node(self, expr)

    def visit_RootNode(self, node):
        self._nb = node.get_scope(NonBlockingData)
        visit_node(self, node.child_source)

    def visit_PluginSourceNode(self, node):
        visit_node(self, node.child_declaration_list)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            visit_node(self, each)

    def visit_StateDataStuctDeclarationNode(self, node):

        tk = node.ctx.start
        self._w.insertBeforeToken(tk, u"struct _sa_state_data_t {")

        for each in self._nb.refs_moved_var_decls:
            start = each.ctx.declarationSpecifier(0).start
            stop = each.ctx.initDeclaratorList().initDeclarator(
                0).declarator().stop

            txt = self._w.tokens.getText((start.tokenIndex, stop.tokenIndex))
            self._w.insertBeforeToken(tk, u"%s;" % txt)

        self._w.insertBeforeToken(tk, u"};")

    def visit_FunctionDeclNode(self, node):
        visit_node(self, node.child_statement_list)

    def visit_StmtListNode(self, node):
        for each in node.childs_statements:
            visit_node(self, each)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):

        if self._nb.is_moved_var_decl(node):

            decl_list = node.ctx.initDeclaratorList()
            assert decl_list is not None
            assert len(decl_list.initDeclarator()) == 1
            tk = get_declarator_name(decl_list.initDeclarator(0).declarator())

            if node.child_initializer is not None:
                self._w.replaceTokens(
                    node.ctx.start, tk.symbol,
                    u"_sa_state->%s" % node.txt_name)
            else:
                self._w.deleteTokens(node.ctx.start, node.ctx.stop)

        if node.child_initializer is not None:
            self._visit_expression(node.child_initializer)

    def visit_ExpressionStmtNode(self, node):
        self._visit_expression(node.child_expression)

    def visit_BlockingCallStmtNode(self, node):
        self._visit_expression(node.child_expression)

    def visit_ReturnStmtNode(self, node):
        if node.child_expression is not None:
            self._visit_expression(node.child_expression)

    def visit_IfElseStmtNode(self, node):
        self._visit_expression(node.child_expression)
        visit_node(self, node.child_if_branch)
        if node.child_else_branch is not None:
            visit_node(self, node.child_else_branch)

    def visit_StateMachineStmtNode(self, node):

        assert len(node.childs_states) != 0

        b = node.childs_states[
            0].child_statement_list.childs_statements[0].ctx.start

        self._w.insertBeforeToken(b, u"switch(_sa_state->_sa_next) {")
        for each in node.childs_states:
            l = each.child_statement_list.childs_statements[0].ctx.start
            self._w.insertBeforeToken(l, u"case %s:" % each.txt_id)
            visit_node(self, each.child_statement_list)

        e = node.childs_states[
            -1].child_statement_list.childs_statements[-1].ctx.stop

        self._w.insertAfterToken(e, u"} assert(false);")

    def visit_NextStateStmtNode(self, node):

        self._w.insertAfterToken(
            node.ctx.stop,
            u"_sa_state->_sa_next = %s; return WAIT;" %
            node.ref_next_state.txt_id)

    def visit_InitStateStmtNode(self, node):

        self._w.insertBeforeToken(
            node.ctx.start,
            u"_sa_state->_sa_next = 0;")

    def visit_StateDataCastStmtNode(self, node):
        self._w.insertAfterToken(
            node.ctx,
            u"_sa_state_data_t* _sa_state = (_sa_state_data_t*)%s;" %
            node.txt_arg)

    def visit_JumpStateStmtNode(self, node):
        self._w.insertBeforeToken(
            node.ctx.stop,
            u"/* goto %s; */" % node.ref_next_state.txt_id)

    def visit_DontCareExprNode(self, node):
        for each in node.childs_expressions:
            visit_node(self, each)

    def visit_TypeCastExprNode(self, node):
        visit_node(self, node.child_expression)

    def visit_VariableExprNode(self, node):

        if node.ref_decl is not None:
            if self._nb.is_moved_var_decl(node.ref_decl):
                self._w.replaceToken(
                    node.ctx.symbol,
                    u"(_sa_state->%s)" % node.txt_name)

    def visit_FunctionCallExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_ArgumentListNode(self, node):
        for each in node.childs_arguments:
            visit_node(self, each)
