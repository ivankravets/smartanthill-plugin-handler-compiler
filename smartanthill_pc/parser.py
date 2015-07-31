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

from smartanthill_pc.antlr_parser import CVisitor


def c_parse_tree_to_syntax_tree(compiler, js_tree):
    '''
    Translates a parse tree as returned by antlr4 into a
    syntax tree as used by the compiler, this tree transformation
    replaces syntax directed translation written directly into the grammar
    as used by yacc-lex.
    The antlr parser creates a parse tree from the grammar without actions,
    and at this point the parse tree is transformed into the syntax tree
    needed by the application.
    '''

    visitor = _CParseTreeVisitor()
    source = visitor.visit(js_tree)

    compiler.check_stage('syntax')

    return source

# Generated from java-escape by ANTLR 4.5
# This class defines a complete generic visitor for a parse tree produced
# by CParser.


class _CParseTreeVisitor(CVisitor):

    '''
    The template for the visitor is copy&paste from super class interface
    ECMAScriptVisitor.ECMAScriptVisitor
    '''

    def __init__(self, compiler):
        '''
        Constructor
        '''
        self._c = compiler

    def visitChildren(self, current):
        '''
        Overrides antlr4.ParseTreeVisitor method
        Changes default action, from walking down the tree to
        fail with assert, this will expose any parsed node that does not have
        a valid interpretation rule here
        '''
        self._c.report_error(current, "Unsupported syntax!")
        self._c.report_error(current, "Unmatched parser token")
        assert False

    # Visit a parse tree produced by CParser#primaryExpression.
    def visitPrimaryExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#genericAssociation.
    def visitGenericAssociation(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#postfixExpression.
    def visitPostfixExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#unaryExpression.
    def visitUnaryExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#unaryOperator.
    def visitUnaryOperator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#castExpression.
    def visitCastExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#additiveExpression.
    def visitAdditiveExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#shiftExpression.
    def visitShiftExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#relationalExpression.
    def visitRelationalExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#equalityExpression.
    def visitEqualityExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#andExpression.
    def visitAndExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#exclusiveOrExpression.
    def visitExclusiveOrExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#inclusiveOrExpression.
    def visitInclusiveOrExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#conditionalExpression.
    def visitConditionalExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#constantExpression.
    def visitConstantExpression(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#declaration.
    def visitDeclaration(self, ctx):
        return self.visitChildren(ctx)

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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#labeledStatement.
    def visitLabeledStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#compoundStatement.
    def visitCompoundStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#blockItemList.
    def visitBlockItemList(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#blockItem.
    def visitBlockItem(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#expressionStatement.
    def visitExpressionStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#selectionStatement.
    def visitSelectionStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#iterationStatement.
    def visitIterationStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#jumpStatement.
    def visitJumpStatement(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#compilationUnit.
    def visitCompilationUnit(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#translationUnit.
    def visitTranslationUnit(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#externalDeclaration.
    def visitExternalDeclaration(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#functionDefinition.
    def visitFunctionDefinition(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CParser#declarationList.
    def visitDeclarationList(self, ctx):
        return self.visitChildren(ctx)
