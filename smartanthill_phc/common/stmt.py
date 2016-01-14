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


from smartanthill_phc.common.base import ExpressionNode,\
    ResolutionHelper, StatementNode, StmtListNode, TypeNode


def make_statement_list(compiler, statement):
    '''
    If statement is instance of StmtListNode, returns statement.
    Otherwise, creates and returns an StmtListNode holding statement

    This helper function is used to always use StmtListNode as child
    of statements like if-else, or for loops, even when a single statement
    (without braces) is used.
    '''
    assert isinstance(statement, StatementNode)

    if isinstance(statement, StmtListNode):
        return statement

    stmt_list = compiler.init_node(StmtListNode(), statement.ctx)
    stmt_list.statements.add(statement)

    return stmt_list


class NopStmtNode(StatementNode):

    '''
    Node class representing an empty statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NopStmtNode, self).__init__()


class ErrorStmtNode(StatementNode):

    '''
    Node class representing a syntax error
    Used as a place holder when we can not return a real statement,
    and returning None is neither possible
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ErrorStmtNode, self).__init__()


class ReturnStmtNode(StatementNode):

    '''
    Node class representing 'return' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ReturnStmtNode, self).__init__()
        self.child_expression = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child

    def is_closed_stmt(self):
        '''
        Returns true when this is a flow statement
        '''
        # pylint: disable=no-self-use
        return True

    def get_return_type(self, void_type):
        '''
        Returns the type returned by this return, or void_type if no expression
        '''
        if self.child_expression is not None:
            return self.child_expression.get_type()
        else:
            return void_type


class VariableDeclarationStmtNode(StatementNode, ResolutionHelper):

    '''
    Node class representing variable declaration statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(VariableDeclarationStmtNode, self).__init__()
        self.txt_name = None
        self.child_declaration_type = None
        self.child_initializer_expression = None

    def set_declaration_type(self, child):
        '''
        statement list setter
        '''
        assert isinstance(child, TypeNode)
        child.set_parent(self)
        self.child_declaration_type = child

    def set_initializer(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_initializer_expression = child

    def get_static_value(self):
        '''
        Returns compile-time value of this declaration is possible,
        Returns None otherwise
        '''

        if self.child_initializer_expression is not None:
            return self.child_initializer_expression.get_static_value()
        else:
            return None


class ExpressionStmtNode(StatementNode):

    '''
    Node class representing an statement that is an expression
    Used for assignments
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ExpressionStmtNode, self).__init__()
        self.child_expression = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child


class IfElseStmtNode(StatementNode):

    '''
    Node class representing 'if' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(IfElseStmtNode, self).__init__()
        self.child0_expression = None
        self.child1_if_stmt_list = None
        self.child2_else_stmt_list = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child0_expression = child

    def set_if_stmt_list(self, child):
        '''
        if_branch setter
        '''
        assert isinstance(child, StmtListNode)
        child.set_parent(self)
        self.child1_if_stmt_list = child

    def set_else_stmt_list(self, child):
        '''
        else_branch setter
        '''
        assert isinstance(child, StmtListNode)
        child.set_parent(self)
        self.child2_else_stmt_list = child

    def is_closed_stmt(self):
        '''
        Returns true when last statement is closed
        '''
        if self.child2_else_stmt_list is not None:
            return self.child1_if_stmt_list.is_closed_stmt() and\
                self.child2_else_stmt_list.is_closed_stmt()
        else:
            return False

#         t = self.get_scope(RootScope).lookup_type('_zc_boolean')
#
#         if not expression_type_match(compiler, t, self, 'child_expression'):
#             compiler.report_error(
#                 self.ctx, "Condition can not be evaluated to boolean")
        # no need to raise here
