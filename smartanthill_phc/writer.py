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
from smartanthill_phc.c_node import VoidTypeDeclNode, IntTypeDeclNode
from smartanthill_phc.common.visitor import visit_node, NodeVisitor
from smartanthill_phc.root import NonBlockingData


def write_code(compiler, root):
    '''
    Rewrites code tree
    '''
    visitor = _WriterVisitor(compiler)
    visit_node(visitor, root)

    text = visitor.get_text()

    compiler.check_stage('write')

    return text


class _WriterVisitor(NodeVisitor):

    '''
    Visitor class for plugin rewrite
    '''

    def __init__(self, compiler):
        '''
        Constructor
        '''
        super(_WriterVisitor, self).__init__()
        self._c = compiler
        self._w = _Writer()
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
        if isinstance(self._func.child_return_type.ref_type_declaration,
                      VoidTypeDeclNode):
            self._w.write_line("return;")
        elif isinstance(self._func.child_return_type.ref_type_declaration,
                        IntTypeDeclNode):
            self._w.write_line("return 0;")
        else:
            assert False

    def _format_result_return(self, txt_result):
        if self._sm.ref_state_machine.is_main_machine():
            self._w.write_line("return %s;" % txt_result)
        else:
            self._w.write_line("*sa_result = %s;" % txt_result)
            self._get_func_return()

    def get_text(self):
        return self._w.get_text()

    def write_expr(self, expr):
        self.visit(expr)

    def visit_RootNode(self, node):
        self._nb = node.get_scope(NonBlockingData)
        self.visit(node.child_source)

    def visit_PluginSourceNode(self, node):
        self.visit(node.child_declaration_list)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            self.visit(each)

    def visit_FunctionDeclNode(self, node):

        self._func = node
        self._sm = self._nb.get_state_machine_data(node)
        self.visit(node.child_return_type)
        self._w.write(' ')
        self._w.write(node.txt_name)
        self._w.write('(')

        first = True
        for each in node.child_argument_decl_list.childs_declarations:

            if not first:
                self._w.write(',')
            first = False
            self.visit(each.child_argument_type)
            self._w.write(' ')
            self._w.write(each.txt_name)

        self._w.write(')')

        self.visit(node.child_stmt_list)

    def visit_StmtListNode(self, node):
        self._w.write('{')
        self._w.end_of_statement()

        for each in node.childs_statements:
            self.visit(each)

        self._w.write('}')
        self._w.end_of_statement()

    def visit_NopStmtNode(self, node):
        # pylint: disable=unused-argument
        # Nothing to do here
        self._w.write(';')
        self._w.end_of_statement()

    def visit_VariableDeclarationStmtNode(self, node):

        self.visit(node.child_declaration_type)
        self._w.write(' ')
        self._w.write(node.txt_name)
        if node.child_initializer_expression is not None:
            self._w.write('=')
            self.write_expr(node.child_initializer_expression)

        self._w.write(';')
        self._w.end_of_statement()

    def visit_ExpressionStmtNode(self, node):
        self.write_expr(node.child_expression)
        self._w.write(';')
        self._w.end_of_statement()

    def visit_FunctionCallStmtNode(self, node):
        self.write_expr(node.child_expression)
        self._w.write(';')
        self._w.end_of_statement()

        if node.child_expression.bool_is_blocking:
            assert False

    def visit_PapiWaitStmtNode(self, node):
        self._w.write(node.txt_name)
        self.write_expr(node.child_expression)
        self._w.write(';')
        self._w.end_of_statement()

        self._w.write("papi_wait_handler_add_wait_for_")
        self._w.write(node.txt_wait_for)
        self._w.write("(sa_wf,")
        self.write_expr(node.child_argument_list.childs_arguments[0])
        self._w.write(')')
        self._w.write(';')
        self._w.end_of_statement()

        self._w.write_line("sa_state->sa_next = %s;" % node.int_next_state)
        self._format_result_return("PLUGIN_WAITING")

        self._w.write("label_%s:" % node.int_next_state)

        self._w.write("if(papi_wait_handler_is_waiting_for_")
        self._w.write(node.txt_wait_for)
        self._w.write("(sa_wf,")
        self.write_expr(node.child_argument_list.childs_arguments[0])
        self._w.write('))')
        self._w.end_of_statement()
        self._w.write_line('{')

        self._format_result_return("PLUGIN_WAITING")

        self._w.write_line('}')


