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

from smartanthill_phc import resolve
from smartanthill_phc.common import base, decl, expr
from smartanthill_phc.common.base import ExpressionNode,\
    Node, StmtListNode,\
    StatementNode, TypeDeclNode,\
    TypeNode, ResolutionHelper, DeclarationListNode, Child
from smartanthill_phc.common.expr import LiteralExprNode


class DontCareExprNode(ExpressionNode):

    '''
    Node class representing a operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(DontCareExprNode, self).__init__()
        self.argument_list = Child(self, base.ArgumentListNode)

    @staticmethod
    def create(compiler, ctx):
        '''
        Creates a new instance, and a new argument list
        '''
        node = compiler.init_node(DontCareExprNode(), ctx)
        node.argument_list.set(
            compiler.init_node(base.ArgumentListNode(), ctx))
        return node


class CastExprNode(ExpressionNode):

    '''
    Node class representing an explicit type cast
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(CastExprNode, self).__init__()
        self.child0_cast_type = None
        self.child1_expression = None

    def set_cast_type(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, TypeNode)
        child.set_parent(self)
        self.child0_cast_type = child

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child1_expression = child


class MemberExprNode(ExpressionNode):

    '''
    Node class representing a dot member access
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(MemberExprNode, self).__init__()
        self.txt_name = None
        self.child_expression = None
        self.ref_declaration = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child


class IntegerLiteralExprNode(LiteralExprNode):

    '''
    Node class representing a number literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(IntegerLiteralExprNode, self).__init__()
        self.int_value = 0

    def get_static_value(self):
        '''
        Returns the float value of this literal
        Used for complile-time evaluation of expressions
        TODO check literal for validity
        '''
        return self.int_value


class BooleanLiteralExprNode(LiteralExprNode):

    '''
    Node class representing a boolean literal
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BooleanLiteralExprNode, self).__init__()
        self.bool_value = False

    def get_static_value(self):
        '''
        Returns the float value of this literal
        Used for complile-time evaluation of expressions
        '''
        return self.bool_value


class FunctionCallStmtNode(StatementNode):

    '''
    Node class representing a blocking function call statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionCallStmtNode, self).__init__()
        self.child_expression = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child


class LoopStmtNode(StatementNode):

    '''
    Base class for loop nodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(LoopStmtNode, self).__init__()


class WhileStmtNode(LoopStmtNode):

    '''
    Node class representing a 'while' loop
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(WhileStmtNode, self).__init__()
        self.child0_expression = None
        self.child1_stmt_list = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child0_expression = child

    def set_statement_list(self, child):
        '''
        statement_list setter
        '''
        assert isinstance(child, StmtListNode)
        child.set_parent(self)
        self.child1_stmt_list = child


class DoWhileStmtNode(WhileStmtNode):

    '''
    Node class representing a 'do-while' loop
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(DoWhileStmtNode, self).__init__()


class ForStmtNode(LoopStmtNode):

    '''
    Node class representing a 'for' with expression and not declaration.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ForStmtNode, self).__init__()
        self.child0_init_expression = None
        self.child1_condition_expression = None
        self.child2_iteration_expression = None
        self.child3_stmt_list = None

    def set_init_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child0_init_expression = child

    def set_condition_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child1_condition_expression = child

    def set_iteration_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child2_iteration_expression = child

    def set_statement_list(self, child):
        '''
        statement_list setter
        '''
        assert isinstance(child, StmtListNode)
        child.set_parent(self)
        self.child3_stmt_list = child


class BasicTypeDeclNode(TypeDeclNode):

    '''
    Basic, built-in types are implemented using this class
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(BasicTypeDeclNode, self).__init__(type_name)


class VoidTypeDeclNode(TypeDeclNode):

    '''
    void pseudotype is implemented using this class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(VoidTypeDeclNode, self).__init__('void')


class IntTypeDeclNode(TypeDeclNode):

    '''
    Basic integral built-in types are implemented using this class
    '''

    def __init__(self, type_name):
        '''
        Constructor
        '''
        super(IntTypeDeclNode, self).__init__(type_name)
        self.child0_operator_decl_list = None
        self.child1_cast_rules_list = None

    def set_operator_decl_list(self, child):
        '''
        Setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child0_operator_decl_list = child

    def set_cast_rule_list(self, child):
        '''
        Setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child1_cast_rules_list = child

    def can_cast_from(self, source_type):
        '''
        Base method for type casting
        If self can be constructed from source_type returns True
        Otherwise returns False
        '''
        for each in self.child1_cast_rules_list.declarations:
            if each.get().can_cast_from(source_type):
                return True
        return False

    def insert_cast(self, compiler, source_type, expression):
        '''
        Inserts a cast from the source type
        Only implemented by types that return true to can_cast_from
        '''
        # pylint: disable=unused-argument
        for each in self.child1_cast_rules_list.declarations:
            if each.get().can_cast_from(source_type):
                return each.get().insert_cast(compiler, self, expression)
        assert False

    def lookup_operator(self, name):
        result = []
        for each in self.child0_operator_decl_list.declarations:
            if each.get().txt_name == name:
                result.append(each.get())
        return result


