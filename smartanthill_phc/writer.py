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


def write_code(compiler, root, source_file):
    '''
    Writes code tree
    '''
    visitor = _WriterVisitor(compiler, source_file)
    visit_node(visitor, root)

    text = visitor.get_text()

    compiler.check_stage('write')

    return text


def write_header(compiler, root, source_file):
    '''
    Write header file
    '''
    visitor = _HeaderWriterVisitor(compiler, source_file)
    visit_node(visitor, root)

    text = visitor.get_text()
    compiler.check_stage('header')

    return text


class _WriterVisitor(NodeVisitor):

    '''
    Visitor class for plugin rewrite
    '''

    def __init__(self, compiler, source_file):
        '''
        Constructor
        '''
        super(_WriterVisitor, self).__init__()
        self._c = compiler
        self._w = _Writer(source_file)
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

    def _write_func_return(self):
        if isinstance(self._func.child_return_type.ref_type_declaration,
                      VoidTypeDeclNode):
            self._w.write_line("return;")
        elif isinstance(self._func.child_return_type.ref_type_declaration,
                        IntTypeDeclNode):
            self._w.write_line("return 0;")
        else:
            assert False

    def _write_result_return(self, txt_result):
        if self._sm.ref_state_machine.is_main_machine():
            self._w.write_line("return %s;" % txt_result)
        else:
            self._w.write_line("*sa_result = %s;" % txt_result)
            self._write_func_return()

    def get_text(self):
        return self._w.get_text()

    def write_expr(self, expr):

        if expr.bool_parenthesis:
            self._w.write('(')
        self.visit(expr)
        if expr.bool_parenthesis:
            self._w.write(')')

    def visit_RootNode(self, node):
        self._nb = node.get_scope(NonBlockingData)
        self.visit(node.child_source)

    def visit_PluginSourceNode(self, node):
        self.visit(node.child_declaration_list)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            self.visit(each)

    def visit_PreprocessorDirectiveNode(self, node):
        self._w.write_line(node.txt_body)

    def visit_FunctionDeclNode(self, node):

        self._func = node
        self._sm = self._nb.get_state_machine_data(node)
        self.visit(node.child_return_type)
        self._w.write(' ')
        self._w.write(node.txt_name)
        self._w.write('(')

        first = True
        if self._sm is not None and\
                not self._sm.ref_state_machine.is_main_machine():
            self._w.write(
                "void* sa_state0, waiting_for* sa_wf, uint8_t* sa_result")
            first = False

        for each in node.child_argument_decl_list.childs_declarations:

            if not first:
                self._w.write(', ')
            first = False
            self.visit(each.child_argument_type)
            self._w.write(' ')
            self._w.write(each.txt_name)

        self._w.write(')')
        self._w.end_of_statement(node.ctx.start)

        self.visit(node.child_stmt_list)

    def visit_StmtListNode(self, node):
        self._w.write_line('{')

        for each in node.childs_statements:
            self.visit(each)

        self._w.write_line('}')

    def visit_NopStmtNode(self, node):
        # pylint: disable=unused-argument
        # Nothing to do here
        self._w.write(';')
        self._w.end_of_statement(node.ctx.stop)

    def visit_VariableDeclarationStmtNode(self, node):

        if self._sm is not None and\
                self._sm.is_moved_var_decl(node):
            if node.child_initializer_expression is not None:

                self._w.write('sa_state->')
                self._w.write(node.txt_name)

                self._w.write(' = ')
                self.write_expr(node.child_initializer_expression)

                self._w.write(';')
                self._w.end_of_statement(node.ctx.stop)

        else:
            self.visit(node.child_declaration_type)
            self._w.write(' ')
            self._w.write(node.txt_name)
            if node.child_initializer_expression is not None:
                self._w.write(' = ')
                self.write_expr(node.child_initializer_expression)

            self._w.write(';')
            self._w.end_of_statement(node.ctx.stop)

    def visit_ExpressionStmtNode(self, node):
        self.write_expr(node.child_expression)
        self._w.write(';')
        self._w.end_of_statement(node.ctx.stop)

    def visit_FunctionCallStmtNode(self, node):
        self.write_expr(node.child_expression)
        self._w.write(';')
        self._w.end_of_statement(node.ctx.stop)

        if node.child_expression.bool_is_blocking:
            assert False

    def visit_PapiWaitStmtNode(self, node):
        self._w.write(node.txt_name)
        self._writeArgumentListNode(node.child_argument_list)
        self._w.write(';')
        self._w.end_of_statement(node.ctx.stop)

        self._w.write("papi_wait_handler_add_wait_for_")
        self._w.write(node.txt_wait_for)
        self._w.write("(sa_wf, ")
        self.write_expr(node.child_argument_list.childs_arguments[0])
        self._w.write(')')
        self._w.write(';')
        self._w.end_of_statement(None)

        self._w.write_line("sa_state->sa_next = %s;" % node.int_next_state)
        self._write_result_return("PLUGIN_WAITING")

        self._w.write("label_%s:" % node.int_next_state)

        self._w.write("if(papi_wait_handler_is_waiting_for_")
        self._w.write(node.txt_wait_for)
        self._w.write("(sa_wf, ")
        self.write_expr(node.child_argument_list.childs_arguments[0])
        self._w.write('))')
        self._w.end_of_statement(None)
        self._w.write_line('{')

        self._write_result_return("PLUGIN_WAITING")

        self._w.write_line('}')


