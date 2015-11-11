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

from smartanthill_phc.c_node import TypeCastExprNode, IntTypeDeclNode,\
    VoidTypeDeclNode
from smartanthill_phc.common.expression import VariableExprNode,\
    FunctionCallExprNode
from smartanthill_phc.common.node import StmtListNode, StatementNode
from smartanthill_phc.common.statement import VariableDeclarationStmtNode
from smartanthill_phc.common.visitor import NodeVisitor, visit_node
from smartanthill_phc.root import NonBlockingData


def create_states(compiler, root, prefix, split_all):
    '''
    Creates state machine and state related nodes
    '''
    nb = root.get_scope(NonBlockingData)
    nb.set_prefix(prefix)
    visitor = StateMachineVisitor(compiler, nb, split_all)
    visit_node(visitor, root)

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
        self.int_last_state = 0
        self.flag_main_machine = False

    def increment_state(self):
        '''
        Increments the state counter
        '''
        self.int_last_state += 1

        return self.int_last_state

    def get_last_state(self):
        '''
        Returns the last added state
        '''
        return self.int_last_state

    def has_states(self):
        '''
        Returns where this state machine really has states
        '''
        return self.int_last_state != 0

#     def get_name(self):
#         '''
#         Returns the name of the variable with the state of this machine
#         '''
#         if self.int_machine_index == 0:
#             return "sa_next"
#         else:
#             return "sa_next%s" % str(self.int_machine_index)

    def is_main_machine(self):
        '''
        Returns True if this is the main state machine
        '''
        return self.flag_main_machine


class MainFirstStmtNode(StatementNode):

    '''
    Node class inserted as first statement of main state machine function
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(MainFirstStmtNode, self).__init__()
        self.txt_arg2 = None
        self.txt_arg5 = None


class InitFirstStmtNode(StatementNode):

    '''
    Statement node representing the initialization of state machine state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(InitFirstStmtNode, self).__init__()
        self.txt_arg1 = None


class SubFirstStmtNode(StatementNode):

    '''
    Node class inserted as first statement on functions with substates
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(SubFirstStmtNode, self).__init__()


class WaitStateStmtNode(StatementNode):

    '''
    Statement node class representing state to be processed next time we enter
    this function
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(WaitStateStmtNode, self).__init__()
        self.int_next_state = None
        self.ref_waiting_for = None


class DebugStateStmtNode(StatementNode):

    '''
    Statement node class representing state to be processed next time we enter
    this function
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(DebugStateStmtNode, self).__init__()
        self.int_next_state = None


class BeforeSubStmtNode(StatementNode):

    '''
    Statement node class to be placed before an statement with sub states
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BeforeSubStmtNode, self).__init__()
        self.int_next_state = None


class AfterSubStmtNode(StatementNode):

    '''
    Statement node class to be placed after an statement with sub states
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(AfterSubStmtNode, self).__init__()


class BeforeReturnStmtNode(StatementNode):

    '''
    Statement node representing the re initialization of state machine
    just before a return statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(BeforeReturnStmtNode, self).__init__()


class DeclsHelper(object):

    '''
    Helper class to detect which variables are accessed in each state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._decls = {}
        self._decls2 = []
        self._loop_stack = []
        self._used_inside_loop = []

    def add_var_decl(self, decl, st):
        '''
        Adds a variable declaration
        '''
        assert decl not in self._decls

        name = decl.txt_name
        i = 0
        while self._has_decl_with_name(name):
            i += 1
            name = decl.txt_name + str(i)

        decl.txt_name = name  # TODO improve
        self._decls[decl] = st

    def _has_decl_with_name(self, name):

        for each in self._decls:
            if each.txt_name == name:
                return True
        return False

    def add_var_expr(self, expr, st):
        '''
        Adds a reference (access) to a variable in certain state
        '''
        if expr.ref_decl is None:
            return

        if expr.ref_decl not in self._decls:
            return

        if expr.ref_decl in self._decls2:
            return

        if self._decls[expr.ref_decl] != st:
            self._decls2.append(expr.ref_decl)
            return

        if len(self._loop_stack) != 0:
            self._used_inside_loop.append(expr.ref_decl)

    def begin_loop(self, st):
        self._loop_stack.append(st)

    def end_loop(self, st):
        if self._loop_stack.pop() != st:
            for each in self._used_inside_loop:
                if each not in self._decls2:
                    self._decls2.append(each)

            self._used_inside_loop = []

    def get_decls_to_be_moved(self):

        return self._decls2


class DeclsHelper2(object):

    '''
    Helper class to detect which variables are accessed in each state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._funcs_with_sub_states = {}
        self.int_last_machine = 0

    def increment_state_machine(self):
        '''
        Increments the state counter
        '''
        self.int_last_machine += 1

        return self.int_last_machine

    def add_function_with_sub_states(self, txt_name, machine):

        self._funcs_with_sub_states[txt_name] = machine

    def has_sub_states(self, txt_name):

        return txt_name in self._funcs_with_sub_states

    def get_sub_machine(self, txt_name):

        assert txt_name in self._funcs_with_sub_states
        return self._funcs_with_sub_states[txt_name]

    def get_state_machines(self):

        return self._funcs_with_sub_states.values()

    def get_functions(self):

        return self._funcs_with_sub_states.keys()


