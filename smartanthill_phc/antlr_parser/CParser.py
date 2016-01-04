# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .CListener import CListener
    from .CVisitor import CVisitor
else:
    from CListener import CListener
    from CVisitor import CVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"i\u0345\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\6\2{\n\2\r\2\16")
        buf.write(u"\2|\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\5\2\u008f\n\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\5\2\u0099\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\7\2\u00a4\n\2\f\2\16\2\u00a7\13\2\3\3\3\3\3\3")
        buf.write(u"\7\3\u00ac\n\3\f\3\16\3\u00af\13\3\3\4\3\4\3\4\3\4\3")
        buf.write(u"\4\3\4\5\4\u00b7\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5")
        buf.write(u"\u00da\n\5\f\5\16\5\u00dd\13\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\5\6\u00e6\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u00ed\n")
        buf.write(u"\7\3\b\3\b\3\b\7\b\u00f2\n\b\f\b\16\b\u00f5\13\b\3\t")
        buf.write(u"\3\t\3\n\6\n\u00fa\n\n\r\n\16\n\u00fb\3\n\5\n\u00ff\n")
        buf.write(u"\n\3\n\3\n\3\n\5\n\u0104\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\5\13\u010b\n\13\3\f\3\f\3\f\7\f\u0110\n\f\f\f\16\f\u0113")
        buf.write(u"\13\f\3\r\3\r\3\r\3\r\3\r\5\r\u011a\n\r\3\16\3\16\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\5\17\u0123\n\17\3\20\3\20\5\20\u0127")
        buf.write(u"\n\20\3\20\3\20\6\20\u012b\n\20\r\20\16\20\u012c\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\5\20\u0134\n\20\3\21\3\21\3\22\3")
        buf.write(u"\22\5\22\u013a\n\22\3\22\3\22\3\22\5\22\u013f\n\22\3")
        buf.write(u"\23\3\23\5\23\u0143\n\23\3\23\3\23\5\23\u0147\n\23\5")
        buf.write(u"\23\u0149\n\23\3\24\3\24\3\24\7\24\u014e\n\24\f\24\16")
        buf.write(u"\24\u0151\13\24\3\25\3\25\5\25\u0155\n\25\3\25\3\25\5")
        buf.write(u"\25\u0159\n\25\3\26\3\26\5\26\u015d\n\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\5\26\u0165\n\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\5\26\u016e\n\26\3\27\3\27\3\27\7\27\u0173")
        buf.write(u"\n\27\f\27\16\27\u0176\13\27\3\30\3\30\3\30\5\30\u017b")
        buf.write(u"\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\5\33\u0189\n\33\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\5\34\u0195\n\34\3\35\5\35\u0198")
        buf.write(u"\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u01a2")
        buf.write(u"\n\36\f\36\16\36\u01a5\13\36\3\36\5\36\u01a8\n\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\7\36\u01af\n\36\f\36\16\36\u01b2")
        buf.write(u"\13\36\3\36\3\36\3\36\3\36\3\36\3\36\6\36\u01ba\n\36")
        buf.write(u"\r\36\16\36\u01bb\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\7\36\u01c5\n\36\f\36\16\36\u01c8\13\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u01d4\n\36\3")
        buf.write(u"\36\7\36\u01d7\n\36\f\36\16\36\u01da\13\36\3\37\3\37")
        buf.write(u"\7\37\u01de\n\37\f\37\16\37\u01e1\13\37\3\37\5\37\u01e4")
        buf.write(u"\n\37\3 \3 \3 \7 \u01e9\n \f \16 \u01ec\13 \3 \3 \5 ")
        buf.write(u"\u01f0\n \3!\6!\u01f3\n!\r!\16!\u01f4\3!\3!\3!\6!\u01fa")
        buf.write(u"\n!\r!\16!\u01fb\3!\5!\u01ff\n!\5!\u0201\n!\3\"\3\"\3")
        buf.write(u"\"\7\"\u0206\n\"\f\"\16\"\u0209\13\"\3#\3#\5#\u020d\n")
        buf.write(u"#\3$\3$\5$\u0211\n$\3$\5$\u0214\n$\3%\3%\3%\3%\3%\3%")
        buf.write(u"\3%\7%\u021d\n%\f%\16%\u0220\13%\3%\5%\u0223\n%\3%\3")
        buf.write(u"%\3%\3%\7%\u0229\n%\f%\16%\u022c\13%\3%\3%\3%\3%\3%\7")
        buf.write(u"%\u0233\n%\f%\16%\u0236\13%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write(u"%\5%\u0241\n%\3%\5%\u0244\n%\3%\3%\3%\7%\u0249\n%\f%")
        buf.write(u"\16%\u024c\13%\3%\5%\u024f\n%\3%\3%\3%\3%\3%\7%\u0256")
        buf.write(u"\n%\f%\16%\u0259\13%\3%\3%\3%\3%\3%\3%\6%\u0261\n%\r")
        buf.write(u"%\16%\u0262\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0270")
        buf.write(u"\n%\3%\7%\u0273\n%\f%\16%\u0276\13%\3&\3&\3\'\3\'\3\'")
        buf.write(u"\3\'\5\'\u027e\n\'\3\'\3\'\5\'\u0282\n\'\3(\3(\5(\u0286")
        buf.write(u"\n(\3(\3(\3(\3(\3(\5(\u028d\n(\3(\7(\u0290\n(\f(\16(")
        buf.write(u"\u0293\13(\3)\6)\u0296\n)\r)\16)\u0297\3)\3)\3*\3*\3")
        buf.write(u"*\3*\3*\3*\5*\u02a2\n*\3+\3+\3+\3+\3+\6+\u02a9\n+\r+")
        buf.write(u"\16+\u02aa\3+\3+\3+\3,\3,\3,\3,\3,\3,\5,\u02b6\n,\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u02c3\n-\3.\3.\7.\u02c7")
        buf.write(u"\n.\f.\16.\u02ca\13.\3.\3.\3/\3/\5/\u02d0\n/\3\60\5\60")
        buf.write(u"\u02d3\n\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\5\61\u02de\n\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61")
        buf.write(u"\u02e6\n\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\3\64\3\64\5\64\u02fd\n\64\3\64\3\64\5\64\u0301\n\64")
        buf.write(u"\3\64\3\64\5\64\u0305\n\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\5\64\u030d\n\64\3\64\3\64\5\64\u0311\n\64\3\64\3")
        buf.write(u"\64\3\64\5\64\u0316\n\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write(u"\3\65\3\65\3\65\5\65\u0321\n\65\3\65\5\65\u0324\n\65")
        buf.write(u"\3\66\7\66\u0327\n\66\f\66\16\66\u032a\13\66\3\66\3\66")
        buf.write(u"\3\67\3\67\3\67\3\67\5\67\u0332\n\67\38\78\u0335\n8\f")
        buf.write(u"8\168\u0338\138\38\38\78\u033c\n8\f8\168\u033f\138\3")
        buf.write(u"8\38\39\39\39\2\7\2\b:HN:\2\4\6\b\n\f\16\20\22\24\26")
        buf.write(u"\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write(u"^`bdfhjlnp\2\20\4\2>>@@\7\2==??AADDIJ\3\2AC\4\2==??\3")
        buf.write(u"\2;<\3\2\67:\3\2Z[\3\2OY\b\2\5\5\20\20\30\30\36\36!!")
        buf.write(u"\60\60\t\2\b\b\r\r\21\21\26\27\33\34#$*+\4\2\37\37\"")
        buf.write(u"\"\6\2\t\t\31\31%%))\5\2\3\3\25\25..\3\2be\u039d\2\u008e")
        buf.write(u"\3\2\2\2\4\u00a8\3\2\2\2\6\u00b6\3\2\2\2\b\u00b8\3\2")
        buf.write(u"\2\2\n\u00e5\3\2\2\2\f\u00ec\3\2\2\2\16\u00ee\3\2\2\2")
        buf.write(u"\20\u00f6\3\2\2\2\22\u0103\3\2\2\2\24\u010a\3\2\2\2\26")
        buf.write(u"\u010c\3\2\2\2\30\u0119\3\2\2\2\32\u011b\3\2\2\2\34\u0122")
        buf.write(u"\3\2\2\2\36\u0133\3\2\2\2 \u0135\3\2\2\2\"\u013e\3\2")
        buf.write(u"\2\2$\u0148\3\2\2\2&\u014a\3\2\2\2(\u0158\3\2\2\2*\u016d")
        buf.write(u"\3\2\2\2,\u016f\3\2\2\2.\u0177\3\2\2\2\60\u017c\3\2\2")
        buf.write(u"\2\62\u0181\3\2\2\2\64\u0188\3\2\2\2\66\u0194\3\2\2\2")
        buf.write(u"8\u0197\3\2\2\2:\u019b\3\2\2\2<\u01db\3\2\2\2>\u01e5")
        buf.write(u"\3\2\2\2@\u0200\3\2\2\2B\u0202\3\2\2\2D\u020a\3\2\2\2")
        buf.write(u"F\u0213\3\2\2\2H\u0243\3\2\2\2J\u0277\3\2\2\2L\u0281")
        buf.write(u"\3\2\2\2N\u0283\3\2\2\2P\u0295\3\2\2\2R\u02a1\3\2\2\2")
        buf.write(u"T\u02a3\3\2\2\2V\u02b5\3\2\2\2X\u02c2\3\2\2\2Z\u02c4")
        buf.write(u"\3\2\2\2\\\u02cf\3\2\2\2^\u02d2\3\2\2\2`\u02e5\3\2\2")
        buf.write(u"\2b\u02e7\3\2\2\2d\u02e9\3\2\2\2f\u0315\3\2\2\2h\u0323")
        buf.write(u"\3\2\2\2j\u0328\3\2\2\2l\u0331\3\2\2\2n\u0336\3\2\2\2")
        buf.write(u"p\u0342\3\2\2\2rs\b\2\1\2st\t\2\2\2t\u008f\5\2\2\7uv")
        buf.write(u"\7\35\2\2v\u008f\5\2\2\5w\u008f\7_\2\2x\u008f\7`\2\2")
        buf.write(u"y{\7a\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\u008f")
        buf.write(u"\3\2\2\2~\177\7\61\2\2\177\u0080\5\16\b\2\u0080\u0081")
        buf.write(u"\7\62\2\2\u0081\u008f\3\2\2\2\u0082\u0083\t\3\2\2\u0083")
        buf.write(u"\u008f\5\6\4\2\u0084\u0085\7\35\2\2\u0085\u0086\7\61")
        buf.write(u"\2\2\u0086\u0087\5D#\2\u0087\u0088\7\62\2\2\u0088\u008f")
        buf.write(u"\3\2\2\2\u0089\u008a\7(\2\2\u008a\u008b\7\61\2\2\u008b")
        buf.write(u"\u008c\5D#\2\u008c\u008d\7\62\2\2\u008d\u008f\3\2\2\2")
        buf.write(u"\u008er\3\2\2\2\u008eu\3\2\2\2\u008ew\3\2\2\2\u008ex")
        buf.write(u"\3\2\2\2\u008ez\3\2\2\2\u008e~\3\2\2\2\u008e\u0082\3")
        buf.write(u"\2\2\2\u008e\u0084\3\2\2\2\u008e\u0089\3\2\2\2\u008f")
        buf.write(u"\u00a5\3\2\2\2\u0090\u0091\f\f\2\2\u0091\u0092\7\63\2")
        buf.write(u"\2\u0092\u0093\5\16\b\2\u0093\u0094\7\64\2\2\u0094\u00a4")
        buf.write(u"\3\2\2\2\u0095\u0096\f\13\2\2\u0096\u0098\7\61\2\2\u0097")
        buf.write(u"\u0099\5\4\3\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2")
        buf.write(u"\2\u0099\u009a\3\2\2\2\u009a\u00a4\7\62\2\2\u009b\u009c")
        buf.write(u"\f\n\2\2\u009c\u009d\7]\2\2\u009d\u00a4\7_\2\2\u009e")
        buf.write(u"\u009f\f\t\2\2\u009f\u00a0\7\\\2\2\u00a0\u00a4\7_\2\2")
        buf.write(u"\u00a1\u00a2\f\b\2\2\u00a2\u00a4\t\2\2\2\u00a3\u0090")
        buf.write(u"\3\2\2\2\u00a3\u0095\3\2\2\2\u00a3\u009b\3\2\2\2\u00a3")
        buf.write(u"\u009e\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\3\2\2")
        buf.write(u"\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\3\3")
        buf.write(u"\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00ad\5\f\7\2\u00a9")
        buf.write(u"\u00aa\7N\2\2\u00aa\u00ac\5\f\7\2\u00ab\u00a9\3\2\2\2")
        buf.write(u"\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write(u"\3\2\2\2\u00ae\5\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b7")
        buf.write(u"\5\2\2\2\u00b1\u00b2\7\61\2\2\u00b2\u00b3\5D#\2\u00b3")
        buf.write(u"\u00b4\7\62\2\2\u00b4\u00b5\5\6\4\2\u00b5\u00b7\3\2\2")
        buf.write(u"\2\u00b6\u00b0\3\2\2\2\u00b6\u00b1\3\2\2\2\u00b7\7\3")
        buf.write(u"\2\2\2\u00b8\u00b9\b\5\1\2\u00b9\u00ba\5\6\4\2\u00ba")
        buf.write(u"\u00db\3\2\2\2\u00bb\u00bc\f\f\2\2\u00bc\u00bd\t\4\2")
        buf.write(u"\2\u00bd\u00da\5\b\5\r\u00be\u00bf\f\13\2\2\u00bf\u00c0")
        buf.write(u"\t\5\2\2\u00c0\u00da\5\b\5\f\u00c1\u00c2\f\n\2\2\u00c2")
        buf.write(u"\u00c3\t\6\2\2\u00c3\u00da\5\b\5\13\u00c4\u00c5\f\t\2")
        buf.write(u"\2\u00c5\u00c6\t\7\2\2\u00c6\u00da\5\b\5\n\u00c7\u00c8")
        buf.write(u"\f\b\2\2\u00c8\u00c9\t\b\2\2\u00c9\u00da\5\b\5\t\u00ca")
        buf.write(u"\u00cb\f\7\2\2\u00cb\u00cc\7D\2\2\u00cc\u00da\5\b\5\b")
        buf.write(u"\u00cd\u00ce\f\6\2\2\u00ce\u00cf\7H\2\2\u00cf\u00da\5")
        buf.write(u"\b\5\7\u00d0\u00d1\f\5\2\2\u00d1\u00d2\7E\2\2\u00d2\u00da")
        buf.write(u"\5\b\5\6\u00d3\u00d4\f\4\2\2\u00d4\u00d5\7F\2\2\u00d5")
        buf.write(u"\u00da\5\b\5\5\u00d6\u00d7\f\3\2\2\u00d7\u00d8\7G\2\2")
        buf.write(u"\u00d8\u00da\5\b\5\4\u00d9\u00bb\3\2\2\2\u00d9\u00be")
        buf.write(u"\3\2\2\2\u00d9\u00c1\3\2\2\2\u00d9\u00c4\3\2\2\2\u00d9")
        buf.write(u"\u00c7\3\2\2\2\u00d9\u00ca\3\2\2\2\u00d9\u00cd\3\2\2")
        buf.write(u"\2\u00d9\u00d0\3\2\2\2\u00d9\u00d3\3\2\2\2\u00d9\u00d6")
        buf.write(u"\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write(u"\u00dc\3\2\2\2\u00dc\t\3\2\2\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write(u"\u00e6\5\b\5\2\u00df\u00e0\5\b\5\2\u00e0\u00e1\7K\2\2")
        buf.write(u"\u00e1\u00e2\5\16\b\2\u00e2\u00e3\7L\2\2\u00e3\u00e4")
        buf.write(u"\5\n\6\2\u00e4\u00e6\3\2\2\2\u00e5\u00de\3\2\2\2\u00e5")
        buf.write(u"\u00df\3\2\2\2\u00e6\13\3\2\2\2\u00e7\u00ed\5\n\6\2\u00e8")
        buf.write(u"\u00e9\5\2\2\2\u00e9\u00ea\t\t\2\2\u00ea\u00eb\5\f\7")
        buf.write(u"\2\u00eb\u00ed\3\2\2\2\u00ec\u00e7\3\2\2\2\u00ec\u00e8")
        buf.write(u"\3\2\2\2\u00ed\r\3\2\2\2\u00ee\u00f3\5\f\7\2\u00ef\u00f0")
        buf.write(u"\7N\2\2\u00f0\u00f2\5\f\7\2\u00f1\u00ef\3\2\2\2\u00f2")
        buf.write(u"\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2")
        buf.write(u"\2\u00f4\17\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\5")
        buf.write(u"\n\6\2\u00f7\21\3\2\2\2\u00f8\u00fa\5\24\13\2\u00f9\u00f8")
        buf.write(u"\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb")
        buf.write(u"\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00ff\5\26\f")
        buf.write(u"\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100")
        buf.write(u"\3\2\2\2\u0100\u0101\7M\2\2\u0101\u0104\3\2\2\2\u0102")
        buf.write(u"\u0104\5T+\2\u0103\u00f9\3\2\2\2\u0103\u0102\3\2\2\2")
        buf.write(u"\u0104\23\3\2\2\2\u0105\u010b\5\32\16\2\u0106\u010b\5")
        buf.write(u"\34\17\2\u0107\u010b\5\62\32\2\u0108\u010b\5\64\33\2")
        buf.write(u"\u0109\u010b\5\66\34\2\u010a\u0105\3\2\2\2\u010a\u0106")
        buf.write(u"\3\2\2\2\u010a\u0107\3\2\2\2\u010a\u0108\3\2\2\2\u010a")
        buf.write(u"\u0109\3\2\2\2\u010b\25\3\2\2\2\u010c\u0111\5\30\r\2")
        buf.write(u"\u010d\u010e\7N\2\2\u010e\u0110\5\30\r\2\u010f\u010d")
        buf.write(u"\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111")
        buf.write(u"\u0112\3\2\2\2\u0112\27\3\2\2\2\u0113\u0111\3\2\2\2\u0114")
        buf.write(u"\u011a\58\35\2\u0115\u0116\58\35\2\u0116\u0117\7O\2\2")
        buf.write(u"\u0117\u0118\5L\'\2\u0118\u011a\3\2\2\2\u0119\u0114\3")
        buf.write(u"\2\2\2\u0119\u0115\3\2\2\2\u011a\31\3\2\2\2\u011b\u011c")
        buf.write(u"\t\n\2\2\u011c\33\3\2\2\2\u011d\u0123\t\13\2\2\u011e")
        buf.write(u"\u0123\5\60\31\2\u011f\u0123\5\36\20\2\u0120\u0123\5")
        buf.write(u"*\26\2\u0121\u0123\5J&\2\u0122\u011d\3\2\2\2\u0122\u011e")
        buf.write(u"\3\2\2\2\u0122\u011f\3\2\2\2\u0122\u0120\3\2\2\2\u0122")
        buf.write(u"\u0121\3\2\2\2\u0123\35\3\2\2\2\u0124\u0126\5 \21\2\u0125")
        buf.write(u"\u0127\7_\2\2\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write(u"\u0127\u0128\3\2\2\2\u0128\u012a\7\65\2\2\u0129\u012b")
        buf.write(u"\5\"\22\2\u012a\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write(u"\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\3\2\2")
        buf.write(u"\2\u012e\u012f\7\66\2\2\u012f\u0134\3\2\2\2\u0130\u0131")
        buf.write(u"\5 \21\2\u0131\u0132\7_\2\2\u0132\u0134\3\2\2\2\u0133")
        buf.write(u"\u0124\3\2\2\2\u0133\u0130\3\2\2\2\u0134\37\3\2\2\2\u0135")
        buf.write(u"\u0136\t\f\2\2\u0136!\3\2\2\2\u0137\u0139\5$\23\2\u0138")
        buf.write(u"\u013a\5&\24\2\u0139\u0138\3\2\2\2\u0139\u013a\3\2\2")
        buf.write(u"\2\u013a\u013b\3\2\2\2\u013b\u013c\7M\2\2\u013c\u013f")
        buf.write(u"\3\2\2\2\u013d\u013f\5T+\2\u013e\u0137\3\2\2\2\u013e")
        buf.write(u"\u013d\3\2\2\2\u013f#\3\2\2\2\u0140\u0142\5\34\17\2\u0141")
        buf.write(u"\u0143\5$\23\2\u0142\u0141\3\2\2\2\u0142\u0143\3\2\2")
        buf.write(u"\2\u0143\u0149\3\2\2\2\u0144\u0146\5\62\32\2\u0145\u0147")
        buf.write(u"\5$\23\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write(u"\u0149\3\2\2\2\u0148\u0140\3\2\2\2\u0148\u0144\3\2\2")
        buf.write(u"\2\u0149%\3\2\2\2\u014a\u014f\5(\25\2\u014b\u014c\7N")
        buf.write(u"\2\2\u014c\u014e\5(\25\2\u014d\u014b\3\2\2\2\u014e\u0151")
        buf.write(u"\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write(u"\'\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0159\58\35\2\u0153")
        buf.write(u"\u0155\58\35\2\u0154\u0153\3\2\2\2\u0154\u0155\3\2\2")
        buf.write(u"\2\u0155\u0156\3\2\2\2\u0156\u0157\7L\2\2\u0157\u0159")
        buf.write(u"\5\20\t\2\u0158\u0152\3\2\2\2\u0158\u0154\3\2\2\2\u0159")
        buf.write(u")\3\2\2\2\u015a\u015c\7\17\2\2\u015b\u015d\7_\2\2\u015c")
        buf.write(u"\u015b\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2")
        buf.write(u"\2\u015e\u015f\7\65\2\2\u015f\u0160\5,\27\2\u0160\u0161")
        buf.write(u"\7\66\2\2\u0161\u016e\3\2\2\2\u0162\u0164\7\17\2\2\u0163")
        buf.write(u"\u0165\7_\2\2\u0164\u0163\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write(u"\u0165\u0166\3\2\2\2\u0166\u0167\7\65\2\2\u0167\u0168")
        buf.write(u"\5,\27\2\u0168\u0169\7N\2\2\u0169\u016a\7\66\2\2\u016a")
        buf.write(u"\u016e\3\2\2\2\u016b\u016c\7\17\2\2\u016c\u016e\7_\2")
        buf.write(u"\2\u016d\u015a\3\2\2\2\u016d\u0162\3\2\2\2\u016d\u016b")
        buf.write(u"\3\2\2\2\u016e+\3\2\2\2\u016f\u0174\5.\30\2\u0170\u0171")
        buf.write(u"\7N\2\2\u0171\u0173\5.\30\2\u0172\u0170\3\2\2\2\u0173")
        buf.write(u"\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2")
        buf.write(u"\2\u0175-\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u017a\7_")
        buf.write(u"\2\2\u0178\u0179\7O\2\2\u0179\u017b\5\20\t\2\u017a\u0178")
        buf.write(u"\3\2\2\2\u017a\u017b\3\2\2\2\u017b/\3\2\2\2\u017c\u017d")
        buf.write(u"\7)\2\2\u017d\u017e\7\61\2\2\u017e\u017f\5D#\2\u017f")
        buf.write(u"\u0180\7\62\2\2\u0180\61\3\2\2\2\u0181\u0182\t\r\2\2")
        buf.write(u"\u0182\63\3\2\2\2\u0183\u0189\t\16\2\2\u0184\u0185\7")
        buf.write(u"\4\2\2\u0185\u0186\7\61\2\2\u0186\u0187\7_\2\2\u0187")
        buf.write(u"\u0189\7\62\2\2\u0188\u0183\3\2\2\2\u0188\u0184\3\2\2")
        buf.write(u"\2\u0189\65\3\2\2\2\u018a\u018b\7\'\2\2\u018b\u018c\7")
        buf.write(u"\61\2\2\u018c\u018d\5D#\2\u018d\u018e\7\62\2\2\u018e")
        buf.write(u"\u0195\3\2\2\2\u018f\u0190\7\'\2\2\u0190\u0191\7\61\2")
        buf.write(u"\2\u0191\u0192\5\20\t\2\u0192\u0193\7\62\2\2\u0193\u0195")
        buf.write(u"\3\2\2\2\u0194\u018a\3\2\2\2\u0194\u018f\3\2\2\2\u0195")
        buf.write(u"\67\3\2\2\2\u0196\u0198\5<\37\2\u0197\u0196\3\2\2\2\u0197")
        buf.write(u"\u0198\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\5:\36")
        buf.write(u"\2\u019a9\3\2\2\2\u019b\u019c\b\36\1\2\u019c\u019d\7")
        buf.write(u"_\2\2\u019d\u01d8\3\2\2\2\u019e\u019f\f\b\2\2\u019f\u01a3")
        buf.write(u"\7\63\2\2\u01a0\u01a2\5\62\32\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write(u"\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2")
        buf.write(u"\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a8")
        buf.write(u"\5\f\7\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write(u"\u01a9\3\2\2\2\u01a9\u01d7\7\64\2\2\u01aa\u01ab\f\7\2")
        buf.write(u"\2\u01ab\u01ac\7\63\2\2\u01ac\u01b0\7\36\2\2\u01ad\u01af")
        buf.write(u"\5\62\32\2\u01ae\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0")
        buf.write(u"\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b3\3\2\2")
        buf.write(u"\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4\5\f\7\2\u01b4\u01b5")
        buf.write(u"\7\64\2\2\u01b5\u01d7\3\2\2\2\u01b6\u01b7\f\6\2\2\u01b7")
        buf.write(u"\u01b9\7\63\2\2\u01b8\u01ba\5\62\32\2\u01b9\u01b8\3\2")
        buf.write(u"\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc")
        buf.write(u"\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\7\36\2\2\u01be")
        buf.write(u"\u01bf\5\f\7\2\u01bf\u01c0\7\64\2\2\u01c0\u01d7\3\2\2")
        buf.write(u"\2\u01c1\u01c2\f\5\2\2\u01c2\u01c6\7\63\2\2\u01c3\u01c5")
        buf.write(u"\5\62\32\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6")
        buf.write(u"\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c9\3\2\2")
        buf.write(u"\2\u01c8\u01c6\3\2\2\2\u01c9\u01ca\7A\2\2\u01ca\u01d7")
        buf.write(u"\7\64\2\2\u01cb\u01cc\f\4\2\2\u01cc\u01cd\7\61\2\2\u01cd")
        buf.write(u"\u01ce\5> \2\u01ce\u01cf\7\62\2\2\u01cf\u01d7\3\2\2\2")
        buf.write(u"\u01d0\u01d1\f\3\2\2\u01d1\u01d3\7\61\2\2\u01d2\u01d4")
        buf.write(u"\5B\"\2\u01d3\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write(u"\u01d5\3\2\2\2\u01d5\u01d7\7\62\2\2\u01d6\u019e\3\2\2")
        buf.write(u"\2\u01d6\u01aa\3\2\2\2\u01d6\u01b6\3\2\2\2\u01d6\u01c1")
        buf.write(u"\3\2\2\2\u01d6\u01cb\3\2\2\2\u01d6\u01d0\3\2\2\2\u01d7")
        buf.write(u"\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2")
        buf.write(u"\2\u01d9;\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01df\7A")
        buf.write(u"\2\2\u01dc\u01de\5\62\32\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write(u"\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2")
        buf.write(u"\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e4")
        buf.write(u"\5<\37\2\u01e3\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write(u"=\3\2\2\2\u01e5\u01ea\5@!\2\u01e6\u01e7\7N\2\2\u01e7")
        buf.write(u"\u01e9\5@!\2\u01e8\u01e6\3\2\2\2\u01e9\u01ec\3\2\2\2")
        buf.write(u"\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ef")
        buf.write(u"\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ee\7N\2\2\u01ee")
        buf.write(u"\u01f0\7^\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write(u"\u01f0?\3\2\2\2\u01f1\u01f3\5\24\13\2\u01f2\u01f1\3\2")
        buf.write(u"\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write(u"\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\58\35\2\u01f7")
        buf.write(u"\u0201\3\2\2\2\u01f8\u01fa\5\24\13\2\u01f9\u01f8\3\2")
        buf.write(u"\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc")
        buf.write(u"\3\2\2\2\u01fc\u01fe\3\2\2\2\u01fd\u01ff\5F$\2\u01fe")
        buf.write(u"\u01fd\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0201\3\2\2")
        buf.write(u"\2\u0200\u01f2\3\2\2\2\u0200\u01f9\3\2\2\2\u0201A\3\2")
        buf.write(u"\2\2\u0202\u0207\7_\2\2\u0203\u0204\7N\2\2\u0204\u0206")
        buf.write(u"\7_\2\2\u0205\u0203\3\2\2\2\u0206\u0209\3\2\2\2\u0207")
        buf.write(u"\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208C\3\2\2\2\u0209")
        buf.write(u"\u0207\3\2\2\2\u020a\u020c\5$\23\2\u020b\u020d\5F$\2")
        buf.write(u"\u020c\u020b\3\2\2\2\u020c\u020d\3\2\2\2\u020dE\3\2\2")
        buf.write(u"\2\u020e\u0214\5<\37\2\u020f\u0211\5<\37\2\u0210\u020f")
        buf.write(u"\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212\3\2\2\2\u0212")
        buf.write(u"\u0214\5H%\2\u0213\u020e\3\2\2\2\u0213\u0210\3\2\2\2")
        buf.write(u"\u0214G\3\2\2\2\u0215\u0216\b%\1\2\u0216\u0217\7\61\2")
        buf.write(u"\2\u0217\u0218\5F$\2\u0218\u0219\7\62\2\2\u0219\u0244")
        buf.write(u"\3\2\2\2\u021a\u021e\7\63\2\2\u021b\u021d\5\62\32\2\u021c")
        buf.write(u"\u021b\3\2\2\2\u021d\u0220\3\2\2\2\u021e\u021c\3\2\2")
        buf.write(u"\2\u021e\u021f\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e")
        buf.write(u"\3\2\2\2\u0221\u0223\5\f\7\2\u0222\u0221\3\2\2\2\u0222")
        buf.write(u"\u0223\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0244\7\64\2")
        buf.write(u"\2\u0225\u0226\7\63\2\2\u0226\u022a\7\36\2\2\u0227\u0229")
        buf.write(u"\5\62\32\2\u0228\u0227\3\2\2\2\u0229\u022c\3\2\2\2\u022a")
        buf.write(u"\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022d\3\2\2")
        buf.write(u"\2\u022c\u022a\3\2\2\2\u022d\u022e\5\f\7\2\u022e\u022f")
        buf.write(u"\7\64\2\2\u022f\u0244\3\2\2\2\u0230\u0234\7\63\2\2\u0231")
        buf.write(u"\u0233\5\62\32\2\u0232\u0231\3\2\2\2\u0233\u0236\3\2")
        buf.write(u"\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0237")
        buf.write(u"\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u0238\7\36\2\2\u0238")
        buf.write(u"\u0239\5\f\7\2\u0239\u023a\7\64\2\2\u023a\u0244\3\2\2")
        buf.write(u"\2\u023b\u023c\7\63\2\2\u023c\u023d\7A\2\2\u023d\u0244")
        buf.write(u"\7\64\2\2\u023e\u0240\7\61\2\2\u023f\u0241\5> \2\u0240")
        buf.write(u"\u023f\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0242\3\2\2")
        buf.write(u"\2\u0242\u0244\7\62\2\2\u0243\u0215\3\2\2\2\u0243\u021a")
        buf.write(u"\3\2\2\2\u0243\u0225\3\2\2\2\u0243\u0230\3\2\2\2\u0243")
        buf.write(u"\u023b\3\2\2\2\u0243\u023e\3\2\2\2\u0244\u0274\3\2\2")
        buf.write(u"\2\u0245\u0246\f\7\2\2\u0246\u024a\7\63\2\2\u0247\u0249")
        buf.write(u"\5\62\32\2\u0248\u0247\3\2\2\2\u0249\u024c\3\2\2\2\u024a")
        buf.write(u"\u0248\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024e\3\2\2")
        buf.write(u"\2\u024c\u024a\3\2\2\2\u024d\u024f\5\f\7\2\u024e\u024d")
        buf.write(u"\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250\3\2\2\2\u0250")
        buf.write(u"\u0273\7\64\2\2\u0251\u0252\f\6\2\2\u0252\u0253\7\63")
        buf.write(u"\2\2\u0253\u0257\7\36\2\2\u0254\u0256\5\62\32\2\u0255")
        buf.write(u"\u0254\3\2\2\2\u0256\u0259\3\2\2\2\u0257\u0255\3\2\2")
        buf.write(u"\2\u0257\u0258\3\2\2\2\u0258\u025a\3\2\2\2\u0259\u0257")
        buf.write(u"\3\2\2\2\u025a\u025b\5\f\7\2\u025b\u025c\7\64\2\2\u025c")
        buf.write(u"\u0273\3\2\2\2\u025d\u025e\f\5\2\2\u025e\u0260\7\63\2")
        buf.write(u"\2\u025f\u0261\5\62\32\2\u0260\u025f\3\2\2\2\u0261\u0262")
        buf.write(u"\3\2\2\2\u0262\u0260\3\2\2\2\u0262\u0263\3\2\2\2\u0263")
        buf.write(u"\u0264\3\2\2\2\u0264\u0265\7\36\2\2\u0265\u0266\5\f\7")
        buf.write(u"\2\u0266\u0267\7\64\2\2\u0267\u0273\3\2\2\2\u0268\u0269")
        buf.write(u"\f\4\2\2\u0269\u026a\7\63\2\2\u026a\u026b\7A\2\2\u026b")
        buf.write(u"\u0273\7\64\2\2\u026c\u026d\f\3\2\2\u026d\u026f\7\61")
        buf.write(u"\2\2\u026e\u0270\5> \2\u026f\u026e\3\2\2\2\u026f\u0270")
        buf.write(u"\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0273\7\62\2\2\u0272")
        buf.write(u"\u0245\3\2\2\2\u0272\u0251\3\2\2\2\u0272\u025d\3\2\2")
        buf.write(u"\2\u0272\u0268\3\2\2\2\u0272\u026c\3\2\2\2\u0273\u0276")
        buf.write(u"\3\2\2\2\u0274\u0272\3\2\2\2\u0274\u0275\3\2\2\2\u0275")
        buf.write(u"I\3\2\2\2\u0276\u0274\3\2\2\2\u0277\u0278\7_\2\2\u0278")
        buf.write(u"K\3\2\2\2\u0279\u0282\5\f\7\2\u027a\u027b\7\65\2\2\u027b")
        buf.write(u"\u027d\5N(\2\u027c\u027e\7N\2\2\u027d\u027c\3\2\2\2\u027d")
        buf.write(u"\u027e\3\2\2\2\u027e\u027f\3\2\2\2\u027f\u0280\7\66\2")
        buf.write(u"\2\u0280\u0282\3\2\2\2\u0281\u0279\3\2\2\2\u0281\u027a")
        buf.write(u"\3\2\2\2\u0282M\3\2\2\2\u0283\u0285\b(\1\2\u0284\u0286")
        buf.write(u"\5P)\2\u0285\u0284\3\2\2\2\u0285\u0286\3\2\2\2\u0286")
        buf.write(u"\u0287\3\2\2\2\u0287\u0288\5L\'\2\u0288\u0291\3\2\2\2")
        buf.write(u"\u0289\u028a\f\3\2\2\u028a\u028c\7N\2\2\u028b\u028d\5")
        buf.write(u"P)\2\u028c\u028b\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u028e")
        buf.write(u"\3\2\2\2\u028e\u0290\5L\'\2\u028f\u0289\3\2\2\2\u0290")
        buf.write(u"\u0293\3\2\2\2\u0291\u028f\3\2\2\2\u0291\u0292\3\2\2")
        buf.write(u"\2\u0292O\3\2\2\2\u0293\u0291\3\2\2\2\u0294\u0296\5R")
        buf.write(u"*\2\u0295\u0294\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0295")
        buf.write(u"\3\2\2\2\u0297\u0298\3\2\2\2\u0298\u0299\3\2\2\2\u0299")
        buf.write(u"\u029a\7O\2\2\u029aQ\3\2\2\2\u029b\u029c\7\63\2\2\u029c")
        buf.write(u"\u029d\5\20\t\2\u029d\u029e\7\64\2\2\u029e\u02a2\3\2")
        buf.write(u"\2\2\u029f\u02a0\7]\2\2\u02a0\u02a2\7_\2\2\u02a1\u029b")
        buf.write(u"\3\2\2\2\u02a1\u029f\3\2\2\2\u02a2S\3\2\2\2\u02a3\u02a4")
        buf.write(u"\7/\2\2\u02a4\u02a5\7\61\2\2\u02a5\u02a6\5\20\t\2\u02a6")
        buf.write(u"\u02a8\7N\2\2\u02a7\u02a9\7a\2\2\u02a8\u02a7\3\2\2\2")
        buf.write(u"\u02a9\u02aa\3\2\2\2\u02aa\u02a8\3\2\2\2\u02aa\u02ab")
        buf.write(u"\3\2\2\2\u02ab\u02ac\3\2\2\2\u02ac\u02ad\7\62\2\2\u02ad")
        buf.write(u"\u02ae\7M\2\2\u02aeU\3\2\2\2\u02af\u02b6\5X-\2\u02b0")
        buf.write(u"\u02b6\5Z.\2\u02b1\u02b6\5^\60\2\u02b2\u02b6\5`\61\2")
        buf.write(u"\u02b3\u02b6\5f\64\2\u02b4\u02b6\5h\65\2\u02b5\u02af")
        buf.write(u"\3\2\2\2\u02b5\u02b0\3\2\2\2\u02b5\u02b1\3\2\2\2\u02b5")
        buf.write(u"\u02b2\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b5\u02b4\3\2\2")
        buf.write(u"\2\u02b6W\3\2\2\2\u02b7\u02b8\7_\2\2\u02b8\u02b9\7L\2")
        buf.write(u"\2\u02b9\u02c3\5V,\2\u02ba\u02bb\7\7\2\2\u02bb\u02bc")
        buf.write(u"\5\20\t\2\u02bc\u02bd\7L\2\2\u02bd\u02be\5V,\2\u02be")
        buf.write(u"\u02c3\3\2\2\2\u02bf\u02c0\7\13\2\2\u02c0\u02c1\7L\2")
        buf.write(u"\2\u02c1\u02c3\5V,\2\u02c2\u02b7\3\2\2\2\u02c2\u02ba")
        buf.write(u"\3\2\2\2\u02c2\u02bf\3\2\2\2\u02c3Y\3\2\2\2\u02c4\u02c8")
        buf.write(u"\7\65\2\2\u02c5\u02c7\5\\/\2\u02c6\u02c5\3\2\2\2\u02c7")
        buf.write(u"\u02ca\3\2\2\2\u02c8\u02c6\3\2\2\2\u02c8\u02c9\3\2\2")
        buf.write(u"\2\u02c9\u02cb\3\2\2\2\u02ca\u02c8\3\2\2\2\u02cb\u02cc")
        buf.write(u"\7\66\2\2\u02cc[\3\2\2\2\u02cd\u02d0\5\22\n\2\u02ce\u02d0")
        buf.write(u"\5V,\2\u02cf\u02cd\3\2\2\2\u02cf\u02ce\3\2\2\2\u02d0")
        buf.write(u"]\3\2\2\2\u02d1\u02d3\5\16\b\2\u02d2\u02d1\3\2\2\2\u02d2")
        buf.write(u"\u02d3\3\2\2\2\u02d3\u02d4\3\2\2\2\u02d4\u02d5\7M\2\2")
        buf.write(u"\u02d5_\3\2\2\2\u02d6\u02d7\7\24\2\2\u02d7\u02d8\7\61")
        buf.write(u"\2\2\u02d8\u02d9\5\16\b\2\u02d9\u02da\7\62\2\2\u02da")
        buf.write(u"\u02dd\5V,\2\u02db\u02dc\7\16\2\2\u02dc\u02de\5V,\2\u02dd")
        buf.write(u"\u02db\3\2\2\2\u02dd\u02de\3\2\2\2\u02de\u02e6\3\2\2")
        buf.write(u"\2\u02df\u02e0\7 \2\2\u02e0\u02e1\7\61\2\2\u02e1\u02e2")
        buf.write(u"\5\16\b\2\u02e2\u02e3\7\62\2\2\u02e3\u02e4\5V,\2\u02e4")
        buf.write(u"\u02e6\3\2\2\2\u02e5\u02d6\3\2\2\2\u02e5\u02df\3\2\2")
        buf.write(u"\2\u02e6a\3\2\2\2\u02e7\u02e8\5\16\b\2\u02e8c\3\2\2\2")
        buf.write(u"\u02e9\u02ea\5\16\b\2\u02eae\3\2\2\2\u02eb\u02ec\7&\2")
        buf.write(u"\2\u02ec\u02ed\7\61\2\2\u02ed\u02ee\5\16\b\2\u02ee\u02ef")
        buf.write(u"\7\62\2\2\u02ef\u02f0\5V,\2\u02f0\u0316\3\2\2\2\u02f1")
        buf.write(u"\u02f2\7\f\2\2\u02f2\u02f3\5V,\2\u02f3\u02f4\7&\2\2\u02f4")
        buf.write(u"\u02f5\7\61\2\2\u02f5\u02f6\5\16\b\2\u02f6\u02f7\7\62")
        buf.write(u"\2\2\u02f7\u02f8\7M\2\2\u02f8\u0316\3\2\2\2\u02f9\u02fa")
        buf.write(u"\7\22\2\2\u02fa\u02fc\7\61\2\2\u02fb\u02fd\5b\62\2\u02fc")
        buf.write(u"\u02fb\3\2\2\2\u02fc\u02fd\3\2\2\2\u02fd\u02fe\3\2\2")
        buf.write(u"\2\u02fe\u0300\7M\2\2\u02ff\u0301\5\16\b\2\u0300\u02ff")
        buf.write(u"\3\2\2\2\u0300\u0301\3\2\2\2\u0301\u0302\3\2\2\2\u0302")
        buf.write(u"\u0304\7M\2\2\u0303\u0305\5d\63\2\u0304\u0303\3\2\2\2")
        buf.write(u"\u0304\u0305\3\2\2\2\u0305\u0306\3\2\2\2\u0306\u0307")
        buf.write(u"\7\62\2\2\u0307\u0316\5V,\2\u0308\u0309\7\22\2\2\u0309")
        buf.write(u"\u030a\7\61\2\2\u030a\u030c\5\22\n\2\u030b\u030d\5\16")
        buf.write(u"\b\2\u030c\u030b\3\2\2\2\u030c\u030d\3\2\2\2\u030d\u030e")
        buf.write(u"\3\2\2\2\u030e\u0310\7M\2\2\u030f\u0311\5d\63\2\u0310")
        buf.write(u"\u030f\3\2\2\2\u0310\u0311\3\2\2\2\u0311\u0312\3\2\2")
        buf.write(u"\2\u0312\u0313\7\62\2\2\u0313\u0314\5V,\2\u0314\u0316")
        buf.write(u"\3\2\2\2\u0315\u02eb\3\2\2\2\u0315\u02f1\3\2\2\2\u0315")
        buf.write(u"\u02f9\3\2\2\2\u0315\u0308\3\2\2\2\u0316g\3\2\2\2\u0317")
        buf.write(u"\u0318\7\23\2\2\u0318\u0319\7_\2\2\u0319\u0324\7M\2\2")
        buf.write(u"\u031a\u031b\7\n\2\2\u031b\u0324\7M\2\2\u031c\u031d\7")
        buf.write(u"\6\2\2\u031d\u0324\7M\2\2\u031e\u0320\7\32\2\2\u031f")
        buf.write(u"\u0321\5\16\b\2\u0320\u031f\3\2\2\2\u0320\u0321\3\2\2")
        buf.write(u"\2\u0321\u0322\3\2\2\2\u0322\u0324\7M\2\2\u0323\u0317")
        buf.write(u"\3\2\2\2\u0323\u031a\3\2\2\2\u0323\u031c\3\2\2\2\u0323")
        buf.write(u"\u031e\3\2\2\2\u0324i\3\2\2\2\u0325\u0327\5l\67\2\u0326")
        buf.write(u"\u0325\3\2\2\2\u0327\u032a\3\2\2\2\u0328\u0326\3\2\2")
        buf.write(u"\2\u0328\u0329\3\2\2\2\u0329\u032b\3\2\2\2\u032a\u0328")
        buf.write(u"\3\2\2\2\u032b\u032c\7\2\2\3\u032ck\3\2\2\2\u032d\u0332")
        buf.write(u"\5n8\2\u032e\u0332\5\22\n\2\u032f\u0332\5p9\2\u0330\u0332")
        buf.write(u"\7M\2\2\u0331\u032d\3\2\2\2\u0331\u032e\3\2\2\2\u0331")
        buf.write(u"\u032f\3\2\2\2\u0331\u0330\3\2\2\2\u0332m\3\2\2\2\u0333")
        buf.write(u"\u0335\5\24\13\2\u0334\u0333\3\2\2\2\u0335\u0338\3\2")
        buf.write(u"\2\2\u0336\u0334\3\2\2\2\u0336\u0337\3\2\2\2\u0337\u0339")
        buf.write(u"\3\2\2\2\u0338\u0336\3\2\2\2\u0339\u033d\58\35\2\u033a")
        buf.write(u"\u033c\5\22\n\2\u033b\u033a\3\2\2\2\u033c\u033f\3\2\2")
        buf.write(u"\2\u033d\u033b\3\2\2\2\u033d\u033e\3\2\2\2\u033e\u0340")
        buf.write(u"\3\2\2\2\u033f\u033d\3\2\2\2\u0340\u0341\5Z.\2\u0341")
        buf.write(u"o\3\2\2\2\u0342\u0343\t\17\2\2\u0343q\3\2\2\2d|\u008e")
        buf.write(u"\u0098\u00a3\u00a5\u00ad\u00b6\u00d9\u00db\u00e5\u00ec")
        buf.write(u"\u00f3\u00fb\u00fe\u0103\u010a\u0111\u0119\u0122\u0126")
        buf.write(u"\u012c\u0133\u0139\u013e\u0142\u0146\u0148\u014f\u0154")
        buf.write(u"\u0158\u015c\u0164\u016d\u0174\u017a\u0188\u0194\u0197")
        buf.write(u"\u01a3\u01a7\u01b0\u01bb\u01c6\u01d3\u01d6\u01d8\u01df")
        buf.write(u"\u01e3\u01ea\u01ef\u01f4\u01fb\u01fe\u0200\u0207\u020c")
        buf.write(u"\u0210\u0213\u021e\u0222\u022a\u0234\u0240\u0243\u024a")
        buf.write(u"\u024e\u0257\u0262\u026f\u0272\u0274\u027d\u0281\u0285")
        buf.write(u"\u028c\u0291\u0297\u02a1\u02aa\u02b5\u02c2\u02c8\u02cf")
        buf.write(u"\u02d2\u02dd\u02e5\u02fc\u0300\u0304\u030c\u0310\u0315")
        buf.write(u"\u0320\u0323\u0328\u0331\u0336\u033d")
        return buf.getvalue()


class CParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'__stdcall'", u"'__declspec'", u"'auto'", 
                     u"'break'", u"'case'", u"'char'", u"'const'", u"'continue'", 
                     u"'default'", u"'do'", u"'double'", u"'else'", u"'enum'", 
                     u"'extern'", u"'float'", u"'for'", u"'goto'", u"'if'", 
                     u"'inline'", u"'int'", u"'long'", u"'register'", u"'restrict'", 
                     u"'return'", u"'short'", u"'signed'", u"'sizeof'", 
                     u"'static'", u"'struct'", u"'switch'", u"'typedef'", 
                     u"'union'", u"'unsigned'", u"'void'", u"'volatile'", 
                     u"'while'", u"'_Alignas'", u"'_Alignof'", u"'_Atomic'", 
                     u"'_Bool'", u"'_Complex'", u"'_Generic'", u"'_Imaginary'", 
                     u"'_Noreturn'", u"'_Static_assert'", u"'_Thread_local'", 
                     u"'('", u"')'", u"'['", u"']'", u"'{'", u"'}'", u"'<'", 
                     u"'<='", u"'>'", u"'>='", u"'<<'", u"'>>'", u"'+'", 
                     u"'++'", u"'-'", u"'--'", u"'*'", u"'/'", u"'%'", u"'&'", 
                     u"'|'", u"'&&'", u"'||'", u"'^'", u"'!'", u"'~'", u"'?'", 
                     u"':'", u"';'", u"','", u"'='", u"'*='", u"'/='", u"'%='", 
                     u"'+='", u"'-='", u"'<<='", u"'>>='", u"'&='", u"'^='", 
                     u"'|='", u"'=='", u"'!='", u"'->'", u"'.'", u"'...'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"Auto", 
                      u"Break", u"Case", u"Char", u"Const", u"Continue", 
                      u"Default", u"Do", u"Double", u"Else", u"Enum", u"Extern", 
                      u"Float", u"For", u"Goto", u"If", u"Inline", u"Int", 
                      u"Long", u"Register", u"Restrict", u"Return", u"Short", 
                      u"Signed", u"Sizeof", u"Static", u"Struct", u"Switch", 
                      u"Typedef", u"Union", u"Unsigned", u"Void", u"Volatile", 
                      u"While", u"Alignas", u"Alignof", u"Atomic", u"Bool", 
                      u"Complex", u"Generic", u"Imaginary", u"Noreturn", 
                      u"StaticAssert", u"ThreadLocal", u"LeftParen", u"RightParen", 
                      u"LeftBracket", u"RightBracket", u"LeftBrace", u"RightBrace", 
                      u"Less", u"LessEqual", u"Greater", u"GreaterEqual", 
                      u"LeftShift", u"RightShift", u"Plus", u"PlusPlus", 
                      u"Minus", u"MinusMinus", u"Star", u"Div", u"Mod", 
                      u"And", u"Or", u"AndAnd", u"OrOr", u"Caret", u"Not", 
                      u"Tilde", u"Question", u"Colon", u"Semi", u"Comma", 
                      u"Assign", u"StarAssign", u"DivAssign", u"ModAssign", 
                      u"PlusAssign", u"MinusAssign", u"LeftShiftAssign", 
                      u"RightShiftAssign", u"AndAssign", u"XorAssign", u"OrAssign", 
                      u"Equal", u"NotEqual", u"Arrow", u"Dot", u"Ellipsis", 
                      u"Identifier", u"Constant", u"StringLiteral", u"LineDirective", 
                      u"PragmaDirective", u"IncludeDirective", u"DefineDirective", 
                      u"Whitespace", u"Newline", u"BlockComment", u"LineComment" ]

    RULE_unaryExpression = 0
    RULE_argumentExpressionList = 1
    RULE_castExpression = 2
    RULE_logicalOrExpression = 3
    RULE_conditionalExpression = 4
    RULE_assignmentExpression = 5
    RULE_expression = 6
    RULE_constantExpression = 7
    RULE_declaration = 8
    RULE_declarationSpecifier = 9
    RULE_initDeclaratorList = 10
    RULE_initDeclarator = 11
    RULE_storageClassSpecifier = 12
    RULE_typeSpecifier = 13
    RULE_structOrUnionSpecifier = 14
    RULE_structOrUnion = 15
    RULE_structDeclaration = 16
    RULE_specifierQualifierList = 17
    RULE_structDeclaratorList = 18
    RULE_structDeclarator = 19
    RULE_enumSpecifier = 20
    RULE_enumeratorList = 21
    RULE_enumerator = 22
    RULE_atomicTypeSpecifier = 23
    RULE_typeQualifier = 24
    RULE_functionSpecifier = 25
    RULE_alignmentSpecifier = 26
    RULE_declarator = 27
    RULE_directDeclarator = 28
    RULE_pointer = 29
    RULE_parameterTypeList = 30
    RULE_parameterDeclaration = 31
    RULE_identifierList = 32
    RULE_typeName = 33
    RULE_abstractDeclarator = 34
    RULE_directAbstractDeclarator = 35
    RULE_typedefName = 36
    RULE_initializer = 37
    RULE_initializerList = 38
    RULE_designation = 39
    RULE_designator = 40
    RULE_staticAssertDeclaration = 41
    RULE_statement = 42
    RULE_labeledStatement = 43
    RULE_compoundStatement = 44
    RULE_blockItem = 45
    RULE_expressionStatement = 46
    RULE_selectionStatement = 47
    RULE_initExpression = 48
    RULE_iterationExpression = 49
    RULE_iterationStatement = 50
    RULE_jumpStatement = 51
    RULE_compilationUnit = 52
    RULE_externalDeclaration = 53
    RULE_functionDefinition = 54
    RULE_preprocessorDirective = 55

    ruleNames =  [ u"unaryExpression", u"argumentExpressionList", u"castExpression", 
                   u"logicalOrExpression", u"conditionalExpression", u"assignmentExpression", 
                   u"expression", u"constantExpression", u"declaration", 
                   u"declarationSpecifier", u"initDeclaratorList", u"initDeclarator", 
                   u"storageClassSpecifier", u"typeSpecifier", u"structOrUnionSpecifier", 
                   u"structOrUnion", u"structDeclaration", u"specifierQualifierList", 
                   u"structDeclaratorList", u"structDeclarator", u"enumSpecifier", 
                   u"enumeratorList", u"enumerator", u"atomicTypeSpecifier", 
                   u"typeQualifier", u"functionSpecifier", u"alignmentSpecifier", 
                   u"declarator", u"directDeclarator", u"pointer", u"parameterTypeList", 
                   u"parameterDeclaration", u"identifierList", u"typeName", 
                   u"abstractDeclarator", u"directAbstractDeclarator", u"typedefName", 
                   u"initializer", u"initializerList", u"designation", u"designator", 
                   u"staticAssertDeclaration", u"statement", u"labeledStatement", 
                   u"compoundStatement", u"blockItem", u"expressionStatement", 
                   u"selectionStatement", u"initExpression", u"iterationExpression", 
                   u"iterationStatement", u"jumpStatement", u"compilationUnit", 
                   u"externalDeclaration", u"functionDefinition", u"preprocessorDirective" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Auto=3
    Break=4
    Case=5
    Char=6
    Const=7
    Continue=8
    Default=9
    Do=10
    Double=11
    Else=12
    Enum=13
    Extern=14
    Float=15
    For=16
    Goto=17
    If=18
    Inline=19
    Int=20
    Long=21
    Register=22
    Restrict=23
    Return=24
    Short=25
    Signed=26
    Sizeof=27
    Static=28
    Struct=29
    Switch=30
    Typedef=31
    Union=32
    Unsigned=33
    Void=34
    Volatile=35
    While=36
    Alignas=37
    Alignof=38
    Atomic=39
    Bool=40
    Complex=41
    Generic=42
    Imaginary=43
    Noreturn=44
    StaticAssert=45
    ThreadLocal=46
    LeftParen=47
    RightParen=48
    LeftBracket=49
    RightBracket=50
    LeftBrace=51
    RightBrace=52
    Less=53
    LessEqual=54
    Greater=55
    GreaterEqual=56
    LeftShift=57
    RightShift=58
    Plus=59
    PlusPlus=60
    Minus=61
    MinusMinus=62
    Star=63
    Div=64
    Mod=65
    And=66
    Or=67
    AndAnd=68
    OrOr=69
    Caret=70
    Not=71
    Tilde=72
    Question=73
    Colon=74
    Semi=75
    Comma=76
    Assign=77
    StarAssign=78
    DivAssign=79
    ModAssign=80
    PlusAssign=81
    MinusAssign=82
    LeftShiftAssign=83
    RightShiftAssign=84
    AndAssign=85
    XorAssign=86
    OrAssign=87
    Equal=88
    NotEqual=89
    Arrow=90
    Dot=91
    Ellipsis=92
    Identifier=93
    Constant=94
    StringLiteral=95
    LineDirective=96
    PragmaDirective=97
    IncludeDirective=98
    DefineDirective=99
    Whitespace=100
    Newline=101
    BlockComment=102
    LineComment=103

    def __init__(self, input):
        super(CParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class UnaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.UnaryExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_unaryExpression

     
        def copyFrom(self, ctx):
            super(CParser.UnaryExpressionContext, self).copyFrom(ctx)


    class FunctionExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.FunctionExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)

        def argumentExpressionList(self):
            return self.getTypedRuleContext(CParser.ArgumentExpressionListContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitFunctionExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitFunctionExpression(self)
            else:
                return visitor.visitChildren(self)


    class DotExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.DotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDotExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDotExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.ParenthesizedExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.LiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Constant(self):
            return self.getToken(CParser.Constant, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitLiteralExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class PostIncrementExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.PostIncrementExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterPostIncrementExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitPostIncrementExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitPostIncrementExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArrowExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.ArrowExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterArrowExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitArrowExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitArrowExpression(self)
            else:
                return visitor.visitChildren(self)


    class IndexExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.IndexExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIndexExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIndexExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIndexExpression(self)
            else:
                return visitor.visitChildren(self)


    class SizeOfTypeExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.SizeOfTypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterSizeOfTypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitSizeOfTypeExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitSizeOfTypeExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.IdentifierExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryOperatorExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.UnaryOperatorExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def castExpression(self):
            return self.getTypedRuleContext(CParser.CastExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterUnaryOperatorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitUnaryOperatorExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitUnaryOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class AlignOfTypeExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.AlignOfTypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAlignOfTypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAlignOfTypeExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAlignOfTypeExpression(self)
            else:
                return visitor.visitChildren(self)


    class SizeOfExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.SizeOfExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterSizeOfExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitSizeOfExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitSizeOfExpression(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.StringLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def StringLiteral(self, i=None):
            if i is None:
                return self.getTokens(CParser.StringLiteral)
            else:
                return self.getToken(CParser.StringLiteral, i)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStringLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStringLiteralExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStringLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class PreIncrementExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.PreIncrementExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterPreIncrementExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitPreIncrementExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitPreIncrementExpression(self)
            else:
                return visitor.visitChildren(self)



    def unaryExpression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.UnaryExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_unaryExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CParser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 113
                _la = self._input.LA(1)
                if not(_la==CParser.PlusPlus or _la==CParser.MinusMinus):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 114
                self.unaryExpression(5)
                pass

            elif la_ == 2:
                localctx = CParser.SizeOfExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(CParser.Sizeof)
                self.state = 116
                self.unaryExpression(3)
                pass

            elif la_ == 3:
                localctx = CParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.match(CParser.Identifier)
                pass

            elif la_ == 4:
                localctx = CParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(CParser.Constant)
                pass

            elif la_ == 5:
                localctx = CParser.StringLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 119
                        self.match(CParser.StringLiteral)

                    else:
                        raise NoViableAltException(self)
                    self.state = 122 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass

            elif la_ == 6:
                localctx = CParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(CParser.LeftParen)
                self.state = 125
                self.expression()
                self.state = 126
                self.match(CParser.RightParen)
                pass

            elif la_ == 7:
                localctx = CParser.UnaryOperatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                _la = self._input.LA(1)
                if not(((((_la - 59)) & ~0x3f) == 0 and ((1 << (_la - 59)) & ((1 << (CParser.Plus - 59)) | (1 << (CParser.Minus - 59)) | (1 << (CParser.Star - 59)) | (1 << (CParser.And - 59)) | (1 << (CParser.Not - 59)) | (1 << (CParser.Tilde - 59)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 129
                self.castExpression()
                pass

            elif la_ == 8:
                localctx = CParser.SizeOfTypeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(CParser.Sizeof)
                self.state = 131
                self.match(CParser.LeftParen)
                self.state = 132
                self.typeName()
                self.state = 133
                self.match(CParser.RightParen)
                pass

            elif la_ == 9:
                localctx = CParser.AlignOfTypeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(CParser.Alignof)
                self.state = 136
                self.match(CParser.LeftParen)
                self.state = 137
                self.typeName()
                self.state = 138
                self.match(CParser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 161
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CParser.IndexExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 142
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 143
                        self.match(CParser.LeftBracket)
                        self.state = 144
                        self.expression()
                        self.state = 145
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.FunctionExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 147
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 148
                        self.match(CParser.LeftParen)
                        self.state = 150
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                            self.state = 149
                            self.argumentExpressionList()


                        self.state = 152
                        self.match(CParser.RightParen)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DotExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 153
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 154
                        self.match(CParser.Dot)
                        self.state = 155
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ArrowExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 156
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 157
                        self.match(CParser.Arrow)
                        self.state = 158
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 5:
                        localctx = CParser.PostIncrementExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 159
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 160
                        _la = self._input.LA(1)
                        if not(_la==CParser.PlusPlus or _la==CParser.MinusMinus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        pass

             
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArgumentExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ArgumentExpressionListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.AssignmentExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.AssignmentExpressionContext,i)


        def getRuleIndex(self):
            return CParser.RULE_argumentExpressionList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterArgumentExpressionList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitArgumentExpressionList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitArgumentExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def argumentExpressionList(self):

        localctx = CParser.ArgumentExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_argumentExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.assignmentExpression()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 167
                self.match(CParser.Comma)
                self.state = 168
                self.assignmentExpression()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CastExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.CastExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def castExpression(self):
            return self.getTypedRuleContext(CParser.CastExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_castExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitCastExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitCastExpression(self)
            else:
                return visitor.visitChildren(self)




    def castExpression(self):

        localctx = CParser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_castExpression)
        try:
            self.state = 180
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.unaryExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(CParser.LeftParen)
                self.state = 176
                self.typeName()
                self.state = 177
                self.match(CParser.RightParen)
                self.state = 178
                self.castExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LogicalOrExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.LogicalOrExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def castExpression(self):
            return self.getTypedRuleContext(CParser.CastExpressionContext,0)


        def logicalOrExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.LogicalOrExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.LogicalOrExpressionContext,i)


        def getRuleIndex(self):
            return CParser.RULE_logicalOrExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)



    def logicalOrExpression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.LogicalOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_logicalOrExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.castExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 215
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 185
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 186
                        _la = self._input.LA(1)
                        if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (CParser.Star - 63)) | (1 << (CParser.Div - 63)) | (1 << (CParser.Mod - 63)))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 187
                        self.logicalOrExpression(11)
                        pass

                    elif la_ == 2:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 188
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 189
                        _la = self._input.LA(1)
                        if not(_la==CParser.Plus or _la==CParser.Minus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 190
                        self.logicalOrExpression(10)
                        pass

                    elif la_ == 3:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 191
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 192
                        _la = self._input.LA(1)
                        if not(_la==CParser.LeftShift or _la==CParser.RightShift):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 193
                        self.logicalOrExpression(9)
                        pass

                    elif la_ == 4:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 194
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 195
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Less) | (1 << CParser.LessEqual) | (1 << CParser.Greater) | (1 << CParser.GreaterEqual))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 196
                        self.logicalOrExpression(8)
                        pass

                    elif la_ == 5:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 197
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 198
                        _la = self._input.LA(1)
                        if not(_la==CParser.Equal or _la==CParser.NotEqual):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 199
                        self.logicalOrExpression(7)
                        pass

                    elif la_ == 6:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 200
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 201
                        self.match(CParser.And)
                        self.state = 202
                        self.logicalOrExpression(6)
                        pass

                    elif la_ == 7:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 203
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 204
                        self.match(CParser.Caret)
                        self.state = 205
                        self.logicalOrExpression(5)
                        pass

                    elif la_ == 8:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 206
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 207
                        self.match(CParser.Or)
                        self.state = 208
                        self.logicalOrExpression(4)
                        pass

                    elif la_ == 9:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 209
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 210
                        self.match(CParser.AndAnd)
                        self.state = 211
                        self.logicalOrExpression(3)
                        pass

                    elif la_ == 10:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 212
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 213
                        self.match(CParser.OrOr)
                        self.state = 214
                        self.logicalOrExpression(2)
                        pass

             
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ConditionalExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ConditionalExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(CParser.LogicalOrExpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def conditionalExpression(self):
            return self.getTypedRuleContext(CParser.ConditionalExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_conditionalExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterConditionalExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitConditionalExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitConditionalExpression(self)
            else:
                return visitor.visitChildren(self)




    def conditionalExpression(self):

        localctx = CParser.ConditionalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditionalExpression)
        try:
            self.state = 227
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.logicalOrExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.logicalOrExpression(0)
                self.state = 222
                self.match(CParser.Question)
                self.state = 223
                self.expression()
                self.state = 224
                self.match(CParser.Colon)
                self.state = 225
                self.conditionalExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.AssignmentExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(CParser.ConditionalExpressionContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(CParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_assignmentExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = CParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignmentExpression)
        self._la = 0 # Token type
        try:
            self.state = 234
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.unaryExpression(0)
                self.state = 231
                _la = self._input.LA(1)
                if not(((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & ((1 << (CParser.Assign - 77)) | (1 << (CParser.StarAssign - 77)) | (1 << (CParser.DivAssign - 77)) | (1 << (CParser.ModAssign - 77)) | (1 << (CParser.PlusAssign - 77)) | (1 << (CParser.MinusAssign - 77)) | (1 << (CParser.LeftShiftAssign - 77)) | (1 << (CParser.RightShiftAssign - 77)) | (1 << (CParser.AndAssign - 77)) | (1 << (CParser.XorAssign - 77)) | (1 << (CParser.OrAssign - 77)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 232
                self.assignmentExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.AssignmentExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.AssignmentExpressionContext,i)


        def getRuleIndex(self):
            return CParser.RULE_expression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.assignmentExpression()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 237
                self.match(CParser.Comma)
                self.state = 238
                self.assignmentExpression()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ConstantExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(CParser.ConditionalExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_constantExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitConstantExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitConstantExpression(self)
            else:
                return visitor.visitChildren(self)




    def constantExpression(self):

        localctx = CParser.ConstantExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constantExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.conditionalExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarationSpecifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationSpecifierContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationSpecifierContext,i)


        def initDeclaratorList(self):
            return self.getTypedRuleContext(CParser.InitDeclaratorListContext,0)


        def staticAssertDeclaration(self):
            return self.getTypedRuleContext(CParser.StaticAssertDeclarationContext,0)


        def getRuleIndex(self):
            return CParser.RULE_declaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = CParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.state = 257
            token = self._input.LA(1)
            if token in [CParser.T__0, CParser.T__1, CParser.Auto, CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Extern, CParser.Float, CParser.Inline, CParser.Int, CParser.Long, CParser.Register, CParser.Restrict, CParser.Short, CParser.Signed, CParser.Static, CParser.Struct, CParser.Typedef, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Volatile, CParser.Alignas, CParser.Atomic, CParser.Bool, CParser.Complex, CParser.Noreturn, CParser.ThreadLocal, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 246
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 249 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 252
                _la = self._input.LA(1)
                if _la==CParser.Star or _la==CParser.Identifier:
                    self.state = 251
                    self.initDeclaratorList()


                self.state = 254
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.staticAssertDeclaration()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DeclarationSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def storageClassSpecifier(self):
            return self.getTypedRuleContext(CParser.StorageClassSpecifierContext,0)


        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def typeQualifier(self):
            return self.getTypedRuleContext(CParser.TypeQualifierContext,0)


        def functionSpecifier(self):
            return self.getTypedRuleContext(CParser.FunctionSpecifierContext,0)


        def alignmentSpecifier(self):
            return self.getTypedRuleContext(CParser.AlignmentSpecifierContext,0)


        def getRuleIndex(self):
            return CParser.RULE_declarationSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDeclarationSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDeclarationSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDeclarationSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def declarationSpecifier(self):

        localctx = CParser.DeclarationSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declarationSpecifier)
        try:
            self.state = 264
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.storageClassSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.typeSpecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
                self.typeQualifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.functionSpecifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 263
                self.alignmentSpecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitDeclaratorListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.InitDeclaratorListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def initDeclarator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.InitDeclaratorContext)
            else:
                return self.getTypedRuleContext(CParser.InitDeclaratorContext,i)


        def getRuleIndex(self):
            return CParser.RULE_initDeclaratorList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterInitDeclaratorList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitInitDeclaratorList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitInitDeclaratorList(self)
            else:
                return visitor.visitChildren(self)




    def initDeclaratorList(self):

        localctx = CParser.InitDeclaratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_initDeclaratorList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.initDeclarator()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 267
                self.match(CParser.Comma)
                self.state = 268
                self.initDeclarator()
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.InitDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CParser.DeclaratorContext,0)


        def initializer(self):
            return self.getTypedRuleContext(CParser.InitializerContext,0)


        def getRuleIndex(self):
            return CParser.RULE_initDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterInitDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitInitDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitInitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def initDeclarator(self):

        localctx = CParser.InitDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_initDeclarator)
        try:
            self.state = 279
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.declarator()
                self.state = 276
                self.match(CParser.Assign)
                self.state = 277
                self.initializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StorageClassSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StorageClassSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_storageClassSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStorageClassSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStorageClassSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStorageClassSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def storageClassSpecifier(self):

        localctx = CParser.StorageClassSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_storageClassSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Auto) | (1 << CParser.Extern) | (1 << CParser.Register) | (1 << CParser.Static) | (1 << CParser.Typedef) | (1 << CParser.ThreadLocal))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.TypeSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomicTypeSpecifier(self):
            return self.getTypedRuleContext(CParser.AtomicTypeSpecifierContext,0)


        def structOrUnionSpecifier(self):
            return self.getTypedRuleContext(CParser.StructOrUnionSpecifierContext,0)


        def enumSpecifier(self):
            return self.getTypedRuleContext(CParser.EnumSpecifierContext,0)


        def typedefName(self):
            return self.getTypedRuleContext(CParser.TypedefNameContext,0)


        def getRuleIndex(self):
            return CParser.RULE_typeSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = CParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.state = 288
            token = self._input.LA(1)
            if token in [CParser.Char, CParser.Double, CParser.Float, CParser.Int, CParser.Long, CParser.Short, CParser.Signed, CParser.Unsigned, CParser.Void, CParser.Bool, CParser.Complex]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Char) | (1 << CParser.Double) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [CParser.Atomic]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.atomicTypeSpecifier()

            elif token in [CParser.Struct, CParser.Union]:
                self.enterOuterAlt(localctx, 3)
                self.state = 285
                self.structOrUnionSpecifier()

            elif token in [CParser.Enum]:
                self.enterOuterAlt(localctx, 4)
                self.state = 286
                self.enumSpecifier()

            elif token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 5)
                self.state = 287
                self.typedefName()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructOrUnionSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructOrUnionSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def structOrUnion(self):
            return self.getTypedRuleContext(CParser.StructOrUnionContext,0)


        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def structDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StructDeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.StructDeclarationContext,i)


        def getRuleIndex(self):
            return CParser.RULE_structOrUnionSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructOrUnionSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructOrUnionSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructOrUnionSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def structOrUnionSpecifier(self):

        localctx = CParser.StructOrUnionSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structOrUnionSpecifier)
        self._la = 0 # Token type
        try:
            self.state = 305
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.structOrUnion()
                self.state = 292
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 291
                    self.match(CParser.Identifier)


                self.state = 294
                self.match(CParser.LeftBrace)
                self.state = 296 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 295
                    self.structDeclaration()
                    self.state = 298 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Struct) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.StaticAssert))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 300
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.structOrUnion()
                self.state = 303
                self.match(CParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructOrUnionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructOrUnionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_structOrUnion

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructOrUnion(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructOrUnion(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructOrUnion(self)
            else:
                return visitor.visitChildren(self)




    def structOrUnion(self):

        localctx = CParser.StructOrUnionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_structOrUnion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            _la = self._input.LA(1)
            if not(_la==CParser.Struct or _la==CParser.Union):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def specifierQualifierList(self):
            return self.getTypedRuleContext(CParser.SpecifierQualifierListContext,0)


        def structDeclaratorList(self):
            return self.getTypedRuleContext(CParser.StructDeclaratorListContext,0)


        def staticAssertDeclaration(self):
            return self.getTypedRuleContext(CParser.StaticAssertDeclarationContext,0)


        def getRuleIndex(self):
            return CParser.RULE_structDeclaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def structDeclaration(self):

        localctx = CParser.StructDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_structDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 316
            token = self._input.LA(1)
            if token in [CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Float, CParser.Int, CParser.Long, CParser.Restrict, CParser.Short, CParser.Signed, CParser.Struct, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Volatile, CParser.Atomic, CParser.Bool, CParser.Complex, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.specifierQualifierList()
                self.state = 311
                _la = self._input.LA(1)
                if ((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (CParser.Star - 63)) | (1 << (CParser.Colon - 63)) | (1 << (CParser.Identifier - 63)))) != 0):
                    self.state = 310
                    self.structDeclaratorList()


                self.state = 313
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.staticAssertDeclaration()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SpecifierQualifierListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.SpecifierQualifierListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def specifierQualifierList(self):
            return self.getTypedRuleContext(CParser.SpecifierQualifierListContext,0)


        def typeQualifier(self):
            return self.getTypedRuleContext(CParser.TypeQualifierContext,0)


        def getRuleIndex(self):
            return CParser.RULE_specifierQualifierList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterSpecifierQualifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitSpecifierQualifierList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitSpecifierQualifierList(self)
            else:
                return visitor.visitChildren(self)




    def specifierQualifierList(self):

        localctx = CParser.SpecifierQualifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_specifierQualifierList)
        try:
            self.state = 326
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.typeSpecifier()
                self.state = 320
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 319
                    self.specifierQualifierList()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.typeQualifier()
                self.state = 324
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 323
                    self.specifierQualifierList()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructDeclaratorListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructDeclaratorListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def structDeclarator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StructDeclaratorContext)
            else:
                return self.getTypedRuleContext(CParser.StructDeclaratorContext,i)


        def getRuleIndex(self):
            return CParser.RULE_structDeclaratorList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructDeclaratorList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructDeclaratorList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructDeclaratorList(self)
            else:
                return visitor.visitChildren(self)




    def structDeclaratorList(self):

        localctx = CParser.StructDeclaratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_structDeclaratorList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.structDeclarator()
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 329
                self.match(CParser.Comma)
                self.state = 330
                self.structDeclarator()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CParser.DeclaratorContext,0)


        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_structDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def structDeclarator(self):

        localctx = CParser.StructDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_structDeclarator)
        self._la = 0 # Token type
        try:
            self.state = 342
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                _la = self._input.LA(1)
                if _la==CParser.Star or _la==CParser.Identifier:
                    self.state = 337
                    self.declarator()


                self.state = 340
                self.match(CParser.Colon)
                self.state = 341
                self.constantExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.EnumSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enumeratorList(self):
            return self.getTypedRuleContext(CParser.EnumeratorListContext,0)


        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def getRuleIndex(self):
            return CParser.RULE_enumSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterEnumSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitEnumSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitEnumSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def enumSpecifier(self):

        localctx = CParser.EnumSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_enumSpecifier)
        self._la = 0 # Token type
        try:
            self.state = 363
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(CParser.Enum)
                self.state = 346
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 345
                    self.match(CParser.Identifier)


                self.state = 348
                self.match(CParser.LeftBrace)
                self.state = 349
                self.enumeratorList()
                self.state = 350
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.match(CParser.Enum)
                self.state = 354
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 353
                    self.match(CParser.Identifier)


                self.state = 356
                self.match(CParser.LeftBrace)
                self.state = 357
                self.enumeratorList()
                self.state = 358
                self.match(CParser.Comma)
                self.state = 359
                self.match(CParser.RightBrace)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.match(CParser.Enum)
                self.state = 362
                self.match(CParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumeratorListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.EnumeratorListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enumerator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.EnumeratorContext)
            else:
                return self.getTypedRuleContext(CParser.EnumeratorContext,i)


        def getRuleIndex(self):
            return CParser.RULE_enumeratorList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterEnumeratorList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitEnumeratorList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitEnumeratorList(self)
            else:
                return visitor.visitChildren(self)




    def enumeratorList(self):

        localctx = CParser.EnumeratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_enumeratorList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.enumerator()
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 366
                    self.match(CParser.Comma)
                    self.state = 367
                    self.enumerator() 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumeratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.EnumeratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_enumerator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterEnumerator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitEnumerator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitEnumerator(self)
            else:
                return visitor.visitChildren(self)




    def enumerator(self):

        localctx = CParser.EnumeratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_enumerator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(CParser.Identifier)
            self.state = 376
            _la = self._input.LA(1)
            if _la==CParser.Assign:
                self.state = 374
                self.match(CParser.Assign)
                self.state = 375
                self.constantExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomicTypeSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.AtomicTypeSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def getRuleIndex(self):
            return CParser.RULE_atomicTypeSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAtomicTypeSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAtomicTypeSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAtomicTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def atomicTypeSpecifier(self):

        localctx = CParser.AtomicTypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_atomicTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(CParser.Atomic)
            self.state = 379
            self.match(CParser.LeftParen)
            self.state = 380
            self.typeName()
            self.state = 381
            self.match(CParser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeQualifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.TypeQualifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_typeQualifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterTypeQualifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitTypeQualifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitTypeQualifier(self)
            else:
                return visitor.visitChildren(self)




    def typeQualifier(self):

        localctx = CParser.TypeQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeQualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.FunctionSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def getRuleIndex(self):
            return CParser.RULE_functionSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterFunctionSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitFunctionSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitFunctionSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def functionSpecifier(self):

        localctx = CParser.FunctionSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionSpecifier)
        self._la = 0 # Token type
        try:
            self.state = 390
            token = self._input.LA(1)
            if token in [CParser.T__0, CParser.Inline, CParser.Noreturn]:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.Inline) | (1 << CParser.Noreturn))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [CParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.match(CParser.T__1)
                self.state = 387
                self.match(CParser.LeftParen)
                self.state = 388
                self.match(CParser.Identifier)
                self.state = 389
                self.match(CParser.RightParen)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlignmentSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.AlignmentSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_alignmentSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAlignmentSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAlignmentSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAlignmentSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def alignmentSpecifier(self):

        localctx = CParser.AlignmentSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_alignmentSpecifier)
        try:
            self.state = 402
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(CParser.Alignas)
                self.state = 393
                self.match(CParser.LeftParen)
                self.state = 394
                self.typeName()
                self.state = 395
                self.match(CParser.RightParen)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.match(CParser.Alignas)
                self.state = 398
                self.match(CParser.LeftParen)
                self.state = 399
                self.constantExpression()
                self.state = 400
                self.match(CParser.RightParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def directDeclarator(self):
            return self.getTypedRuleContext(CParser.DirectDeclaratorContext,0)


        def pointer(self):
            return self.getTypedRuleContext(CParser.PointerContext,0)


        def getRuleIndex(self):
            return CParser.RULE_declarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def declarator(self):

        localctx = CParser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 404
                self.pointer()


            self.state = 407
            self.directDeclarator(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirectDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DirectDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def directDeclarator(self):
            return self.getTypedRuleContext(CParser.DirectDeclaratorContext,0)


        def typeQualifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.TypeQualifierContext)
            else:
                return self.getTypedRuleContext(CParser.TypeQualifierContext,i)


        def assignmentExpression(self):
            return self.getTypedRuleContext(CParser.AssignmentExpressionContext,0)


        def parameterTypeList(self):
            return self.getTypedRuleContext(CParser.ParameterTypeListContext,0)


        def identifierList(self):
            return self.getTypedRuleContext(CParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return CParser.RULE_directDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDirectDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDirectDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDirectDeclarator(self)
            else:
                return visitor.visitChildren(self)



    def directDeclarator(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.DirectDeclaratorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_directDeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(CParser.Identifier)
            self._ctx.stop = self._input.LT(-1)
            self.state = 470
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 468
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 412
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 413
                        self.match(CParser.LeftBracket)
                        self.state = 417
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 414
                            self.typeQualifier()
                            self.state = 419
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 421
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                            self.state = 420
                            self.assignmentExpression()


                        self.state = 423
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 424
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 425
                        self.match(CParser.LeftBracket)
                        self.state = 426
                        self.match(CParser.Static)
                        self.state = 430
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 427
                            self.typeQualifier()
                            self.state = 432
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 433
                        self.assignmentExpression()
                        self.state = 434
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 436
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 437
                        self.match(CParser.LeftBracket)
                        self.state = 439 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 438
                            self.typeQualifier()
                            self.state = 441 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                                break

                        self.state = 443
                        self.match(CParser.Static)
                        self.state = 444
                        self.assignmentExpression()
                        self.state = 445
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 4:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 447
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 448
                        self.match(CParser.LeftBracket)
                        self.state = 452
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 449
                            self.typeQualifier()
                            self.state = 454
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 455
                        self.match(CParser.Star)
                        self.state = 456
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 5:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 457
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 458
                        self.match(CParser.LeftParen)
                        self.state = 459
                        self.parameterTypeList()
                        self.state = 460
                        self.match(CParser.RightParen)
                        pass

                    elif la_ == 6:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 462
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 463
                        self.match(CParser.LeftParen)
                        self.state = 465
                        _la = self._input.LA(1)
                        if _la==CParser.Identifier:
                            self.state = 464
                            self.identifierList()


                        self.state = 467
                        self.match(CParser.RightParen)
                        pass

             
                self.state = 472
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class PointerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.PointerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typeQualifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.TypeQualifierContext)
            else:
                return self.getTypedRuleContext(CParser.TypeQualifierContext,i)


        def pointer(self):
            return self.getTypedRuleContext(CParser.PointerContext,0)


        def getRuleIndex(self):
            return CParser.RULE_pointer

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterPointer(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitPointer(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)




    def pointer(self):

        localctx = CParser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(CParser.Star)
            self.state = 477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                self.state = 474
                self.typeQualifier()
                self.state = 479
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 481
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 480
                self.pointer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterTypeListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ParameterTypeListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parameterDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ParameterDeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.ParameterDeclarationContext,i)


        def getRuleIndex(self):
            return CParser.RULE_parameterTypeList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterParameterTypeList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitParameterTypeList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitParameterTypeList(self)
            else:
                return visitor.visitChildren(self)




    def parameterTypeList(self):

        localctx = CParser.ParameterTypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_parameterTypeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.parameterDeclaration()
            self.state = 488
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 484
                    self.match(CParser.Comma)
                    self.state = 485
                    self.parameterDeclaration() 
                self.state = 490
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

            self.state = 493
            _la = self._input.LA(1)
            if _la==CParser.Comma:
                self.state = 491
                self.match(CParser.Comma)
                self.state = 492
                self.match(CParser.Ellipsis)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ParameterDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CParser.DeclaratorContext,0)


        def declarationSpecifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationSpecifierContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationSpecifierContext,i)


        def abstractDeclarator(self):
            return self.getTypedRuleContext(CParser.AbstractDeclaratorContext,0)


        def getRuleIndex(self):
            return CParser.RULE_parameterDeclaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterParameterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitParameterDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitParameterDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def parameterDeclaration(self):

        localctx = CParser.ParameterDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_parameterDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 510
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 495
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 498 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

                self.state = 500
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 502
                    self.declarationSpecifier()
                    self.state = 505 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 508
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.LeftParen) | (1 << CParser.LeftBracket) | (1 << CParser.Star))) != 0):
                    self.state = 507
                    self.abstractDeclarator()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.IdentifierListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i=None):
            if i is None:
                return self.getTokens(CParser.Identifier)
            else:
                return self.getToken(CParser.Identifier, i)

        def getRuleIndex(self):
            return CParser.RULE_identifierList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIdentifierList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = CParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(CParser.Identifier)
            self.state = 517
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 513
                self.match(CParser.Comma)
                self.state = 514
                self.match(CParser.Identifier)
                self.state = 519
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.TypeNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def specifierQualifierList(self):
            return self.getTypedRuleContext(CParser.SpecifierQualifierListContext,0)


        def abstractDeclarator(self):
            return self.getTypedRuleContext(CParser.AbstractDeclaratorContext,0)


        def getRuleIndex(self):
            return CParser.RULE_typeName

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterTypeName(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitTypeName(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)




    def typeName(self):

        localctx = CParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.specifierQualifierList()
            self.state = 522
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.LeftParen) | (1 << CParser.LeftBracket) | (1 << CParser.Star))) != 0):
                self.state = 521
                self.abstractDeclarator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AbstractDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.AbstractDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def pointer(self):
            return self.getTypedRuleContext(CParser.PointerContext,0)


        def directAbstractDeclarator(self):
            return self.getTypedRuleContext(CParser.DirectAbstractDeclaratorContext,0)


        def getRuleIndex(self):
            return CParser.RULE_abstractDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAbstractDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAbstractDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAbstractDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def abstractDeclarator(self):

        localctx = CParser.AbstractDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_abstractDeclarator)
        self._la = 0 # Token type
        try:
            self.state = 529
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.pointer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                _la = self._input.LA(1)
                if _la==CParser.Star:
                    self.state = 525
                    self.pointer()


                self.state = 528
                self.directAbstractDeclarator(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirectAbstractDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DirectAbstractDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstractDeclarator(self):
            return self.getTypedRuleContext(CParser.AbstractDeclaratorContext,0)


        def typeQualifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.TypeQualifierContext)
            else:
                return self.getTypedRuleContext(CParser.TypeQualifierContext,i)


        def assignmentExpression(self):
            return self.getTypedRuleContext(CParser.AssignmentExpressionContext,0)


        def parameterTypeList(self):
            return self.getTypedRuleContext(CParser.ParameterTypeListContext,0)


        def directAbstractDeclarator(self):
            return self.getTypedRuleContext(CParser.DirectAbstractDeclaratorContext,0)


        def getRuleIndex(self):
            return CParser.RULE_directAbstractDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDirectAbstractDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDirectAbstractDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDirectAbstractDeclarator(self)
            else:
                return visitor.visitChildren(self)



    def directAbstractDeclarator(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.DirectAbstractDeclaratorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_directAbstractDeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 532
                self.match(CParser.LeftParen)
                self.state = 533
                self.abstractDeclarator()
                self.state = 534
                self.match(CParser.RightParen)
                pass

            elif la_ == 2:
                self.state = 536
                self.match(CParser.LeftBracket)
                self.state = 540
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 537
                    self.typeQualifier()
                    self.state = 542
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 544
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 543
                    self.assignmentExpression()


                self.state = 546
                self.match(CParser.RightBracket)
                pass

            elif la_ == 3:
                self.state = 547
                self.match(CParser.LeftBracket)
                self.state = 548
                self.match(CParser.Static)
                self.state = 552
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 549
                    self.typeQualifier()
                    self.state = 554
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 555
                self.assignmentExpression()
                self.state = 556
                self.match(CParser.RightBracket)
                pass

            elif la_ == 4:
                self.state = 558
                self.match(CParser.LeftBracket)
                self.state = 562
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 559
                    self.typeQualifier()
                    self.state = 564
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 565
                self.match(CParser.Static)
                self.state = 566
                self.assignmentExpression()
                self.state = 567
                self.match(CParser.RightBracket)
                pass

            elif la_ == 5:
                self.state = 569
                self.match(CParser.LeftBracket)
                self.state = 570
                self.match(CParser.Star)
                self.state = 571
                self.match(CParser.RightBracket)
                pass

            elif la_ == 6:
                self.state = 572
                self.match(CParser.LeftParen)
                self.state = 574
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                    self.state = 573
                    self.parameterTypeList()


                self.state = 576
                self.match(CParser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 626
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 624
                    la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                    if la_ == 1:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 579
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 580
                        self.match(CParser.LeftBracket)
                        self.state = 584
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 581
                            self.typeQualifier()
                            self.state = 586
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 588
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                            self.state = 587
                            self.assignmentExpression()


                        self.state = 590
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 591
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 592
                        self.match(CParser.LeftBracket)
                        self.state = 593
                        self.match(CParser.Static)
                        self.state = 597
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 594
                            self.typeQualifier()
                            self.state = 599
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 600
                        self.assignmentExpression()
                        self.state = 601
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 603
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 604
                        self.match(CParser.LeftBracket)
                        self.state = 606 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 605
                            self.typeQualifier()
                            self.state = 608 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                                break

                        self.state = 610
                        self.match(CParser.Static)
                        self.state = 611
                        self.assignmentExpression()
                        self.state = 612
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 4:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 614
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 615
                        self.match(CParser.LeftBracket)
                        self.state = 616
                        self.match(CParser.Star)
                        self.state = 617
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 5:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 618
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 619
                        self.match(CParser.LeftParen)
                        self.state = 621
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                            self.state = 620
                            self.parameterTypeList()


                        self.state = 623
                        self.match(CParser.RightParen)
                        pass

             
                self.state = 628
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TypedefNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.TypedefNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def getRuleIndex(self):
            return CParser.RULE_typedefName

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterTypedefName(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitTypedefName(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitTypedefName(self)
            else:
                return visitor.visitChildren(self)




    def typedefName(self):

        localctx = CParser.TypedefNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_typedefName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(CParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.InitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(CParser.AssignmentExpressionContext,0)


        def initializerList(self):
            return self.getTypedRuleContext(CParser.InitializerListContext,0)


        def getRuleIndex(self):
            return CParser.RULE_initializer

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitInitializer(self)
            else:
                return visitor.visitChildren(self)




    def initializer(self):

        localctx = CParser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_initializer)
        self._la = 0 # Token type
        try:
            self.state = 639
            token = self._input.LA(1)
            if token in [CParser.Sizeof, CParser.Alignof, CParser.LeftParen, CParser.Plus, CParser.PlusPlus, CParser.Minus, CParser.MinusMinus, CParser.Star, CParser.And, CParser.Not, CParser.Tilde, CParser.Identifier, CParser.Constant, CParser.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 631
                self.assignmentExpression()

            elif token in [CParser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 632
                self.match(CParser.LeftBrace)
                self.state = 633
                self.initializerList(0)
                self.state = 635
                _la = self._input.LA(1)
                if _la==CParser.Comma:
                    self.state = 634
                    self.match(CParser.Comma)


                self.state = 637
                self.match(CParser.RightBrace)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.InitializerListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def initializer(self):
            return self.getTypedRuleContext(CParser.InitializerContext,0)


        def designation(self):
            return self.getTypedRuleContext(CParser.DesignationContext,0)


        def initializerList(self):
            return self.getTypedRuleContext(CParser.InitializerListContext,0)


        def getRuleIndex(self):
            return CParser.RULE_initializerList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterInitializerList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitInitializerList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitInitializerList(self)
            else:
                return visitor.visitChildren(self)



    def initializerList(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.InitializerListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_initializerList, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            _la = self._input.LA(1)
            if _la==CParser.LeftBracket or _la==CParser.Dot:
                self.state = 642
                self.designation()


            self.state = 645
            self.initializer()
            self._ctx.stop = self._input.LT(-1)
            self.state = 655
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.InitializerListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerList)
                    self.state = 647
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 648
                    self.match(CParser.Comma)
                    self.state = 650
                    _la = self._input.LA(1)
                    if _la==CParser.LeftBracket or _la==CParser.Dot:
                        self.state = 649
                        self.designation()


                    self.state = 652
                    self.initializer() 
                self.state = 657
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,75,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DesignationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DesignationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def designator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DesignatorContext)
            else:
                return self.getTypedRuleContext(CParser.DesignatorContext,i)


        def getRuleIndex(self):
            return CParser.RULE_designation

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDesignation(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDesignation(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDesignation(self)
            else:
                return visitor.visitChildren(self)




    def designation(self):

        localctx = CParser.DesignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_designation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 659 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 658
                self.designator()
                self.state = 661 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.LeftBracket or _la==CParser.Dot):
                    break

            self.state = 663
            self.match(CParser.Assign)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DesignatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DesignatorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def getRuleIndex(self):
            return CParser.RULE_designator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDesignator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDesignator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDesignator(self)
            else:
                return visitor.visitChildren(self)




    def designator(self):

        localctx = CParser.DesignatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_designator)
        try:
            self.state = 671
            token = self._input.LA(1)
            if token in [CParser.LeftBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 665
                self.match(CParser.LeftBracket)
                self.state = 666
                self.constantExpression()
                self.state = 667
                self.match(CParser.RightBracket)

            elif token in [CParser.Dot]:
                self.enterOuterAlt(localctx, 2)
                self.state = 669
                self.match(CParser.Dot)
                self.state = 670
                self.match(CParser.Identifier)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StaticAssertDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StaticAssertDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def StringLiteral(self, i=None):
            if i is None:
                return self.getTokens(CParser.StringLiteral)
            else:
                return self.getToken(CParser.StringLiteral, i)

        def getRuleIndex(self):
            return CParser.RULE_staticAssertDeclaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStaticAssertDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStaticAssertDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStaticAssertDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def staticAssertDeclaration(self):

        localctx = CParser.StaticAssertDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_staticAssertDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
            self.match(CParser.StaticAssert)
            self.state = 674
            self.match(CParser.LeftParen)
            self.state = 675
            self.constantExpression()
            self.state = 676
            self.match(CParser.Comma)
            self.state = 678 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 677
                self.match(CParser.StringLiteral)
                self.state = 680 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.StringLiteral):
                    break

            self.state = 682
            self.match(CParser.RightParen)
            self.state = 683
            self.match(CParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def labeledStatement(self):
            return self.getTypedRuleContext(CParser.LabeledStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(CParser.CompoundStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(CParser.ExpressionStatementContext,0)


        def selectionStatement(self):
            return self.getTypedRuleContext(CParser.SelectionStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(CParser.IterationStatementContext,0)


        def jumpStatement(self):
            return self.getTypedRuleContext(CParser.JumpStatementContext,0)


        def getRuleIndex(self):
            return CParser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_statement)
        try:
            self.state = 691
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 685
                self.labeledStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 686
                self.compoundStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 687
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 688
                self.selectionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 689
                self.iterationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 690
                self.jumpStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabeledStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.LabeledStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_labeledStatement

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterLabeledStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitLabeledStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitLabeledStatement(self)
            else:
                return visitor.visitChildren(self)




    def labeledStatement(self):

        localctx = CParser.LabeledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_labeledStatement)
        try:
            self.state = 704
            token = self._input.LA(1)
            if token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 693
                self.match(CParser.Identifier)
                self.state = 694
                self.match(CParser.Colon)
                self.state = 695
                self.statement()

            elif token in [CParser.Case]:
                self.enterOuterAlt(localctx, 2)
                self.state = 696
                self.match(CParser.Case)
                self.state = 697
                self.constantExpression()
                self.state = 698
                self.match(CParser.Colon)
                self.state = 699
                self.statement()

            elif token in [CParser.Default]:
                self.enterOuterAlt(localctx, 3)
                self.state = 701
                self.match(CParser.Default)
                self.state = 702
                self.match(CParser.Colon)
                self.state = 703
                self.statement()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompoundStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.CompoundStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def blockItem(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.BlockItemContext)
            else:
                return self.getTypedRuleContext(CParser.BlockItemContext,i)


        def getRuleIndex(self):
            return CParser.RULE_compoundStatement

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitCompoundStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitCompoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundStatement(self):

        localctx = CParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(CParser.LeftBrace)
            self.state = 710
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Break) | (1 << CParser.Case) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Continue) | (1 << CParser.Default) | (1 << CParser.Do) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.For) | (1 << CParser.Goto) | (1 << CParser.If) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Return) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Sizeof) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Switch) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.While) | (1 << CParser.Alignas) | (1 << CParser.Alignof) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal) | (1 << CParser.LeftParen) | (1 << CParser.LeftBrace) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Semi - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                self.state = 707
                self.blockItem()
                self.state = 712
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 713
            self.match(CParser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockItemContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.BlockItemContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def getRuleIndex(self):
            return CParser.RULE_blockItem

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterBlockItem(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitBlockItem(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitBlockItem(self)
            else:
                return visitor.visitChildren(self)




    def blockItem(self):

        localctx = CParser.BlockItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_blockItem)
        try:
            self.state = 717
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 715
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 716
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ExpressionStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_expressionStatement

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = CParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                self.state = 719
                self.expression()


            self.state = 722
            self.match(CParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SelectionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.SelectionStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_selectionStatement

     
        def copyFrom(self, ctx):
            super(CParser.SelectionStatementContext, self).copyFrom(ctx)



    class IfStatementContext(SelectionStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.SelectionStatementContext)
            super(CParser.IfStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatementContext)
            else:
                return self.getTypedRuleContext(CParser.StatementContext,i)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIfStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)


    class SwitchStatementContext(SelectionStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.SelectionStatementContext)
            super(CParser.SwitchStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)



    def selectionStatement(self):

        localctx = CParser.SelectionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_selectionStatement)
        try:
            self.state = 739
            token = self._input.LA(1)
            if token in [CParser.If]:
                localctx = CParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 724
                self.match(CParser.If)
                self.state = 725
                self.match(CParser.LeftParen)
                self.state = 726
                self.expression()
                self.state = 727
                self.match(CParser.RightParen)
                self.state = 728
                self.statement()
                self.state = 731
                la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
                if la_ == 1:
                    self.state = 729
                    self.match(CParser.Else)
                    self.state = 730
                    self.statement()



            elif token in [CParser.Switch]:
                localctx = CParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 733
                self.match(CParser.Switch)
                self.state = 734
                self.match(CParser.LeftParen)
                self.state = 735
                self.expression()
                self.state = 736
                self.match(CParser.RightParen)
                self.state = 737
                self.statement()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.InitExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_initExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterInitExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitInitExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitInitExpression(self)
            else:
                return visitor.visitChildren(self)




    def initExpression(self):

        localctx = CParser.InitExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_initExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.IterationExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_iterationExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIterationExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIterationExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIterationExpression(self)
            else:
                return visitor.visitChildren(self)




    def iterationExpression(self):

        localctx = CParser.IterationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_iterationExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.IterationStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_iterationStatement

     
        def copyFrom(self, ctx):
            super(CParser.IterationStatementContext, self).copyFrom(ctx)



    class DeclForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.IterationStatementContext)
            super(CParser.DeclForStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)

        def iterationExpression(self):
            return self.getTypedRuleContext(CParser.IterationExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDeclForStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDeclForStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDeclForStatement(self)
            else:
                return visitor.visitChildren(self)


    class DoWhileStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.IterationStatementContext)
            super(CParser.DoWhileStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDoWhileStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDoWhileStatement(self)
            else:
                return visitor.visitChildren(self)


    class ForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.IterationStatementContext)
            super(CParser.ForStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)

        def initExpression(self):
            return self.getTypedRuleContext(CParser.InitExpressionContext,0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)

        def iterationExpression(self):
            return self.getTypedRuleContext(CParser.IterationExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterForStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitForStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.IterationStatementContext)
            super(CParser.WhileStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitWhileStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)



    def iterationStatement(self):

        localctx = CParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 787
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                localctx = CParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 745
                self.match(CParser.While)
                self.state = 746
                self.match(CParser.LeftParen)
                self.state = 747
                self.expression()
                self.state = 748
                self.match(CParser.RightParen)
                self.state = 749
                self.statement()
                pass

            elif la_ == 2:
                localctx = CParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 751
                self.match(CParser.Do)
                self.state = 752
                self.statement()
                self.state = 753
                self.match(CParser.While)
                self.state = 754
                self.match(CParser.LeftParen)
                self.state = 755
                self.expression()
                self.state = 756
                self.match(CParser.RightParen)
                self.state = 757
                self.match(CParser.Semi)
                pass

            elif la_ == 3:
                localctx = CParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 759
                self.match(CParser.For)
                self.state = 760
                self.match(CParser.LeftParen)
                self.state = 762
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 761
                    self.initExpression()


                self.state = 764
                self.match(CParser.Semi)
                self.state = 766
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 765
                    self.expression()


                self.state = 768
                self.match(CParser.Semi)
                self.state = 770
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 769
                    self.iterationExpression()


                self.state = 772
                self.match(CParser.RightParen)
                self.state = 773
                self.statement()
                pass

            elif la_ == 4:
                localctx = CParser.DeclForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 774
                self.match(CParser.For)
                self.state = 775
                self.match(CParser.LeftParen)
                self.state = 776
                self.declaration()
                self.state = 778
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 777
                    self.expression()


                self.state = 780
                self.match(CParser.Semi)
                self.state = 782
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 781
                    self.iterationExpression()


                self.state = 784
                self.match(CParser.RightParen)
                self.state = 785
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JumpStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.JumpStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_jumpStatement

     
        def copyFrom(self, ctx):
            super(CParser.JumpStatementContext, self).copyFrom(ctx)



    class ContinueStatementContext(JumpStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.JumpStatementContext)
            super(CParser.ContinueStatementContext, self).__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitContinueStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)


    class GotoStatementContext(JumpStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.JumpStatementContext)
            super(CParser.GotoStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterGotoStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitGotoStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitGotoStatement(self)
            else:
                return visitor.visitChildren(self)


    class ReturnStatementContext(JumpStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.JumpStatementContext)
            super(CParser.ReturnStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitReturnStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)


    class BreakStatementContext(JumpStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.JumpStatementContext)
            super(CParser.BreakStatementContext, self).__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitBreakStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)



    def jumpStatement(self):

        localctx = CParser.JumpStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_jumpStatement)
        self._la = 0 # Token type
        try:
            self.state = 801
            token = self._input.LA(1)
            if token in [CParser.Goto]:
                localctx = CParser.GotoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 789
                self.match(CParser.Goto)
                self.state = 790
                self.match(CParser.Identifier)
                self.state = 791
                self.match(CParser.Semi)

            elif token in [CParser.Continue]:
                localctx = CParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 792
                self.match(CParser.Continue)
                self.state = 793
                self.match(CParser.Semi)

            elif token in [CParser.Break]:
                localctx = CParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 794
                self.match(CParser.Break)
                self.state = 795
                self.match(CParser.Semi)

            elif token in [CParser.Return]:
                localctx = CParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 796
                self.match(CParser.Return)
                self.state = 798
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.Constant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 797
                    self.expression()


                self.state = 800
                self.match(CParser.Semi)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompilationUnitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.CompilationUnitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CParser.EOF, 0)

        def externalDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExternalDeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.ExternalDeclarationContext,i)


        def getRuleIndex(self):
            return CParser.RULE_compilationUnit

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitCompilationUnit(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = CParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 806
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal) | (1 << CParser.Star))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CParser.Semi - 75)) | (1 << (CParser.Identifier - 75)) | (1 << (CParser.LineDirective - 75)) | (1 << (CParser.PragmaDirective - 75)) | (1 << (CParser.IncludeDirective - 75)) | (1 << (CParser.DefineDirective - 75)))) != 0):
                self.state = 803
                self.externalDeclaration()
                self.state = 808
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 809
            self.match(CParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExternalDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ExternalDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def functionDefinition(self):
            return self.getTypedRuleContext(CParser.FunctionDefinitionContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def preprocessorDirective(self):
            return self.getTypedRuleContext(CParser.PreprocessorDirectiveContext,0)


        def getRuleIndex(self):
            return CParser.RULE_externalDeclaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterExternalDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitExternalDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitExternalDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def externalDeclaration(self):

        localctx = CParser.ExternalDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_externalDeclaration)
        try:
            self.state = 815
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 811
                self.functionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 812
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 813
                self.preprocessorDirective()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 814
                self.match(CParser.Semi)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.FunctionDefinitionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CParser.DeclaratorContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(CParser.CompoundStatementContext,0)


        def declarationSpecifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationSpecifierContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationSpecifierContext,i)


        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationContext,i)


        def getRuleIndex(self):
            return CParser.RULE_functionDefinition

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = CParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 820
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,96,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 817
                    self.declarationSpecifier() 
                self.state = 822
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,96,self._ctx)

            self.state = 823
            self.declarator()
            self.state = 827
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                self.state = 824
                self.declaration()
                self.state = 829
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 830
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PreprocessorDirectiveContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.PreprocessorDirectiveContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LineDirective(self):
            return self.getToken(CParser.LineDirective, 0)

        def PragmaDirective(self):
            return self.getToken(CParser.PragmaDirective, 0)

        def IncludeDirective(self):
            return self.getToken(CParser.IncludeDirective, 0)

        def DefineDirective(self):
            return self.getToken(CParser.DefineDirective, 0)

        def getRuleIndex(self):
            return CParser.RULE_preprocessorDirective

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterPreprocessorDirective(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitPreprocessorDirective(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitPreprocessorDirective(self)
            else:
                return visitor.visitChildren(self)




    def preprocessorDirective(self):

        localctx = CParser.PreprocessorDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_preprocessorDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 832
            _la = self._input.LA(1)
            if not(((((_la - 96)) & ~0x3f) == 0 and ((1 << (_la - 96)) & ((1 << (CParser.LineDirective - 96)) | (1 << (CParser.PragmaDirective - 96)) | (1 << (CParser.IncludeDirective - 96)) | (1 << (CParser.DefineDirective - 96)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.unaryExpression_sempred
        self._predicates[3] = self.logicalOrExpression_sempred
        self._predicates[28] = self.directDeclarator_sempred
        self._predicates[35] = self.directAbstractDeclarator_sempred
        self._predicates[38] = self.initializerList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unaryExpression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

    def logicalOrExpression_sempred(self, localctx, predIndex):
            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 1)
         

    def directDeclarator_sempred(self, localctx, predIndex):
            if predIndex == 15:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 1)
         

    def directAbstractDeclarator_sempred(self, localctx, predIndex):
            if predIndex == 21:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 25:
                return self.precpred(self._ctx, 1)
         

    def initializerList_sempred(self, localctx, predIndex):
            if predIndex == 26:
                return self.precpred(self._ctx, 1)
         