#         if node.ctx.stop.line is not None:
#             txt += u"//#line %s\n" % node.ctx.stop.line

    def visit_PapiSleepStmtNode(self, node):
        #         self._w.write('')
        #         self.write_expr(node.child_expression)
        #         self._w.write(';')
        #         self._w.end_of_statement()

        self._w.write("papi_wait_handler_add_wait_for_timeout(sa_wf, ")
        self.write_expr(node.child_argument_list.childs_arguments[0])
        self._w.write(')')
        self._w.write(';')
        self._w.end_of_statement(node.ctx.stop)

        self._w.write_line("sa_state->sa_next = %s;" % node.int_next_state)

        self._write_result_return("PLUGIN_WAITING")

        self._w.write("label_%s:" % node.int_next_state)

        self._w.write("if(papi_wait_handler_is_waiting_for_timeout(0, sa_wf))")
        self._w.end_of_statement(None)
        self._w.write_line('{')

        self._write_result_return("PLUGIN_WAITING")

        self._w.write_line('}')


#         if node.ctx.stop.line is not None:
#             txt += u"//#line %s\n" % node.ctx.stop.line

    def visit_WhileStmtNode(self, node):
        self._w.write('while')
        self._w.write('(')
        self.write_expr(node.child0_expression)
        self._w.write(')')
        self._w.end_of_statement(node.ctx.start)
        self.visit(node.child1_stmt_list)

    def visit_DoWhileStmtNode(self, node):
        self._w.write('do')
        self._w.end_of_statement(None)
        self.visit(node.child1_stmt_list)
        self._w.write('while')
        self._w.write('(')
        self.write_expr(node.child0_expression)
        self._w.write(');')
        self._w.end_of_statement(node.ctx.stop)

    def visit_ForStmtNode(self, node):
        self._w.write('for')
        self._w.write('(')
        if node.child0_init_expression is not None:
            self.write_expr(node.child0_init_expression)
        self._w.write(';')
        if node.child1_condition_expression is not None:
            self._w.write(' ')
            self.write_expr(node.child1_condition_expression)
        self._w.write('; ')
        if node.child2_iteration_expression is not None:
            self._w.write(' ')
            self.write_expr(node.child2_iteration_expression)
        self._w.write(')')
        self._w.end_of_statement(node.ctx.start)
        self.visit(node.child3_stmt_list)

    def visit_ReturnStmtNode(self, node):

        self._w.write('return')
        if node.child_expression is not None:
            self._w.write(' ')
            self.write_expr(node.child_expression)

        self._w.write(';')
        self._w.end_of_statement(node.ctx.stop)

    def visit_IfElseStmtNode(self, node):

        self._w.write('if')
        self._w.write('(')
        self.write_expr(node.child0_expression)
        self._w.write(')')
        self._w.end_of_statement(node.ctx.start)
        self.visit(node.child1_if_stmt_list)
        if node.child2_else_stmt_list is not None:
            self._w.write('else')
            self._w.end_of_statement(None)
            self.visit(node.child2_else_stmt_list)

    def visit_StateMachineStmtNode(self, node):

        self._w.write_line("switch(sa_state->sa_next) {")

        self._w.write_line("case 0: break;")
        for i in range(1, node.int_last_state + 1):
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

        self._write_result_return("PLUGIN_WAITING")

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
        self._write_result_return("PLUGIN_WAITING")
        self._w.write_line("}")

