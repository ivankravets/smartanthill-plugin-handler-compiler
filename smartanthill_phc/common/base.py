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
from smartanthill_phc.common.child import Child, ChildList
from smartanthill_phc.common.lookup import RootScope, StatementListScope


class OnDemandResolution(object):

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
        super(OnDemandResolution, self).__init__()
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

    def for_each_child(self, functor):
        '''
        Walks all node childs
        '''
        for each in self._childs:
            each.call(functor)


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
        Returns true when there is a closed statement is this statement list
        '''
        for each in self.statements:
            if each.get().is_closed_stmt():
                return True
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


class ChildExpr(Child):
    '''
    Specialized Child used for expressions
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        super(ChildExpr, self).__init__(parent, ExpressionNode, False)


class ChildExprOpt(Child):
    '''
    Specialized Child used for expressions
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        super(ChildExprOpt, self).__init__(parent, ExpressionNode, True)


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

    def can_cast_from(self, source_type):
        '''
        Base method for type casting
        If self can be constructed from source_type returns True
        Otherwise returns False
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        return False

    def insert_cast_from(self, compiler, source_type, expression):
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