class StateMachineVisitor(NodeVisitor):

    def __init__(self, compiler, nb, split_all):
        '''
        Constructor
        '''
        self._c = compiler
        self._nb = nb
        self._split_all = split_all

    def visit_RootNode(self, node):
        visit_node(self, node.child_source)

    def visit_PluginSourceNode(self, node):
        visit_node(self, node.child_declaration_list)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            visit_node(self, each)

    def visit_FunctionDeclNode(self, node):
        if node.txt_name == self._nb.handler_name:

            ctx = node.child_statement_list.ctx.start

            stmt = self._c.init_node(MainFirstStmtNode(), ctx)

            args = node.child_argument_list.childs_declarations
            if len(args) >= 6:
                stmt.txt_arg2 = args[2].txt_name
                stmt.txt_arg5 = args[5].txt_name
            else:
                self._c.report_error(node.ctx, "Too few arguments")

            node.child_statement_list.insert_statement_at(0, stmt)

            _create_state_machine(
                self._c, node, self._nb, self._split_all)
        elif node.txt_name == self._nb.exec_init_name:

            ctx = node.child_statement_list.ctx.start

            stmt = self._c.init_node(InitFirstStmtNode(), ctx)

            args = node.child_argument_list.childs_declarations
            if len(args) >= 2:
                stmt.txt_arg1 = args[1].txt_name
            else:
                self._c.report_error(node.ctx, "Too few arguments")

            node.child_statement_list.insert_statement_at(0, stmt)
        elif node.txt_name == self._nb.handler_init_name:
            pass
        else:
            _create_sub_state_machine(
                self._c, node, self._nb, self._split_all)


def _create_sub_state_machine(compiler, node, nb, split_all):
    '''
    Creates a sub-state machine

    '''

    stmt_list = node.child_statement_list
    i = _skip_statements(stmt_list)

    if i == 0:
        ctx = stmt_list.ctx.start
    elif i == 1:
        assert isinstance(
            stmt_list.childs_statements[0], MainFirstStmtNode)
        ctx = stmt_list.ctx.start
    else:
        ctx = stmt_list.childs_statements[i - 1].ctx.stop

    sm = compiler.init_node(StateMachineStmtNode(), ctx)
    stmt_list.insert_statement_at(i, sm)

    v = _StatementsVisitor(compiler, sm, nb, split_all)
    v.visit_stmt_list(stmt_list, i + 1)

    if sm.has_states():
        moved_vars = v.get_moved_vars()
        nb.add_function_with_states(node, sm, moved_vars)

        ctx = stmt_list.ctx.start
        stmt = compiler.init_node(SubFirstStmtNode(), ctx)
        stmt_list.insert_statement_at(0, stmt)

        if not isinstance(node.child_return_type.ref_type_declaration,
                          (VoidTypeDeclNode, IntTypeDeclNode)):
            compiler.report_error(
                node.ctx,
                "Function return type not supported for sub states creation")

        if not stmt_list.is_closed_stmt():
            stmt = compiler.init_node(
                BeforeReturnStmtNode(), stmt_list.ctx.stop)
            stmt_list.add_statement(stmt)


def _create_state_machine(compiler, node, nb, split_all):
    '''
    Creates an state machine
    '''
    stmt_list = node.child_statement_list

    if not stmt_list.is_closed_stmt():
        compiler.report_error(stmt_list.ctx, "Missing 'return' statement")
        return

    i = _skip_statements(stmt_list)

    if i == 0:
        assert False
    if i == 1:
        assert isinstance(
            stmt_list.childs_statements[0], MainFirstStmtNode)
        ctx = stmt_list.ctx.start
    else:
        ctx = stmt_list.childs_statements[i - 1].ctx.stop

    sm = compiler.init_node(StateMachineStmtNode(), ctx)
    sm.flag_main_machine = True
    stmt_list.insert_statement_at(i, sm)

    v = _StatementsVisitor(compiler, sm, nb, split_all)
    v.visit_stmt_list(stmt_list, i + 1)

    moved_vars = v.get_moved_vars()
    nb.add_function_with_states(node, sm, moved_vars)


