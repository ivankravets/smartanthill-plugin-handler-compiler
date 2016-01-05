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

from smartanthill_phc.common import base
from smartanthill_phc.common.base import ExpressionNode,\
    Node, StmtListNode,\
    StatementNode, TypeDeclNode,\
    TypeNode, ResolutionHelper


class DontCareExprNode(ExpressionNode):

    '''
    Node class representing a operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(DontCareExprNode, self).__init__()
        self.child_argument_list = None

    def set_argument_list(self, child):
        '''
        argument_list setter
        '''
        assert isinstance(child, base.ArgumentListNode)
        child.set_parent(self)
        self.child_argument_list = child

    @staticmethod
    def create(compiler, ctx):
        '''
        Creates a new instance, and a new argument list
        '''
        node = compiler.init_node(DontCareExprNode(), ctx)
        node.set_argument_list(
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
        self.child_cast_type = None
        self.child_expression = None

    def set_cast_type(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, TypeNode)
        child.set_parent(self)
        self.child_cast_type = child

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child


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
