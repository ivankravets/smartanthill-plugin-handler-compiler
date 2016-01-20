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


def lookup_type(name, root_scope, stmt_scope):
    '''
    Type lookup algorithm
    Will lookup for typedef in every StatementListScope,
    if not found will lookup for type or typedef at RootScope
    '''

    while stmt_scope is not None:
        t = stmt_scope.typedefs.lookup(name)
        if t is not None:
            return t.get_type()

        stmt_scope = stmt_scope.get_parent_scope()

    # If we reach here stmt_scope is None, and name was not found

    assert root_scope is not None
    t = root_scope.typedefs.lookup(name)
    if t is not None:
        return t.get_type()

    return root_scope.types.lookup(name)


def lookup_variable(name, scope):
    '''
    Variable lookup algorithm
    It will look up name in this scope,
    and if not found it will look up in the containing scope recursively
    until either it is found, or no more scopes are available
    '''
    assert scope is not None

    while scope is not None:
        v = scope.variables.lookup(name)
        if v is not None:
            return v

        scope = scope.get_parent_scope()

    return None


class BaseScope(object):

    def __init__(self, owner):
        '''
        Constructor
        '''
        super(BaseScope, self).__init__()
        self._owner = owner
        self._data = {}

    def get_parent_scope(self):
        return self._owner.get_parent_scope(type(self))

    def reserved_name(self, helper, compiler, name, node):
        if name in self._data and self._data[name] != helper:
            compiler.report_error(
                node.ctx, "Redeclaration of '%s'" % name)
            compiler.report_error(
                self._data[name].ctx, "Previous was here")

            return True

        else:
            self._data[name] = helper
            return False


class LookupHelper(object):

    def __init__(self, reserver, overloadable=False):
        '''
        Constructor
        '''
        self._reserver = reserver
        self._overloadable = overloadable
        self._data = {}

    def add(self, compiler, name, node):
        '''
        Adds an operator
        '''
        if self._reserver.reserved_name(self, compiler, name, node):
            return

        if self._overloadable:
            if name not in self._data:
                self._data[name] = []

            self._data[name].append(node)
        else:
            if name in self._data:
                compiler.report_error(
                    node.ctx, "Redeclaration of '%s'" % name)
                compiler.report_error(
                    self._typedefs[name].ctx, "Previous was here")
                return
            else:
                self._data[name] = node

    def lookup(self, name):
        '''
        Looks up an operator
        '''
        return self._data[name] if name in self._data else None


class StatementListScope(BaseScope):

    '''
    The scope created by statement lists, where variables are look up
    '''

    def __init__(self, owner):
        '''
        Constructor
        '''
        super(StatementListScope, self).__init__(owner)

        self.variables = LookupHelper(self)
        self.typedefs = LookupHelper(self)


class FunctionScope(BaseScope):

    '''
    The scope created by statement lists, where variables are look up
    '''

    def __init__(self, owner):
        '''
        Constructor
        '''
        super(FunctionScope, self).__init__(owner)
        self.arguments = LookupHelper(self)


class TypeScope(BaseScope):

    '''
    The scope used by root and types to hold functions / methods, attributes /
    global variables, and operators
    basic types
    '''

    def __init__(self, owner):
        '''
        Constructor
        '''
        super(TypeScope, self).__init__(owner)
        self._owner = owner
        self.types = LookupHelper(self)
        self.typedefs = LookupHelper(self)
        self.functions = LookupHelper(self, True)
        self.operators = LookupHelper(self, True)
        self.attributes = LookupHelper(self)


class RootScope(TypeScope):

    '''
    The scope used by root to hold root elements, as plugins, functions,
    basic types
    '''

    def __init__(self, owner):
        '''
        Constructor
        '''
        super(RootScope, self).__init__(owner)
