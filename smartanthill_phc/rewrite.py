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

from smartanthill_phc.TokenStreamRewriter import TokenStreamRewriter
from smartanthill_phc.c_node import VoidTypeDeclNode, IntTypeDeclNode
from smartanthill_phc.common.visitor import visit_node, CodeVisitor
from smartanthill_phc.parser import get_declarator_identifier
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


class _RewriteVisitor(CodeVisitor):

    '''
    Visitor class for plugin rewrite
    '''

    def __init__(self, compiler, writer):
        '''
        Constructor
        '''
        super(_RewriteVisitor, self).__init__()
        self._c = compiler
        self._w = writer
        self._nb = None
        self._sm = None
        self._func = None

    def _get_text(self, ctx):
        '''
        Helper method
        '''
        if isinstance(ctx, TerminalNodeImpl):
            return self._w.getIntervalText(ctx.symbol, ctx.symbol)
        elif isinstance(ctx, ParserRuleContext):
            return self._w.getIntervalText(ctx.start, ctx.stop)
        else:
            assert False

    def _get_func_return(self):
        if isinstance(self._func.return_type.get().ref_type_declaration,
                      VoidTypeDeclNode):
            return u"return;"
        elif isinstance(self._func.return_type.get().ref_type_declaration,
                        IntTypeDeclNode):
            return u"return 0;"
        else:
            assert False

    def _format_result_return(self, txt_result):
        if self._sm.ref_state_machine.is_main_machine():
            return u"\nreturn %s;" % txt_result
        else:
            return u"\n*sa_result = %s;\n%s" % (txt_result,
                                                self._get_func_return())

    def visit_RootNode(self, node):
        self._nb = node.get_scope(NonBlockingData)
        self.visit(node.source)

    def visit_PluginSourceNode(self, node):
        self.visit_childs(node)

    def visit_DeclarationListNode(self, node):
        self.visit_childs(node)

    def visit_PreprocessorDirectiveNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        pass

    def visit_ConstantDefineNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        pass

    def visit_FunctionDefinitionNode(self, node):
        self.visit_childs(node)

    def visit_FunctionDeclNode(self, node):

        self._func = node
        self._sm = self._nb.get_state_machine_data(node)

        if self._sm is not None:
            if not self._sm.ref_state_machine.is_main_machine():
                txt = u"void* sa_state0"
                txt += u", waiting_for* sa_wf, uint8_t* sa_result"
                if node.argument_decl_list.get().declarations.get_size() >= 1:
                    txt += u", "

                self._w.insertAfterToken(
                    node.argument_decl_list.get().ctx.symbol, txt)

    def visit_StmtListNode(self, node):
        self.visit_childs(node)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):

        if self._sm is not None:
            if self._sm.is_moved_var_decl(node):

                decl_list = node.ctx.initDeclaratorList()
                assert decl_list is not None
                assert len(decl_list.initDeclarator()) == 1
                tk = get_declarator_identifier(
                    decl_list.initDeclarator(0).declarator())

                if not node.initializer_expression.is_none():
                    self._w.replaceTokens(
                        node.ctx.start, tk.symbol,
                        u"sa_state->%s" % node.txt_name)
                else:
                    self._w.deleteTokens(node.ctx.start, node.ctx.stop)

            if not node.initializer_expression.is_none():
                self.visit(node.initializer_expression)

    def visit_ExpressionStmtNode(self, node):
        self.visit_childs(node)

    def visit_FunctionCallStmtNode(self, node):

        self.visit_childs(node)

        if node.expression.get().bool_is_blocking:
            assert False

    def visit_PapiWaitStmtNode(self, node):

        self.visit_childs(node)

        args = node.argument_list.get().arguments
        assert args.get_size() >= 1
        arg0 = self._get_text(args.at(0).get().ctx)

        self._w.replaceToken(
            node.ctx_function_name.symbol, node.txt_name)

        txt = u"\npapi_wait_handler_add_wait_for_%s(sa_wf, %s);" % (
            node.txt_wait_for, arg0)
        self._w.insertAfterToken(node.ctx.stop, txt)

        nxt = str(node.int_next_state)
        txt = u"\nsa_state->sa_next = %s;" % nxt

        txt += self._format_result_return("PLUGIN_WAITING")

        txt += u"\n\nlabel_%s:" % nxt

        args = node.argument_list.get().arguments
        assert args.get_size() >= 1
        arg0 = self._get_text(args.at(0).get().ctx)

        txt += u"\nif(papi_wait_handler_is_waiting_for_%s(sa_wf, %s)) {" % (
            node.txt_wait_for, arg0)
        txt += self._format_result_return("PLUGIN_WAITING")
        txt += u"\n}\n"

        if node.ctx.stop.line is not None:
            txt += u"//#line %s\n" % node.ctx.stop.line

        self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_PapiSleepStmtNode(self, node):

        self.visit_childs(node)

        args = node.argument_list.get().arguments
        assert args.get_size() >= 1
        arg0 = self._get_text(args.at(0).get().ctx)

        self._w.deleteTokens(node.ctx.start, node.ctx.stop)

        txt = u"\npapi_wait_handler_add_wait_for_timeout(sa_wf, %s);" % (
            arg0)
        self._w.insertAfterToken(node.ctx.stop, txt)

        nxt = str(node.int_next_state)
        txt = u"\nsa_state->sa_next = %s;" % nxt

        txt += self._format_result_return("PLUGIN_WAITING")

        txt += u"\n\nlabel_%s:" % nxt

        args = node.argument_list.get().arguments
        assert args.get_size() >= 1
        arg0 = self._get_text(args.at(0).get().ctx)

        txt += u"\nif(papi_wait_handler_is_waiting_for_timeout(0, sa_wf)) {"
        txt += self._format_result_return("PLUGIN_WAITING")
        txt += u"\n}\n"

        if node.ctx.stop.line is not None:
            txt += u"//#line %s\n" % node.ctx.stop.line

        self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_LoopStmtNode(self, node):
        self.visit_childs(node)

    def visit_ReturnStmtNode(self, node):
        self.visit_childs(node)

    def visit_IfElseStmtNode(self, node):
        self.visit_childs(node)

    def visit_StateMachineStmtNode(self, node):

        txt = u"\n\nswitch(sa_state->sa_next) {"

        txt += u"\ncase 0: break;"
        for i in range(1, node.int_last_state + 1):

            txt += u"\ncase %s: goto label_%s;" % (str(i), str(i))
    #            visit_node(self, each.child_statement_list)

        txt += u"\ndefault: ZEPTO_ASSERT(0);"
        txt += u"\n}\n\n"

        if node.ctx.line is not None:
            txt += u"\n//#line %s\n" % node.ctx.line

        self._w.insertAfterToken(node.ctx, txt)

    def visit_DebugStateStmtNode(self, node):

        nxt = str(node.int_next_state)
        txt = u"\nsa_state->sa_next = %s;" % nxt

        txt += self._format_result_return("PLUGIN_DEBUG")

        # we add a nop here, because C compiler will complain if next
        # statement is a declaration.
        # Only pure statements allowed right after a label
        # Adding a NOP will silence it
        txt += u"\nlabel_%s: /* nop */ ;" % nxt

        if node.ctx.stop.line is not None:
            txt += u"\n//#line %s\n" % node.ctx.stop.line

        self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_BeforeSubStmtNode(self, node):

        nxt = str(node.int_next_state)
        txt = u"\n*(uint8_t*)(sa_state + 1) = 0;"
        txt += u"\nsa_state->sa_next = %s;" % nxt
        txt += u"\nlabel_%s: " % nxt

        self._w.insertBeforeToken(node.ctx.start, txt)

    def visit_AfterSubStmtNode(self, node):

        txt = u"\nif(*(uint8_t*)(sa_state + 1) != 0) "

        if self._sm.ref_state_machine.is_main_machine():
            txt += u"return *sa_result;"
        else:
            txt += self._get_func_return()

        self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_FunctionCallSubStmtNode(self, node):

        args = node.expression.get().argument_list.get()
        txt_args = u"(void*)(sa_state + 1), sa_wf, sa_result"
        if args.arguments.get_size() >= 2:
            txt_args += u", "
        self._w.insertAfterToken(args.ctx.symbol, txt_args)

        nxt = str(node.int_next_state)
        txt = u"\n*(uint8_t*)(sa_state + 1) = 0;"
        txt += u"\nsa_state->sa_next = %s;" % nxt
        txt += u"\nlabel_%s: ;/*nop*/" % nxt

        t = node.expression.get().ref_declaration.return_type.get().txt_name
        txt += u"\n%s %s = %s;" % (t, node.txt_name,
                                   self._get_text(node.expression.get().ctx))

        txt += u"\nif(*(uint8_t*)(sa_state + 1) != 0) "

        if self._sm.ref_state_machine.is_main_machine():
            txt += u"return *sa_result;"
        else:
            txt += self._get_func_return()

        self._w.insertBeforeToken(node.ctx.start, txt)

    def visit_InitFirstStmtNode(self, node):

        txt = u"\n*(uint8_t*)%s = 0;" % node.txt_arg1
        self._w.insertAfterToken(node.ctx, txt)

    def visit_BeforeReturnStmtNode(self, node):

        txt = u"sa_state->sa_next = 0;"
        self._w.insertBeforeToken(node.ctx, txt)

    def visit_MainFirstStmtNode(self, node):

        txt = u"\n%s* sa_state = (%s*)%s;" % (
            self._sm.txt_struct_name, self._sm.txt_struct_name, node.txt_arg2)
        txt += u"\nwaiting_for* sa_wf = %s;" % node.txt_arg5

        if self._nb.has_sub_machines():
            txt += u"\nuint8_t sa_result0 = PLUGIN_OK;"
            txt += u"\nuint8_t* sa_result = &sa_result0;"

        self._w.insertAfterToken(node.ctx, txt)

    def visit_SubFirstStmtNode(self, node):

        txt = u"\n%s* sa_state = (%s*)sa_state0;" % (
            self._sm.txt_struct_name, self._sm.txt_struct_name)

        self._w.insertAfterToken(node.ctx, txt)

    def visit_TypeNode(self, node):
        pass

    def visit_ExpressionNode(self, node):
        self.visit_childs(node)

    def visit_VariableExprNode(self, node):

        if node.ref_declaration is not None:
            if self._sm is not None:
                if self._sm.is_moved_var_decl(node.ref_declaration):
                    self._w.replaceToken(
                        node.ctx.symbol,
                        u"(sa_state->%s)" % node.ref_declaration.txt_name)

    def visit_FunctionCallExprNode(self, node):
        self.visit_childs(node)

        if self._nb.has_states(node.ref_declaration):
            args = node.argument_list.get()
            txt = u"(void*)(sa_state + 1), sa_wf, sa_result"
            if args.arguments.get_size() >= 2:
                txt += u", "

            self._w.insertAfterToken(args.ctx.symbol, txt)

    def visit_FunctionCallSubExprNode(self, node):

        self._w.replaceTokens(node.ctx.start, node.ctx.stop,
                              u"(%s)" % node.ref_declaration.txt_name)

    def visit_ArgumentListNode(self, node):
        self.visit_childs(node)
