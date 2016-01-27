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

from smartanthill_phc.common.base import Node, StmtListNode


def visit_node(visitor, node, box=None):
    '''
    Dynamic version of node visitor using reflection
    If visitor of specific type is not found, we look up for base classes
    in the Node hierarchy
    '''
    assert isinstance(node, Node)
    cls = type(node)

    while cls is not None:
        name = 'visit_' + cls.__name__
        attr = getattr(visitor, name, None)
        if attr is not None:
            if box is not None:
                return attr(node, box)
            else:
                return attr(node)
        else:
            b = None
            for each in cls.__bases__:
                if issubclass(each, Node):
                    assert b is None  # only one Node super is allowed
                    b = each
            cls = b

    return getattr(visitor, 'default_visit')(node)


class NodeWalker(object):

    '''
    Base class for walker
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NodeWalker, self).__init__()

    def walk(self, box):
        '''
        Walk a single node
        '''
        box.call(self.walk_node)

    def walk_childs(self, node):
        '''
        Walks all node childs
        '''
        node.for_each_child(self.walk_node)

    def walk_node(self, node, box=None):
        '''
        Base method node walking
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        assert False


class NodeVisitor(object):

    '''
    Base class for visitor
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(NodeVisitor, self).__init__()
        self._current_child = None

    def visit(self, box):
        '''
        Visit a single node
        '''
        return box.call(self._visit_wrapper)

    def visit_childs(self, node):
        '''
        Visit all childs of node
        '''

        node.for_each_child(self._visit_wrapper)

    def _visit_wrapper(self, node, box=None):
        '''
        Generic visit function wrapper
        '''
        return visit_node(self, node, box)

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        print "Node   : %s" % type(node).__name__
        print "Visitor: %s" % type(self).__name__
        assert False


class CodeVisitor(NodeVisitor):

    '''
    Base visitor with helpers for statement list modification

    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(CodeVisitor, self).__init__()
        self._stmt_list = []
        self._index = []

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

        while self._index[-1] < self._stmt_list[-1].statements.get_size():

            s = self._stmt_list[-1].statements.at(self._index[-1])
            visit_node(self, s.get())

            self._index[-1] += 1

        self._stmt_list.pop()
        self._index.pop()

    def insert_before_current(self, statement):
        '''
        Insert statement before current one
        Index will be incremented to account for the extra statement
        Inserted statement will never be visited, because it will be inserted
        at a place visitor already did
        '''
        self._stmt_list[-1].statements.insert_at(self._index[-1], statement)

        self._index[-1] += 1

    def insert_after_current(self, statement):
        '''
        Insert statement after current one
        Index will be incremented to account for the extra statement
        and to avoid visitation of inserted statement
        '''
        self._stmt_list[-1].statements.insert_at(self._index[-1] + 1,
                                                 statement)

        self._index[-1] += 1

    def replace_current_statement(self, statement):
        '''
        Replace current statement
        '''
        return self._stmt_list[-1].statements.replace_at(self._index[-1],
                                                         statement)

    def get_current_statement(self):
        '''
        Returns current statement
        '''
        return self._stmt_list[-1].statements.at(self._index[-1]).get()


def check_all_nodes_reachables(compiler, root):
    '''
    Checks a syntax tree walking it down and verifying that all node id are
    reachable and verifying parenthood relationship
    Is used as a self check to verify on common issues of the tree structure
    '''
    walker = _CheckReachableWalker(
        compiler.removed_nodes, compiler.next_node_id)
    walker.walk_node(root)
    walker.finish()


class _CheckReachableWalker(NodeWalker):

    '''
    Walker class used by check_all_nodes_reachables function
    '''

    def __init__(self, removed_nodes, next_node_id):
        super(_CheckReachableWalker, self).__init__()
        self.dones = []
        self.parents = []
        self.removed_nodes = removed_nodes
        self.next_node_id = next_node_id

    def walk_node(self, node, box=None):
        assert node
        if len(self.parents) != 0:
            assert self.parents[-1] == node.get_parent()

        self.dones.append(node.node_id)

        self.parents.append(node)
        self.walk_childs(node)
        self.parents.pop()

    def finish(self):
        self.dones += self.removed_nodes
        self.dones.sort()
        expected = 0
        for current in self.dones:
            if current == expected:
                expected += 1
            elif current == expected - 1:
                print 'Node %i has been reached again' % current
            elif current == expected + 1:
                print 'Node %i has not been reached' % expected
                expected = current + 1
            elif current > expected + 1:
                print ('Node range %i to %i has not been reached' %
                       (expected, current - 1))
                expected = current + 1
            else:
                assert False

        if expected < self.next_node_id:
            print ('Node range %i to %i has not been reached' %
                   (expected, self.next_node_id - 1))
        elif expected > self.next_node_id:
            assert False


def dump_tree(node):
    '''
    Dump a syntax tree to a human readable text format
    Used for debugging and testing
    '''
    walker = _DumpTreeWalker()
    walker.walk_node(node)
    return walker.result


class _DumpTreeWalker(NodeWalker):

    '''
    Walker class used by dump_tree function
    '''

    def __init__(self):
        super(_DumpTreeWalker, self).__init__()
        self.result = []
        self.index = 0

    def walk_node(self, node, box=None):
        ctx_attrs = ''
        names = dir(node)
        for current in names:
            if current.startswith('tk_'):
                assert False
            elif current.startswith('str_'):
                assert False
            elif current.startswith('txt_'):
                ctx_attrs += " %s='%s'" % (current[4:],
                                           getattr(node, current))
            elif current.startswith('ref_'):
                if getattr(node, current) is not None:
                    ctx_attrs += " %s>#%s" % (current[4:],
                                              getattr(node, current).node_id)
                else:
                    ctx_attrs += " <%s>" % current[4:]

        s = '+-' * self.index + type(node).__name__ + ctx_attrs
        self.result.append(s)
        self.index += 1
        self.walk_childs(node)
        self.index -= 1
