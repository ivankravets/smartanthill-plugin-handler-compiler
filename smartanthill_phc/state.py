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

from smartanthill_phc.c_node import CastExprNode, IntTypeDeclNode,\
    VoidTypeDeclNode
from smartanthill_phc.common.base import StatementNode, ExpressionNode,\
    ArgumentListNode, Child, ChildExpr
from smartanthill_phc.common.compiler import BuiltinCtx
from smartanthill_phc.common.expr import VariableExprNode,\
    FunctionCallExprNode
from smartanthill_phc.common.stmt import VariableDeclarationStmtNode
from smartanthill_phc.common.visitor import visit_node, CodeVisitor,\
    NodeVisitor
from smartanthill_phc.root import NonBlockingData


STATE = BuiltinCtx('<state>')


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
        self.expression = ChildExpr(self)
        self.txt_name = None


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


class StatefullCallArgumentExprNode(ExpressionNode):

    '''
    Node class representing the extra arguments needed when doing an statefull
    function call
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StatefullCallArgumentExprNode, self).__init__()


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


class PapiWaitStmtNode(StatementNode):

    '''
    Node class representing a blocking function call statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PapiWaitStmtNode, self).__init__()
        self.int_next_state = None
        self.txt_name = None
        self.txt_wait_for = None
        self.argument_list = Child(self, ArgumentListNode)
        self.ctx_function_name = None


class PapiSleepStmtNode(StatementNode):

    '''
    Node class representing a blocking function call statement
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PapiSleepStmtNode, self).__init__()
        self.int_next_state = None
        self.argument_list = Child(self, ArgumentListNode)


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

    def add_var_expr(self, e, st):
        '''
        Adds a reference (access) to a variable in certain state
        '''

        if e.ref_declaration is None or e.ref_declaration not in self._decls:
            return

        if e.ref_declaration in self._to_be_moved:  # already moved
            return

        if self._decls[e.ref_declaration] != st:
            self._to_be_moved.append(e.ref_declaration)
            return

        # Still may need to be moved because of loops
        self._loops.add_var_ref(e.ref_declaration)

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


class _StateCountHelper(object):

    '''
    Node class representing an state machine
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._last_state = 0

    def increment_state(self):
        '''
        Increments the state counter
        '''
        self._last_state += 1

        return self._last_state

    def get_last_state(self):
        '''
        Returns the last added state
        '''
        return self._last_state

    def has_states(self):
        '''
        Returns where this state machine really has states
        '''
        return self._last_state != 0


