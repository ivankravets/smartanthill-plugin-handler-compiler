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
        assert self._parent
        return self._parent


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
        self.childs_statements = []
        self.add_scope(StatementListScope, StatementListScope(self))

    def add_statement(self, child):
        '''
        statement adder
        '''
        if not child:
            assert False
        assert isinstance(child, StatementNode)
        child.set_parent(self)
        self.childs_statements.append(child)

    def insert_statement_at(self, index, child):
        '''
        statement adder
        '''
        assert child is not None
        assert isinstance(child, StatementNode)
        assert index >= 0
        assert index <= len(self.childs_statements)

        child.set_parent(self)
        self.childs_statements.insert(index, child)

    def remove_statement_at(self, index):
        '''
        statement adder
        '''
        assert index >= 0
        assert index <= len(self.childs_statements)

        return self.childs_statements.pop(index)

    def split_at(self, index, other):
        '''
        Splits this StmtListNode,
        all items with index equal or greater than are moved to the other
        '''
        assert isinstance(other, StmtListNode)
        assert index <= len(self.childs_statements)
        assert index >= 0

        for i in range(index, len(self.childs_statements)):
            other.add_statement(self.childs_statements[i])
            self.childs_statements[i] = None

        self.childs_statements = self.childs_statements[0:index]

    def is_closed_stmt(self):
        '''
        Returns true when last statement is closed
        '''
        if len(self.childs_statements) != 0:
            return self.childs_statements[-1].is_closed_stmt()
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
        self.has_parenthesis = False

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
        assert self._resolved_type
        return self._resolved_type

    def assert_resolved(self):
        '''
        Asserts this instance has a resolved type
        '''
        assert self._resolved_type

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

    def add_qualifiers(self, compiler, qualifiers):
        '''
        Add qualifiers to this type.
        To be implemented by derived classes
        '''
        # pylint: disable=no-self-use
        # pylint: disable=unused-argument
        pass


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
    elif expr_type.can_cast_to(lhs_type):
        cast = expr_type.insert_cast_to(compiler, lhs_type, e)
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
        self.childs_declarations = []

    def add_declaration(self, child):
        '''
        statement adder
        '''
        assert child
        assert isinstance(child, Node)
        child.set_parent(self)
        self.childs_declarations.append(child)

    def insert_declaration_at(self, index, child):
        '''
        statement adder
        '''
        assert child is not None
        assert isinstance(child, Node)
        assert index >= 0
        assert index <= len(self.childs_declarations)

        child.set_parent(self)
        self.childs_declarations.insert(index, child)


class ArgumentListNode(Node):

    '''
    Node class used as container of arguments in function calls
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(ArgumentListNode, self).__init__()
        self.childs_arguments = []

    def add_argument(self, child):
        '''
        argument adder
        '''
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.childs_arguments.append(child)

    def insert_argument_at(self, index, child):
        '''
        statement adder
        '''
        assert child is not None
        assert isinstance(child, ExpressionNode)
        assert index >= 0
        assert index <= len(self.childs_arguments)

        child.set_parent(self)
        self.childs_arguments.insert(index, child)

    def overload_filter(self, compiler, decl_list):
        '''
        From a list declarations, returns one that can match the arguments,
        if no candidate is found, reports error an raises
        '''
        exact_match = []
        cast_match = []
        for current in decl_list:
            r = self.can_match(current.child_parameter_list)

            if r == TypeDeclNode.NO_MATCH:
                pass
            elif r == TypeDeclNode.EXACT_MATCH:
                exact_match.append(current)
            elif r == TypeDeclNode.CAST_MATCH:
                cast_match.append(current)
            else:
                assert False

        if len(exact_match) == 1:
            return exact_match[0]
        elif len(exact_match) == 0:
            if len(cast_match) == 1:
                return cast_match[0]
            elif len(cast_match) == 0:
                compiler.report_error(
                    self.ctx, "None of candidates can match the arguments")
                compiler.raise_error()
            elif len(cast_match) > 1:
                compiler.report_error(
                    self.ctx, "More than a candidate can match the arguments")
                compiler.raise_error()
            else:
                assert False
        else:
            assert False

    def can_match(self, params):
        '''
        If this argument list can not used to initialize given argument list
        Returns TypeDeclNode.NO_MATCH when there is no chance to make it match
        TypeDeclNode.EXACT_MATCH when match does not need any cast
        and TypeDeclNode.CAST_MATCH when it can match but casting needed
        '''
        if len(self.childs_arguments) != params.get_size():
            return TypeDeclNode.NO_MATCH

        result = TypeDeclNode.EXACT_MATCH
        for i in range(len(self.childs_arguments)):

            source = self.childs_arguments[i].get_type()
            target = params.get_type_at(i)

            if source == target:
                pass
            elif source.can_cast_to(target):
                result = TypeDeclNode.CAST_MATCH
            elif target.can_cast_from(source):
                result = TypeDeclNode.CAST_MATCH
            else:
                return TypeDeclNode.NO_MATCH

        return result

    def make_match(self, compiler, params):
        '''
        Makes this argument list to initialize given declaration,
        inserting casts if required.
        '''

        if len(self.childs_arguments) != params.get_size():
            compiler.report_error(
                self.ctx, "Wrong number of arguments, need %s but given %s" % (
                    str(params.get_size()), str(len(self.childs_arguments))))
            compiler.raise_error()

        for i in range(len(self.childs_arguments)):
            target = params.get_type_at(i)
            source = self.childs_arguments[i].get_type()

            if source == target:
                pass
            elif source.can_cast_to(target):
                e = source.insert_cast_to(
                    compiler, target, self.childs_arguments[i])
                e.set_parent(self)
                self.childs_arguments[i] = e
            elif target.can_cast_from(source):
                e = target.insert_cast_from(
                    compiler, source, self.childs_arguments[i])
                e.set_parent(self)
                self.childs_arguments[i] = e
            else:
                compiler.report_error(
                    self.ctx, "Invalid argument type at %s" % i)
                compiler.raise_error()
