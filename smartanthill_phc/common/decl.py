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

from smartanthill_phc.common.base import Node, ResolutionHelper, TypeNode,\
    StmtListNode, DeclarationListNode, TypeDeclNode, Child
from smartanthill_phc.common.lookup import ReturnStmtScope, StatementListScope,\
    FunctionScope


class CallableDeclNode(Node):

    '''
    Base class for declarations that can match an argument list
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(CallableDeclNode, self).__init__()

    def can_match_arguments(self, compiler, ctx, args):
        '''
        Base method for argument matching
        Returns where this declaration can be called with given expressions
        as arguments
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        return TypeDeclNode.NO_MATCH

    def make_arguments_match(self, compiler, ctx, args):
        '''
        Base method for argument matching
        Adds any necesary cast to make the types of the given arguments match
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        assert False


class FunctionDeclNode(CallableDeclNode, ResolutionHelper):

    '''
    Node class representing a function declaration
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionDeclNode, self).__init__()
        self.txt_name = None
        self.return_type = Child(self, TypeNode)
        self.statement_list = Child(self, StmtListNode)
        self.argument_decl_list = Child(self, ArgumentDeclListNode)
        self.add_scope(ReturnStmtScope, ReturnStmtScope(self))
        self.add_scope(StatementListScope, None)  # stop scope recursion
        self.add_scope(FunctionScope, FunctionScope(self))


class ArgumentDeclNode(Node, ResolutionHelper):

    '''
    Node class representing a function argument declaration
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ArgumentDeclNode, self).__init__()
        self.argument_type = Child(self, TypeNode)
        self.txt_name = None


class ArgumentDeclListNode(DeclarationListNode):

    '''
    Node class used as container of argument declaration in functions
    '''
    pass
