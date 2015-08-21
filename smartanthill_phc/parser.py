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


from smartanthill_phc import c_node
from smartanthill_phc.antlr_parser import CVisitor, CParser
from smartanthill_phc.c_node import DontCareExprNode, FunctionDeclNode,\
    TypeCastExprNode
from smartanthill_phc.common import expression
from smartanthill_phc.common import node
from smartanthill_phc.common import statement
from smartanthill_phc.common.antlr_helper import get_token_text
from smartanthill_phc.root import PluginSourceNode


def c_parse_tree_to_syntax_tree(compiler, tree):
    '''
    Translates a parse tree as returned by antlr4 into a
    syntax tree as used by the compiler, this tree transformation
    replaces syntax directed translation written directly into the grammar
    as used by yacc-lex.
    The antlr parser creates a parse tree from the grammar without actions,
    and at this point the parse tree is transformed into the syntax tree
    needed by the application.
    '''

    assert isinstance(tree, CParser.CParser.CompilationUnitContext)

    source = compiler.init_node(PluginSourceNode(), tree)
    ls = compiler.init_node(node.DeclarationListNode(), tree)
    source.set_declaration_list(ls)
    v = _CParseTreeVisitor(compiler, source)
    v.visit(tree)

    compiler.check_stage('syntax')

    return source


def _is_blocking_api_function(name):
    '''
    Returns true if this name is in blocking api functions list
    '''
    return name == 'zepto_wait_for_pin'


def _get_direct_declarator_name(ctx):

    assert isinstance(ctx, CParser.CParser.DirectDeclaratorContext)
    if ctx.Identifier() is not None:
        return ctx.Identifier()
    elif ctx.declarator() is not None:
        return get_declarator_name(ctx.declarator())
    else:
        assert ctx.directDeclarator() is not None
        return _get_direct_declarator_name(ctx.directDeclarator())


def get_declarator_name(ctx):
    '''
    Returns the Identifier token from a nested declarator
    '''
    assert isinstance(ctx, CParser.CParser.DeclaratorContext)
    return _get_direct_declarator_name(ctx.directDeclarator())


# Generated from java-escape by ANTLR 4.5
# This class defines a complete generic visitor for a parse tree produced
# by CParser.


