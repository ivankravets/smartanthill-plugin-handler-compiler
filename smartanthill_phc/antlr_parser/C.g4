/*
 [The "BSD licence"]
 Copyright (c) 2013 Sam Harwell
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/** C 2011 grammar built from the C11 Spec */
grammar C;


unaryExpression
    :   Identifier # IdentifierExpression
    |   Constant   # LiteralExpression
    |   StringLiteral+ # StringLiteralExpression
    |   '(' expression ')' # ParenthesizedExpression
//    |   '_Generic' '(' assignmentExpression ',' genericAssociation ( ',' genericAssociation )* ')'
//    |   '__extension__'? '(' compoundStatement ')' // Blocks (GCC extension)
//    |   '__builtin_va_arg' '(' unaryExpression ',' typeName ')'
//    |   '__builtin_offsetof' '(' typeName ',' unaryExpression ')'
    |   unaryExpression '[' expression ']' # IndexExpression
//    |   unaryExpression '(' argumentExpressionList? ')' # FunctionExpression
    |   Identifier '(' argumentExpressionList? ')' # FunctionExpression
    |   unaryExpression '.' Identifier # DotExpression
    |   unaryExpression '->' Identifier # ArrowExpression
    |   unaryExpression ('++'|'--') # PostIncrementExpression
//    |   '__extension__'? '(' typeName ')' '{' initializerList ','? '}'
    |   ('++'|'--') unaryExpression # PreIncrementExpression
    |   ('&' | '*' | '+' | '-' | '~' | '!') castExpression # UnaryOperatorExpression
    |   'sizeof' unaryExpression # SizeOfExpression
    |   'sizeof' '(' typeName ')' # SizeOfTypeExpression
    |   '_Alignof' '(' typeName ')' # AlignOfTypeExpression
//    |   '&&' Identifier // GCC extension address of label
    ;

//genericAssociation
//    :   typeName ':' assignmentExpression
//    |   'default' ':' assignmentExpression
//    ;

argumentExpressionList
    :   assignmentExpression (',' assignmentExpression)*
    ;

castExpression
    :   unaryExpression
//    |   '__extension__'? '(' typeName ')' castExpression
    |   '(' typeName ')' castExpression
    ;

logicalOrExpression
    :   castExpression
    |   logicalOrExpression ('*'|'/'|'%') logicalOrExpression
    |   logicalOrExpression ('+'|'-') logicalOrExpression
    |   logicalOrExpression ('<<'|'>>') logicalOrExpression
    |   logicalOrExpression ('<'|'>'|'<='|'>=') logicalOrExpression
    |   logicalOrExpression ('=='|'!=') logicalOrExpression
    |   logicalOrExpression '&' logicalOrExpression
    |   logicalOrExpression '^' logicalOrExpression
    |   logicalOrExpression '|' logicalOrExpression
    |   logicalOrExpression '&&' logicalOrExpression
    |   logicalOrExpression '||' logicalOrExpression
    ;

conditionalExpression
    :   logicalOrExpression
    |   logicalOrExpression '?' expression ':' conditionalExpression
    ;

assignmentExpression
    :   conditionalExpression
    |   unaryExpression ('='|'*='|'/='|'%='|'+='|'-='|'<<='|'>>='|'&='|'^='|'|=') assignmentExpression
    ;

expression
    :   assignmentExpression (',' assignmentExpression)*
    ;

constantExpression
    :   conditionalExpression
    ;

declaration
    :   declarationSpecifier+ initDeclaratorList? ';'
    |   staticAssertDeclaration
    ;

declarationSpecifier
    :   storageClassSpecifier
    |   typeSpecifier
    |   typeQualifier
    |   functionSpecifier
    |   alignmentSpecifier
    ;

initDeclaratorList
    :   initDeclarator ( ',' initDeclarator )*
    ;

initDeclarator
    :   declarator
    |   declarator '=' initializer
    ;

storageClassSpecifier
    :   'typedef'
    |   'extern'
    |   'static'
    |   '_Thread_local'
    |   'auto'
    |   'register'
    ;

typeSpecifier
    :   ('void'
    |   'char'
    |   'short'
    |   'int'
    |   'long'
    |   'float'
    |   'double'
    |   'signed'
    |   'unsigned'
    |   '_Bool'
    |   '_Complex'
    |   '__m128'
    |   '__m128d'
    |   '__m128i')
    |   '__extension__' '(' ('__m128' | '__m128d' | '__m128i') ')'
    |   atomicTypeSpecifier
    |   structOrUnionSpecifier
    |   enumSpecifier
    |   typedefName
