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


class StatementListScope(object):

    '''
    The scope created by statement lists, where variables are look up
    '''

    def __init__(self, owner):
        '''
        Constructor
        '''
        self._owner = owner
        self._variables = {}
        self._typedefs = {}

    def get_parent_scope(self):
        '''
        Returns parent scope of this same type
        '''
        return self._owner.get_parent_scope(StatementListScope)

    def add_variable(self, compiler, name, node):
        '''
        Adds a variable to this scope
        '''
        if name in self._variables:
            compiler.report_error(
                node.ctx, "Redeclaration of '%s'" % name)
            compiler.report_error(
                self._variables[name].ctx, "Previous was here")

        self._variables[name] = node

    def lookup_variable(self, name):
        '''
        Variable lookup algorithm
        It will look up name in this scope,
        and if not found it will look up in the containing scope recursively
        until either it is found, or no more scopes are available
        '''
        if name in self._variables:
            return self._variables[name]
        else:
            p = self.get_parent_scope()
            if p is not None:
                return p.lookup_variable(name)
            else:
                return None

    def add_typedef(self, compiler, name, node):
        '''
        Adds a typedef to this scope
        '''
        if name in self._typedefs:
            compiler.report_error(
                node.ctx, "Redeclaration of '%s'" % name)
            compiler.report_error(
                self._typedefs[name].ctx, "Previous was here")

        self._typedefs[name] = node

    def get_typedef(self, name):
        '''
        Typedef lookup
        '''
        return self._typedefs[name] if name in self._typedefs else None


class ReturnStmtScope(object):

    '''
    The scope a 'return' will exit
    Used for tracking return statements, and type compatibility check when
    more than one return is found
    '''

    def __init__(self, owner):
        '''
        Constructor
        '''
        self._owner = owner
        self._previous_return_type = None
        self._previous_ctx = None

    def add_return_stmt(self, compiler, ctx, return_type):
        '''
        Adds a return statement to this scope, check type compatibility with
        previous ones
        '''

        if not self._previous_return_type:
            self._previous_return_type = return_type
            self._previous_ctx = ctx
        elif self._previous_return_type == return_type:
            pass
        else:
            compiler.report_error(
                ctx,
                "Return statement type does not exactly match previous one")
            compiler.report_error(
                self._previous_ctx, "Previous was here")

    def get_return_type(self):
        '''
        Return type getter
        '''
        assert self._previous_return_type
        return self._previous_return_type


class RootScope(object):

    '''
    The scope used by root to hold root elements, as plugins, functions,
    basic types
    '''

    def __init__(self, owner):
        '''
        Constructor
        '''
        self._owner = owner
        self._bodyparts = {}
        self._types = {}
        self._typedefs = {}
        self._functions = {}
        self._operators = {}
        self._parameters = {}

    def add_bodypart(self, compiler, name, node):
        '''
        Adds a plug-in
        '''

        if name in self._bodyparts:
            compiler.report_error(
                node.ctx, "Duplicate use of plug-in name '%s'" % name)

        self._bodyparts[name] = node

    def lookup_bodypart(self, name):
        '''
        Looks up a plug-in
        '''
        return self._bodyparts[name] if name in self._bodyparts else None

    def add_type(self, compiler, name, node):
        '''
        Adds a type
        '''

        if name in self._types:
            compiler.report_error(
                node.ctx, "Duplicate use of type name '%s'" % name)

        self._types[name] = node

    def get_type(self, name):
        '''
        Looks up a type
        '''
        return self._types[name] if name in self._types else None

    def add_typedef(self, compiler, name, node):
        '''
        Adds a typedef to this scope
        '''
        if name in self._typedefs:
            compiler.report_error(
                node.ctx, "Redeclaration of '%s'" % name)
            compiler.report_error(
                self._typedefs[name].ctx, "Previous was here")

        self._typedefs[name] = node

    def get_typedef(self, name):
        '''
        Typedef lookup will look up name here
        '''
        return self._typedefs[name] if name in self._typedefs else None

    def add_operator(self, compiler, name, node):
        '''
        Adds an operator
        '''
        del compiler

        if name not in self._operators:
            self._operators[name] = []

        self._operators[name].append(node)

    def lookup_operator(self, name):
        '''
        Looks up an operator
        '''
        return self._operators[name] if name in self._operators else []

    def add_function(self, compiler, name, node):
        '''
        Adds a function
        '''

        if name in self._functions:
            compiler.report_error(
                node.ctx, "Duplicate use of name '%s'" % name)

        self._functions[name] = node

    def lookup_function(self, name):
        '''
        Looks up a function
        '''
        return self._functions[name] if name in self._functions else None

    def add_parameter(self, compiler, name, node):
        '''
        Adds a parameter to this scope
        '''
        if name in self._parameters:
            compiler.report_error(
                node.ctx, "Redeclaration of '%s'" % name)
            compiler.report_error(
                self._parameters[name].ctx, "Previous was here")

        self._parameters[name] = node

    def lookup_parameter(self, name):
        '''
        Looks up a parameter in this scope
        Returns None if not found
        '''
        return self._parameters[name] if name in self._parameters else None


def lookup_type(name, root_scope, stmt_scope):
    '''
    Type lookup algorithm
    Will lookup for typedef in every StatementListScope,
    if not found will lookup for type or typedef at RootScope
    '''

    while stmt_scope is not None:
        t = stmt_scope.get_typedef(name)
        if t is not None:
            return t.get_type()

        stmt_scope = stmt_scope.get_parent_scope()

    # If we reach here stmt_scope is None, and name was not found

    assert root_scope is not None
    t = root_scope.get_typedef(name)
    if t is not None:
        return t.get_type()

    return root_scope.get_type(name)
