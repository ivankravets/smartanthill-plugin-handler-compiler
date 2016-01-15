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


from smartanthill_phc.common.base import OnDemandResolution, StatementNode,\
    StmtListNode, TypeNode, ChildExprOpt, ChildExpr, Child


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
        self.expression = ChildExprOpt(self)

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
        if not self.expression.is_none():
            return self.expression.get().get_type()
        else:
            return void_type


class VariableDeclarationStmtNode(StatementNode, OnDemandResolution):

    '''
    Node class representing variable declaration statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(VariableDeclarationStmtNode, self).__init__()
        self.txt_name = None
        self.declaration_type = Child(self, TypeNode)
        self.initializer_expression = ChildExprOpt(self)

    def get_static_value(self):
        '''
        Returns compile-time value of this declaration is possible,
        Returns None otherwise
        '''

        if not self.initializer_expression.is_none():
            return self.initializer_expression.get().get_static_value()
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
        self.expression = ChildExpr(self)


class IfElseStmtNode(StatementNode):

    '''
    Node class representing 'if' statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(IfElseStmtNode, self).__init__()
        self.expression = ChildExpr(self)
        self.if_stmt_list = Child(self, StmtListNode)
        self.else_stmt_list = Child(self, StmtListNode, True)

    def is_closed_stmt(self):
        '''
        Returns true when last statement is closed
        '''
        if not self.else_stmt_list.is_none():
            return self.if_stmt_list.get().is_closed_stmt() and\
                self.else_stmt_list.get().is_closed_stmt()
        else:
            return False

#         t = self.get_scope(RootScope).lookup_type('_zc_boolean')
#
#         if not expression_type_match(compiler, t, self, 'child_expression'):
#             compiler.report_error(
#                 self.ctx, "Condition can not be evaluated to boolean")
        # no need to raise here
