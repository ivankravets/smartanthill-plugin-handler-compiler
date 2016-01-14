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


from smartanthill_phc.common import errors
from smartanthill_phc.common.lookup import RootScope, StatementListScope


class ResolutionHelper(object):

    '''
    Helper base class provides resolution cycle safety
    It must be used by all classes that can be called to resolve
    on demand (as the result of some look-up)
    '''

    _NOT_RESOLVED = 0
    _RESOLVING_NOW = 1
    _RESOLVED_OK = 2
    _RESOLUTION_ERROR = 3

    def __init__(self):
        '''
        Constructor
        '''
        super(ResolutionHelper, self).__init__()
        self._resolved_flag = self._NOT_RESOLVED
        self._resolved_type = None

#     def resolve(self, compiler):
#         '''
#         Resolve, will call template method do_resolve_declaration that needs
#         be at implementing class
#         '''
#         try:
#             if self._resolved_flag == self._NOT_RESOLVED:
#                 self._resolved_flag = self._RESOLVING_NOW
#                 self._resolved_type = self.do_resolve_declaration(compiler)
#                 assert self._resolved_type
#                 self._resolved_flag = self._RESOLVED_OK
#             elif self._resolved_flag == self._RESOLVING_NOW:
#                 raise errors.ResolutionCycleError()
#             elif self._resolved_flag == self._RESOLVED_OK:
#                 pass
#             elif self.resolved_flag == self._RESOLUTION_ERROR:
#                 pass
#             else:
#                 assert False
#         except:
#             self._resolved_flag = self._RESOLUTION_ERROR
#             self._resolved_type = None
#             raise

    def begin_resolution(self):
        if self._resolved_flag == self._NOT_RESOLVED:
            self._resolved_flag = self._RESOLVING_NOW
            return True
        else:
            return False

    def get_type(self):
        '''
        Returns the type of this declaration, if resolve was not called before,
        or it did not complete properly, it will raise an error
        '''

        if self._resolved_flag == self._NOT_RESOLVED:
            raise errors.UnresolvedError()
        elif self._resolved_flag == self._RESOLVING_NOW:
            raise errors.ResolutionCycleError()
        elif self._resolved_flag == self._RESOLVED_OK:
            return self._resolved_type
        elif self._resolved_flag == self._RESOLUTION_ERROR:
            raise errors.PreviousResolutionError()
        else:
            assert False

    def set_type(self, type_ref):
        '''
        Sets the type of this declaration
        '''

        assert self._resolved_flag == self._RESOLVING_NOW
        assert type_ref
        self._resolved_type = type_ref
        self._resolved_flag = self._RESOLVED_OK


class Child(object):
    '''
    Intermediate instance to hold a child reference
    '''

    def __init__(self, parent, allowed_type, optional=False, list_item=False):
        '''
        Constructor
        '''
        super(Child, self).__init__()
        self._child_node = None
        self._parent = parent
        self._allowed_type = allowed_type
        self._optional = optional

        if not list_item:
            parent.add_child(self)

    def set(self, child):
        '''
        Sets the child
        There must not be any previous child
        '''
        assert isinstance(child, self._allowed_type)
        assert self._child_node is None
        child.set_parent(self._parent)
        self._child_node = child

    def is_none(self):
        '''
        Returns where there is a child here
        '''
        return self._child_node is None

    def is_kind(self, some_kind):
        '''
        Returns where there is a child here
        '''
        return self._allowed_type == some_kind

    def get(self):
        '''
        Returns the current child
        '''
        assert self._optional or self._child_node is not None
        return self._child_node

    def reset(self, child):
        '''
        Replaces existing child
        '''
        temp = self._child_node
        self._child_node = None
        self.set(child)
        return temp

    def clear(self):
        '''
        Replaces existing child
        '''
        temp = self._child_node
        self._child_node = None
        return temp

    def call(self, doer):
        '''
        Walks this child
        '''
        if self._child_node is not None:
            doer.do_child(self)


