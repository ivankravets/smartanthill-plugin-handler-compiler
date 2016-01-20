# Copyright (C) 2016 OLogN Technologies AG
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

from smartanthill_phc import c_node, builtin
from smartanthill_phc.common import base
from smartanthill_phc.common.child import ChildList
from smartanthill_phc.common.compiler import Ctx


def make_pointer_of(compiler, type_decl):
    '''
    Creates a pointer to a type declaration, if not already there
    '''
    if type_decl.pointer.is_none():
        d = compiler.init_node(
            PointerTypeDeclNode(type_decl.txt_name), Ctx.INTERNAL)
        d.ref_pointer_of = type_decl

        for each in builtin.make_pointer_operators(compiler, Ctx.INTERNAL, d):
            d.members.add(each)

        type_decl.pointer.set(d)

    return type_decl.pointer.get()


def get_pointed_by(compiler, ctx, type_decl):
    '''
    Returns the type pointed by this type
    Only implemented by pointer types
    '''

    if isinstance(
            type_decl, PointerTypeDeclNode):
        return type_decl.ref_pointer_of
    else:
        compiler.report_error(
            ctx,
            "Invalid pointer dereference on expression of type '%s'" %
            type_decl.to_string())
        compiler.raise_error()


class PointerTypeDeclNode(c_node.CTypeDeclNode):

    '''
    Basic, built-in types are implemented using this class
    '''

    def __init__(self, pointed_name):
        '''
        Constructor
        '''
        super(PointerTypeDeclNode, self).__init__(pointed_name + '*')
        self.members = ChildList(self, base.Node)
        self.ref_pointer_of = None