#         if node.ctx.stop.line is not None:
#             txt += u"//#line %s\n" % node.ctx.stop.line

    def visit_PapiSleepStmtNode(self, node):
        #         self._w.write('')
        #         self.write_expr(node.child_expression)
        #         self._w.write(';')
        #         self._w.end_of_statement()

        self._w.write("papi_wait_handler_add_wait_for_timeout(sa_wf,")
        self.write_expr(node.child_argument_list.childs_arguments[0])
        self._w.write(')')
        self._w.write(';')
        self._w.end_of_statement()

        self._w.write_line("sa_state->sa_next = %s;" % node.int_next_state)

        self._format_result_return("PLUGIN_WAITING")

        self._w.write("label_%s:" % node.int_next_state)

        self._w.write("if(papi_wait_handler_is_waiting_for_timeout(0, sa_wf))")
        self._w.end_of_statement()
        self._w.write_line('{')

        self._format_result_return("PLUGIN_WAITING")

        self._w.write_line('}')


#         if node.ctx.stop.line is not None:
#             txt += u"//#line %s\n" % node.ctx.stop.line

    def visit_WhileStmtNode(self, node):
        self._w.write('while')
        self._w.write('(')
        self.write_expr(node.child0_expression)
        self._w.write(')')
        self.visit(node.child1_stmt_list)
        self._w.end_of_statement()

    def visit_DoWhileStmtNode(self, node):
        self._w.write('do')
        self.visit(node.child1_stmt_list)
        self._w.write('while')
        self._w.write('(')
        self.write_expr(node.child0_expression)
        self._w.write(')')
        self._w.end_of_statement()

    def visit_ForStmtNode(self, node):
        self._w.write('for')
        self._w.write('(')
        if node.child0_init_expression is not None:
            self.write_expr(node.child0_init_expression)
        self._w.write(';')
        if node.child1_condition_expression is not None:
            self.write_expr(node.child1_condition_expression)
        self._w.write(';')
        if node.child2_iteration_expression is not None:
            self.write_expr(node.child2_iteration_expression)
        self._w.write(')')
        self.visit(node.child3_stmt_list)
        self._w.end_of_statement()

    def visit_ReturnStmtNode(self, node):

        self._w.write('return')
        if node.child_expression is not None:
            self._w.write(' ')
            self.write_expr(node.child_expression)

        self._w.write(';')
        self._w.end_of_statement()

    def visit_IfElseStmtNode(self, node):

        self._w.write('if')
        self._w.write('(')
        self.write_expr(node.child0_expression)
        self._w.write(')')
        self.visit(node.child1_if_stmt_list)
        if node.child2_else_stmt_list is not None:
            self._w.write('else')
            self.visit(node.child2_else_stmt_list)
        self._w.end_of_statement()

    def visit_StateMachineStmtNode(self, node):

        if node.has_states():

            self._w.write_line("switch(sa_state->sa_next) {")

            self._w.write_line("case 0: break;")
            for i in range(1, node.get_last_state() + 1):
                self._w.write_line(
                    "case %s: goto label_%s;" % (str(i), str(i)))
    #            visit_node(self, each.child_statement_list)

            self._w.write_line("default: ZEPTO_ASSERT(0);")
            self._w.write_line('}')

#             if node.ctx.line is not None:
#                 txt += u"\n//#line %s\n" % node.ctx.line

    def visit_WaitStateStmtNode(self, node):

        nxt = str(node.int_next_state)
        self._w.write_line("sa_state->sa_next = %s;" % nxt)

        self._format_result_return("PLUGIN_WAITING")

        self._w.write_line("label_%s:" % nxt)

        n = node.ref_waiting_for.txt_name
        args = node.ref_waiting_for.child_argument_list.childs_arguments
        assert len(args) >= 1
