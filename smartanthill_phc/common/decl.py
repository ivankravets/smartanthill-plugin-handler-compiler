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

from smartanthill_phc.common.base import Node, OnDemandResolution, TypeNode,\
    StmtListNode, DeclarationListNode, TypeDeclNode, Child
from smartanthill_phc.common.lookup import FunctionScope, StatementListScope


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

    def make_arguments_match(self, compiler, ctx, args, arg_boxes):
        '''
        Base method for argument matching
        Adds any necesary cast to make the types of the given arguments match
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        assert False


def _can_match_helper(compiler, ctx, args, arg_boxes, decls, make_match):
    '''
    If this argument list can not used to initialize given argument list
    Returns TypeDeclNode.NO_MATCH when there is no chance to make it match
    TypeDeclNode.EXACT_MATCH when match does not need any cast
    and TypeDeclNode.CAST_MATCH when it can match but casting needed
    '''
    assert arg_boxes is None or len(args) == arg_boxes.get_size()

    if len(args) != decls.get_size():
        if make_match:
            compiler.report_error(
                ctx, "Wrong number of arguments, need %s but given %s" % (
                    len(args),
                    decls.get_size()))
            compiler.raise_error()

        return TypeDeclNode.NO_MATCH

    result = TypeDeclNode.EXACT_MATCH
    for i in range(len(args)):

        source = args[i]
        target = decls.at(i).get().get_type()

        if source == target:
            pass
        elif target.can_cast_from(source):
            result += TypeDeclNode.CAST_MATCH
            if make_match:
                target.insert_cast_from(compiler, source, arg_boxes.at(i))
        else:
            if make_match:
                compiler.report_error(
                    ctx, "Bad argument type at position %s" % i)
                compiler.raise_error()

            return TypeDeclNode.NO_MATCH

    return result


class FunctionDeclNode(CallableDeclNode, OnDemandResolution):

    '''
    Node class representing a function declaration
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionDeclNode, self).__init__()
        self.bool_static = False
        self.bool_inline = False
        self.txt_name = None
        self.return_type = Child(self, TypeNode)
        self.argument_decl_list = Child(self, ArgumentDeclListNode)

    def can_match_arguments(self, compiler, ctx, args):

        return _can_match_helper(
            compiler, ctx, args, None,
            self.argument_decl_list.get().declarations, False)

    def make_arguments_match(self, compiler, ctx, args, arg_boxes):

        return _can_match_helper(
            compiler, ctx, args, arg_boxes,
            self.argument_decl_list.get().declarations, True)

    def add_qualifier(self, compiler, ctx, qualifier):
        '''
        Add qualifiers to this type.
        To be implemented by derived classes
        '''
        # pylint: disable=no-self-use
        compiler.report_error(ctx, "Unsupported qualifier '%s'" % qualifier)


class FunctionDefinitionNode(Node):

    '''
    Node class representing a function definition
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionDefinitionNode, self).__init__()
        self.declaration = Child(self, FunctionDeclNode)
        self.statement_list = Child(self, StmtListNode)
        self.add_scope(StatementListScope, None)  # stop scope recursion
        self.add_scope(FunctionScope, FunctionScope(self))


class ArgumentDeclNode(Node, OnDemandResolution):

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

    def add_qualifier(self, compiler, ctx, qualifier):
        '''
        Add qualifiers to this type.
        To be implemented by derived classes
        '''
        # pylint: disable=no-self-use
        compiler.report_error(ctx, "Unsupported qualifier '%s'" % qualifier)


class ArgumentDeclListNode(DeclarationListNode):

    '''
    Node class used as container of argument declaration in functions
    '''
    pass
