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

from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl

from smartanthill_phc import banner
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
    Write header file
    '''
    nb = root.get_scope(NonBlockingData)
    text = _write_header_file(token_stream, struct_name, include_guard, nb)

    compiler.check_stage('header')

    return text


def _write_header_file(token_stream, struct_name, include_guard, nb):

    txt = banner.get_copyright_banner()

    txt += "\n"

    txt += "#if !defined %s\n" % include_guard
    txt += "#define %s\n\n" % include_guard

    txt += "#include <stdint.h>\n\n\n"

    txt += "typedef struct _%s {\n" % struct_name

    if nb.has_sub_machines():
        txt += "uint8_t sa_result;\n"

    for each in nb.refs_state_machines:
        txt += "uint8_t %s;\n" % each.get_name()

    for each in nb.refs_moved_var_decls:
        start = each.ctx.declarationSpecifier(0).start
        stop = each.ctx.declarationSpecifier(0).stop

        tk = token_stream.getText((start.tokenIndex, stop.tokenIndex))
        txt += "%s %s;\n" % (str(tk), each.txt_name)

    txt += "} %s;\n\n" % struct_name
    txt += "#endif // %s\n" % include_guard

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
        self._sm = None

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

    def _get_text(self, ctx):
        '''
        Helper method to create an expression visitor an call it
        '''
        if isinstance(ctx, TerminalNodeImpl):
            return self._w.getIntervalText(ctx.symbol, ctx.symbol)
        elif isinstance(ctx, ParserRuleContext):
            return self._w.getIntervalText(ctx.start, ctx.stop)
        else:
            assert False

    def _format_result_return(self, txt_result):
        if self._sm.is_main_machine():
            return u"\nreturn %s;" % txt_result
        else:
            return u"\n{sa_state->sa_result = %s; return;}" % txt_result

    def visit_RootNode(self, node):
        self._nb = node.get_scope(NonBlockingData)
        visit_node(self, node.child_source)

    def visit_PluginSourceNode(self, node):
        visit_node(self, node.child_declaration_list)

        if self._nb.has_sub_machines():
            ctx = node.child_declaration_list.childs_declarations[0].ctx
            txt = u"\nstatic %s* sa_state = 0;" % self._tn
            txt += u"\nstatic waiting_for* sa_wf = 0;"
            txt += u"\n\n"
            self._w.insertBeforeToken(ctx.start, txt)

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

    def visit_FunctionCallStmtNode(self, node):

        self._visit_expression(node.child_expression)

        if node.flg_is_blocking:
            n = node.child_expression.txt_name
            args = node.child_expression.child_argument_list.childs_arguments
            assert len(args) >= 1
            arg0 = self._get_text(args[0].ctx)

            if n == "papi_sleep":
                w = u"timeout"
                self._w.deleteTokens(node.ctx.start, node.ctx.stop)
            else:
                if n == "papi_wait_for_spi_send":
                    f = u"papi_start_sending_spi_command_16"
                    w = u"spi_send"
                elif n == "papi_wait_for_i2c_send":
                    f = u"papi_start_sending_i2c_command_16"
                    w = u"i2c_send"
                elif n == "papi_wait_for_spi_receive":
                    f = u"papi_start_receiving_spi_data_16"
                    w = u"spi_receive"
                elif n == "papi_wait_for_i2c_receive":
                    f = u"papi_start_receiving_i2c_data_16"
                    w = u"i2c_receive"
                else:
                    assert False

                self._w.replaceToken(
                    node.child_expression.ctx.Identifier().symbol, f)

            txt = u"\npapi_wait_handler_add_wait_for_%s(sa_wf, %s);" % (
                w, arg0)
            self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_LoopStmtNode(self, node):
        self._visit_expression(node.child_expression)
        visit_node(self, node.child_statement_list)

    def visit_ReturnStmtNode(self, node):
        if node.child_expression is not None:
            self._visit_expression(node.child_expression)

    def visit_IfElseStmtNode(self, node):
        self._visit_expression(node.child_expression)
        visit_node(self, node.child_if_branch)
        if node.child_else_branch is not None:
            visit_node(self, node.child_else_branch)

    def visit_StateMachineStmtNode(self, node):

        self._sm = node

        if node.has_states():

            txt = u"\n\nswitch(sa_state->%s) {" % node.get_name()

            txt += u"\ncase 0: break;"
            for i in range(1, node.get_last_state() + 1):

                txt += u"\ncase %s: goto label_%s;" % (str(i), str(i))
    #            visit_node(self, each.child_statement_list)

            txt += u"\ndefault: ZEPTO_ASSERT(0);"
            txt += u"\n}\n\n"

            if node.ctx.line is not None:
                txt += u"\n//#line %s\n" % node.ctx.line

            self._w.insertAfterToken(node.ctx, txt)

    def visit_NextStateStmtNode(self, node):

        nxt = str(node.int_next_state)
        txt = u"\nsa_state->%s = %s;" % (self._sm.get_name(), nxt)

        if node.ref_waiting_for is None:
            txt += self._format_result_return("PLUGIN_DEBUG")

            # we add a nop here, because C compiler will complain if next
            # statement is a declaration.
            # Only pure statements allowed right after a label
            # Adding a NOP will silence it
            txt += u"\nlabel_%s: /* nop */ ;" % nxt

        else:
            txt += self._format_result_return("PLUGIN_WAITING")

            txt += u"\n\nlabel_%s:" % nxt

            n = node.ref_waiting_for.txt_name
            args = node.ref_waiting_for.child_argument_list.childs_arguments
            assert len(args) >= 1
            arg0 = self._get_text(args[0].ctx)

            if n == "papi_sleep":
                f = u"timeout(0, sa_wf)"
            elif n == "papi_wait_for_spi_send":
                f = u"spi_send(sa_wf, %s)" % arg0
            elif n == "papi_wait_for_i2c_send":
                f = u"i2c_send(sa_wf, %s)" % arg0
            elif n == "papi_wait_for_spi_receive":
                f = u"spi_receive(sa_wf, %s)" % arg0
            elif n == "papi_wait_for_i2c_receive":
                f = u"i2c_receive(sa_wf, %s)" % arg0
            else:
                assert False

            txt += u"\nif(papi_wait_handler_is_waiting_for_%s)" % f
            txt += self._format_result_return("PLUGIN_WAITING")

        if node.ctx.stop.line is not None:
            txt += u"\n//#line %s\n" % node.ctx.stop.line

        self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_BeforeSubStmtNode(self, node):

        nxt = str(node.int_next_state)
        txt = u"\nsa_state->%s = %s;" % (self._sm.get_name(), nxt)
        txt += u"\nlabel_%s: " % nxt

        self._w.insertBeforeToken(node.ctx.start, txt)

    def visit_AfterSubStmtNode(self, node):

        txt = u"\nif(sa_state->%s != 0)" % node.ref_sub_machine.get_name()

        if self._sm.is_main_machine():
            txt += u" return sa_state->sa_result;"
        else:
            txt += u" return;"

        self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_InitStateStmtNode(self, node):

        txt = u"\n%s* sa_state = (%s*)%s;" % (self._tn, self._tn, node.txt_arg)

        if self._nb.has_sub_machines():
            txt += u"\nsa_state->sa_result = PLUGIN_OK;"

        for each in self._nb.refs_state_machines:
            txt += u"\nsa_state->%s = 0;" % each.get_name()

        self._w.insertAfterToken(node.ctx, txt)

    def visit_BeforeReturnStmtNode(self, node):

        if node.ref_state_machine.has_states():
            txt = u"sa_state->%s = 0;" % node.ref_state_machine.get_name()
            self._w.insertBeforeToken(node.ctx.start, txt)

    def visit_StateDataCastStmtNode(self, node):

        if self._nb.has_sub_machines():
            txt = u"\nsa_state = (%s*)%s;" % (self._tn, node.txt_arg2)
            txt += u"\nsa_wf = %s;" % node.txt_arg5
        else:
            txt = u"\n%s* sa_state = (%s*)%s;" % (self._tn,
                                                  self._tn, node.txt_arg2)
            txt += u"\nwaiting_for* sa_wf = %s;" % node.txt_arg5

        self._w.insertAfterToken(node.ctx, txt)

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
                    u"(sa_state->%s)" % node.ref_decl.txt_name)

    def visit_FunctionCallExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_ArgumentListNode(self, node):
        for each in node.childs_arguments:
            visit_node(self, each)
