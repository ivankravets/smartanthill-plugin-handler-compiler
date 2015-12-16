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


from smartanthill_phc.common.base import ArgumentListNode, ExpressionNode


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
        self.child_argument_list = None
        self.ref_declaration = None

    def set_argument_list(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ArgumentListNode)
        child.set_parent(self)
        self.child_argument_list = child


class MemberAccessExprNode(ExpressionNode):

    '''
    Node class representing a member access, usually a body-part reply
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(MemberAccessExprNode, self).__init__()
        self.txt_member = None
        self.child_expression = None
        self.type_decl = None
        self.member_decl = None

    def set_expression(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

    def get_member_field_sequence(self):
        '''
        Creates a field sequence to represent this member
        '''
        return self.member_decl.field_sequence


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


class NumberLiteralExprNode(ExpressionNode):

    '''
    Node class representing a number literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NumberLiteralExprNode, self).__init__()
        self.txt_literal = None

    def get_static_value(self):
        '''
        Returns the float value of this literal
        Used for complile-time evaluation of expressions
        TODO check literal for validity
        '''
        return float(self.txt_literal)


class BooleanLiteralExprNode(ExpressionNode):

    '''
    Node class representing a boolean literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BooleanLiteralExprNode, self).__init__()
        self.boolean_value = False

    def get_static_value(self):
        '''
        Returns the float value of this literal
        Used for complile-time evaluation of expressions
        '''
        return self.boolean_value


class StaticEvaluatedExprNode(ExpressionNode):

    '''
    Node class representing an statically (compile-time) evaluated expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StaticEvaluatedExprNode, self).__init__()
        self.child_replaced = None
        self._static_value = None

    def set_replaced(self, child):
        '''
        replaced setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_replaced = child

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
        self.child_expression = None

    def set_expression(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

    def get_static_value(self):
        return self.child_expression.get_static_value()

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
        self.txt_name = None
        self.child_rhs_expression = None
        self.ref_declaration = None

    def set_rhs_expression(self, child):
        '''
        rhs setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_rhs_expression = child


class OperatorExprNode(ExpressionNode):

    '''
    Node class representing a operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(OperatorExprNode, self).__init__()
        self.txt_operator = None
        self.child_argument_list = None
        self.ref_declaration = None

    def set_argument_list(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, ArgumentListNode)
        child.set_parent(self)
        self.child_argument_list = child


class BinaryOpExprNode(OperatorExprNode):

    '''
    Node class representing a binary operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BinaryOpExprNode, self).__init__()

    @staticmethod
    def create(compiler, ctx):
        '''
        Creates a new instance, and a new argument list
        '''
        node = compiler.init_node(BinaryOpExprNode(), ctx)
        node.set_argument_list(compiler.init_node(ArgumentListNode(), ctx))
        return node


class LogicOpExprNode(OperatorExprNode):

    '''
    Node class representing a logic operator expression
    '&&', '||' and '!'
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(LogicOpExprNode, self).__init__()


class ArithmeticOpExprNode(OperatorExprNode):

    '''
    Node class representing an arithmetic operator expression
    '+', '-, '*', '/' and '%'
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ArithmeticOpExprNode, self).__init__()


class UnaryOpExprNode(OperatorExprNode):

    '''
    Node class representing an unary arithmetic operator expression
    Prefix '+', '-'
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(UnaryOpExprNode, self).__init__()

    @staticmethod
    def create(compiler, ctx):
        '''
        Creates a new instance, and a new argument list
        '''
        node = compiler.init_node(UnaryOpExprNode(), ctx)
        node.set_argument_list(compiler.init_node(ArgumentListNode(), ctx))
        return node


class PostfixOpExprNode(OperatorExprNode):

    '''
    Node class representing a postfix unary operator expression
    Postfix '++', '--'
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PostfixOpExprNode, self).__init__()

    @staticmethod
    def create(compiler, ctx):
        '''
        Creates a new instance, and a new argument list
        '''
        node = compiler.init_node(PostfixOpExprNode(), ctx)
        node.set_argument_list(compiler.init_node(ArgumentListNode(), ctx))
        return node


class ComparisonOpExprNode(OperatorExprNode):

    '''
    Node class representing a comparison operator expression
    '<', '>', '<=', '>=', '==' and '!='
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ComparisonOpExprNode, self).__init__()