//    |   '__typeof__' '(' constantExpression ')' // GCC extension
    ;

structOrUnionSpecifier
    :   structOrUnion Identifier? '{' structDeclaration+ '}'
    |   structOrUnion Identifier
    ;

structOrUnion
    :   'struct'
    |   'union'
    ;

structDeclaration
    :   specifierQualifierList structDeclaratorList? ';'
    |   staticAssertDeclaration
    ;

specifierQualifierList
    :   typeSpecifier specifierQualifierList?
    |   typeQualifier specifierQualifierList?
    ;

structDeclaratorList
    :   structDeclarator ( ',' structDeclarator )*
    ;

structDeclarator
    :   declarator
    |   declarator? ':' constantExpression
    ;

enumSpecifier
    :   'enum' Identifier? '{' enumeratorList '}'
    |   'enum' Identifier? '{' enumeratorList ',' '}'
    |   'enum' Identifier
    ;

enumeratorList
    :   enumerator ( ',' enumerator )*
    ;

enumerator
    :   Identifier ('=' constantExpression)?
    ;

atomicTypeSpecifier
    :   '_Atomic' '(' typeName ')'
    ;

typeQualifier
    :   'const'
    |   'restrict'
    |   'volatile'
    |   '_Atomic'
    ;

functionSpecifier
    :   ('inline'
    |   '_Noreturn'
//    |   '__inline__' // GCC extension
    |   '__stdcall')
//    |   gccAttributeSpecifier
    |   '__declspec' '(' Identifier ')'
    ;

alignmentSpecifier
    :   '_Alignas' '(' typeName ')'
    |   '_Alignas' '(' constantExpression ')'
    ;

declarator
    :   pointer? directDeclarator
    ;

directDeclarator
    :   Identifier
    |   '(' declarator ')'
    |   directDeclarator '[' typeQualifier* assignmentExpression? ']'
    |   directDeclarator '[' 'static' typeQualifier* assignmentExpression ']'
    |   directDeclarator '[' typeQualifier+ 'static' assignmentExpression ']'
    |   directDeclarator '[' typeQualifier* '*' ']'
    |   directDeclarator '(' parameterTypeList ')'
    |   directDeclarator '(' identifierList? ')'
    ;

//gccAttributeSpecifier
//    :   '__attribute__' '(' '(' gccAttributeList ')' ')'
//    ;

//gccAttributeList
//    :   gccAttribute (',' gccAttribute)*
//    ;

//gccAttribute
//    :   ~(',' | '(' | ')') // relaxed def for "identifier or reserved word"
//        ('(' argumentExpressionList? ')')?
//    |   // empty
//    ;

pointer
    :   '*' typeQualifier* pointer?
    ;

parameterTypeList
    :   parameterDeclaration ( ',' parameterDeclaration )* (',' '...')?
    ;

parameterDeclaration
    :   declarationSpecifier+ declarator
    |   declarationSpecifier+ abstractDeclarator?
    ;

identifierList
    :   Identifier ( ',' Identifier )*
    ;

typeName
    :   specifierQualifierList abstractDeclarator?
    ;

abstractDeclarator
    :   pointer
    |   pointer? directAbstractDeclarator
    ;

directAbstractDeclarator
    :   '(' abstractDeclarator ')'
    |   '[' typeQualifier* assignmentExpression? ']'
    |   '[' 'static' typeQualifier* assignmentExpression ']'
    |   '[' typeQualifier* 'static' assignmentExpression ']'
    |   '[' '*' ']'
    |   '(' parameterTypeList? ')'
    |   directAbstractDeclarator '[' typeQualifier* assignmentExpression? ']'
    |   directAbstractDeclarator '[' 'static' typeQualifier* assignmentExpression ']'
    |   directAbstractDeclarator '[' typeQualifier+ 'static' assignmentExpression ']'
    |   directAbstractDeclarator '[' '*' ']'
    |   directAbstractDeclarator '(' parameterTypeList? ')'
    ;

typedefName
    :   Identifier
    ;

initializer
    :   assignmentExpression
    |   '{' initializerList ','? '}'
    ;

initializerList
    :   designation? initializer
    |   initializerList ',' designation? initializer
    ;

designation
    :   designator+ '='
    ;

designator
    :   '[' constantExpression ']'
    |   '.' Identifier
    ;

staticAssertDeclaration
    :   '_Static_assert' '(' constantExpression ',' StringLiteral+ ')' ';'
    ;

statement
    :   labeledStatement
    |   compoundStatement
    |   expressionStatement
    |   selectionStatement
    |   iterationStatement
    |   jumpStatement
