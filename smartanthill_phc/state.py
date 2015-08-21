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
from smartanthill_phc.root import NonBlockingDataNode


def create_states(compiler, root, func_name):
    '''
    Creates state machine and state related nodes
    '''
    visitor = StateMachineVisitor(compiler, func_name)
    visit_node(visitor, root)
    nb = visitor.finish()
    root.set_non_blocking_data(nb)

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


#     def resolve(self, compiler):
#         compiler.resolve_node(self.child_statement_list)


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
    Node class representing an state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NextStateStmtNode, self).__init__()
        self.ref_next_state = None


class StateMachineDataNode(Node):
    '''
    Keep track of all data accessed by each state
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StateMachineDataNode, self).__init__()


class DeclsHelper(object):

    '''
    Node class representing an state machine
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
        nb = self._c.init_node(NonBlockingDataNode(), Ctx.BUILTIN)
        nb.refs_moved_var_decls = self._h.analyze_vars()
        return nb

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

    def visit_FunctionDeclNode(self, node):
        if node.txt_name == self._func_name:
            self._func_found = True
            _create_state_machine(
                self._c, node.child_statement_list, self._h)


def _create_state_machine(compiler, stmt_list, helper):
    '''
    Creates an state machine
    '''

    assert len(stmt_list.childs_statements) != 0

    sm = compiler.init_node(StateMachineStmtNode(), Ctx.NONE)

    sl = compiler.init_node(StmtListNode(), Ctx.NONE)

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


class _StatementsSplitterVisitor(NodeVisitor):

    def __init__(self, compiler, state_machine, state, helper):
        '''
        Constructor
        '''
        self._c = compiler
        self._sm = state_machine
        self._st = state
        self._h = helper
        self._split = False
        self._was_return = False

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._c.report_error(
            node.ctx, "Statement not supported")

    def visit_StmtListNode(self, node):

        for i in range(len(node.childs_statements)):
            visit_node(self, node.childs_statements[i])
            if self._split:
                sl = self._c.init_node(StmtListNode(), Ctx.NONE)
                node.split_at(i + 1, sl)

                # use last statement ctx
                ctx = node.childs_statements[-1].ctx
                stmt = self._c.init_node(NextStateStmtNode(), ctx)
                stmt.ref_next_state = _create_state(
                    self._c, self._sm, sl, self._h)
                node.add_statement(stmt)
                node.has_flow_stmt = True

                # this node does not have more statements to process, return
                self._split = False
                return
            elif self._was_return:
                # remove all statements below this
                sl = self._c.init_node(StmtListNode(), Ctx.NONE)
                node.split_at(i + 1, sl)
                self._c.remove_nodes(sl)

                # use last statement ctx
                ctx = node.childs_statements[-1].ctx
                stmt = self._c.init_node(NextStateStmtNode(), ctx)
                # stmt.ref_next_state = None
                node.insert_statement_at(i, stmt)
                node.has_flow_stmt = True

                # this node does not have more statements to process,
                # return
                self._was_return = False
                return

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):

        self._h.add_var_decl(node, self._st)
        visit_node(self, node.child_initializer)

    def visit_ExpressionStmtNode(self, node):
        visit_node(self, node.child_expression)

    def visit_BlockingCallStmtNode(self, node):
        self._split = True
        visit_node(self, node.child_expression)

    def visit_ReturnStmtNode(self, node):
        self._was_return = True
        visit_node(self, node.child_expression)

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
