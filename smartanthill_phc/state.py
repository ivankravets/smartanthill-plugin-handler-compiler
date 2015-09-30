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

from smartanthill_phc.c_node import TypeCastExprNode
from smartanthill_phc.common.compiler import Ctx
from smartanthill_phc.common.expression import VariableExprNode
from smartanthill_phc.common.node import Node, StmtListNode, StatementNode
from smartanthill_phc.common.statement import VariableDeclarationStmtNode
from smartanthill_phc.common.visitor import NodeVisitor, visit_node
from smartanthill_phc.root import NonBlockingData


def create_states(compiler, root, handler, exec_init):
    '''
    Creates state machine and state related nodes
    '''
    visitor = StateMachineVisitor(compiler, handler, exec_init)
    visit_node(visitor, root)
    nb = visitor.finish()
    root.get_scope(NonBlockingData).refs_moved_var_decls = nb

    compiler.check_stage('state')


class StateMachineStmtNode(StatementNode):

    '''
    Node class representing an state machine
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StateMachineStmtNode, self).__init__()
        self.childs_states = []
        self.refs_moved_var_decls = []
        self._decls = {}

    def add_state(self, child):
        '''
        statement list setter
        '''
        assert isinstance(child, StateNode)
        assert child is not None
        child.set_parent(self)
        self.childs_states.append(child)

    def add_var_decl(self, decl):
        '''
        Adds a variable declaration
        '''
        assert decl not in self._decls
        assert len(self.childs_states) != 0
        st = self.childs_states[-1]
        self._decls[decl] = (st, [])

    def add_var_expr(self, expr):
        '''
        Adds a reference (access) to a variable in certain state
        '''
        if expr.ref_decl is not None:
            assert expr.ref_decl in self._decls
            assert len(self.childs_states) != 0

            st = self.childs_states[-1]
            if st == self._decls[expr.ref_decl][0]:
                return
            elif st in self._decls[expr.ref_decl][1]:
                return
            else:
                self._decls[expr.ref_decl][1].append(st)

    def analyze_vars(self):

        for (key, value) in self._decls.iteritems():
            if len(value[1]) != 0:
                self.refs_moved_var_decls.append(key)

    def resolve(self, compiler):
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        assert False


class StateNode(Node):

    '''
    Node class representing an state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StateNode, self).__init__()
        self.txt_id = None
        self.wait_condition = None

#     def resolve(self, compiler):
#         compiler.resolve_node(self.child_statement_list)


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


class NextStateStmtNode(StatementNode):

    '''
    Statement node class representing state to be processed next time we enter
    this function
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NextStateStmtNode, self).__init__()
        self.ref_next_state = None


class InitStateStmtNode(StatementNode):

    '''
    Statement node representing the initialization of state machine state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(InitStateStmtNode, self).__init__()
        self.txt_arg = None


class ReturnStateStmtNode(StatementNode):

    '''
    Statement node representing the re initialization of state machine
    just before a return statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ReturnStateStmtNode, self).__init__()


class DeclsHelper(object):

    '''
    Helper class to detect which variables are accessed in each state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._decls = {}

    def add_var_decl(self, decl, st):
        '''
        Adds a variable declaration
        '''
        assert decl not in self._decls
        self._decls[decl] = (st, [])

    def add_var_expr(self, expr, st):
        '''
        Adds a reference (access) to a variable in certain state
        '''
        if expr.ref_decl is not None:
            if expr.ref_decl in self._decls:

                if st == self._decls[expr.ref_decl][0]:
                    return
                elif st in self._decls[expr.ref_decl][1]:
                    return
                else:
                    self._decls[expr.ref_decl][1].append(st)

    def analyze_vars(self):

        result = []
        for (key, value) in self._decls.iteritems():
            if len(value[1]) != 0:
                result.append(key)

        return result


class StateMachineVisitor(NodeVisitor):

    def __init__(self, compiler, handler, exec_init):
        '''
        Constructor
        '''
        self._c = compiler
        self._handler = handler
        self._exec_init = exec_init
        self._handler_found = False
        self._exec_init_found = False
        self._h = DeclsHelper()

    def finish(self):
        return self._h.analyze_vars()

    def visit_RootNode(self, node):
        visit_node(self, node.child_source)

    def visit_PluginSourceNode(self, node):
        visit_node(self, node.child_declaration_list)

        if not self._handler_found:
            self._c.report_error(
                node.ctx, "Function '%s' not found" % self._handler)
        if not self._exec_init_found:
            self._c.report_error(
                node.ctx, "Function '%s' not found" % self._handler_init)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            visit_node(self, each)

    def visit_StateDataStuctDeclarationNode(self, node):
        pass

    def visit_FunctionDeclNode(self, node):
        if node.txt_name == self._handler:
            if self._handler_found:
                self._c.report_error(node.ctx, "Function redefinition")

            self._handler_found = True
            ctx = node.child_statement_list.ctx.start

            stmt = self._c.init_node(StateDataCastStmtNode(), ctx)

            args = node.child_argument_list.childs_declarations
            if len(args) >= 2:
                stmt.txt_arg = args[1].txt_name
            else:
                self._c.report_error(node.ctx, "Too few arguments")

            node.child_statement_list.insert_statement_at(0, stmt)

            _create_state_machine(
                self._c, node.child_statement_list, self._h)
        elif node.txt_name == self._exec_init:
            if self._exec_init_found:
                self._c.report_error(node.ctx, "Function redefinition")

            self._exec_init_found = True
            ctx = node.child_statement_list.ctx.start

            stmt = self._c.init_node(InitStateStmtNode(), ctx)

            args = node.child_argument_list.childs_declarations
            if len(args) >= 2:
                stmt.txt_arg = args[1].txt_name
            else:
                self._c.report_error(node.ctx, "Too few arguments")

            node.child_statement_list.insert_statement_at(0, stmt)


