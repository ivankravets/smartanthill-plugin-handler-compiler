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

    def is_flow_stmt(self):
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


class JumpStateStmtNode(StatementNode):

    '''
    Statement node class representing an state jump that does not need to wait
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(JumpStateStmtNode, self).__init__()
        self.ref_next_state = None

    def is_flow_stmt(self):
        '''
        Returns true
        '''
        # pylint: disable=no-self-use
        return True


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

    assert len(stmt_list.childs_statements) != 0

    sm = compiler.init_node(StateMachineStmtNode(), Ctx.NONE)

    sl = compiler.init_node(StmtListNode(), stmt_list.ctx)

    i = _skip_statements(stmt_list)
    stmt_list.split_at(i, sl)
    stmt_list.add_statement(sm)

    _create_state(compiler, sm, sl, helper)

    if not sm.childs_states[-1].child_statement_list.has_flow_stmt:
        x = sm.childs_states[-1].child_statement_list.childs_statements[-1].ctx
        compiler.report_error(x, "Missing 'return' statement")


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

    v = _StatementsSplitterVisitor(compiler, state_machine, st, helper)
    visit_node(v, stmt_list)

    return st


# pylint: disable=too-many-instance-attributes


class _StatementsSplitterVisitor(NodeVisitor):

    def __init__(self, compiler, state_machine, state, helper):
        '''
        Constructor
        '''
        self._c = compiler
        self._sm = state_machine
        self._st = state
        self._h = helper
        self._was_blocking = False
        self._was_split = False
        self._was_return = False
        self._jumps = []

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._c.report_error(
            node.ctx, "Statement not supported")

    def _create_state(self, stmt_list):
        return _create_state(self._c, self._sm, stmt_list, self._h)

    def _visit_stmt_list(self, node):

        for i in range(len(node.childs_statements)):
            visit_node(self, node.childs_statements[i])

            if self._was_blocking:
                sl = self._c.init_node(StmtListNode(), node.ctx)
                node.split_at(i + 1, sl)

                if not node.has_flow_stmt:
                    jmp = self._c.init_node(JumpStateStmtNode(), node.ctx)
                    sl.add_statement(jmp)
                    sl.has_flow_stmt = True
                    self._jumps.append(jmp)

                # use last statement ctx
                ctx = node.childs_statements[-1].ctx
                nxt = self._c.init_node(NextStateStmtNode(), ctx)
                nxt.ref_next_state = self._create_state(sl)
                node.add_statement(nxt)
                node.has_flow_stmt = True

                # this node does not have more statements to process, return
                self._was_blocking = False
                return
            elif self._was_split:
                if len(self._jumps) == 0:
                    # nothing to do
                    self._was_split = False
                elif len(node.childs_statements) == i + 1:
                    # make it else where
                    return
                else:
                    self._was_split = False

                    sl = self._c.init_node(StmtListNode(), node.ctx)
                    node.split_at(i + 1, sl)

                    # use last statement ctx
                    ctx = node.childs_statements[-1].ctx
                    jmp = self._c.init_node(JumpStateStmtNode(), ctx)
                    jmp.ref_next_state = self._create_state(sl)
                    node.add_statement(jmp)
                    node.has_flow_stmt = True

                    for j in self._jumps:
                        j.ref_next_state = jmp.ref_next_state

                    self._jumps = []
                    # this node does not have more statements to process,
                    # return
                    return
            elif self._was_return:
                # remove all statements below this
                sl = self._c.init_node(StmtListNode(), node.ctx)
                node.split_at(i + 1, sl)
                self._c.remove_nodes(sl)

                # use last statement ctx
                ctx = node.childs_statements[-1].ctx
                nxt = self._c.init_node(InitStateStmtNode(), ctx)
                node.insert_statement_at(i, nxt)
                node.has_flow_stmt = True

                # this node does not have more statements to process,
                # return
                self._was_return = False
                return

    def visit_StmtListNode(self, node):
        self._visit_stmt_list(node)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):

        self._h.add_var_decl(node, self._st)
        visit_node(self, node.child_initializer)

    def visit_ExpressionStmtNode(self, node):
        visit_node(self, node.child_expression)

    def visit_BlockingCallStmtNode(self, node):
        self._was_blocking = True
        visit_node(self, node.child_expression)

    def visit_ReturnStmtNode(self, node):
        self._was_return = True
        visit_node(self, node.child_expression)

    def visit_IfElseStmtNode(self, node):
        visit_node(self, node.child_expression)
        visit_node(self, node.child_if_branch)
        if node.child_else_branch is not None:
            visit_node(self, node.child_else_branch)

        self._was_split = True

    def visit_JumpStateStmtNode(self, node):
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