class ChildList(object):
    '''
    Intermediate instance to hold a child list

    '''

    def __init__(self, parent, allowed_type):
        '''
        Constructor
        '''
        super(ChildList, self).__init__()
        self._child_list = []
        self._parent = parent
        self._allowed_type = allowed_type

        parent.add_child(self)

    def __iter__(self):
        '''
        Easy iteration
        '''
        return self._child_list.__iter__()

    def _make(self, child):
        '''
        Helper method
        '''
        box = Child(self._parent, self._allowed_type, False, True)
        box.set(child)
        return box

    def get_size(self):
        '''
        Returns the child count
        '''
        return len(self._child_list)

    def add(self, child):
        '''
        Adds a child
        '''
        self._child_list.append(self._make(child))

    def add_all(self, childs):
        '''
        Adds all childs in iterable
        '''
        for each in childs:
            self.add(each)

    def at(self, index):
        '''
        Returns a child
        '''
        return self._child_list[index].get()

    def insert_at(self, index, child):
        '''
        Inserts a child
        '''
        self._child_list.insert(index, self._make(child))

    def remove_at(self, index):
        '''
        Removes a child
        '''
        return self._child_list.pop(index).get()

    def replace_at(self, index, child):
        '''
        Replaces a child
        '''
        assert isinstance(child, self._allowed_type)

        temp = self.remove_at(index)
        self.insert_at(index, child)
        return temp

    def split_at(self, index):
        '''
        Splits this list at index, all items from index on, are returned
        '''
        assert index <= len(self._child_list)
        assert index >= 0

        other = []
        for i in range(index, len(self._child_list)):
            other.append(self._child_list[i].get())
            self._child_list[i] = None

        self._child_list = self._child_list[0:index]
        return other

    def call(self, doer):
        '''
        Walks all childs
        '''
        for each in self._child_list:
            doer.do_child(each)


class Node(object):

    '''
    Base class for all tree nodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(Node, self).__init__()
        self._parent = None
        self._resolved = False
        self._scopes = {}
        self._childs = []

    def get_scope(self, kind):
        '''
        Walks the tree up, until an scope of requested kind if found
        '''
        if kind in self._scopes:
            return self._scopes[kind]
        else:
            return self.get_parent_scope(kind)

    def get_parent_scope(self, kind):
        '''
        Asks parent node for scope
        '''
        if self._parent is not None:
            return self._parent.get_scope(kind)
        else:
            return None

    def add_scope(self, kind, scope):
        '''
        Adds an scope to this node
        '''
        assert kind not in self._scopes
        self._scopes[kind] = scope

    def set_parent(self, parent):
        '''
        helper method for setting node parent
        '''
        self._parent = parent

    def get_parent(self):
        '''
        parent getter
        '''
        assert self._parent is not None
        return self._parent

    def add_child(self, child):
        '''
        Adds a child to this node
        '''
        self._childs.append(child)

    def for_each_child(self, doer):
        '''
        Walks all node childs
        '''
        for each in self._childs:
            each.call(doer)


class StatementNode(Node):

    '''
    Base class for all statements nodes
    '''

    def __init__(self):
        super(StatementNode, self).__init__()

    def is_closed_stmt(self):
        '''
        Returns true when this is a flow statement
        Next statement in statement list will not be executed
        '''
        # pylint: disable=no-self-use
        return False


class StmtListNode(StatementNode):

    '''
    Node class representing an statement list
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(StmtListNode, self).__init__()
        self.statements = ChildList(self, StatementNode)
        self.add_scope(StatementListScope, StatementListScope(self))

    def split_at(self, index, other):
        '''
        Splits this StmtListNode,
        all items with index equal or greater than are moved to the other
        '''
        assert isinstance(other, StmtListNode)
        o = self.statements.split_at(index)
        o.statements.add_all(o)

    def is_closed_stmt(self):
        '''
        Returns true when last statement is closed
        '''
        if self.statements.get_size() != 0:
            return self.statements.at(-1).is_closed_stmt()
        else:
            return False