class TrivialCastRuleNode(Node):

    '''
    Rule that  integral built-in types are implemented using this class
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(TrivialCastRuleNode, self).__init__()
        self.int_min_value = 0
        self.int_max_value = 0
        self.child_type = None

    def set_type(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, TypeNode)
        child.set_parent(self)
        self.child_type = child

    def can_cast_from(self, source_type):
        '''
        Base method for type casting
        If self can be constructed from source_type returns True
        Otherwise returns False
        '''
        return source_type == self.child_type.ref_type_declaration

    def insert_cast(self, compiler, target_type, expression):
        '''
        Inserts a cast to the target type
        '''
        # pylint: disable=no-self-use
        node = compiler.init_node(expr.TrivialCastExprNode(), expression.ctx)
        node.set_expression(expression)
        node.set_type(target_type)

        return node


class RefTypeNode(TypeNode):

    '''
    Node class representing hard coded type
    Used at automatic code generation
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(RefTypeNode, self).__init__()


class SimpleTypeNode(TypeNode):

    '''
    Node class representing a type
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(SimpleTypeNode, self).__init__()
        self.txt_name = None
        self.bool_const = False

    def add_qualifier(self, compiler, ctx, qualifier):
        '''
        Add qualifiers to this type.
        '''
        # pylint: disable=no-self-use
        if qualifier == "const":
            if not self.bool_const:
                self.bool_const = True
            else:
                compiler.report_error(
                    ctx, "Duplicate qualifier '%s'" % qualifier)
        else:
            super(SimpleTypeNode, self).add_qualifier(compiler, ctx, qualifier)


class InvalidTypeNode(TypeNode):

    '''
    Node class representing an error while parsing a type
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(InvalidTypeNode, self).__init__()
        self.txt_name = None


class PointerTypeNode(TypeNode):

    '''
    Node class representing an pointer to type
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PointerTypeNode, self).__init__()
        self.child_pointed_type = None
        self.bool_const = False

    def set_pointed_type(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, TypeNode)
        child.set_parent(self)
        self.child_pointed_type = child

    def add_qualifier(self, compiler, ctx, qualifier):
        '''
        Add qualifiers to this type.
        '''
        # pylint: disable=no-self-use
        if qualifier == "const":
            if not self.bool_const:
                self.bool_const = True
            else:
                compiler.report_error(
                    ctx, "Duplicate qualifier '%s'" % qualifier)
        else:
            super(PointerTypeNode, self).add_qualifier(
                compiler, ctx, qualifier)


class PapiFunctionDeclNode(Node):

    '''
    Node class representing a plugin api function
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        super(PapiFunctionDeclNode, self).__init__()
        self.txt_name = name


class TypedefStmtNode(StatementNode, ResolutionHelper):

    '''
    Node class representing variable declaration statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(TypedefStmtNode, self).__init__()
        self.txt_name = None
        self.child_type = None

    def set_type(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, TypeNode)
        child.set_parent(self)
        self.child_type = child


class PreprocessorDirectiveNode(Node):

    '''
    Node class representing a preprocessor directive
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PreprocessorDirectiveNode, self).__init__()
        self.txt_body = None


class OperatorDeclNode(decl.CallableDeclNode, ResolutionHelper):

    '''
    Node class representing a function declaration
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(OperatorDeclNode, self).__init__()
        self.txt_name = None
        self.child0_return_type = None
        self.child1_argument_decl_list = None

    def set_return_type(self, child):
        '''
        Setter
        '''
        assert isinstance(child, TypeNode)
        child.set_parent(self)
        self.child0_return_type = child

    def set_argument_decl_list(self, child):
        '''
        Setter
        '''
        assert isinstance(child, decl.ArgumentDeclListNode)
        child.set_parent(self)
        self.child1_argument_decl_list = child

    def can_match_arguments(self, compiler, ctx, args):

        return resolve.can_match_helper(
            compiler, ctx, args,
            self.child1_argument_decl_list.declarations, False)

    def make_arguments_match(self, compiler, ctx, args):

        return resolve.can_match_helper(
            compiler, ctx, args,
            self.child1_argument_decl_list.declarations, True)
