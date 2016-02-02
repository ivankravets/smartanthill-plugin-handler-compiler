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

from smartanthill_phc import c_node

from smartanthill_phc.common import decl
from smartanthill_phc.common.base import DeclarationListNode

_builtin_papi_defines = [
    "#define PLUGIN_OK 0",
    "#define PLUGIN_WAITING 1",
    "#define PLUGIN_DEBUG 2"
]


_builtin_typedefs = [
    "typedef void parser_obj;",
    "typedef void waiting_for;",
    "typedef uint8_t ZEPTO_PARSER;",
    "typedef uint8_t REPLY_HANDLE;",
    "typedef uint8_t MEMORY_HANDLE;",
    "typedef uint16_t SA_TIME_VAL;",
    "typedef uint32_t sa_size_type;"
]

_builtin_papi = [
    # pylint: disable=line-too-long
    "void ZEPTO_ASSERT(bool test);",


    "uint8_t papi_parser_read_byte( parser_obj* po );",
    "uint16_t papi_parser_read_encoded_uint16( parser_obj* po );",
    "uint16_t papi_parser_read_encoded_signed_int16( parser_obj* po );",

    "void papi_reply_write_byte( REPLY_HANDLE mem_h, uint8_t val );",
    "void papi_reply_write_encoded_uint16( REPLY_HANDLE mem_h, uint16_t num );",
    "void papi_reply_write_encoded_signed_int16( REPLY_HANDLE mem_h, int16_t sx );",

    "void papi_init_parser_with_parser( parser_obj* po, const parser_obj* po_base );",
    "bool papi_parser_is_parsing_done( parser_obj* po );",
    "uint16_t papi_parser_get_remaining_size( parser_obj* po );",

    "bool papi_eeprom_write( uint16_t plugin_id, const uint8_t* data );",
    "bool papi_eeprom_read( uint16_t plugin_id, uint8_t* data );",

    "void papi_eeprom_flush();",

    "bool papi_read_digital_pin( uint16_t pin_num );",
    "void papi_write_digital_pin( uint16_t pin_num, bool value );",

    "void papi_start_sending_spi_command_16( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint16_t command, uint8_t command_sz);",
    "void papi_start_sending_spi_command_32( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint32_t command, uint8_t command_sz);",
    "void papi_start_sending_i2c_command_16( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint16_t command, uint8_t command_sz);",
    "void papi_start_sending_i2c_command_32( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint32_t command, uint8_t command_sz);",

    "void papi_start_receiving_spi_data_16( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint16_t* data);",
    "void papi_start_receiving_spi_data_32( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint32_t* data);",
    "void papi_start_receiving_i2c_data_16( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint16_t* data);",
    "void papi_start_receiving_i2c_data_32( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint32_t* data);",

    "void papi_cancel_spi_send( uint8_t spi_id );",
    "void papi_cancel_spi_receive( uint8_t spi_id );",
    "void papi_cancel_i2c_send( uint8_t i2c_id );",
    "void papi_cancel_i2c_receive( uint8_t i2c_id );",

    "void papi_sleep( uint16_t millisec );",

    "void papi_wait_for_spi_send( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint16_t command, uint8_t command_sz );",
    "void papi_wait_for_i2c_send( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint16_t command, uint8_t command_sz );",
    "void papi_wait_for_spi_receive( uint8_t spi_id, uint16_t addr, uint8_t addr_sz, uint16_t* data );",
    "void papi_wait_for_i2c_receive( uint8_t i2c_id, uint16_t addr, uint8_t addr_sz, uint16_t* data );",
    "void papi_wait_for_wait_handler( waiting_for* wf );",

    "void papi_init_wait_handler( waiting_for* wf );",
    "void papi_wait_handler_add_wait_for_spi_send( waiting_for* wf, uint8_t spi_id );",
    "void papi_wait_handler_add_wait_for_i2c_send( waiting_for* wf, uint8_t i2c_id );",
    "void papi_wait_handler_add_wait_for_spi_receive( waiting_for* wf, uint8_t spi_id );",
    "void papi_wait_handler_add_wait_for_i2c_receive( waiting_for* wf, uint8_t i2c_id );",
    "void papi_wait_handler_add_wait_for_timeout( waiting_for* wf, SA_TIME_VAL tv );",
    "bool papi_wait_handler_is_waiting_for_spi_send( const waiting_for* wf, uint8_t spi_id );",
    "bool papi_wait_handler_is_waiting_for_i2c_send( const waiting_for* wf, uint8_t i2c_id );",
    "bool papi_wait_handler_is_waiting_for_spi_receive( const waiting_for* wf, uint8_t spi_id );",
    "bool papi_wait_handler_is_waiting_for_i2c_receive( const waiting_for* wf, uint8_t i2c_id );",
    "bool papi_wait_handler_is_waiting_for_timeout( SA_TIME_VAL* remaining, const waiting_for* wf );",

    "void papi_gravely_power_inefficient_micro_sleep( SA_TIME_VAL* timeval );"
]


