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

from smartanthill_phc.common.lookup import RootScope, ReturnStmtScope,\
    StatementListScope
from smartanthill_phc.common.node import ExpressionNode,\
    resolve_expression_list, Node, StmtListNode,\
    StatementNode, resolve_expression, DeclarationListNode


class DontCareExprNode(ExpressionNode):

    '''
    Node class representing a operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(DontCareExprNode, self).__init__()
        self.childs_expressions = []

    def add_expression(self, child):
        '''
        expression adder
        '''
        assert child is not None
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.childs_expressions.append(child)

    def resolve_expr(self, compiler):

        resolve_expression_list(compiler, self, self.childs_expressions)

        return self.get_scope(RootScope).lookup_type('_zc_dont_care')


class TypeCastExprNode(ExpressionNode):

    '''
    Node class representing an explicit type cast
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(TypeCastExprNode, self).__init__()
        self.child_expression = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

    def resolve_expr(self, compiler):

        resolve_expression(compiler, self, 'child_expression')

        return self.get_scope(RootScope).lookup_type('_zc_dont_care')


class FunctionDeclNode(Node):

    '''
    Node class representing a function declaration
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionDeclNode, self).__init__()
        self.child_statement_list = None
        self.child_argument_list = None
        self.txt_name = None
        self.add_scope(ReturnStmtScope, ReturnStmtScope(self))
        self.add_scope(StatementListScope, None)

    def set_statement_list(self, child):
        '''
        statement list setter
        '''
        assert isinstance(child, StmtListNode)
        child.set_parent(self)
        self.child_statement_list = child

    def set_argument_list(self, child):
        '''
        argument list setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_argument_list = child

    def resolve(self, compiler):
        compiler.resolve_node(self.child_statement_list)


class ArgumentDeclNode(Node):

    '''
    Node class representing a function argument declaration
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ArgumentDeclNode, self).__init__()
        self.txt_name = None

    def resolve(self, compiler):
        pass


class BlockingCallStmtNode(StatementNode):

    '''
    Node class representing a blocking function call statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BlockingCallStmtNode, self).__init__()
        self.child_expression = None
        self.txt_next = u"TODO"

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

    def resolve(self, compiler):
        resolve_expression(compiler, self, 'child_expression')


class StateDataStuctDeclarationNode(Node):

    '''
    Node class representing struct declaration for plugin data type
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StateDataStuctDeclarationNode, self).__init__()

    def resolve(self, compiler):
        pass


class StateDataCastStmtNode(StatementNode):

    '''
    Node class representing argument cast of state data
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StateDataCastStmtNode, self).__init__()
        self.txt_arg = None

    def resolve(self, compiler):
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        assert False