//    |   ('__asm' | '__asm__') ('volatile' | '__volatile__') '(' (logicalOrExpression (',' logicalOrExpression)*)? (':' (logicalOrExpression (',' logicalOrExpression)*)?)* ')' ';'
    ;

labeledStatement
    :   Identifier ':' statement
    |   'case' constantExpression ':' statement
    |   'default' ':' statement
    ;

compoundStatement
    :   '{' blockItem* '}'
    ;

blockItem
    :   declaration
    |   statement
    ;

expressionStatement
    :   expression? ';'
    ;

selectionStatement
    :   'if' '(' expression ')' statement ('else' statement)? # IfStatement
    |   'switch' '(' expression ')' statement # SwitchStatement
    ;

iterationStatement
    :   'while' '(' expression ')' statement
    |   'do' statement 'while' '(' expression ')' ';'
    |   'for' '(' expression? ';' expression? ';' expression? ')' statement
    |   'for' '(' declaration expression? ';' expression? ')' statement
    ;

jumpStatement
    :   'goto' Identifier ';' # GotoStatement
    |   'continue' ';' # ContinueStatement
    |   'break' ';' # BreakStatement
    |   'return' expression? ';'  # ReturnStatement
//    |   'goto' unaryExpression ';' // GCC extension
    ;

compilationUnit
    :   externalDeclaration* EOF
    ;

externalDeclaration
    :   functionDefinition
    |   declaration
    |   ';' // stray ;
    ;

functionDefinition
    :   declarationSpecifier* declarator declaration* compoundStatement
    ;

Auto : 'auto';
Break : 'break';
Case : 'case';
Char : 'char';
Const : 'const';
Continue : 'continue';
Default : 'default';
Do : 'do';
Double : 'double';
Else : 'else';
Enum : 'enum';
Extern : 'extern';
Float : 'float';
For : 'for';
Goto : 'goto';
If : 'if';
Inline : 'inline';
Int : 'int';
Long : 'long';
Register : 'register';
Restrict : 'restrict';
Return : 'return';
Short : 'short';
Signed : 'signed';
Sizeof : 'sizeof';
Static : 'static';
Struct : 'struct';
Switch : 'switch';
Typedef : 'typedef';
Union : 'union';
Unsigned : 'unsigned';
Void : 'void';
Volatile : 'volatile';
While : 'while';

Alignas : '_Alignas';
Alignof : '_Alignof';
Atomic : '_Atomic';
Bool : '_Bool';
Complex : '_Complex';
Generic : '_Generic';
Imaginary : '_Imaginary';
Noreturn : '_Noreturn';
StaticAssert : '_Static_assert';
ThreadLocal : '_Thread_local';

LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
LeftBrace : '{';
RightBrace : '}';

Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';
LeftShift : '<<';
RightShift : '>>';

Plus : '+';
PlusPlus : '++';
Minus : '-';
MinusMinus : '--';
Star : '*';
Div : '/';
Mod : '%';

And : '&';
Or : '|';
AndAnd : '&&';
OrOr : '||';
Caret : '^';
Not : '!';
Tilde : '~';

Question : '?';
Colon : ':';
Semi : ';';
Comma : ',';

Assign : '=';
// '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
StarAssign : '*=';
DivAssign : '/=';
ModAssign : '%=';
PlusAssign : '+=';
MinusAssign : '-=';
LeftShiftAssign : '<<=';
RightShiftAssign : '>>=';
AndAssign : '&=';
XorAssign : '^=';
OrAssign : '|=';

Equal : '==';
NotEqual : '!=';

Arrow : '->';
Dot : '.';
Ellipsis : '...';

Identifier
    :   IdentifierNondigit
        (   IdentifierNondigit
        |   Digit
        )*
    ;

fragment
IdentifierNondigit
    :   Nondigit
    |   UniversalCharacterName
    //|   // other implementation-defined characters...
    ;

fragment
Nondigit
    :   [a-zA-Z_]
    ;

fragment
Digit
    :   [0-9]
    ;

fragment
UniversalCharacterName
    :   '\\u' HexQuad
    |   '\\U' HexQuad HexQuad
    ;

fragment
HexQuad
    :   HexadecimalDigit HexadecimalDigit HexadecimalDigit HexadecimalDigit
    ;

Constant
    :   IntegerConstant
    |   FloatingConstant
    //|   EnumerationConstant
    |   CharacterConstant
    ;

fragment
IntegerConstant
    :   DecimalConstant IntegerSuffix?
    |   OctalConstant IntegerSuffix?
    |   HexadecimalConstant IntegerSuffix?
    ;

