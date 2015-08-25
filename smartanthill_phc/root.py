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

from smartanthill_phc.common.lookup import RootScope
from smartanthill_phc.common.node import Node, DeclarationListNode


class PluginSourceNode(Node):

    '''
    Node class container of a source program
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PluginSourceNode, self).__init__()
        self.child_declaration_list = None

    def set_declaration_list(self, child):
        '''
        statement list setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_declaration_list = child

    def resolve(self, compiler):
        compiler.resolve_node(self.child_declaration_list)


class NonBlockingData(object):

    '''
    Helper container for state machine related info
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.refs_moved_var_decls = []

    def is_moved_var_decl(self, decl):
        '''
        Checks if a declaration was moved because of non-blocking modifications
        '''
        return decl in self.refs_moved_var_decls


class RootNode(Node):

    '''
    Root node class used as root of the tree
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(RootNode, self).__init__()
        self.child_builtins = None
        self.child_source = None
        self.add_scope(RootScope, RootScope(self))
        self.add_scope(NonBlockingData, NonBlockingData())

    def set_builtins(self, child):
        '''
        built-ins setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_builtins = child

    def set_source(self, child):
        '''
        program setter
        '''
        assert isinstance(child, PluginSourceNode)
        child.set_parent(self)
        self.child_source = child

    def resolve(self, compiler):
        # First built-ins
        compiler.resolve_node(self.child_builtins)
        # Last user code
        compiler.resolve_node(self.child_source)
