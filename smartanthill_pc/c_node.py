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

from smartanthill_zc.node import ExpressionNode, resolve_expression_list,\
    Node, StmtListNode, DeclarationListNode


class DontCareExprNode(ExpressionNode):

    '''
    Node class representing a operator expression
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(DontCareExprNode, self).__init__()
        self.childs_expressions = []
        self.ref_decl = None

    def add_expression(self, child):
        '''
        expression adder
        '''
        assert child is not None
        assert isinstance(child, ExpressionNode)
        child.set_parent(self)
        self.childs_expressions.append(child)

    def resolve_expr(self, compiler):

        resolve_expression_list(compiler, self, self.childs_arguments)

#        self.set_type(self.ref_decl.get_type())

        return None


class PluginSourceNode(Node):

    '''
    Node class container of a source program
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PluginSourceNode, self).__init__()
        self.child_declaration_list = None

    def set_declaration_list(self, child):
        '''
        statement list setter
        '''
        assert isinstance(child, DeclarationListNode)
        child.set_parent(self)
        self.child_declaration_list = child

    def resolve(self, compiler):
        compiler.resolve_node(self.child_declaration_list)


class FunctionDeclNode(Node):

    '''
    Node class representing a function declaration
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(FunctionDeclNode, self).__init__()
        self.child_statement_list = None

    def set_statement_list(self, child):
        '''
        statement list setter
        '''
        assert isinstance(child, StmtListNode)
        child.set_parent(self)
        self.child_statement_list = child

    def resolve(self, compiler):
        compiler.resolve_node(self.child_statement_list)