_builtin_bool = [
    "@this-type @op ==( @this-type, @this-type );",
    "@this-type @op !=( @this-type, @this-type );",
    "@this-type @op &&( @this-type, @this-type );",
    "@this-type @op ||( @this-type, @this-type );"
]

_builtin_bool_member = [
    "@this-type @op !( );"
]
_builtin_int = [
    "@this-type @op +( @this-type, @this-type );",
    "@this-type @op -( @this-type, @this-type );",
    "@this-type @op *( @this-type, @this-type );",
    "@this-type @op /( @this-type, @this-type );",
    "@this-type @op %( @this-type, @this-type );",

    "@this-type @op &( @this-type, @this-type );",
    "@this-type @op ^( @this-type, @this-type );",
    "@this-type @op |( @this-type, @this-type );",

    "bool @op ==( @this-type, @this-type );",
    "bool @op !=( @this-type, @this-type );",
    "bool @op <( @this-type, @this-type );",
    "bool @op >( @this-type, @this-type );",
    "bool @op <=( @this-type, @this-type );",
    "bool @op >=( @this-type, @this-type );"
]

_builtin_int_member = [
    "@this-type @op +=( @this-type );",
    "@this-type @op -=( @this-type );",
    "@this-type @op *=( @this-type );",
    "@this-type @op /=( @this-type );",
    "@this-type @op %=( @this-type );",

    "@this-type @op &=( @this-type );",
    "@this-type @op ^=( @this-type );",
    "@this-type @op |=( @this-type );",

    "@this-type @op +( );",
    "@this-type @op -( );",
    "@this-type @op ~( );",

    "@this-type @op ++( );",
    "@this-type @op --( );",
    "@this-type @op post++( );",
    "@this-type @op post--( );"
]

_builtin_ptr_member = [
    "@this-type @op +( uint32_t );",
    "@this-type @op -( uint32_t );",
    "@this-type @op []( uint32_t );"
]


def create_builtins(compiler, ctx):
    '''
    Creates all built in nodes and adds them to the root
    '''

    decls = compiler.init_node(DeclarationListNode(), ctx)
    decls.declarations.add(compiler.init_node(c_node.VoidTypeDeclNode(), ctx))

    _make_basic_type(compiler, ctx, decls, '_zc_dont_care')
    _make_basic_type(compiler, ctx, decls, 'sa_int_literal')
    _make_basic_type(compiler, ctx, decls, 'sa_bool_literal')

    decls.declarations.add(_make_bool_lit(compiler, ctx, "true"))
    decls.declarations.add(_make_bool_lit(compiler, ctx, "false"))

    _make_bool(compiler, ctx, decls, ['sa_bool_literal', 'sa_int_literal'])
    _make_integer(compiler, ctx, decls, 'uint8_t', ['sa_int_literal'])
    _make_integer(
        compiler, ctx, decls, 'uint16_t', ['sa_int_literal', 'uint8_t'])
    _make_integer(
        compiler, ctx, decls, 'uint32_t', ['sa_int_literal', 'uint8_t',
                                           'uint16_t'])
    _make_integer(compiler, ctx, decls, 'int8_t', ['sa_int_literal'])
    _make_integer(
        compiler, ctx, decls, 'int16_t', ['sa_int_literal', 'int8_t'])