def _skip_statements(stmt_list):

    for i in range(len(stmt_list.childs_statements)):
        stmt = stmt_list.childs_statements[i]
        if isinstance(stmt, MainFirstStmtNode):
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
    Here we insert cut point into the code, to mark where each state ends
    and the next one begins.

    Since we use goto to jump to the appropriate place into the source code,
    the logic is very simple, just insert a cut point into the source code,
    and give it an index to identify it
    Once we finish we will have the same source code, but cut into logic
    segments
    '''

    def __init__(self, compiler, state_machine, nb, split_all):
        '''
        Constructor
        '''
        self._c = compiler
        self._sm = state_machine
        self._nb = nb
        self._h = DeclsHelper()
        self._split_all = split_all

        self._stmt_list = []
        self._index = []

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._c.report_error(
            node.ctx, "Statement not supported")

    def get_moved_vars(self):
        return self._h.get_decls_to_be_moved()

    def insert_before_current(self, stmt):
        '''
        Insert statement before current one
        Index will be incremented to account for the extra statement
        Inserted statement will never be visited, because it will be inserted
        at a place visitor already did
        '''
        self._stmt_list[-1].insert_statement_at(self._index[-1], stmt)

        self._index[-1] += 1

    def insert_after_current(self, stmt):
        '''
        Insert statement after current one
        Index will be incremented to account for the extra statement
        and to avoid visitation of inserted statement
        '''
        self._stmt_list[-1].insert_statement_at(self._index[-1] + 1, stmt)

        self._index[-1] += 1

    def _wait_after_current(self, wait_condition, ctx):
        '''
        Adds 'PLUGIN_WAITING' state change after current statement
        '''
        nxt = self._c.init_node(WaitStateStmtNode(), ctx)
        nxt.ref_waiting_for = wait_condition
        nxt.int_next_state = self._sm.increment_state()
        self.insert_after_current(nxt)

    def _debug_after_current(self, ctx):
        '''
        Adds 'PLUGIN_DEBUG' state change after current statement
        '''
        nxt = self._c.init_node(DebugStateStmtNode(), ctx)
        nxt.int_next_state = self._sm.increment_state()
        self.insert_after_current(nxt)

    def _substates_around_current(self, ctx):
        '''
        Adds before and after statements for sub states function calls
        '''
        bef = self._c.init_node(BeforeSubStmtNode(), ctx)
        bef.int_next_state = self._sm.increment_state()
        self.insert_before_current(bef)

        aft = self._c.init_node(AfterSubStmtNode(), ctx)
        self.insert_after_current(aft)

    def visit_stmt_list(self, stmt_list, begin=0):
        '''
        Visit each statement in stmt_list starting from begin
        Visiting an StmtListNode will call this method, so it is reentrant
        And we also need access to current StmtListNode and index for statement
        insertion, so we keep an stack of StmtListNode and the index on each
        list we currently are
        '''

        assert isinstance(stmt_list, StmtListNode)

        self._stmt_list.append(stmt_list)
        self._index.append(begin)

        while self._index[-1] < len(self._stmt_list[-1].childs_statements):
            stmt = self._stmt_list[-1].childs_statements[self._index[-1]]
            visit_node(self, stmt)

            self._index[-1] += 1

        self._stmt_list.pop()
        self._index.pop()

    def visit_StmtListNode(self, node):
        self.visit_stmt_list(node)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):

        self._h.add_var_decl(node, self._sm.get_last_state())

        if node.child_initializer is not None:
            if isinstance(node.child_initializer, FunctionCallExprNode):
                if self._nb.has_states(node.child_initializer.txt_name):
                    visit_node(
                        self, node.child_initializer.child_argument_list)
                    self._substates_around_current(node.ctx)
                    return

        visit_node(self, node.child_initializer)

        if self._split_all:
            self._debug_after_current(node.ctx)

    def visit_ExpressionStmtNode(self, node):
        visit_node(self, node.child_expression)

        if self._split_all:
            self._debug_after_current(node.ctx)

    def visit_FunctionCallStmtNode(self, node):

        visit_node(self, node.child_expression.child_argument_list)

        if self._nb.has_states(node.child_expression.txt_name):
            self._substates_around_current(node.ctx)
        elif node.flg_is_blocking:
            self._wait_after_current(node.child_expression, node.ctx)
        elif self._split_all:
            self._debug_after_current(node.ctx)

    def visit_LoopStmtNode(self, node):

        self._h.begin_loop(self._sm.get_last_state())
        visit_node(self, node.child_expression)

        self.visit_stmt_list(node.child_statement_list)
        self._h.end_loop(self._sm.get_last_state())

    def visit_ReturnStmtNode(self, node):
        if node.child_expression is not None:
            visit_node(self, node.child_expression)

        if self._sm.has_states():  # Only needed if we already have states
            stmt = self._c.init_node(BeforeReturnStmtNode(), node.ctx.start)
            self.insert_before_current(stmt)

    def visit_ImplicitReturnStmtNode(self, node):
        if self._sm.has_states():  # Only needed if we already have states
            stmt = self._c.init_node(BeforeReturnStmtNode(), node.ctx.stop)
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
        self._h.add_var_expr(node, self._sm.get_last_state())

    def visit_FunctionCallExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_ArgumentListNode(self, node):
        for each in node.childs_arguments:
            visit_node(self, each)
