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

from smartanthill_phc.c_node import VoidTypeDeclNode, IntTypeDeclNode,\
    BasicTypeDeclNode, PapiFunctionDeclNode
from smartanthill_phc.common.base import DeclarationListNode


def create_builtins(compiler, ctx):
    '''
    Creates all built in nodes and adds them to the root
    '''

    decls = compiler.init_node(DeclarationListNode(), ctx)
    decls.add_declaration(
        compiler.init_node(VoidTypeDeclNode(), ctx))
    decls.add_declaration(
        compiler.init_node(IntTypeDeclNode('uint8_t'), ctx))
    decls.add_declaration(
        compiler.init_node(IntTypeDeclNode('bool'), ctx))
    decls.add_declaration(
        compiler.init_node(IntTypeDeclNode('_Bool'), ctx))

    decls.add_declaration(
        compiler.init_node(BasicTypeDeclNode('_zc_dont_care'), ctx))

    decls.add_declaration(compiler.init_node(
        PapiFunctionDeclNode('papi_sleep'), ctx))
    decls.add_declaration(compiler.init_node(
        PapiFunctionDeclNode('papi_wait_for_spi_send'), ctx))
    decls.add_declaration(compiler.init_node(
        PapiFunctionDeclNode('papi_wait_for_i2c_send'), ctx))
    decls.add_declaration(compiler.init_node(
        PapiFunctionDeclNode('papi_wait_for_spi_receive'), ctx))
    decls.add_declaration(compiler.init_node(
        PapiFunctionDeclNode('papi_wait_for_i2c_receive'), ctx))

    compiler.check_stage('built_in')

    return decls