#     for each in _builtin_typedefs:
#         d = _pseudo_parse_typedef(compiler, ctx, each)
#         decls.declarations.add(d)

#     for each in _builtin_papi_defines:
#         d = _pseudo_parse_define(compiler, ctx, each)
#         decls.declarations.add(d)
#
#     for each in _builtin_papi:
#         d = pseudo_parser(compiler, ctx, each)
#         decls.declarations.add(d)

    return decls


def make_pointer_operators(compiler, ctx, this_type):
    '''
    Creates built in operators for each pointer type
    '''
    result = []
    for each in _builtin_ptr_member:
        op = _pseudo_parse_operator(compiler, ctx, each, this_type)
        result.append(op)
    return result


def _make_integer(compiler, ctx, decls, type_name, trivial_casts):

    tn = compiler.init_node(c_node.IntTypeDeclNode(type_name), ctx)
    ol = compiler.init_node(DeclarationListNode(), ctx)
    tn.operator_decl_list.set(ol)

    decls.declarations.add(tn)
    for each in _builtin_int:
        op = _pseudo_parse_operator(compiler, ctx, each, tn)
        decls.declarations.add(op)

    for each in _builtin_int_member:
        op = _pseudo_parse_operator(compiler, ctx, each, tn)
        ol.declarations.add(op)

    casts = compiler.init_node(DeclarationListNode(), ctx)

    for each in trivial_casts:
        c0 = compiler.init_node(c_node.TrivialCastRuleNode(), ctx)

        t0 = compiler.init_node(c_node.SimpleTypeNode(), ctx)
        t0.txt_name = each

        t1 = compiler.init_node(c_node.RefTypeNode(), ctx)
        t1.set_type(tn)

        c0.source_type.set(t0)
        c0.target_type.set(t1)

        casts.declarations.add(c0)

    tn.cast_rules_list.set(casts)


def _make_bool(compiler, ctx, decls, trivial_casts):

    tn = compiler.init_node(c_node.IntTypeDeclNode('bool'), ctx)
    ol = compiler.init_node(DeclarationListNode(), ctx)
    tn.operator_decl_list.set(ol)

    decls.declarations.add(tn)
    for each in _builtin_bool:
        op = _pseudo_parse_operator(compiler, ctx, each, tn)
        decls.declarations.add(op)

    for each in _builtin_bool_member:
        op = _pseudo_parse_operator(compiler, ctx, each, tn)
        ol.declarations.add(op)

    casts = compiler.init_node(DeclarationListNode(), ctx)

    for each in trivial_casts:
        c0 = compiler.init_node(c_node.TrivialCastRuleNode(), ctx)

        t0 = compiler.init_node(c_node.SimpleTypeNode(), ctx)
        t0.txt_name = each

        t1 = compiler.init_node(c_node.RefTypeNode(), ctx)
        t1.set_type(tn)

        c0.source_type.set(t0)
        c0.target_type.set(t1)

        casts.declarations.add(c0)

    tn.cast_rules_list.set(casts)


def _make_basic_type(compiler, ctx, decls, name):

    d = compiler.init_node(c_node.BasicTypeDeclNode(name), ctx)
    decls.declarations.add(d)


def _make_bool_lit(compiler, ctx, name):

    d = compiler.init_node(c_node.ConstantDefineNode(), ctx)
    d.txt_name = name

    e = compiler.init_node(c_node.BooleanLiteralExprNode(), ctx)
    e.txt_literal = name
    e.bool_value = name == "true"

    d.expression.set(e)

    return d


def _make_type_ref(compiler, ctx, name, this_type):

    if name == "@this-type":
        t = compiler.init_node(c_node.RefTypeNode(), ctx)
        t.set_type(this_type)
        return t
    else:
        t = compiler.init_node(c_node.SimpleTypeNode(), ctx)
        each = name
        ptr = t
        while each.endswith('*'):
            each = each[:-1]
            temp = compiler.init_node(c_node.PointerTypeNode(), ctx)
            temp.pointed_type.set(ptr)
            ptr = temp

        t.txt_name = each
        return t