#         arg0 = self._get_text(args[0].ctx)
        arg0 = '/* TODO */'

        if n == "papi_sleep":
            f = "timeout(0, sa_wf)"
        elif n == "papi_wait_for_spi_send":
            f = "spi_send(sa_wf, %s)" % arg0
        elif n == "papi_wait_for_i2c_send":
            f = "i2c_send(sa_wf, %s)" % arg0
        elif n == "papi_wait_for_spi_receive":
            f = "spi_receive(sa_wf, %s)" % arg0
        elif n == "papi_wait_for_i2c_receive":
            f = "i2c_receive(sa_wf, %s)" % arg0
        else:
            assert False

        self._w.write_line("if(papi_wait_handler_is_waiting_for_%s) {" % f)
        self._w.write_line(self._format_result_return("PLUGIN_WAITING"))
        self._w.write_line("}")

#         if node.ctx.stop.line is not None:
#             txt += u"//#line %s\n" % node.ctx.stop.line

    def visit_DebugStateStmtNode(self, node):

        nxt = str(node.int_next_state)
        self._w.write_line("sa_state->sa_next = %s;" % nxt)

        self._w.write_line(self._format_result_return("PLUGIN_DEBUG"))

        # we add a nop here, because C compiler will complain if next
        # statement is a declaration.
        # Only pure statements allowed right after a label
        # Adding a NOP will silence it
        self._w.write_line("label_%s: /* nop */ ;" % nxt)

#         if node.ctx.stop.line is not None:
#             txt += u"\n//#line %s\n" % node.ctx.stop.line
#
#         self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_BeforeSubStmtNode(self, node):

        nxt = str(node.int_next_state)
        self._w.write_line("*(uint8_t*)(sa_state + 1) = 0;")
        self._w.write_line("sa_state->sa_next = %s;" % nxt)
        self._w.write_line("label_%s: " % nxt)

#         self._w.insertBeforeToken(node.ctx.start, txt)

    def visit_AfterSubStmtNode(self, node):
        # pylint: disable=unused-argument
        self._w.write_line("if(*(uint8_t*)(sa_state + 1) != 0) ")

        if self._sm.ref_state_machine.is_main_machine():
            self._w.write_line("return *sa_result;")
        else:
            self._w.write_line(self._get_func_return())

#         self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_FunctionCallSubStmtNode(self, node):

        #         args = node.child_expression.child_argument_list
        #         txt_args = u"(void*)(sa_state + 1), sa_wf, sa_result"
        #         if len(args.childs_arguments) >= 1:
        #             txt_args += u", "
        #        self._w.insertAfterToken(args.ctx.symbol, txt_args)

        nxt = str(node.int_next_state)
        self._w.write_line("*(uint8_t*)(sa_state + 1) = 0;")
        self._w.write_line("sa_state->sa_next = %s;" % nxt)
        self._w.write_line("label_%s: ;/*nop*/" % nxt)

        self.visit(node.child_expression.ref_declaration.child_return_type)
        self._w.write(' ')
        self._w.write(node.txt_name)
        self._w.write('=')
        self.visit(node.child_expression)
        self._w.write(';')
        self._w.end_of_statement()

        self._w.write_line("if(*(uint8_t*)(sa_state + 1) != 0)")

        if self._sm.ref_state_machine.is_main_machine():
            self._w.write_line("return *sa_result;")
        else:
            self._w.write_line(self._get_func_return())

#        self._w.insertBeforeToken(node.ctx.start, txt)

    def visit_InitFirstStmtNode(self, node):
        self._w.write_line("*(uint8_t*)%s = 0;" % node.txt_arg1)
#        self._w.insertAfterToken(node.ctx, txt)

    def visit_BeforeReturnStmtNode(self, node):
        # pylint: disable=unused-argument
        self._w.write_line("sa_state->sa_next = 0;")