def _create_state_machine(compiler, stmt_list, helper):
    '''
    Creates an state machine
    '''
    if not stmt_list.is_closed_stmt():
        compiler.report_error(stmt_list.ctx, "Missing 'return' statement")
        return

    i = _skip_statements(stmt_list)

    if i == 0:
        assert False
    if i == 1:
        assert isinstance(
            stmt_list.childs_statements[0], StateDataCastStmtNode)
        ctx = stmt_list.ctx.start
    else:
        ctx = stmt_list.childs_statements[i - 1].ctx.stop

    sm = compiler.init_node(StateMachineStmtNode(), ctx)

    stmt_list.insert_statement_at(i, sm)

    v = _StatementsVisitor(stmt_list, i + 1, compiler, sm, helper, None)
    v.create_state(None)
    v.visit_each_stmt()


def _skip_statements(stmt_list):

    for i in range(len(stmt_list.childs_statements)):
        stmt = stmt_list.childs_statements[i]
        if isinstance(stmt, StateDataCastStmtNode):
            continue

        if not isinstance(stmt, VariableDeclarationStmtNode):
            return i
        if not isinstance(stmt.child_initializer, TypeCastExprNode):
            return i
        if not isinstance(stmt.child_initializer.child_expression,
                          VariableExprNode):
            return i

    return len(stmt_list.childs_statements)


class _StatementsVisitor(NodeVisitor):
    '''
    Here we insert goto's labels into the code
    '''

    def __init__(self, stmt_list, index, compiler, state_machine, helper,
                 current_state):
        '''
        Constructor
        '''
        self._c = compiler
        self._sm = state_machine
        self._h = helper

        self._stmt_list = stmt_list
        self._index = index

        self._current_st = current_state

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._c.report_error(
            node.ctx, "Statement not supported")

    def create_state(self, wait_condition):
        st = self._c.init_node(StateNode(), Ctx.NONE)

        # begin from 0
        st.txt_id = str(len(self._sm.childs_states))
        st.wait_condition = wait_condition
        self._sm.add_state(st)

        self._current_st = st

        return st

    def insert_before_current(self, stmt):
        '''
        Insert statement before current one
        Index will be incremented to account for the extra statement
        Inserted statement will never be visited, because it will be inserted
        at a place visitor already did
        '''
        self._stmt_list.insert_statement_at(self._index, stmt)

        self._index += 1

    def insert_after_current(self, stmt):
        '''
        Insert statement after current one
        Index will be incremented to account for the extra statement
        and to avoid visitation of inserted statement
        '''
        self._stmt_list.insert_statement_at(self._index + 1, stmt)

        self._index += 1

    def _split_after_current(self, wait_condition, ctx):
        '''
        Adds state change after current statement
        '''

        nxt = self._c.init_node(NextStateStmtNode(), ctx)
        nxt.ref_next_state = self.create_state(wait_condition)
        self.insert_after_current(nxt)

    def visit_stmt_list(self, stmt_list):

        assert isinstance(stmt_list, StmtListNode)

        v = _StatementsVisitor(
            stmt_list, 0, self._c, self._sm, self._h, self._current_st)
        v.visit_each_stmt()

    def visit_each_stmt(self):

        while self._index < len(self._stmt_list.childs_statements):
            stmt = self._stmt_list.childs_statements[self._index]
            visit_node(self, stmt)

            self._index += 1

    def visit_StmtListNode(self, node):
        self.visit_stmt_list(node)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):

        self._h.add_var_decl(node, self._current_st)
        visit_node(self, node.child_initializer)

    def visit_ExpressionStmtNode(self, node):
        visit_node(self, node.child_expression)

    def visit_BlockingCallStmtNode(self, node):

        visit_node(self, node.child_expression)

        self._split_after_current(None, node.ctx)

    def visit_ReturnStmtNode(self, node):

        visit_node(self, node.child_expression)
        stmt = self._c.init_node(ReturnStateStmtNode(), node.ctx)
        self.insert_before_current(stmt)

    def visit_IfElseStmtNode(self, node):

        visit_node(self, node.child_expression)
        self.visit_stmt_list(node.child_if_branch)
        if node.child_else_branch is not None:
            self.visit_stmt_list(node.child_else_branch)

    def visit_DontCareExprNode(self, node):
        for each in node.childs_expressions:
            visit_node(self, each)

    def visit_BinaryOpExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_UnaryOpExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_PostfixOpExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_LiteralExprNode(self, node):
        pass

    def visit_TypeCastExprNode(self, node):
        visit_node(self, node.child_expression)

    def visit_VariableExprNode(self, node):
        self._h.add_var_expr(node, self._current_st)

    def visit_FunctionCallExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_ArgumentListNode(self, node):
        for each in node.childs_arguments:
            visit_node(self, each)
