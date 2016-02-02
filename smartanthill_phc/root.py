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

from smartanthill_phc.common.base import Node, DeclarationListNode, Child
from smartanthill_phc.common.child import ChildList
from smartanthill_phc.common.lookup import RootScope


class PluginSourceNode(Node):

    '''
    Node class container of a source program
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PluginSourceNode, self).__init__()
        self.declaration_list = Child(self, DeclarationListNode)


class PluginManifestNode(Node):

    '''
    Node class container of a code representation of data in plugin manifest
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PluginManifestNode, self).__init__()
        self.txt_prefix = None
        self.txt_include_guard = None
        self.elements = ChildList(self, Node)


class StateMachineData(object):

    '''
    Helper container for state machine related info
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.ref_function_decl = None
        self.refs_moved_var_decls = None
        self.ref_state_machine = None
        self.txt_struct_name = None

    def is_moved_var_decl(self, decl):
        '''
        Checks if a declaration was moved because of non-blocking modifications
        '''
        return decl in self.refs_moved_var_decls


class NonBlockingData(object):

    '''
    Helper container for state machine related info
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.functions_with_states = []
        self.state_name = None
        self.include_guard = None
        self.handler_name = None
        self.handler_init_name = None
        self.exec_init_name = None

    def set_prefix(self, prefix):

        self.state_name = prefix + "_plugin_state"
        self.include_guard = "__SA_%s_PLUGIN_STATE_H__" % prefix.upper()
        self.handler_name = prefix + "_plugin_handler"
        self.handler_init_name = prefix + "_plugin_handler_init"
        self.exec_init_name = prefix + "_plugin_exec_init"

    def has_sub_machines(self):
        '''
        Returns true if there are more than one function with states
        '''
        return len(self.functions_with_states) > 1

    def get_state_machine_data(self, func):
        '''
        Returns the state machine data of a function
        '''
        for each in self.functions_with_states:
            if each.ref_function_decl == func:
                return each

        return None

    def has_states(self, func_decl):
        '''
        Returns true if function has states
        '''

        for each in self.functions_with_states:
            if each.ref_function_decl == func_decl:
                return True

        return False

    def add_function_with_states(self, func, sm, moved_vars):

        tmp = StateMachineData()
        tmp.ref_function_decl = func
        tmp.refs_moved_var_decls = moved_vars
        tmp.ref_state_machine = sm

        tmp.txt_struct_name = self.state_name

        if func.txt_name != self.handler_name:
            tmp.txt_struct_name += str(
                len(self.functions_with_states) + 1)

        assert not self.has_states(func)
        self.functions_with_states.append(tmp)


class RootNode(Node):

    '''
    Root node class used as root of the tree
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(RootNode, self).__init__()
        self.builtins = Child(self, DeclarationListNode)
        self.manifest = Child(self, PluginManifestNode)
        self.papi = Child(self, PluginSourceNode, True)
        self.source = Child(self, PluginSourceNode, True)
        self.add_scope(RootScope, RootScope(self))
        self.add_scope(NonBlockingData, NonBlockingData())
