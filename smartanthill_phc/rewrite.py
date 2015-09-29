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


def rewrite_code(compiler, root, token_stream, struct_name):
    '''
    Rewrites code tree
    '''
    rewriter = TokenStreamRewriter(token_stream)
    visitor = _RewriteVisitor(compiler, rewriter, struct_name)
    visit_node(visitor, root)

    text = rewriter.getText()

    compiler.check_stage('rewrite')

    return text


def write_header(compiler, root, token_stream, struct_name, include_guard):
    '''
    Rewrites code tree
    '''
    nb = root.get_scope(NonBlockingData)
    text = _write_header_file(token_stream, struct_name, include_guard, nb)

    compiler.check_stage('header')

    return text


_header_file_banner = u"/* Add copyright banner here */\n\n\n"


def _write_header_file(token_stream, struct_name, include_guard, nb):

    txt = _header_file_banner

    txt += u"#if !defined %s\n" % include_guard
    txt += u"#define %s\n\n" % include_guard

    txt += u"#include <stdint.h>\n\n\n"

    txt += u"typedef struct _%s {\n" % struct_name
    txt += u"uint8_t sa_next;\n"

    for each in nb.refs_moved_var_decls:
        start = each.ctx.declarationSpecifier(0).start
        stop = each.ctx.initDeclaratorList().initDeclarator(
            0).declarator().stop

        txt += token_stream.getText((start.tokenIndex, stop.tokenIndex))
        txt += u";\n"

    txt += u"} %s;\n\n" % struct_name
    txt += u"#endif // %s\n" % include_guard

    return txt


class _RewriteVisitor(NodeVisitor):

    '''
    Visitor class for plugin rewrite
    '''

    def __init__(self, compiler, writer, type_name):
        '''
        Constructor
        '''
        self._c = compiler
        self._w = writer
        self._tn = type_name
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
        pass

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
                    u"sa_state->%s" % node.txt_name)
            else:
                self._w.deleteTokens(node.ctx.start, node.ctx.stop)

        if node.child_initializer is not None:
            self._visit_expression(node.child_initializer)

    def visit_ExpressionStmtNode(self, node):
        self._visit_expression(node.child_expression)

    def visit_BlockingCallStmtNode(self, node):

        self._w.replaceToken(
            node.child_expression.ctx.Identifier().symbol,
            u"%s_non_blocking" % node.child_expression.txt_name)

        self._visit_expression(node.child_expression)

    def visit_ReturnStmtNode(self, node):
        if node.child_expression is not None:
            self._visit_expression(node.child_expression)

        self._w.insertBeforeToken(
            node.ctx.start, u"sa_state->sa_next = 0;")

    def visit_IfElseStmtNode(self, node):
        self._visit_expression(node.child_expression)
        visit_node(self, node.child_if_branch)
        if node.child_else_branch is not None:
            visit_node(self, node.child_else_branch)

    def visit_StateMachineStmtNode(self, node):

        assert len(node.childs_states) != 0

        txt = u"\n\nswitch(sa_state->sa_next) {"
        for each in node.childs_states:

            txt += u"\ncase %s: goto label_%s;" % (each.txt_id, each.txt_id)
#            visit_node(self, each.child_statement_list)

        txt += u"\ndefault: assert(0);"
        txt += u"\n}"
        txt += u"\nlabel_0:;"  # mb: add semicolon after label
        if node.ctx.line is not None:
            txt += u"\n//#line %s\n" % node.ctx.line

        self._w.insertAfterToken(node.ctx, txt)

    def visit_NextStateStmtNode(self, node):

        nxt = node.ref_next_state.txt_id
        txt = u"\nsa_state->sa_next = %s;" % nxt
        txt += u"\nreturn 1; /* WAIT */"
        txt += u"\nlabel_%s:;" % nxt  # mb: add semicolon after label
        if node.ctx.stop.line is not None:
            txt += u"\n//#line %s\n" % node.ctx.stop.line

        self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_InitStateStmtNode(self, node):

        txt = u"\n%s* sa_state = (%s*)%s;" % (self._tn, self._tn, node.txt_arg)
        txt += u"\nsa_state->sa_next = 0;"
        self._w.insertAfterToken(node.ctx, txt)

    def visit_StateDataCastStmtNode(self, node):
        self._w.insertAfterToken(
            node.ctx,
            u"\n%s* sa_state = (%s*)%s;" % (self._tn, self._tn, node.txt_arg))

    def visit_DontCareExprNode(self, node):
        for each in node.childs_expressions:
            visit_node(self, each)

    def visit_TypeCastExprNode(self, node):
        visit_node(self, node.child_expression)

    def visit_LiteralExprNode(self, node):
        # nothing to do here
        pass

    def visit_VariableExprNode(self, node):

        if node.ref_decl is not None:
            if self._nb.is_moved_var_decl(node.ref_decl):
                self._w.replaceToken(
                    node.ctx.symbol,
                    u"(sa_state->%s)" % node.txt_name)

    def visit_FunctionCallExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_ArgumentListNode(self, node):
        for each in node.childs_arguments:
            visit_node(self, each)
