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
from smartanthill_phc.common.node import StatementNode, ExpressionNode
from smartanthill_phc.common.statement import VariableDeclarationStmtNode
from smartanthill_phc.common.visitor import visit_node, CodeVisitor,\
    NodeVisitor
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


class FunctionCallSubStmtNode(StatementNode):

    '''
    Statement node class to be used as replacement for functions calls
    with sub states
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionCallSubStmtNode, self).__init__()
        self.int_next_state = None
        self.child_expression = None
        self.txt_name = None

    def set_expression(self, child):
        '''
        expression setter
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.child_expression = child


class FunctionCallSubExprNode(ExpressionNode):

    '''
    Node class representing the use expression of FunctionCallSubStmtNode
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionCallSubExprNode, self).__init__()
        self.ref_declaration = None


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


class LoopsHelper(object):
    '''
    Helper class to detect which variables are accessed inside loops
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._loop_stack = []
        self._decls_stack = []

    def add_var_ref(self, decl):
        '''
        Adds a variable declaration
        '''
        if len(self._decls_stack) != 0:
            if decl not in self._decls_stack[-1]:
                self._decls_stack[-1].append(decl)

    def begin_loop(self, st):
        '''
        A loop begins, put a mark with state number
        '''
        self._loop_stack.append(st)
        self._decls_stack.append([])

    def end_loop(self, st):
        '''
        A loop ends, if same state number, the loop completed within the
        same state, no special treatment needed, else return a set
        with all variables that may be accessed on the following iteration,
        and which values should be preserved
        '''

        result = []
        if self._loop_stack[-1] != st:
            for loop in self._decls_stack:
                for each in loop:
                    if each not in result:
                        result.append(each)

        self._loop_stack.pop()
        self._decls_stack.pop()

        return result


