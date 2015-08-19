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

from antlr4.Token import CommonToken
from antlr4.tree.Tree import TerminalNodeImpl

from smartanthill_phc.TokenStreamRewriter import TokenStreamRewriter
from smartanthill_phc.common.visitor import NodeVisitor, visit_node


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
        visit_node(self, node.child_source)

    def visit_PluginSourceNode(self, node):
        visit_node(self, node.child_declaration_list)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            visit_node(self, each)

    def visit_FunctionDeclNode(self, node):
        visit_node(self, node.child_statement_list)

    def visit_StmtListNode(self, node):
        for each in node.childs_statements:
            visit_node(self, each)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):
        if node.child_initializer is not None:
            self._visit_expression(node.child_initializer)

    def visit_ExpressionStmtNode(self, node):
        self._visit_expression(node.child_expression)

    def visit_BlockingCallStmtNode(self, node):
        self._visit_expression(node.child_expression)

    def visit_ReturnStmtNode(self, node):
        if node.child_expression is not None:
            self._visit_expression(node.child_expression)

    def visit_StateMachineStmtNode(self, node):

        assert len(node.childs_states) != 0

        b = node.childs_states[
            0].child_statement_list.childs_statements[0].ctx.start

        self._w.insertBeforeToken(b, u"switch(var) {")
        for each in node.childs_states:
            l = each.child_statement_list.childs_statements[0].ctx.start
            self._w.insertBeforeToken(l, u"case %s:" % each.txt_id)
            visit_node(self, each.child_statement_list)

        e = node.childs_states[
            -1].child_statement_list.childs_statements[-1].ctx.stop

        self._w.insertAfterToken(e, u"} assert(false);")

    def visit_NextStateStmtNode(self, node):

        if node.ref_next_state is None:
            self._w.insertBeforeToken(
                node.ctx.start,
                u"/* next state is 'initial' */")
        else:
            self._w.insertAfterToken(
                node.ctx.stop,
                u"/* next state is '%s' */ return WAIT;" %
                node.ref_next_state.txt_id)

    def visit_DontCareExprNode(self, node):
        for each in node.childs_expressions:
            visit_node(self, each)

    def visit_VariableExprNode(self, node):

        # pylint: disable=no-self-use
        assert isinstance(node.ctx, TerminalNodeImpl)
        assert isinstance(node.ctx.symbol, CommonToken)

#        self._w.insertBeforeToken(node.ctx.symbol, u"/* before */")

    def visit_FunctionCallExprNode(self, node):

        # pylint: disable=no-self-use
        assert isinstance(node.ctx.Identifier(), TerminalNodeImpl)
        assert isinstance(node.ctx.Identifier().symbol, CommonToken)

#         self._w.replaceToken(
#             node.ctx.Identifier().symbol, u"/* replaced */")

        visit_node(self, node.child_argument_list)

    def visit_ArgumentListNode(self, node):
        pass
        #         for each in node.childs_arguments:
        #             visit_node(self, each)

#        self._w.insertAfterToken(node.ctx.stop, u"/* after */")
