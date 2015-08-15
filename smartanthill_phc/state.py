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

from smartanthill_phc.common.compiler import Ctx
from smartanthill_phc.common.node import Node, StmtListNode, StatementNode
from smartanthill_phc.common.visitor import NodeVisitor, visit_node


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

    def add_state(self, child):
        '''
        statement list setter
        '''
        assert isinstance(child, StateNode)
        assert child is not None
        child.set_parent(self)
        self.childs_states.append(child)

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


class StateMachineVisitor(NodeVisitor):

    def __init__(self, compiler):
        '''
        Constructor
        '''
        self._c = compiler

    def visit_PluginSourceNode(self, node):
        visit_node(self, node.child_declaration_list)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            visit_node(self, each)

    def visit_FunctionDeclNode(self, node):
        _create_state_machine(self._c, node.child_statement_list)


def _create_state_machine(compiler, stmt_list):
    '''
    Creates an state machine
    '''

    if len(stmt_list.childs_statements) != 0:
        ctx = stmt_list.childs_statements[0].ctx
        sm = compiler.init_node(StateMachineStmtNode(), ctx)

        sl = compiler.init_node(StmtListNode(), Ctx.NONE)
        stmt_list.split_at(0, sl)
        stmt_list.add_statement(sm)

        _create_state(compiler, sm, sl)


def _create_state(compiler, state_machine, stmt_list):
    '''
    Creates a new state
    '''

    st = compiler.init_node(StateNode(), Ctx.NONE)
    st.set_statement_list(stmt_list)

    state_machine.add_state(st)

    st.txt_id = str(len(state_machine.childs_states))

    v = _StatementsSplitterVisitor(compiler, state_machine)
    visit_node(v, stmt_list)

    return st


class _StatementsSplitterVisitor(NodeVisitor):

    def __init__(self, compiler, state_machine):
        '''
        Constructor
        '''
        self._c = compiler
        self._sm = state_machine
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
            if self._split:
                sl = self._c.init_node(StmtListNode(), Ctx.NONE)
                node.split_at(i, sl)

                stmt = self._c.init_node(NextStateStmtNode(), Ctx.NONE)
                stmt.ref_next = _create_state(self._c, self._sm, sl)
                node.add_statement(stmt)

                # this node does not have more statements to process, return
                self._split = False
                return

            else:
                visit_node(self, node.childs_statements[i])
                if self._was_return:
                    # remove all statements below this
                    sl = self._c.init_node(StmtListNode(), Ctx.NONE)
                    node.split_at(i + 1, sl)
                    self._c.remove_nodes(sl)

                    stmt = self._c.init_node(NextStateStmtNode(), Ctx.NONE)
                    # stmt.ref_next = None
                    node.insert_statement_at(i, stmt)

                    # this node does not have more statements to process,
                    # return
                    self._was_return = False
                    return

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):
        # TODO
        pass

    def visit_ExpressionStmtNode(self, node):
        pass

    def visit_BlockingCallStmtNode(self, node):
        # pylint: disable=unused-argument
        self._split = True

    def visit_ReturnStmtNode(self, node):
        # pylint: disable=unused-argument
        self._was_return = True
