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

from smartanthill_phc.c_node import TypeCastExprNode, StateDataCastStmtNode
from smartanthill_phc.common.compiler import Ctx
from smartanthill_phc.common.expression import VariableExprNode
from smartanthill_phc.common.node import Node, StmtListNode, StatementNode
from smartanthill_phc.common.statement import VariableDeclarationStmtNode
from smartanthill_phc.common.visitor import NodeVisitor, visit_node
from smartanthill_phc.root import NonBlockingData


def create_states(compiler, root, func_name):
    '''
    Creates state machine and state related nodes
    '''
    visitor = StateMachineVisitor(compiler, func_name)
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
        self.child_statement_list = None
        self.txt_id = None

    def set_statement_list(self, child):
        '''
        statement list setter
        '''
        assert isinstance(child, StmtListNode)
        child.set_parent(self)
        self.child_statement_list = child

#     def resolve(self, compiler):
#         compiler.resolve_node(self.child_statement_list)


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
        self.flag_wait = False

    def is_closed_stmt(self):
        '''
        Returns true
        '''
        # pylint: disable=no-self-use
        return True


class InitStateStmtNode(StatementNode):

    '''
    Statement node class representing the end of state machine, next entry
    should restart the state machine from the initial state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(InitStateStmtNode, self).__init__()


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

    def __init__(self, compiler, func_name):
        '''
        Constructor
        '''
        self._c = compiler
        self._func_name = func_name
        self._func_found = False
        self._h = DeclsHelper()

    def finish(self):
        return self._h.analyze_vars()

    def visit_RootNode(self, node):
        visit_node(self, node.child_source)

    def visit_PluginSourceNode(self, node):
        visit_node(self, node.child_declaration_list)

        if not self._func_found:
            self._c.report_error(
                node.ctx, "Function '%s' not found" % self._func_name)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            visit_node(self, each)

    def visit_StateDataStuctDeclarationNode(self, node):
        pass

    def visit_FunctionDeclNode(self, node):
        if node.txt_name == self._func_name:
            self._func_found = True
            d = self._c.init_node(
                StateDataCastStmtNode(), node.child_statement_list.ctx.start)

            args = node.child_argument_list.childs_declarations
            if len(args) >= 2:
                d.txt_arg = args[1].txt_name
            else:
                self._c.report_error(node.ctx, "Too few arguments")

            node.child_statement_list.insert_statement_at(0, d)

            _create_state_machine(
                self._c, node.child_statement_list, self._h)


def _create_state_machine(compiler, stmt_list, helper):
    '''
    Creates an state machine
    '''
    if not stmt_list.is_closed_stmt():
        compiler.report_error(stmt_list.ctx, "Missing 'return' statement")
        return

    sm = compiler.init_node(StateMachineStmtNode(), Ctx.NONE)

    sl = compiler.init_node(StmtListNode(), stmt_list.ctx)

    i = _skip_statements(stmt_list)
    stmt_list.split_at(i, sl)
    stmt_list.add_statement(sm)

    _create_state(compiler, sm, sl, helper)

    for each in sm.childs_states:
        assert each.child_statement_list.is_closed_stmt()


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


def _create_state(compiler, state_machine, stmt_list, helper):
    '''
    Creates a new state
    '''

    st = compiler.init_node(StateNode(), Ctx.NONE)
    st.set_statement_list(stmt_list)

    # begin from 0
    st.txt_id = str(len(state_machine.childs_states))
    state_machine.add_state(st)

    assert stmt_list.is_closed_stmt()
    v = _StatementsSplitterVisitor(
        stmt_list, compiler, state_machine, st, helper)
    v.visit_each_stmt()

    return st


class _StatementsSplitterVisitor(NodeVisitor):
    '''
    States are created by splitting statement lists, at blocking statements

    Each statement can be 'open' or 'closed'.
    A 'closed' statement means that execution flow will change.
    'return' is a 'closed' statement.
    An statement list will be 'closed' if it contains one closed statement.
    Flow will certainly find a 'return' within it at some point.
    An 'if else' statement will be closed only if both branches are closed.

    When we create the state machine, we need to split code flow at certain
    points.
    Each time an statement list is split, we create a new state.
    When we split an statement list, we must check if it is 'open' or 'closed'.
    When it is 'closed' it means we can freely split it, without much
    consequence, as flow reaching its end, will find a 'return' statement.
    But when we split an 'open' statement list, we must create a 'merge' point,
    where flow should continue after the end of the statement list.
    To do so, we need two thing,
    First we need to add a jump to the end of current statement list to
    change flow back to the 'merge' point.
    Second, we must create the 'merge' point.
    Such point is the statement to be executed right after the flow falls down
    the previously 'open' statement list.
    To do so, we split the containing (or parent) statement list at such point.
    If the containing statement list is not closed either,
    splitting it will in turn need to create a new 'merge' point
    at its containing statement list.
    This will create a cascade effect that will go up the flow structure until
    a 'closed' statement list if found.

    The 'root' statement list is required to be 'closed'

    When the 'merge' point is after the last statement of an statement list,
    then actual split is not required (it would create an empty statement list)
    and we can just propagate the merge to its containing statement list.

    '''

    def __init__(self, stmt_list, compiler, state_machine, state, helper):
        '''
        Constructor
        '''
        self._c = compiler
        self._sm = state_machine
        self._st = state
        self._h = helper
        self.merges = []

        self._stmt_list = stmt_list
        self._index = 0

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._c.report_error(
            node.ctx, "Statement not supported")

    def _create_state(self, stmt_list):
        return _create_state(self._c, self._sm, stmt_list, self._h)

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

    def split_after_current(self, wait, ctx):
        '''
        Splits current statement list after current statement
        There will be no more statements to visit at current statement list
        If statement list is not closed, then a jump is added at the end,
        to merge code flow back. Such merge will be left pending to complete
        '''
        if not self._stmt_list.is_closed_stmt():
            jmp = self._c.init_node(NextStateStmtNode(), ctx)
            self._stmt_list.add_statement(jmp)
            self.merges.append(jmp)

        sl = self._c.init_node(StmtListNode(), ctx)
        self._stmt_list.split_at(self._index + 1, sl)

        nxt = self._c.init_node(NextStateStmtNode(), ctx)
        nxt.flag_wait = wait
        nxt.ref_next_state = self._create_state(sl)
        self.insert_after_current(nxt)

        return nxt.ref_next_state

    def process_pending_merges(self, ctx):
        '''
        Process pending child merges, and propagate upwards if needed
        '''
        if len(self.merges) == 0:
            # nothing to do
            pass
        elif len(self._stmt_list.childs_statements) == self._index + 1:
            # This is the last statement, no need to make it here
            # Propagate upward
            pass
        else:
            # split_after_curret may create its own merge points
            jumps = self.merges
            self.merges = []

#            ctx = self._stmt_list.childs_statements[-1].ctx
            nxt = self.split_after_current(False, ctx)

            for j in jumps:
                j.ref_next_state = nxt

    def visit_stmt_list(self, stmt_list):

        assert isinstance(stmt_list, StmtListNode)

        v = _StatementsSplitterVisitor(
            stmt_list, self._c, self._sm, self._st, self._h)
        v.visit_each_stmt()

        self.merges.extend(v.merges)

    def visit_each_stmt(self):

        was_closed = self._stmt_list.is_closed_stmt()

        while self._index < len(self._stmt_list.childs_statements):
            stmt = self._stmt_list.childs_statements[self._index]
            visit_node(self, stmt)

            self._index += 1

        if was_closed:
            assert len(self.merges) == 0

    def visit_StmtListNode(self, node):

        self.visit_stmt_list(node)
        self.process_pending_merges(node.ctx)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):

        self._h.add_var_decl(node, self._st)
        visit_node(self, node.child_initializer)

    def visit_ExpressionStmtNode(self, node):
        visit_node(self, node.child_expression)

    def visit_BlockingCallStmtNode(self, node):

        visit_node(self, node.child_expression)

        self.split_after_current(True, node.ctx)

    def visit_ReturnStmtNode(self, node):

        visit_node(self, node.child_expression)

        # this must be last statement
        assert node == self._stmt_list.childs_statements[-1]

        nxt = self._c.init_node(InitStateStmtNode(), node.ctx)
        self.insert_before_current(nxt)

    def visit_IfElseStmtNode(self, node):

        visit_node(self, node.child_expression)
        self.visit_stmt_list(node.child_if_branch)
        if node.child_else_branch is not None:
            self.visit_stmt_list(node.child_else_branch)

        self.process_pending_merges(node.ctx)

    def visit_NextStateStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_DontCareExprNode(self, node):
        for each in node.childs_expressions:
            visit_node(self, each)

    def visit_TypeCastExprNode(self, node):
        visit_node(self, node.child_expression)

    def visit_VariableExprNode(self, node):
        self._h.add_var_expr(node, self._st)

    def visit_FunctionCallExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_ArgumentListNode(self, node):
        for each in node.childs_arguments:
            visit_node(self, each)