fragment
DecimalConstant
    :   NonzeroDigit Digit*
    ;

fragment
OctalConstant
    :   '0' OctalDigit*
    ;

fragment
HexadecimalConstant
    :   HexadecimalPrefix HexadecimalDigit+
    ;

fragment
HexadecimalPrefix
    :   '0' [xX]
    ;

fragment
NonzeroDigit
    :   [1-9]
    ;

fragment
OctalDigit
    :   [0-7]
    ;

fragment
HexadecimalDigit
    :   [0-9a-fA-F]
    ;

fragment
IntegerSuffix
    :   UnsignedSuffix LongSuffix?
    |   UnsignedSuffix LongLongSuffix
    |   LongSuffix UnsignedSuffix?
    |   LongLongSuffix UnsignedSuffix?
    ;

fragment
UnsignedSuffix
    :   [uU]
    ;

fragment
LongSuffix
    :   [lL]
    ;

fragment
LongLongSuffix
    :   'll' | 'LL'
    ;

fragment
FloatingConstant
    :   DecimalFloatingConstant
    |   HexadecimalFloatingConstant
    ;

fragment
DecimalFloatingConstant
    :   FractionalConstant ExponentPart? FloatingSuffix?
    |   DigitSequence ExponentPart FloatingSuffix?
    ;

fragment
HexadecimalFloatingConstant
    :   HexadecimalPrefix HexadecimalFractionalConstant BinaryExponentPart FloatingSuffix?
    |   HexadecimalPrefix HexadecimalDigitSequence BinaryExponentPart FloatingSuffix?
    ;

fragment
FractionalConstant
    :   DigitSequence? '.' DigitSequence
    |   DigitSequence '.'
    ;

fragment
ExponentPart
    :   'e' Sign? DigitSequence
    |   'E' Sign? DigitSequence
    ;

fragment
Sign
    :   '+' | '-'
    ;

fragment
DigitSequence
    :   Digit+
    ;

fragment
HexadecimalFractionalConstant
    :   HexadecimalDigitSequence? '.' HexadecimalDigitSequence
    |   HexadecimalDigitSequence '.'
    ;

fragment
BinaryExponentPart
    :   'p' Sign? DigitSequence
    |   'P' Sign? DigitSequence
    ;

fragment
HexadecimalDigitSequence
    :   HexadecimalDigit+
    ;

fragment
FloatingSuffix
    :   'f' | 'l' | 'F' | 'L'
    ;

fragment
CharacterConstant
    :   '\'' CCharSequence '\''
    |   'L\'' CCharSequence '\''
    |   'u\'' CCharSequence '\''
    |   'U\'' CCharSequence '\''
    ;

fragment
CCharSequence
    :   CChar+
    ;

fragment
CChar
    :   ~['\\\r\n]
    |   EscapeSequence
    ;

fragment
EscapeSequence
    :   SimpleEscapeSequence
    |   OctalEscapeSequence
    |   HexadecimalEscapeSequence
    |   UniversalCharacterName
    ;

fragment
SimpleEscapeSequence
    :   '\\' ['"?abfnrtv\\]
    ;

fragment
OctalEscapeSequence
    :   '\\' OctalDigit
    |   '\\' OctalDigit OctalDigit
    |   '\\' OctalDigit OctalDigit OctalDigit
    ;

fragment
HexadecimalEscapeSequence
    :   '\\x' HexadecimalDigit+
    ;

StringLiteral
    :   EncodingPrefix? '"' SCharSequence? '"'
    ;

fragment
EncodingPrefix
    :   'u8'
    |   'u'
    |   'U'
    |   'L'
    ;

fragment
SCharSequence
    :   SChar+
    ;

fragment
SChar
    :   ~["\\\r\n]
    |   EscapeSequence
    ;

LineDirective
    :   '#' Whitespace? DecimalConstant Whitespace? StringLiteral ~[\r\n]*
        -> channel(HIDDEN)
    ;

PragmaDirective
    :   '#' Whitespace? 'pragma' Whitespace ~[\r\n]*
        -> channel(HIDDEN)
    ;

IncludeDirective
    :   '#' Whitespace? 'include' Whitespace ~[\r\n]*
        -> channel(HIDDEN)
    ;

Whitespace
    :   [ \t]+
        -> channel(HIDDEN)
    ;

Newline
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> channel(HIDDEN)
    ;

BlockComment
    :   '/*' .*? '*/'
        -> channel(HIDDEN)
    ;

LineComment
    :   '//' ~[\r\n]*
        -> channel(HIDDEN)
    ;