class ExpressionNode(Node):

    '''
    Base class for all expressions nodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ExpressionNode, self).__init__()
        self._resolved_type = None
        self.bool_parenthesis = False

    def set_type(self, resolved_type):
        '''
        Type setter, this method can be called only once.
        So type can not change
        '''

        assert resolved_type
        assert not self._resolved_type

        self._resolved_type = resolved_type

    def get_type(self):
        '''
        Returns the type of this expression
        '''
        if self._resolved_type is None:
            print self.__name__
            assert False
        return self._resolved_type

    def get_static_value(self):
        # pylint: disable=no-self-use
        return None


class TypeNode(Node):

    '''
    Base class for types references
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(TypeNode, self).__init__()
        self.ref_type_declaration = None

    def get_type(self):
        '''
        Returns the resolved type
        '''
        assert self.ref_type_declaration
        return self.ref_type_declaration

    def set_type(self, type_ref):
        '''
        Sets the resolved type
        '''
        assert self.ref_type_declaration is None
        assert type_ref is not None

        self.ref_type_declaration = type_ref

    def add_qualifier(self, compiler, ctx, qualifier):
        '''
        Add qualifiers to this type.
        To be implemented by derived classes
        '''
        # pylint: disable=no-self-use
        compiler.report_error(ctx, "Unsupported qualifier '%s'" % qualifier)


class TypeDeclNode(Node):

    '''
    Base class for types declarations
    '''

    NO_MATCH = 0
    EXACT_MATCH = 1
    CAST_MATCH = 2

    def __init__(self, name):
        '''
        Constructor
        '''
        super(TypeDeclNode, self).__init__()
        self.txt_name = name
        self._resolved = False

    def resolve(self, compiler):
        '''
        Resolve
        '''
        assert not self._resolved
        self.get_scope(RootScope).add_type(compiler, self.txt_name, self)
        self._resolved = True

    def can_cast_to(self, target_type):
        '''
        Base method for type casting
        If self can be casted to target_type returns True
        Otherwise returns False
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        return False

    def insert_cast_to(self, compiler, target_type, expression):
        '''
        Inserts a cast to the target type
        Only implemented by types that return true to can_cast_to
        '''
        # pylint: disable=unused-argument
        print "Node: %s" % type(self).__name__
        assert False

    def can_cast_from(self, source_type):
        '''
        Base method for type casting
        If self can be constructed from source_type returns True
        Otherwise returns False
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        return False

    def insert_cast(self, compiler, source_type, expression):
        '''
        Inserts a cast from the source type
        Only implemented by types that return true to can_cast_from
        '''
        # pylint: disable=unused-argument
        print "Node: %s" % type(self).__name__
        assert False

    def to_string(self):
        return self.txt_name

    def lookup_member(self, name):
        '''
        Base method for type member look up
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        return None

    def lookup_operator(self, name):
        '''
        Base method for type operator look up
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        return None


def expression_type_match(compiler, lhs_type, parent, child_name):
    '''
    Helper function for expression type matching
    If no match possible just returns false
    If exact match returns true
    If can match but needs cast, inserts cast and returns true
    '''
    e = getattr(parent, child_name)
    expr_type = e.get_type()

    if expr_type == lhs_type:
        return True
    elif lhs_type.can_cast_from(expr_type):
        cast = lhs_type.insert_cast(compiler, expr_type, e)
        cast.set_parent(parent)
        setattr(parent, child_name, cast)
        return True
    else:
        return False


class DeclarationListNode(Node):

    '''
    Node class representing a list of declaration, used as container
    of built-ins and plug-ins data
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(DeclarationListNode, self).__init__()
        self.declarations = ChildList(self, Node)


class ArgumentListNode(Node):

    '''
    Node class used as container of arguments in function calls
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ArgumentListNode, self).__init__()
        self.arguments = ChildList(self, ExpressionNode)