#         if node.ctx.stop.line is not None:
#             txt += u"//#line %s\n" % node.ctx.stop.line

    def visit_DebugStateStmtNode(self, node):

        nxt = str(node.int_next_state)
        self._w.write_line("sa_state->sa_next = %s;" % nxt)

        self._write_result_return("PLUGIN_DEBUG")

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
            self._write_func_return()

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
        self._w.write(' = ')
        self.visit(node.child_expression)
        self._w.write(';')
        self._w.end_of_statement(node.ctx.stop)

        self._w.write_line("if(*(uint8_t*)(sa_state + 1) != 0)")

        if self._sm.ref_state_machine.is_main_machine():
            self._w.write_line("return *sa_result;")
        else:
            self._write_func_return()

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

    def visit_AssignmentExprNode(self, node):

        self.write_expr(node.child0_left_expression)
        self._w.write('=')
        self.write_expr(node.child1_right_expression)

    def visit_ConditionalExprNode(self, node):

        self.write_expr(node.child0_condition_expression)
        self._w.write('?')
        self.write_expr(node.child1_true_expression)
        self._w.write(':')
        self.write_expr(node.child2_false_expression)

    def visit_BinaryOpExprNode(self, node):
        assert len(node.child_argument_list.childs_arguments) == 2
        self.write_expr(node.child_argument_list.childs_arguments[0])
        self._w.write(node.txt_operator)
        self.write_expr(node.child_argument_list.childs_arguments[1])

    def visit_UnaryOpExprNode(self, node):
        assert len(node.child1_argument_list.childs_arguments) == 0
        self._w.write(node.txt_operator)
        self.write_expr(node.child0_expression)

    def visit_PostUnaryOpExprNode(self, node):
        assert len(node.child1_argument_list.childs_arguments) == 0
        self.write_expr(node.child0_expression)
        self._w.write(node.txt_operator[4:])

    def visit_IndexExprNode(self, node):
        self._w.write(node.child0_expression)
        self._writeArgumentListNode(node.child1_argument_list, '[', ']')

    def visit_LiteralExprNode(self, node):
        self._w.write(node.txt_literal)

    def visit_MemberExprNode(self, node):

        self.write_expr(node.child_expression)

        if node.bool_arrow:
            self._w.write('->')
        else:
            self._w.write('.')

        self._w.write(node.txt_name)

    def visit_CastExprNode(self, node):
        self._w.write('(')
        self.visit(node.child0_cast_type)
        self._w.write(')')
        self.visit(node.child1_expression)

    def visit_TrivialCastExprNode(self, node):
        #         self._w.write('(')
        #         self.visit(node.child0_cast_type)
        #         self._w.write(')')
        self.visit(node.child_expression)

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

        self._writeArgumentListNode(node.child_argument_list)

    def visit_FunctionCallSubExprNode(self, node):

        self._w.write(node.ref_declaration.txt_name)

#         self._w.replaceTokens(node.ctx.start, node.ctx.stop,
#                               u"(%s)" % node.ref_declaration.txt_name)

    def visit_StatefullCallArgumentExprNode(self, node):
        # pylint: disable=unused-argument
        self._w.write("(void*)(sa_state + 1), sa_wf, sa_result")

    def _writeArgumentListNode(self, node, begin='(', end=')'):

        self._w.write(begin)

        first = True
        for each in node.childs_arguments:
            if not first:
                self._w.write(', ')
            first = False
            self.write_expr(each)

        self._w.write(end)

    def visit_SimpleTypeNode(self, node):

        if node.bool_const:
            self._w.write("const ")

        self._w.write(node.txt_name)

    def visit_PointerTypeNode(self, node):

        self.visit(node.child_pointed_type)
        self._w.write('*')
        if node.bool_const:
            self._w.write(" const")


class _HeaderWriterVisitor(_WriterVisitor):

    '''
    Visitor class for plugin header write
    '''

    def __init__(self, compiler, source_file):
        '''
        Constructor
        '''
        super(_HeaderWriterVisitor, self).__init__(compiler, source_file)

    def visit_RootNode(self, node):

        nb = node.get_scope(NonBlockingData)

        self._w.write_line("#if !defined %s" % nb.include_guard)
        self._w.write_line("#define %s" % nb.include_guard)
        self._w.write_line("")

        self._w.write_line("#include <stdint.h>")
        self._w.write_line("")
        self._w.write_line("")

        for f in nb.functions_with_states:

            self._w.write_line("typedef struct _%s {" % f.txt_struct_name)

            self._w.write_line("uint8_t sa_next;")

            for v in f.refs_moved_var_decls:

                self.visit(v.child_declaration_type)
                self._w.write(' ')
                self._w.write(v.txt_name)

                self._w.write(';')
                self._w.end_of_statement(v.ctx.stop)

            self._w.write_line("} %s;" % f.txt_struct_name)
            self._w.write_line("")

        self._w.write_line("#endif // %s" % nb.include_guard)


class _Writer(object):

    '''
    Visitor class for plugin rewrite
    '''

    def __init__(self, source_file):
        '''
        Constructor
        '''
        super(_Writer, self).__init__()
        self._source_file = source_file
        self._buffer = banner.get_copyright_banner2()
        self._current = ''
        self._line = 0

        self._buffer.append("")

    def end_of_statement(self, ctx):
        if len(self._current) != 0:
            if ctx is not None:
                if self._line == 0:
                    self._buffer.append('#line %s "%s"' % (ctx.line,
                                                           self._source_file))
                    self._line = ctx.line
                elif ctx.line == self._line:
                    pass
                elif ctx.line > self._line and ctx.line < self._line + 4:
                    while ctx.line != self._line:
                        self._buffer.append("")
                        self._line += 1
                else:
                    self._buffer.append('#line %s "%s"' % (ctx.line,
                                                           self._source_file))
                    self._line = ctx.line

            self._buffer.append(self._current)
            self._line += 1
            self._current = ''

    def get_text(self):
        assert self._current == ''

        txt = ""
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
        assert line is not None
        self._buffer.append(line)
        self._line += 1