def _pseudo_parse_operator(compiler, ctx, text, this_type):
    '''
    Pseudo parser, creates a function declaration from a line of text
    '''
    t = _pseudo_tokenize(text)
    assert len(t) >= 2
    assert t[1] == "@op"

    d = compiler.init_node(c_node.OperatorDeclNode(), ctx)
    rt = _make_type_ref(compiler, ctx, t[0], this_type)
    d.return_type.set(rt)
    d.txt_name = t[2]

    args = compiler.init_node(decl.ArgumentDeclListNode(), ctx)
    i = 3
    while i < len(t):
        a = compiler.init_node(decl.ArgumentDeclNode(), ctx)
        at = _make_type_ref(compiler, ctx, t[i], this_type)
        a.argument_type.set(at)
#        a.txt_name = t[i + 1]
        args.declarations.add(a)
        i += 1

    d.argument_decl_list.set(args)

    return d


def _pseudo_parse_define(compiler, ctx, text):
    '''
    creates a define constant declaration from a line of text
    '''
    t = _pseudo_tokenize(text)
    assert len(t) == 3
    assert t[0] == "#define"

    d = compiler.init_node(c_node.ConstantDefineNode(), ctx)
    d.txt_name = t[1]

    e = compiler.init_node(c_node.IntegerLiteralExprNode(), ctx)
    e.txt_literal = t[2]
    e.int_value = int(t[2])

    d.expression.set(e)

    return d


def _pseudo_parse_typedef(compiler, ctx, text):
    '''
    creates a define constant declaration from a line of text
    '''
    t = _pseudo_tokenize(text)
    assert len(t) == 3
    assert t[0] == "typedef"

    tpd = compiler.init_node(c_node.TypedefStmtNode(), ctx)
    tpd.txt_name = t[2]
    tpd.typedef_type.set(_pseudo_parse_type(compiler, ctx, t[1]))

    return tpd


def pseudo_parser(compiler, ctx, text):
    '''
    Pseudo parser, creates a function declaration from a line of text
    '''
    t = _pseudo_tokenize(text)
    assert len(t) >= 2

    d = compiler.init_node(decl.FunctionDeclNode(), ctx)
    rt = compiler.init_node(c_node.SimpleTypeNode(), ctx)
    rt.txt_name = t[0]
    d.return_type.set(rt)
    d.txt_name = t[1]

    args = compiler.init_node(decl.ArgumentDeclListNode(), ctx)
    i = 2
    while i < len(t):
        a = compiler.init_node(decl.ArgumentDeclNode(), ctx)
        at = compiler.init_node(c_node.SimpleTypeNode(), ctx)
        each = t[i]
        if each == 'const':
            at.add_qualifier(compiler, ctx, each)
            i += 1
            each = t[i]
        ptr = at
        while each.endswith('*'):
            each = each[:-1]
            temp = compiler.init_node(c_node.PointerTypeNode(), ctx)
            temp.pointed_type.set(ptr)
            ptr = temp

        at.txt_name = each
        a.argument_type.set(ptr)
        a.txt_name = t[i + 1]
        args.declarations.add(a)
        i += 2

    d.argument_decl_list.set(args)

    return d


def _pseudo_parse_type(compiler, ctx, text):
    at = compiler.init_node(c_node.SimpleTypeNode(), ctx)
    each = text
    ptr = at
    while each.endswith('*'):
        each = each[:-1]
        temp = compiler.init_node(c_node.PointerTypeNode(), ctx)
        temp.pointed_type.set(ptr)
        ptr = temp

    at.txt_name = each
    return ptr


def _pseudo_tokenize(text):
    '''
    Pseudo tokenizer that splits a code string into an array used by pseudo
    parsers in this file
    '''
    text = text.replace('(', ' ')
    text = text.replace(',', ' ')
    text = text.replace(')', ' ')
    text = text.replace(';', ' ')
    return text.split()
