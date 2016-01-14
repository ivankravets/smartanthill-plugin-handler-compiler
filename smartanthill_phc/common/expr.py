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


from smartanthill_phc.common.base import ArgumentListNode, ExpressionNode,\
    Child, ChildExpr, ChildExprOpt


class ErrorExprNode(ExpressionNode):

    '''
    Node class representing a syntax error or unsupported contruct
    Used as a place holder when we can not return a real expression,
    and returning None is neither possible
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ErrorExprNode, self).__init__()


class FunctionCallExprNode(ExpressionNode):

    '''
    Node class representing a function call
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionCallExprNode, self).__init__()
        self.txt_name = None
        self.argument_list = Child(self, ArgumentListNode)
        self.ref_declaration = None


class MemberAccessExprNode(ExpressionNode):

    '''
    Node class representing a dot member access
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(MemberAccessExprNode, self).__init__()
        self.txt_name = None
        self.expression = ChildExpr(self)
        self.ref_declaration = None
        self.bool_arrow = False


class LiteralExprNode(ExpressionNode):

    '''
    Node class representing a generic literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(LiteralExprNode, self).__init__()
        self.txt_literal = None


class StaticEvaluatedExprNode(ExpressionNode):

    '''
    Node class representing an statically (compile-time) evaluated expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StaticEvaluatedExprNode, self).__init__()
        self.replaced_expression = ChildExprOpt(self)
        self._static_value = None

    def set_static_value(self, static_value):
        '''
        Value setter
        Sets the evaluated value for the replaced expression
        '''
        self._static_value = static_value

    def get_static_value(self):
        '''
        Value getter
        '''
        return self._static_value


class TrivialCastExprNode(ExpressionNode):

    '''
    Node class representing an automatic cast from literal to non-literal type
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(TrivialCastExprNode, self).__init__()
        self.expression = ChildExpr(self)

    def get_static_value(self):
        return self.expression.get().get_static_value()

    @staticmethod
    def create(compiler, expression, target_type):
        '''
        Creates a new instance
        '''
        node = compiler.init_node(TrivialCastExprNode(), expression.ctx)
        node.set_expression(expression)
        node.set_type(target_type)

        return node


class VariableExprNode(ExpressionNode):

    '''
    Node class representing a variable use
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(VariableExprNode, self).__init__()
        self.txt_name = None
        self.ref_declaration = None

    def get_static_value(self):
        '''
        Returns compile-time value of this expression is possible,
        Returns None otherwise
        '''
        if self.ref_declaration is not None:
            return self.ref_declaration.get_static_value()
        else:
            return None


class AssignmentExprNode(ExpressionNode):

    '''
    Node class representing a variable assignment
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(AssignmentExprNode, self).__init__()
        self.left_expression = ChildExpr(self)
        self.right_expression = ChildExpr(self)
        self.ref_declaration = None


class ConditionalExprNode(ExpressionNode):

    '''
    Node class representing a conditional expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ConditionalExprNode, self).__init__()
        self.condition_expression = ChildExpr(self)
        self.true_expression = ChildExpr(self)
        self.false_expression = ChildExpr(self)


class OperatorExprNode(ExpressionNode):

    '''
    Node class representing a non-member operator expression
    Currently all binary operators are non-member, as they may cast any
    of the arguments
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(OperatorExprNode, self).__init__()
        self.txt_operator = None
        self.argument_list = Child(self, ArgumentListNode)
        self.ref_declaration = None


class MemberOperatorExprNode(ExpressionNode):

    '''
    Node class representing a member operator expression
    Currently member operators are all that can not trigger a convertion
    on the first argument.
    Mostly unary operators
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(MemberOperatorExprNode, self).__init__()
        self.txt_operator = None
        self.expression = ChildExpr(self)
        self.argument_list = Child(self, ArgumentListNode)
        self.ref_declaration = None


class BinaryOpExprNode(OperatorExprNode):

    '''
    Node class representing a binary operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BinaryOpExprNode, self).__init__()


class UnaryOpExprNode(MemberOperatorExprNode):

    '''
    Node class representing an unary arithmetic operator expression
    Prefix '+', '-'
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(UnaryOpExprNode, self).__init__()


class PostUnaryOpExprNode(MemberOperatorExprNode):

    '''
    Node class representing a postfix unary operator expression
    Postfix '++', '--'
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PostUnaryOpExprNode, self).__init__()


class IndexOpExprNode(MemberOperatorExprNode):

    '''
    Node class representing an index operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(IndexOpExprNode, self).__init__()
