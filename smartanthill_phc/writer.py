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
from smartanthill_phc.common import antlr_helper, decl
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


def write_parser(compiler, root):
    '''
    Write header file
    '''
    visitor = _ParserWriterVisitor(compiler, None)
    visit_node(visitor, root)

    text = visitor.get_text()
    compiler.check_stage('parser')

    return text


def _map_parser_type_name(name):

    if name == 'uint8_t':
        return 'byte'
    elif name == 'uint16_t':
        return 'encoded_uint16'
    elif name == 'int16_t':
        return 'encoded_signed_int16'
    else:
        assert False


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
        if isinstance(self._func.return_type.get().ref_type_declaration,
                      VoidTypeDeclNode):
            self._w.write_line("return;")
        elif isinstance(self._func.return_type.get().ref_type_declaration,
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

    def write_expr(self, expr_box):

        if expr_box.get().bool_parenthesis:
            self._w.write('(')
        self.visit(expr_box)
        if expr_box.get().bool_parenthesis:
            self._w.write(')')

    def visit_RootNode(self, node):
        self._nb = node.get_scope(NonBlockingData)
        self.visit(node.source)

    def visit_PluginSourceNode(self, node):
        self._w.write_line('#include "%s_state.h"' % node.txt_prefix)
        self.visit_childs(node)

    def visit_DeclarationListNode(self, node):
        self.visit_childs(node)

    def visit_PreprocessorDirectiveNode(self, node):
        self._w.write_line(node.txt_body)

    def visit_ConstantDefineNode(self, node):
        self._w.write("#define ")
        self._w.write(node.txt_name)
        self._w.write(" ")
        self.write_expr(node.expression)
        self._w.end_of_statement(node.ctx)

    def visit_FunctionDefinitionNode(self, node):
        self.visit_childs(node)

    def visit_FunctionDeclNode(self, node):

        self._func = node
        if self._nb is not None:
            self._sm = self._nb.get_state_machine_data(node)
        else:
            self._sm = None

        if node.bool_static:
            self._w.write("static ")

        if node.bool_inline:
            self._w.write("inline ")

        self.visit(node.return_type)
        self._w.write(' ')
        self._w.write(node.txt_name)
        self._w.write('(')

        first = True
        if self._sm is not None and\
                not self._sm.ref_state_machine.is_main_machine():
            self._w.write(
                "void* sa_state0, waiting_for* sa_wf, uint8_t* sa_result")
            first = False

        for each in node.argument_decl_list.get().declarations:

            if not first:
                self._w.write(', ')
            first = False
            self.visit(each.get().argument_type)
            if each.get().txt_name is not None:
                self._w.write(' ')
                self._w.write(each.get().txt_name)

        self._w.write(')')

        if not isinstance(node.get_parent(), decl.FunctionDefinitionNode):
            self._w.write(';')  # TODO improve

        self._w.end_of_statement(node.ctx, True)

    def visit_StructTypeDeclNode(self, node):

        self._w.write(node.txt_name)
        self._w.end_of_statement(node.ctx, True)
        self._w.write_line('{')
        for each in node.members:
            self.visit(each)
        self._w.write_line('};')

    def visit_AttributeDeclarationNode(self, node):

        self.visit(node.declaration_type)
        self._w.write(' ')
        self._w.write(node.txt_name)
        self._w.write(';')
        self._w.end_of_statement(node.ctx)

    def visit_StmtListNode(self, node):
        self._w.write_line('{')

        for each in node.statements:
            self.visit(each)

        self._w.write_line('}')

    def visit_NopStmtNode(self, node):
        # pylint: disable=unused-argument
        # Nothing to do here
        self._w.write(';')
        self._w.end_of_statement(node.ctx)

    def visit_VariableDeclarationStmtNode(self, node):

        if self._sm is not None and\
                self._sm.is_moved_var_decl(node):
            if not node.initializer_expression.is_none():

                self._w.write('sa_state->')
                self._w.write(node.txt_name)

                self._w.write(' = ')
                self.write_expr(node.initializer_expression)

                self._w.write(';')
                self._w.end_of_statement(node.ctx)

        else:
            self.visit(node.declaration_type)
            self._w.write(' ')
            self._w.write(node.txt_name)
            if not node.initializer_expression.is_none():
                self._w.write(' = ')
                self.write_expr(node.initializer_expression)

            self._w.write(';')
            self._w.end_of_statement(node.ctx)

    def visit_ExpressionStmtNode(self, node):
        self.write_expr(node.expression)
        self._w.write(';')
        self._w.end_of_statement(node.ctx)

    def visit_FunctionCallStmtNode(self, node):
        self.write_expr(node.expression)
        self._w.write(';')
        self._w.end_of_statement(node.ctx)

        if node.expression.get().bool_is_blocking:
            assert False

    def visit_PapiWaitStmtNode(self, node):
        self._w.write(node.txt_name)
        self._writeArgumentListNode(node.argument_list.get())
        self._w.write(';')
        self._w.end_of_statement(node.ctx)

        self._w.write("papi_wait_handler_add_wait_for_")
        self._w.write(node.txt_wait_for)
        self._w.write("(sa_wf, ")
        self.write_expr(node.argument_list.get().arguments.at(0))
        self._w.write(')')
        self._w.write(';')
        self._w.end_of_statement(None)

        self._w.write_line("sa_state->sa_next = %s;" % node.int_next_state)
        self._write_result_return("PLUGIN_WAITING")

        self._w.write("label_%s:" % node.int_next_state)

        self._w.write("if(papi_wait_handler_is_waiting_for_")
        self._w.write(node.txt_wait_for)
        self._w.write("(sa_wf, ")
        self.write_expr(node.argument_list.get().arguments.at(0))
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
        self.write_expr(node.argument_list.get().arguments.at(0))
        self._w.write(')')
        self._w.write(';')
        self._w.end_of_statement(node.ctx)

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
        self.write_expr(node.expression)
        self._w.write(')')
        self._w.end_of_statement(node.ctx, True)
        self.visit(node.statement_list)

    def visit_DoWhileStmtNode(self, node):
        self._w.write('do')
        self._w.end_of_statement(node.ctx, True)
        self.visit(node.statement_list)
        self._w.write('while')
        self._w.write('(')
        self.write_expr(node.expression)
        self._w.write(');')
        self._w.end_of_statement(node.ctx)

    def visit_ForStmtNode(self, node):
        self._w.write('for')
        self._w.write('(')
        if not node.init_expression.is_none():
            self.write_expr(node.init_expression)
        self._w.write(';')
        if not node.condition_expression.is_none():
            self._w.write(' ')
            self.write_expr(node.condition_expression)
        self._w.write('; ')
        if not node.iteration_expression.is_none():
            self._w.write(' ')
            self.write_expr(node.iteration_expression)
        self._w.write(')')
        self._w.end_of_statement(node.ctx, True)
        self.visit(node.statement_list)

    def visit_ReturnStmtNode(self, node):

        self._w.write('return')
        if not node.expression.is_none():
            self._w.write(' ')
            self.write_expr(node.expression)

        self._w.write(';')
        self._w.end_of_statement(node.ctx)

    def visit_TypedefStmtNode(self, node):

        self._w.write('typedef ')
        self.visit(node.typedef_type)
        self._w.write(' ')
        self._w.write(node.txt_name)
        self._w.write(';')
        self._w.end_of_statement(node.ctx)

    def visit_IfElseStmtNode(self, node):

        self._w.write('if')
        self._w.write('(')
        self.write_expr(node.expression)
        self._w.write(')')
        self._w.end_of_statement(node.ctx, True)
        self.visit(node.if_stmt_list)
        if not node.else_stmt_list.is_none():
            self._w.write('else')
            self._w.end_of_statement(None)
            self.visit(node.else_stmt_list)

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

        self.visit(node.expression.get().ref_declaration.return_type)
        self._w.write(' ')
        self._w.write(node.txt_name)
        self._w.write(' = ')
        self.visit(node.expression)
        self._w.write(';')
        self._w.end_of_statement(node.ctx)

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

    def visit_ParserStmtNode(self, node):

        self.visit(node.struct_type)
        self._w.write(" sa_res;")
        self._w.end_of_statement(None)

        for each in node.parser_elements:
            pn = _map_parser_type_name(each.c_type)
            self._w.write_line("sa_res.%s = papi_parser_read_%s(sa_po);" %
                               (each.name, pn))

        self._w.write_line("return sa_res;")

    def visit_ComposerStmtNode(self, node):

        for each in node.parser_elements:
            pn = _map_parser_type_name(each.c_type)
            self._w.write_line("papi_reply_write_%s(sa_rh, %s);" %
                               (pn, each.name))

    def visit_AssignmentExprNode(self, node):

        self.write_expr(node.left_expression)
        self._w.write('=')
        self.write_expr(node.right_expression)

    def visit_ConditionalExprNode(self, node):

        self.write_expr(node.condition_expression)
        self._w.write('?')
        self.write_expr(node.true_expression)
        self._w.write(':')
        self.write_expr(node.false_expression)

    def visit_BinaryOpExprNode(self, node):
        assert node.argument_list.get().arguments.get_size() == 2
        self.write_expr(node.argument_list.get().arguments.at(0))
        self._w.write(node.txt_operator)
        self.write_expr(node.argument_list.get().arguments.at(1))

    def visit_MemberBinaryOpExprNode(self, node):
        assert node.argument_list.get().arguments.get_size() == 1
        self.write_expr(node.expression)
        self._w.write(node.txt_operator)
        self.write_expr(node.argument_list.get().arguments.at(0))

    def visit_UnaryOpExprNode(self, node):
        assert node.argument_list.get().arguments.get_size() == 0
        self._w.write(node.txt_operator)
        self.write_expr(node.expression)

    def visit_PostUnaryOpExprNode(self, node):
        assert node.argument_list.get().arguments.get_size() == 0
        self.write_expr(node.expression)
        self._w.write(node.txt_operator[4:])

    def visit_IndexExprNode(self, node):
        assert node.argument_list.get().arguments.get_size() == 2
        self.write_expr(node.expression)
        self._w.write('[')
        self.write_expr(node.argument_list.get().arguments.at(0))
        self._w.write(']')

    def visit_PointerExprNode(self, node):
        self._w.write('*')
        self.write_expr(node.expression)

    def visit_AddressOfExprNode(self, node):
        self._w.write('&')
        self.write_expr(node.expression)

    def visit_LiteralExprNode(self, node):
        self._w.write(node.txt_literal)

    def visit_MemberAccessExprNode(self, node):

        self.write_expr(node.expression)

        if node.bool_arrow:
            self._w.write('->')
        else:
            self._w.write('.')

        self._w.write(node.txt_name)

    def visit_CastExprNode(self, node):
        self._w.write('(')
        self.visit(node.cast_type)
        self._w.write(')')
        self.write_expr(node.expression)

    def visit_TrivialCastExprNode(self, node):
        #         self._w.write('(')
        #         self.visit(node.child0_cast_type)
        #         self._w.write(')')
        self.write_expr(node.expression)

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

        self._writeArgumentListNode(node.argument_list.get())

    def visit_FunctionCallSubExprNode(self, node):

        self._w.write(node.ref_declaration.txt_name)

#         self._w.replaceTokens(node.ctx.start, node.ctx.stop,
#                               u"(%s)" % node.ref_declaration.txt_name)

    def visit_StatefullCallArgumentExprNode(self, node):
        # pylint: disable=unused-argument
        self._w.write("(void*)(sa_state + 1), sa_wf, sa_result")

    def _writeArgumentListNode(self, node):

        self._w.write('(')

        first = True
        for each in node.arguments:
            if not first:
                self._w.write(', ')
            first = False
            self.write_expr(each)

        self._w.write(')')

    def visit_RefTypeNode(self, node):

        self._w.write(node.get_type().to_string())

    def visit_SimpleTypeNode(self, node):

        if node.bool_const:
            self._w.write("const ")

        self._w.write(node.txt_name)

    def visit_PointerTypeNode(self, node):

        self.visit(node.pointed_type)
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

                self.visit(v.declaration_type)
                self._w.write(' ')
                self._w.write(v.txt_name)

                self._w.write(';')
                self._w.end_of_statement(v.ctx)

            self._w.write_line("} %s;" % f.txt_struct_name)
            self._w.write_line("")

        self._w.write_line("#endif // %s" % nb.include_guard)


class _ParserWriterVisitor(_WriterVisitor):

    '''
    Visitor class for plugin header write
    '''

    def __init__(self, compiler, source_file):
        '''
        Constructor
        '''
        super(_ParserWriterVisitor, self).__init__(compiler, source_file)

    def visit_RootNode(self, node):
        self.visit(node.manifest)

    def visit_PluginManifestNode(self, node):

        include_guard = "__SA_%s_PLUGIN_H__" % node.txt_prefix.upper()

        self._w.write_line("#if !defined %s" % include_guard)
        self._w.write_line("#define %s" % include_guard)
        self._w.write_line("")

        self._w.write_line("#include <stdint.h>")
        self._w.write_line("#include \"papi.h\"")
        self._w.write_line("")

        self.visit_childs(node)

        self._w.write_line("")
        self._w.write_line(
            "typedef struct _%s_plugin_persistent_state" % node.txt_prefix)
        self._w.write_line("{")
        self._w.write_line("uint8_t sa_dummy;")
        self._w.write_line(
            "} %s_plugin_persistent_state;" % node.txt_prefix)

        self._w.write_line("")
        self._w.write_line("#ifdef __cplusplus")
        self._w.write_line('extern "C" {')
        self._w.write_line("#endif")
        self._w.write_line("")
        self._w.write_line("uint8_t %s_plugin_handler_init("
                           " const void* plugin_config,"
                           " void* plugin_state );" % node.txt_prefix)
        self._w.write_line("uint8_t %s_plugin_exec_init("
                           " const void* plugin_config,"
                           " void* plugin_state );" % node.txt_prefix)
        self._w.write_line("uint8_t %s_plugin_handler("
                           " const void* plugin_config,"
                           " void* plugin_persistent_state,"
                           " void* plugin_state, ZEPTO_PARSER* command,"
                           " MEMORY_HANDLE reply, waiting_for* wf,"
                           " uint8_t first_byte );" % node.txt_prefix)
        self._w.write_line("")
        self._w.write_line("#ifdef __cplusplus")
        self._w.write_line("}")
        self._w.write_line("#endif")
        self._w.write_line("")

        self._w.write_line("#endif // %s" % include_guard)


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

    def end_of_statement(self, ctx, use_first=False):
        if len(self._current) != 0:
            lines = antlr_helper.get_reference_lines(ctx)
            if lines is not None:
                l = lines[0] if use_first else lines[1]
                if self._line == 0:
                    self._buffer.append('#line %s "%s"' % (l,
                                                           self._source_file))
                    self._line = l
                elif l == self._line:
                    pass
                elif l > self._line and l < self._line + 4:
                    while l != self._line:
                        self._buffer.append("")
                        self._line += 1
                else:
                    self._buffer.append('#line %s "%s"' % (l,
                                                           self._source_file))
                    self._line = l

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