def _skip_statements(stmt_list):

    for i in range(stmt_list.statements.get_size()):
        s = stmt_list.statements.at(i).get()
        if isinstance(s, MainFirstStmtNode):
            continue

        if not isinstance(s, VariableDeclarationStmtNode):
            return i
        if not isinstance(s.initializer_expression.get(), CastExprNode):
            return i
        if not isinstance(s.initializer_expression.get().expression.get(),
                          VariableExprNode):
            return i

    return stmt_list.statements.get_size()


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
        self.visit(node.source)

    def visit_PluginSourceNode(self, node):
        self.visit_childs(node)

    def visit_DeclarationListNode(self, node):
        self.visit_childs(node)

    def visit_PreprocessorDirectiveNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        pass

    def visit_IncludeFileNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        pass

    def visit_ConstantDefineNode(self, node):
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        pass

    def visit_FunctionDefinitionNode(self, node):
        if node.declaration.get().txt_name == self._nb.handler_name:

            self._create_state_machine(node)
        elif node.declaration.get().txt_name == self._nb.exec_init_name:

            ctx = node.statement_list.get().ctx.start

            s = self._c.init_node(InitFirstStmtNode(), ctx)

            args = node.declaration.get().argument_decl_list.get().declarations
            if args.get_size() >= 2:
                s.txt_arg1 = args.at(1).get().txt_name
            else:
                self._c.report_error(node.ctx, "Too few arguments")

            node.statement_list.get().statements.insert_at(0, s)
        elif node.declaration.get().txt_name == self._nb.handler_init_name:
            pass
        else:
            self._create_sub_state_machine(node)

    def visit_FunctionDeclNode(self, node):
        pass

    def _create_sub_state_machine(self, node):
        '''
        Creates a sub-state machine

        '''

        stmt_list = node.statement_list.get()
        i = _skip_statements(stmt_list)
        if i == 0:
            ctx = stmt_list.ctx.start
        else:
            ctx = stmt_list.statements.at(i - 1).get().ctx.stop

        v = _StatementsVisitor(self._c, self._nb, self._split_all)
        v.visit_stmt_list(stmt_list, i)

        if v.has_states():
            sm = self._c.init_node(StateMachineStmtNode(), ctx)
            sm.int_last_state = v.get_last_state()
            stmt_list.statements.insert_at(i, sm)

            s = self._c.init_node(SubFirstStmtNode(), ctx)
            stmt_list.statements.insert_at(0, s)

            moved_vars = v.get_moved_vars()
            self._nb.add_function_with_states(
                node.declaration.get(), sm, moved_vars)

            if not isinstance(
                    node.declaration.get().return_type.get(
                    ).ref_type_declaration,
                    (VoidTypeDeclNode, IntTypeDeclNode)):
                self._c.report_error(
                    node.ctx,
                    "Function return type not supported for sub states")

            if not stmt_list.is_closed_stmt():
                s = self._c.init_node(
                    BeforeReturnStmtNode(), stmt_list.ctx.stop)
                stmt_list.statements.add(s)

    def _create_state_machine(self, node):
        '''
        Creates an state machine
        '''
        stmt_list = node.statement_list.get()

        if not stmt_list.is_closed_stmt():
            self._c.report_error(stmt_list.ctx, "Missing 'return' statement")
            return

        i = _skip_statements(stmt_list)
        if i == 0:
            ctx = stmt_list.ctx.start
        else:
            ctx = stmt_list.statements.at(i - 1).get().ctx.stop

        v = _StatementsVisitor(self._c, self._nb, self._split_all)
        v.visit_stmt_list(stmt_list, i)

        if v.has_states():
            sm = self._c.init_node(StateMachineStmtNode(), ctx)
            sm.int_last_state = v.get_last_state()
            sm.flag_main_machine = True
            stmt_list.statements.insert_at(i, sm)

            s = self._c.init_node(MainFirstStmtNode(), ctx)

            args = node.declaration.get().argument_decl_list.get().declarations
            if args.get_size() >= 6:
                s.txt_arg2 = args.at(2).get().txt_name
                s.txt_arg5 = args.at(5).get().txt_name
            else:
                self._c.report_error(node.ctx, "Too few arguments")

            stmt_list.statements.insert_at(0, s)

            moved_vars = v.get_moved_vars()
            self._nb.add_function_with_states(
                node.declaration.get(), sm, moved_vars)


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

    def __init__(self, compiler, nb, split_all):
        '''
        Constructor
        '''
        super(_StatementsVisitor, self).__init__()
        self._c = compiler
        self._sc = _StateCountHelper()
        self._nb = nb
        self._h = DeclsHelper()
        self._split_all = split_all

    def get_moved_vars(self):
        return self._h.get_decls_to_be_moved()

    def has_states(self):
        return self._sc.has_states()

    def get_last_state(self):
        return self._sc.get_last_state()

    def _debug_after_current(self, ctx):
        '''
        Adds 'PLUGIN_DEBUG' state change after current statement
        '''
        nxt = self._c.init_node(DebugStateStmtNode(), ctx)
        nxt.int_next_state = self._sc.increment_state()
        self.insert_after_current(nxt)

    def _substates_around_current(self, ctx):
        '''
        Adds before and after statements for sub states function calls
        '''
        bef = self._c.init_node(BeforeSubStmtNode(), ctx)
        bef.int_next_state = self._sc.increment_state()
        self.insert_before_current(bef)

        aft = self._c.init_node(AfterSubStmtNode(), ctx)
        self.insert_after_current(aft)

    def visit_StmtListNode(self, node):
        self.visit_stmt_list(node)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):

        self._h.add_var_decl(node, self._sc.get_last_state())

        if not node.initializer_expression.is_none() and\
                isinstance(node.initializer_expression.get(),
                           FunctionCallExprNode):
            init_expr = node.initializer_expression.get()
            if init_expr.ref_declaration is not None and\
                    self._nb.has_states(init_expr.ref_declaration):

                self.visit(init_expr.argument_list)

                a = self._c.init_node(
                    StatefullCallArgumentExprNode(), init_expr.ctx)
                init_expr.argument_list.get().arguments.insert_at(0, a)

                self._substates_around_current(node.ctx)
                return

        self.visit_childs(node)

        if self._split_all:
            self._debug_after_current(node.ctx)

    def visit_ExpressionStmtNode(self, node):
        self.visit_childs(node)

        if self._split_all:
            self._debug_after_current(node.ctx)

    def visit_FunctionCallStmtNode(self, node):

        self.visit(node.expression.get().argument_list)

        if self._nb.has_states(node.expression.get().ref_declaration):
            a = self._c.init_node(
                StatefullCallArgumentExprNode(), node.expression.get().ctx)
            node.expression.get().argument_list.get().arguments.insert_at(0, a)
            self._substates_around_current(node.ctx)

        elif node.expression.get().bool_is_blocking:
            d = node.expression.get().ref_declaration
            n = d.txt_name
            if n == "papi_sleep":
                s = self._c.init_node(PapiSleepStmtNode(), node.ctx)
            else:
                if n == "papi_wait_for_spi_send":
                    f = u"papi_start_sending_spi_command_16"
                    w = u"spi_send"
                elif n == "papi_wait_for_i2c_send":
                    f = u"papi_start_sending_i2c_command_16"
                    w = u"i2c_send"
                elif n == "papi_wait_for_spi_receive":
                    f = u"papi_start_receiving_spi_data_16"
                    w = u"spi_receive"
                elif n == "papi_wait_for_i2c_receive":
                    f = u"papi_start_receiving_i2c_data_16"
                    w = u"i2c_receive"
                else:
                    assert False

                s = self._c.init_node(PapiWaitStmtNode(), node.ctx)
                s.txt_name = f
                s.txt_wait_for = w
                s.ctx_function_name = node.expression.get().ctx.\
                    unaryExpression().Identifier()

            s.argument_list.set(node.expression.get().argument_list.clear())
            s.int_next_state = self._sc.increment_state()

            old = self.replace_current_statement(s)
            self._c.remove_nodes(old)

        elif self._split_all:
            self._debug_after_current(node.ctx)

    def visit_LoopStmtNode(self, node):

        self._h.begin_loop(self._sc.get_last_state())
        self.visit_childs(node)
        self._h.end_loop(self._sc.get_last_state())

    def visit_ReturnStmtNode(self, node):
        self.visit_childs(node)

        if self._sc.has_states():  # Only needed if we already have states
            s = self._c.init_node(BeforeReturnStmtNode(), node.ctx.start)
            self.insert_before_current(s)

    def visit_ImplicitReturnStmtNode(self, node):
        if self._sc.has_states():  # Only needed if we already have states
            s = self._c.init_node(BeforeReturnStmtNode(), node.ctx.stop)
            self.insert_before_current(s)

    def visit_IfElseStmtNode(self, node):
        self.visit_childs(node)

    def visit_TypeNode(self, node):
        pass

    def visit_MemberAccessExprNode(self, node):
        self.visit_childs(node)

    def visit_AssignmentExprNode(self, node):
        self.visit_childs(node)

    def visit_ConditionalExprNode(self, node):
        self.visit_childs(node)

    def visit_OperatorExprNode(self, node):
        self.visit_childs(node)

    def visit_PointerExprNode(self, node):
        self.visit_childs(node)

    def visit_AddressOfExprNode(self, node):
        self.visit_childs(node)

    def visit_MemberOperatorExprNode(self, node):
        self.visit_childs(node)

