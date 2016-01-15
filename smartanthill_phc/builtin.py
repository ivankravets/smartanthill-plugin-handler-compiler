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
from smartanthill_phc.c_node import VoidTypeDeclNode, IntTypeDeclNode,\
    BasicTypeDeclNode, PapiFunctionDeclNode
from smartanthill_phc.common import decl
from smartanthill_phc.common.base import DeclarationListNode


def create_builtins(compiler, ctx):
    '''
    Creates all built in nodes and adds them to the root
    '''

    decls = compiler.init_node(DeclarationListNode(), ctx)
    decls.declarations.add(
        compiler.init_node(VoidTypeDeclNode(), ctx))

    decls.declarations.add(
        compiler.init_node(BasicTypeDeclNode('_zc_dont_care'), ctx))

    decls.declarations.add(
        compiler.init_node(BasicTypeDeclNode('sa_int_literal'), ctx))
    decls.declarations.add(
        compiler.init_node(BasicTypeDeclNode('sa_bool_literal'), ctx))

    _make_integer(compiler, ctx, decls)
    _make_bool(compiler, ctx, decls)

    decls.declarations.add(compiler.init_node(
        PapiFunctionDeclNode('papi_sleep'), ctx))
    decls.declarations.add(compiler.init_node(
        PapiFunctionDeclNode('papi_wait_for_spi_send'), ctx))
    decls.declarations.add(compiler.init_node(
        PapiFunctionDeclNode('papi_wait_for_i2c_send'), ctx))
    decls.declarations.add(compiler.init_node(
        PapiFunctionDeclNode('papi_wait_for_spi_receive'), ctx))
    decls.declarations.add(compiler.init_node(
        PapiFunctionDeclNode('papi_wait_for_i2c_receive'), ctx))

    compiler.check_stage('built_in')

    return decls


def _make_integer(compiler, ctx, decls):

    tn = compiler.init_node(IntTypeDeclNode('uint8_t'), ctx)
    ol = compiler.init_node(DeclarationListNode(), ctx)
    tn.operator_decl_list.set(ol)

    decls.declarations.add(tn)
    _make_integer_operators(compiler, ctx, tn, decls, ol)

    casts = compiler.init_node(DeclarationListNode(), ctx)

    c0 = compiler.init_node(c_node.TrivialCastRuleNode(), ctx)

    t0 = compiler.init_node(c_node.SimpleTypeNode(), ctx)
    t0.txt_name = 'sa_int_literal'

    t1 = compiler.init_node(c_node.RefTypeNode(), ctx)
    t1.set_type(tn)

    c0.source_type.set(t0)
    c0.target_type.set(t1)

    casts.declarations.add(c0)
    tn.cast_rules_list.set(casts)


def _make_integer_operators(compiler, ctx, tn, decls, membs):

    decls.declarations.add(_make_op(compiler, ctx, '+', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '-', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '*', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '/', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '%', tn, [tn, tn]))

    decls.declarations.add(_make_op(compiler, ctx, '<', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '>', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '<=', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '>=', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '==', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '!=', tn, [tn, tn]))

    decls.declarations.add(_make_op(compiler, ctx, '&', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '^', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '|', tn, [tn, tn]))

#     g.append(_make_op(compiler, ctx, '>>', tn, [tn, tn]))
#     g.append(_make_op(compiler, ctx, '<<', tn, [tn, tn]))

    membs.declarations.add(_make_op(compiler, ctx, '+', tn, []))
    membs.declarations.add(_make_op(compiler, ctx, '-', tn, []))
    membs.declarations.add(_make_op(compiler, ctx, '~', tn, []))

    membs.declarations.add(_make_op(compiler, ctx, '++', tn, []))
    membs.declarations.add(_make_op(compiler, ctx, '--', tn, []))
    membs.declarations.add(_make_op(compiler, ctx, 'post++', tn, []))
    membs.declarations.add(_make_op(compiler, ctx, 'post--', tn, []))

    decls.declarations.add(_make_op(compiler, ctx, '+=', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '-=', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '*=', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '/=', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '%=', tn, [tn, tn]))

    decls.declarations.add(_make_op(compiler, ctx, '&=', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '^=', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '|=', tn, [tn, tn]))

#     m.append(_make_op(compiler, ctx, '<<=', tn, [tn]))
#     m.append(_make_op(compiler, ctx, '>>=', tn, [tn]))

    membs.declarations.add(_make_op(compiler, ctx, '[]', tn, [tn]))


def _make_bool(compiler, ctx, decls):

    tn = compiler.init_node(IntTypeDeclNode('bool'), ctx)
    ol = compiler.init_node(DeclarationListNode(), ctx)
    tn.operator_decl_list.set(ol)

    decls.declarations.add(tn)
    _make_bool_operators(compiler, ctx, tn, decls)

    casts = compiler.init_node(DeclarationListNode(), ctx)

    c0 = compiler.init_node(c_node.TrivialCastRuleNode(), ctx)

    t0 = compiler.init_node(c_node.SimpleTypeNode(), ctx)
    t0.txt_name = 'sa_bool_literal'

    t1 = compiler.init_node(c_node.RefTypeNode(), ctx)
    t1.set_type(tn)

    c0.source_type.set(t0)
    c0.target_type.set(t1)

    casts.declarations.add(c0)
    tn.cast_rules_list.set(casts)


def _make_bool_operators(compiler, ctx, tn, decls):

    decls.declarations.add(_make_op(compiler, ctx, '==', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '!=', tn, [tn, tn]))

    decls.declarations.add(_make_op(compiler, ctx, '&&', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '||', tn, [tn, tn]))
    decls.declarations.add(_make_op(compiler, ctx, '!', tn, [tn]))


def _make_op(compiler, ctx, op_name, return_type, arg_types):

    d = compiler.init_node(c_node.OperatorDeclNode(), ctx)
    d.txt_name = op_name

    rt = compiler.init_node(c_node.RefTypeNode(), ctx)
    rt.set_type(return_type)

    d.return_type.set(rt)

    args = compiler.init_node(decl.ArgumentDeclListNode(), ctx)
    for each in arg_types:
        a = compiler.init_node(decl.ArgumentDeclNode(), ctx)
        at = compiler.init_node(c_node.RefTypeNode(), ctx)
        at.set_type(each)

        a.argument_type.set(at)
        args.declarations.add(a)

    d.argument_decl_list.set(args)

    return d