class DeclsHelper(object):

    '''
    Helper class to detect which variables are accessed in each state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._decls = {}
        self._to_be_moved = []
        self._loops = LoopsHelper()

    def add_var_decl(self, decl, st):
        '''
        Adds a variable declaration
        '''
        assert decl not in self._decls
        self._decls[decl] = st

    def force_move_var_decl(self, decl):
        '''
        Adds a variable declaration and forces it into moveds
        '''
        assert decl in self._decls

        if decl not in self._to_be_moved:
            self._to_be_moved.append(decl)

    def add_var_expr(self, expr, st):
        '''
        Adds a reference (access) to a variable in certain state
        '''

        if expr.ref_decl is None or expr.ref_decl not in self._decls:
            return

        if expr.ref_decl in self._to_be_moved:  # already moved
            return

        if self._decls[expr.ref_decl] != st:
            self._to_be_moved.append(expr.ref_decl)
            return

        # Still may need to be moved because of loops
        self._loops.add_var_ref(expr.ref_decl)

    def begin_loop(self, st):
        '''
        A loop begins, put a mark with state number
        '''
        self._loops.begin_loop(st)

    def end_loop(self, st):
        '''
        A loop ends, if same state number, the loop completed within the
        same state, no special treatment needed
        '''
        result = self._loops.end_loop(st)
        for each in result:
            if each not in self._to_be_moved:
                self._to_be_moved.append(each)

    def get_decls_to_be_moved(self):
        '''
        Now we have the complete list of variable declarations that need to
        be moved, make a sanity check to avoid name duplication,
        mangle name if needed
        '''

        names = set()
        i = 0
        for each in self._to_be_moved:
            if each.txt_name in names:
                tmp = each.txt_name
                while tmp in names:
                    i += 1
                    tmp = each.txt_name + str(i)

                each.txt_name = tmp

            assert each.txt_name not in names
            names.add(each.txt_name)

        return self._to_be_moved


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


class StateMachineVisitor(NodeVisitor):

    def __init__(self, compiler, nb, split_all):
        '''
        Constructor
        '''
        super(StateMachineVisitor, self).__init__()
        self._c = compiler
        self._nb = nb
        self._split_all = split_all

    def visit_RootNode(self, node):
        self.visit(node.child_source)

    def visit_PluginSourceNode(self, node):
        self.visit(node.child_declaration_list)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            self.visit(each)

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

            self._create_state_machine(node)
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
            self._create_sub_state_machine(node)

    def _create_sub_state_machine(self, node):
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

        sm = self._c.init_node(StateMachineStmtNode(), ctx)
        stmt_list.insert_statement_at(i, sm)

        v = _StatementsVisitor(self._c, sm, self._nb, self._split_all)
        v.visit_stmt_list(stmt_list, i + 1)

        if sm.has_states():
            moved_vars = v.get_moved_vars()
            self._nb.add_function_with_states(node, sm, moved_vars)

            ctx = stmt_list.ctx.start
            stmt = self._c.init_node(SubFirstStmtNode(), ctx)
            stmt_list.insert_statement_at(0, stmt)

            if not isinstance(node.child_return_type.ref_type_declaration,
                              (VoidTypeDeclNode, IntTypeDeclNode)):
                self._c.report_error(
                    node.ctx,
                    "Function return type not supported for sub states")

            if not stmt_list.is_closed_stmt():
                stmt = self._c.init_node(
                    BeforeReturnStmtNode(), stmt_list.ctx.stop)
                stmt_list.add_statement(stmt)

    def _create_state_machine(self, node):
        '''
        Creates an state machine
        '''
        stmt_list = node.child_statement_list

        if not stmt_list.is_closed_stmt():
            self._c.report_error(stmt_list.ctx, "Missing 'return' statement")
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

        sm = self._c.init_node(StateMachineStmtNode(), ctx)
        sm.flag_main_machine = True
        stmt_list.insert_statement_at(i, sm)

        v = _StatementsVisitor(self._c, sm, self._nb, self._split_all)
        v.visit_stmt_list(stmt_list, i + 1)

        moved_vars = v.get_moved_vars()
        self._nb.add_function_with_states(node, sm, moved_vars)


class _StatementsVisitor(CodeVisitor):
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
        super(_StatementsVisitor, self).__init__()
        self._c = compiler
        self._sm = state_machine
        self._nb = nb
        self._h = DeclsHelper()
        self._split_all = split_all

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._c.report_error(
            node.ctx, "Statement not supported")

    def get_moved_vars(self):
        return self._h.get_decls_to_be_moved()

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
                    self._h.force_move_var_decl(node)
                    visit_node(
                        self, node.child_initializer.child_argument_list)
                    self._substates_around_current(node.ctx)
                    return

        self.visit_expression(node, 'child_initializer')

        if self._split_all:
            self._debug_after_current(node.ctx)

    def visit_ExpressionStmtNode(self, node):
        self.visit_expression(node, 'child_expression')

        if self._split_all:
            self._debug_after_current(node.ctx)

    def visit_FunctionCallStmtNode(self, node):

        self.visit(node.child_expression.child_argument_list)

        if self._nb.has_states(node.child_expression.txt_name):
            self._substates_around_current(node.ctx)
        elif node.flg_is_blocking:
            self._wait_after_current(node.child_expression, node.ctx)
        elif self._split_all:
            self._debug_after_current(node.ctx)

    def visit_LoopStmtNode(self, node):

        self._h.begin_loop(self._sm.get_last_state())

        self.visit_expression(node, 'child_expression')
        self.visit(node.child_statement_list)

        self._h.end_loop(self._sm.get_last_state())

    def visit_ReturnStmtNode(self, node):
        self.visit_expression(node, 'child_expression')

        if self._sm.has_states():  # Only needed if we already have states
            stmt = self._c.init_node(BeforeReturnStmtNode(), node.ctx.start)
            self.insert_before_current(stmt)

    def visit_ImplicitReturnStmtNode(self, node):
        if self._sm.has_states():  # Only needed if we already have states
            stmt = self._c.init_node(BeforeReturnStmtNode(), node.ctx.stop)
            self.insert_before_current(stmt)

    def visit_IfElseStmtNode(self, node):

        self.visit_expression(node, 'child_expression')
        self.visit(node.child_if_branch)
        if node.child_else_branch is not None:
            self.visit(node.child_else_branch)

    def visit_DontCareExprNode(self, node):
        self.visit_expression_list(node, node.childs_expressions)

    def visit_BinaryOpExprNode(self, node):
        self.visit(node.child_argument_list)

    def visit_UnaryOpExprNode(self, node):
        self.visit(node.child_argument_list)

    def visit_PostfixOpExprNode(self, node):
        self.visit(node.child_argument_list)

    def visit_LiteralExprNode(self, node):
        pass

    def visit_TypeCastExprNode(self, node):
        self.visit_expression(node, 'child_expression')

    def visit_VariableExprNode(self, node):
        self._h.add_var_expr(node, self._sm.get_last_state())

    def visit_FunctionCallExprNode(self, node):
        self.visit(node.child_argument_list)

        if self._nb.has_states(node.txt_name):
            ctx = self.get_current_statement().ctx
            stmt = self._c.init_node(FunctionCallSubStmtNode(), ctx)
            stmt.int_next_state = self._sm.increment_state()
            stmt.set_expression(node)
            stmt.txt_name = 'zc_temp_var'
            self.insert_before_current(stmt)

            var = self._c.init_node(FunctionCallSubExprNode(), node.ctx)
            var.ref_declaration = stmt
            self.replace_expression(var)

    def visit_FunctionCallSubExprNode(self, node):
        pass

    def visit_ArgumentListNode(self, node):
        self.visit_expression_list(node, node.childs_arguments)