class _CParseTreeVisitor(CVisitor.CVisitor):

    '''
    The template for the visitor is copy&paste from super class interface
    ECMAScriptVisitor.ECMAScriptVisitor
    '''

    def __init__(self, compiler, source):
        '''
        Constructor
        '''
        self._c = compiler
        self._s = source

    def visitChildren(self, current):
        '''
        Overrides antlr4.ParseTreeVisitor method
        Changes default action, from walking down the tree to
        fail with assert, this will expose any parsed node that does not have
        a valid interpretation rule here
        '''
        self._c.report_error(current, "Unsupported syntax!")
        self._c.raise_error()

    # Visit a parse tree produced by CParser#FunctionExpression.
    def visitFunctionExpression(self, ctx):

        expr = self._c.init_node(expression.FunctionCallExprNode(), ctx)
        expr.txt_name = get_token_text(self._c, ctx.Identifier())
        args = self.visit(ctx.argumentExpressionList())
        expr.set_argument_list(args)

        return expr

    # Visit a parse tree produced by CParser#DotExpression.
    def visitDotExpression(self, ctx):

        expr = self._c.init_node(DontCareExprNode(), ctx)
        expr.add_expression(self.visit(ctx.unaryExpression()))

        tk = ctx.Identifier()
        member = self._c.init_node(expression.VariableExprNode(), tk)
        member.txt_name = get_token_text(self._c, tk)

        expr.add_expression(member)

        return expr

    # Visit a parse tree produced by CParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx):

        return self.visit(ctx.expression())

    # Visit a parse tree produced by CParser#LiteralExpression.
    def visitLiteralExpression(self, ctx):
        return self._c.init_node(DontCareExprNode(), ctx)

    # Visit a parse tree produced by CParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx):
        expr = self._c.init_node(DontCareExprNode(), ctx)
        expr.add_expression(self.visit(ctx.unaryExpression()))

        return expr

    # Visit a parse tree produced by CParser#ArrowExpression.
    def visitArrowExpression(self, ctx):
        expr = self._c.init_node(DontCareExprNode(), ctx)
        expr.add_expression(self.visit(ctx.unaryExpression()))

        tk = ctx.Identifier()
        member = self._c.init_node(expression.VariableExprNode(), tk)
        member.txt_name = get_token_text(self._c, tk)

        expr.add_expression(member)

        return expr

    # Visit a parse tree produced by CParser#IndexExpression.
    def visitIndexExpression(self, ctx):
        expr = self._c.init_node(DontCareExprNode(), ctx)
        expr.add_expression(self.visit(ctx.unaryExpression()))
        expr.add_expression(self.visit(ctx.expression()))

        return expr

    # Visit a parse tree produced by CParser#SizeOfTypeExpression.
    def visitSizeOfTypeExpression(self, ctx):
        return self._c.init_node(DontCareExprNode(), ctx)

    # Visit a parse tree produced by CParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx):

        tk = ctx.Identifier()
        expr = self._c.init_node(expression.VariableExprNode(), tk)
        expr.txt_name = get_token_text(self._c, tk)

        return expr

    # Visit a parse tree produced by CParser#UnaryOperatorExpression.
    def visitUnaryOperatorExpression(self, ctx):
        expr = self._c.init_node(DontCareExprNode(), ctx)
        expr.add_expression(self.visit(ctx.castExpression()))

        return expr

    # Visit a parse tree produced by CParser#AlignOfTypeExpression.
    def visitAlignOfTypeExpression(self, ctx):
        return self._c.init_node(DontCareExprNode(), ctx)

    # Visit a parse tree produced by CParser#SizeOfExpression.
    def visitSizeOfExpression(self, ctx):
        expr = self._c.init_node(DontCareExprNode(), ctx)
        expr.add_expression(self.visit(ctx.unaryExpression()))

        return expr

    # Visit a parse tree produced by CParser#StringLiteralExpression.
    def visitStringLiteralExpression(self, ctx):
        return self._c.init_node(DontCareExprNode(), ctx)

    # Visit a parse tree produced by CParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx):
        expr = self._c.init_node(DontCareExprNode(), ctx)
        expr.add_expression(self.visit(ctx.unaryExpression()))

        return expr

    # Visit a parse tree produced by CParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx):
        args = self._c.init_node(node.ArgumentListNode(), ctx)

        for e in ctx.assignmentExpression():
            expr = self.visit(e)
            args.add_argument(expr)

        return args

    # Visit a parse tree produced by CParser#castExpression.
    def visitCastExpression(self, ctx):
        if ctx.unaryExpression() is not None:
            return self.visit(ctx.unaryExpression())
        else:
            expr = self._c.init_node(TypeCastExprNode(), ctx)
            expr.set_expression(self.visit(ctx.castExpression()))

            return expr

    # Visit a parse tree produced by CParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx):

        if ctx.castExpression() is not None:
            return self.visit(ctx.castExpression())
        else:
            expr = self._c.init_node(DontCareExprNode(), ctx)
            expr.add_expression(self.visit(ctx.logicalOrExpression(1)))
            expr.add_expression(self.visit(ctx.logicalOrExpression(2)))

            return expr

    # Visit a parse tree produced by CParser#conditionalExpression.
    def visitConditionalExpression(self, ctx):
        if ctx.expression() is None:
            assert ctx.conditionalExpression() is None

            return self.visit(ctx.logicalOrExpression())
        else:
            expr = self._c.init_node(DontCareExprNode(), ctx)
            expr.add_expression(self.visit(ctx.logicalOrExpression()))
            expr.add_expression(self.visit(ctx.expression()))
            expr.add_expression(self.visit(ctx.conditionalExpression()))

            return expr

    # Visit a parse tree produced by CParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx):
        if ctx.conditionalExpression() is not None:
            return self.visit(ctx.conditionalExpression())
        else:
            expr = self._c.init_node(DontCareExprNode(), ctx)
            expr.add_expression(self.visit(ctx.unaryExpression()))
            expr.add_expression(self.visit(ctx.assignmentExpression()))

            return expr

    # Visit a parse tree produced by CParser#expression.
    def visitExpression(self, ctx):
        if len(ctx.assignmentExpression()) == 1:
            return self.visit(ctx.assignmentExpression(0))
        else:
            expr = self._c.init_node(DontCareExprNode(), ctx)
            for each in ctx.assignmentExpression():
                expr.add_expression(self.visit(each))

            return expr

    # Visit a parse tree produced by CParser#constantExpression.
    def visitConstantExpression(self, ctx):
        return self.visit(ctx.conditionalExpression())

    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx):

        if ctx.initDeclaratorList() is None:
            # TODO this is a type declaration
            # self._c.report_error(ctx, "Incomplete declaration not supported")
            return []

        if len(ctx.initDeclaratorList().initDeclarator()) != 1:
            self._c.report_error(ctx, "Combined declaration not supported")
            return []

        decl = self._c.init_node(statement.VariableDeclarationStmtNode(), ctx)
        decl_ctx = ctx.initDeclaratorList().initDeclarator(0).declarator()
        tk = get_declarator_name(decl_ctx)
        decl.txt_name = get_token_text(self._c, tk)

        init_ctx = ctx.initDeclaratorList().initDeclarator(0).initializer()
        if init_ctx is not None:
            init = self.visit(init_ctx)
            decl.set_initializer(init)

        return [decl]

    # Visit a parse tree produced by CParser#declarationSpecifier.
    def visitDeclarationSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#initDeclaratorList.
    def visitInitDeclaratorList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#initDeclarator.
    def visitInitDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#storageClassSpecifier.
    def visitStorageClassSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#structOrUnionSpecifier.
    def visitStructOrUnionSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#structOrUnion.
    def visitStructOrUnion(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#structDeclaration.
    def visitStructDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#specifierQualifierList.
    def visitSpecifierQualifierList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#structDeclaratorList.
    def visitStructDeclaratorList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#structDeclarator.
    def visitStructDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#enumSpecifier.
    def visitEnumSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#enumeratorList.
    def visitEnumeratorList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#enumerator.
    def visitEnumerator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#atomicTypeSpecifier.
    def visitAtomicTypeSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#typeQualifier.
    def visitTypeQualifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#functionSpecifier.
    def visitFunctionSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#alignmentSpecifier.
    def visitAlignmentSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#declarator.
    def visitDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#directDeclarator.
    def visitDirectDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#gccDeclaratorExtension.
    def visitGccDeclaratorExtension(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#gccAttributeSpecifier.
    def visitGccAttributeSpecifier(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#gccAttributeList.
    def visitGccAttributeList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#gccAttribute.
    def visitGccAttribute(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#nestedParenthesesBlock.
    def visitNestedParenthesesBlock(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#pointer.
    def visitPointer(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#parameterTypeList.
    def visitParameterTypeList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#identifierList.
    def visitIdentifierList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#typeName.
    def visitTypeName(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#abstractDeclarator.
    def visitAbstractDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#directAbstractDeclarator.
    def visitDirectAbstractDeclarator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#typedefName.
    def visitTypedefName(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#initializer.
    def visitInitializer(self, ctx):

        if ctx.assignmentExpression() is not None:
            return self.visit(ctx.assignmentExpression())
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#initializerList.
    def visitInitializerList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#designation.
    def visitDesignation(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#designatorList.
    def visitDesignatorList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#designator.
    def visitDesignator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#staticAssertDeclaration.
    def visitStaticAssertDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#statement.
    def visitStatement(self, ctx):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by CParser#labeledStatement.
    def visitLabeledStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#compoundStatement.
    def visitCompoundStatement(self, ctx):

        sl = self._c.init_node(node.StmtListNode(), ctx)
        for each in ctx.blockItem():
            stmt = self.visit(each)
            if isinstance(stmt, node.StatementNode):
                sl.add_statement(stmt)
            else:
                for each in stmt:
                    sl.add_statement(each)

        return sl

    # Visit a parse tree produced by CParser#blockItem.
    def visitBlockItem(self, ctx):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by CParser#expressionStatement.
    def visitExpressionStatement(self, ctx):

        if ctx.expression():
            expr = self.visit(ctx.expression())
            if _is_blocking_api_function(expr.txt_name):
                stmt = self._c.init_node(c_node.BlockingCallStmtNode(), ctx)
                stmt.set_expression(expr)
                return stmt
            else:
                stmt = self._c.init_node(statement.ExpressionStmtNode(), ctx)
                stmt.set_expression(expr)
                return stmt
        else:
            return self._c.init_node(statement.NopStmtNode(), ctx)

    # Visit a parse tree produced by CParser#selectionStatement.
    def visitSelectionStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#iterationStatement.
    def visitIterationStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#ReturnStatement.
    def visitReturnStatement(self, ctx):

        stmt = self._c.init_node(statement.ReturnStmtNode(), ctx)
        if ctx.expression() is not None:
            expr = self.visit(ctx.expression())
            stmt.set_expression(expr)

        return stmt

    # Visit a parse tree produced by CParser#compilationUnit.
    def visitCompilationUnit(self, ctx):

        for d in ctx.externalDeclaration():
            self.visit(d)

        return None

    # Visit a parse tree produced by CParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx):

        if ctx.functionDefinition() is not None:
            self.visit(ctx.functionDefinition())
        elif ctx.declaration() is not None:
            decls = self.visit(ctx.declaration())
            for each in decls:
                self._s.child_declaration_list.add_declaration(each)

        return None

    # Visit a parse tree produced by CParser#functionDefinition.
    def visitFunctionDefinition(self, ctx):

        decl = self._c.init_node(FunctionDeclNode(), ctx)

        dd = ctx.declarator().directDeclarator()
        if dd.directDeclarator() and dd.directDeclarator().Identifier():
            decl.txt_name = get_token_text(
                self._c, dd.directDeclarator().Identifier())
        else:
            self._c.report_error(ctx, "Unsupported function declaration")

        sl = self.visit(ctx.compoundStatement())
        decl.set_statement_list(sl)

        self._s.child_declaration_list.add_declaration(decl)

        return None

    # Visit a parse tree produced by CParser#declarationList.
    def visitDeclarationList(self, ctx):
        return self.visitChildren(ctx)