#         self._w.insertBeforeToken(node.ctx, txt)

    def visit_MainFirstStmtNode(self, node):

        self._w.write_line("%s* sa_state = (%s*)%s;" % (
            self._sm.txt_struct_name, self._sm.txt_struct_name, node.txt_arg2))
        self._w.write_line("waiting_for* sa_wf = %s;" % node.txt_arg5)

        if self._nb.has_sub_machines():
            self._w.write_line("\nuint8_t sa_result0 = PLUGIN_OK;")
            self._w.write_line("\nuint8_t* sa_result = &sa_result0;")

#        self._w.insertAfterToken(node.ctx, txt)

    def visit_SubFirstStmtNode(self, node):
        # pylint: disable=unused-argument
        self._w.write_line("%s* sa_state = (%s*)sa_state0;" % (
            self._sm.txt_struct_name, self._sm.txt_struct_name))

#        self._w.insertAfterToken(node.ctx, txt)

    def visit_DontCareExprNode(self, node):
        # pylint: disable=unused-argument
        # TODO
        # self.visit(node.child_argument_list)
        self._w.write('/* TODO */')

    def visit_BinaryOpExprNode(self, node):
        assert len(node.child_argument_list.childs_arguments) == 2
        self.write_expr(node.child_argument_list.childs_arguments[0])
        self._w.write(node.txt_operator)
        self.write_expr(node.child_argument_list.childs_arguments[1])

    def visit_UnaryOpExprNode(self, node):
        assert len(node.child_argument_list.childs_arguments) == 1
        self._w.write(node.txt_operator)
        self.write_expr(node.child_argument_list.childs_arguments[0])

    def visit_PostfixOpExprNode(self, node):
        assert len(node.child_argument_list.childs_arguments) == 1
        self.write_expr(node.child_argument_list.childs_arguments[0])
        self._w.write(node.txt_operator)

    def visit_MemberExprNode(self, node):

        self.write_expr(node.child_expression)

        if node.bool_arrow:
            self._w.write('->')
        else:
            self._w.write('.')

        self._w.write(node.txt_name)

    def visit_CastExprNode(self, node):
        self._w.write('(')
        self.visit(node.child_cast_type)
        self._w.write(')')
        self.visit(node.child_expression)

    def visit_LiteralExprNode(self, node):
        self._w.write(node.txt_literal)

    def visit_VariableExprNode(self, node):
        if node.ref_declaration is not None:
            if self._sm is not None and\
                    self._sm.is_moved_var_decl(node.ref_declaration):
                self._w.write("(sa_state->%s)" % node.ref_declaration.txt_name)
            else:
                self._w.write(node.ref_declaration.txt_name)
        else:
            self._w.write(node.txt_name)

    def visit_FunctionCallExprNode(self, node):

        if node.ref_declaration is not None:
            self._w.write(node.ref_declaration.txt_name)
        else:
            self._w.write(node.txt_name)
        self._w.write('(')

        first = True
        for each in node.child_argument_list.childs_arguments:
            if not first:
                self._w.write(',')
            first = False
            self.write_expr(each)

        self._w.write(')')

    def visit_FunctionCallSubExprNode(self, node):

        self._w.write(node.ref_declaration.txt_name)

#         self._w.replaceTokens(node.ctx.start, node.ctx.stop,
#                               u"(%s)" % node.ref_declaration.txt_name)

    def visit_SimpleTypeNode(self, node):

        self._w.write(node.txt_name)

    def visit_PointerTypeNode(self, node):

        self.visit(node.child_pointed_type)
        self._w.write('*')


class _Writer(object):

    '''
    Visitor class for plugin rewrite
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(_Writer, self).__init__()
        self._buffer = []
        self._current = ''

    def end_of_statement(self):
        if len(self._current) != 0:
            self._buffer.append(self._current)
            self._current = ''

    def get_text(self):
        assert self._current == ''

        txt = banner.get_copyright_banner()
        txt += "\n"

        for each in self._buffer:
            txt += each
            txt += '\n'

        return txt

    def write(self, txt):
        self._current += txt

    def write_line(self, line):
        '''
        Auto generated source code, better fits a line by line writing
        than a token by token of parsed tree code
        '''

        assert self._current == ''
        self._buffer.append(line)