#     def visit_UnaryOpExprNode(self, node):
#         self.visit(node.child_argument_list)
#
#     def visit_PostfixOpExprNode(self, node):
#         self.visit(node.child_argument_list)

    def visit_LiteralExprNode(self, node):
        pass

    def visit_CastExprNode(self, node):
        self.visit_childs(node)

    def visit_TrivialCastExprNode(self, node):
        self.visit_childs(node)

    def visit_VariableExprNode(self, node):
        self._h.add_var_expr(node, self._sc.get_last_state())

    def visit_FunctionCallExprNode(self, node):
        self.visit_childs(node)

        if self._nb.has_states(node.ref_declaration):
            ctx = self.get_current_statement().ctx
            a = self._c.init_node(StatefullCallArgumentExprNode(), node.ctx)
            node.argument_list.get().arguments.insert_at(0, a)

            s = self._c.init_node(FunctionCallSubStmtNode(), ctx)
            s.int_next_state = self._sc.increment_state()
            s.expression.set(node)
            s.txt_name = 'zc_tmp%s' % s.int_next_state
            self.insert_before_current(s)

            var = self._c.init_node(FunctionCallSubExprNode(), node.ctx)
            var.ref_declaration = s
            self.replace_current_expression(var)

    def visit_FunctionCallSubExprNode(self, node):
        pass

    def visit_ArgumentListNode(self, node):
        self.visit_childs(node)
