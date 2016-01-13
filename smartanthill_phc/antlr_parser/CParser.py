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
        buf.write(u"k\u0347\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\6\2}\n\2")
        buf.write(u"\r\2\16\2~\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\3\2\3\2\5\2\u0091\n\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\5\2\u009b\n\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\7\2\u00a6\n\2\f\2\16\2\u00a9\13\2\3\3")
        buf.write(u"\3\3\3\3\7\3\u00ae\n\3\f\3\16\3\u00b1\13\3\3\4\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\5\4\u00b9\n\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\7\5\u00dc\n\5\f\5\16\5\u00df\13\5\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\5\6\u00e8\n\6\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write(u"\u00ef\n\7\3\b\3\b\3\b\7\b\u00f4\n\b\f\b\16\b\u00f7\13")
        buf.write(u"\b\3\t\3\t\3\n\6\n\u00fc\n\n\r\n\16\n\u00fd\3\n\5\n\u0101")
        buf.write(u"\n\n\3\n\3\n\3\n\5\n\u0106\n\n\3\13\3\13\3\13\3\13\3")
        buf.write(u"\13\5\13\u010d\n\13\3\f\3\f\3\f\7\f\u0112\n\f\f\f\16")
        buf.write(u"\f\u0115\13\f\3\r\3\r\3\r\3\r\3\r\5\r\u011c\n\r\3\16")
        buf.write(u"\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u0125\n\17\3\20\3")
        buf.write(u"\20\5\20\u0129\n\20\3\20\3\20\6\20\u012d\n\20\r\20\16")
        buf.write(u"\20\u012e\3\20\3\20\3\20\3\20\3\20\5\20\u0136\n\20\3")
        buf.write(u"\21\3\21\3\22\3\22\5\22\u013c\n\22\3\22\3\22\3\22\5\22")
        buf.write(u"\u0141\n\22\3\23\3\23\5\23\u0145\n\23\3\23\3\23\5\23")
        buf.write(u"\u0149\n\23\5\23\u014b\n\23\3\24\3\24\3\24\7\24\u0150")
        buf.write(u"\n\24\f\24\16\24\u0153\13\24\3\25\3\25\5\25\u0157\n\25")
        buf.write(u"\3\25\3\25\5\25\u015b\n\25\3\26\3\26\5\26\u015f\n\26")
        buf.write(u"\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0167\n\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\3\26\3\26\5\26\u0170\n\26\3\27\3\27")
        buf.write(u"\3\27\7\27\u0175\n\27\f\27\16\27\u0178\13\27\3\30\3\30")
        buf.write(u"\3\30\5\30\u017d\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3")
        buf.write(u"\32\3\33\3\33\3\33\3\33\3\33\5\33\u018b\n\33\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0197\n")
        buf.write(u"\34\3\35\5\35\u019a\n\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\7\36\u01a4\n\36\f\36\16\36\u01a7\13\36\3\36")
        buf.write(u"\5\36\u01aa\n\36\3\36\3\36\3\36\3\36\3\36\7\36\u01b1")
        buf.write(u"\n\36\f\36\16\36\u01b4\13\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\3\36\6\36\u01bc\n\36\r\36\16\36\u01bd\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\7\36\u01c7\n\36\f\36\16\36\u01ca")
        buf.write(u"\13\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\5\36\u01d6\n\36\3\36\7\36\u01d9\n\36\f\36\16\36\u01dc")
        buf.write(u"\13\36\3\37\3\37\7\37\u01e0\n\37\f\37\16\37\u01e3\13")
        buf.write(u"\37\3\37\5\37\u01e6\n\37\3 \3 \3 \7 \u01eb\n \f \16 ")
        buf.write(u"\u01ee\13 \3 \3 \5 \u01f2\n \3!\6!\u01f5\n!\r!\16!\u01f6")
        buf.write(u"\3!\3!\3!\6!\u01fc\n!\r!\16!\u01fd\3!\5!\u0201\n!\5!")
        buf.write(u"\u0203\n!\3\"\3\"\3\"\7\"\u0208\n\"\f\"\16\"\u020b\13")
        buf.write(u"\"\3#\3#\5#\u020f\n#\3$\3$\5$\u0213\n$\3$\5$\u0216\n")
        buf.write(u"$\3%\3%\3%\3%\3%\3%\3%\7%\u021f\n%\f%\16%\u0222\13%\3")
        buf.write(u"%\5%\u0225\n%\3%\3%\3%\3%\7%\u022b\n%\f%\16%\u022e\13")
        buf.write(u"%\3%\3%\3%\3%\3%\7%\u0235\n%\f%\16%\u0238\13%\3%\3%\3")
        buf.write(u"%\3%\3%\3%\3%\3%\3%\5%\u0243\n%\3%\5%\u0246\n%\3%\3%")
        buf.write(u"\3%\7%\u024b\n%\f%\16%\u024e\13%\3%\5%\u0251\n%\3%\3")
        buf.write(u"%\3%\3%\3%\7%\u0258\n%\f%\16%\u025b\13%\3%\3%\3%\3%\3")
        buf.write(u"%\3%\6%\u0263\n%\r%\16%\u0264\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write(u"%\3%\3%\3%\5%\u0272\n%\3%\7%\u0275\n%\f%\16%\u0278\13")
        buf.write(u"%\3&\3&\3\'\3\'\3\'\3\'\5\'\u0280\n\'\3\'\3\'\5\'\u0284")
        buf.write(u"\n\'\3(\3(\5(\u0288\n(\3(\3(\3(\3(\3(\5(\u028f\n(\3(")
        buf.write(u"\7(\u0292\n(\f(\16(\u0295\13(\3)\6)\u0298\n)\r)\16)\u0299")
        buf.write(u"\3)\3)\3*\3*\3*\3*\3*\3*\5*\u02a4\n*\3+\3+\3+\3+\3+\6")
        buf.write(u"+\u02ab\n+\r+\16+\u02ac\3+\3+\3+\3,\3,\3,\3,\3,\3,\5")
        buf.write(u",\u02b8\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u02c5")
        buf.write(u"\n-\3.\3.\7.\u02c9\n.\f.\16.\u02cc\13.\3.\3.\3/\3/\5")
        buf.write(u"/\u02d2\n/\3\60\5\60\u02d5\n\60\3\60\3\60\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\5\61\u02e0\n\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\5\61\u02e8\n\61\3\62\3\62\3\63\3\63\3")
        buf.write(u"\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u02ff\n\64\3\64\3")
        buf.write(u"\64\5\64\u0303\n\64\3\64\3\64\5\64\u0307\n\64\3\64\3")
        buf.write(u"\64\3\64\3\64\3\64\3\64\5\64\u030f\n\64\3\64\3\64\5\64")
        buf.write(u"\u0313\n\64\3\64\3\64\3\64\5\64\u0318\n\64\3\65\3\65")
        buf.write(u"\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0323\n\65\3")
        buf.write(u"\65\5\65\u0326\n\65\3\66\7\66\u0329\n\66\f\66\16\66\u032c")
        buf.write(u"\13\66\3\66\3\66\3\67\3\67\3\67\3\67\5\67\u0334\n\67")
        buf.write(u"\38\78\u0337\n8\f8\168\u033a\138\38\38\78\u033e\n8\f")
        buf.write(u"8\168\u0341\138\38\38\39\39\39\2\7\2\b:HN:\2\4\6\b\n")
        buf.write(u"\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:")
        buf.write(u"<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\20\4\2>>@@\7\2==??AAD")
        buf.write(u"DIJ\3\2AC\4\2==??\3\2;<\3\2\67:\3\2Z[\3\2OY\b\2\5\5\20")
        buf.write(u"\20\30\30\36\36!!\60\60\t\2\b\b\r\r\21\21\26\27\33\34")
        buf.write(u"#$*+\4\2\37\37\"\"\6\2\t\t\31\31%%))\5\2\3\3\25\25..")
        buf.write(u"\3\2dg\u03a1\2\u0090\3\2\2\2\4\u00aa\3\2\2\2\6\u00b8")
        buf.write(u"\3\2\2\2\b\u00ba\3\2\2\2\n\u00e7\3\2\2\2\f\u00ee\3\2")
        buf.write(u"\2\2\16\u00f0\3\2\2\2\20\u00f8\3\2\2\2\22\u0105\3\2\2")
        buf.write(u"\2\24\u010c\3\2\2\2\26\u010e\3\2\2\2\30\u011b\3\2\2\2")
        buf.write(u"\32\u011d\3\2\2\2\34\u0124\3\2\2\2\36\u0135\3\2\2\2 ")
        buf.write(u"\u0137\3\2\2\2\"\u0140\3\2\2\2$\u014a\3\2\2\2&\u014c")
        buf.write(u"\3\2\2\2(\u015a\3\2\2\2*\u016f\3\2\2\2,\u0171\3\2\2\2")
        buf.write(u".\u0179\3\2\2\2\60\u017e\3\2\2\2\62\u0183\3\2\2\2\64")
        buf.write(u"\u018a\3\2\2\2\66\u0196\3\2\2\28\u0199\3\2\2\2:\u019d")
        buf.write(u"\3\2\2\2<\u01dd\3\2\2\2>\u01e7\3\2\2\2@\u0202\3\2\2\2")
        buf.write(u"B\u0204\3\2\2\2D\u020c\3\2\2\2F\u0215\3\2\2\2H\u0245")
        buf.write(u"\3\2\2\2J\u0279\3\2\2\2L\u0283\3\2\2\2N\u0285\3\2\2\2")
        buf.write(u"P\u0297\3\2\2\2R\u02a3\3\2\2\2T\u02a5\3\2\2\2V\u02b7")
        buf.write(u"\3\2\2\2X\u02c4\3\2\2\2Z\u02c6\3\2\2\2\\\u02d1\3\2\2")
        buf.write(u"\2^\u02d4\3\2\2\2`\u02e7\3\2\2\2b\u02e9\3\2\2\2d\u02eb")
        buf.write(u"\3\2\2\2f\u0317\3\2\2\2h\u0325\3\2\2\2j\u032a\3\2\2\2")
        buf.write(u"l\u0333\3\2\2\2n\u0338\3\2\2\2p\u0344\3\2\2\2rs\b\2\1")
        buf.write(u"\2st\t\2\2\2t\u0091\5\2\2\7uv\7\35\2\2v\u0091\5\2\2\5")
        buf.write(u"w\u0091\7_\2\2x\u0091\7`\2\2y\u0091\7a\2\2z\u0091\7b")
        buf.write(u"\2\2{}\7c\2\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2")
        buf.write(u"\2\2\177\u0091\3\2\2\2\u0080\u0081\7\61\2\2\u0081\u0082")
        buf.write(u"\5\16\b\2\u0082\u0083\7\62\2\2\u0083\u0091\3\2\2\2\u0084")
        buf.write(u"\u0085\t\3\2\2\u0085\u0091\5\6\4\2\u0086\u0087\7\35\2")
        buf.write(u"\2\u0087\u0088\7\61\2\2\u0088\u0089\5D#\2\u0089\u008a")
        buf.write(u"\7\62\2\2\u008a\u0091\3\2\2\2\u008b\u008c\7(\2\2\u008c")
        buf.write(u"\u008d\7\61\2\2\u008d\u008e\5D#\2\u008e\u008f\7\62\2")
        buf.write(u"\2\u008f\u0091\3\2\2\2\u0090r\3\2\2\2\u0090u\3\2\2\2")
        buf.write(u"\u0090w\3\2\2\2\u0090x\3\2\2\2\u0090y\3\2\2\2\u0090z")
        buf.write(u"\3\2\2\2\u0090|\3\2\2\2\u0090\u0080\3\2\2\2\u0090\u0084")
        buf.write(u"\3\2\2\2\u0090\u0086\3\2\2\2\u0090\u008b\3\2\2\2\u0091")
        buf.write(u"\u00a7\3\2\2\2\u0092\u0093\f\f\2\2\u0093\u0094\7\63\2")
        buf.write(u"\2\u0094\u0095\5\16\b\2\u0095\u0096\7\64\2\2\u0096\u00a6")
        buf.write(u"\3\2\2\2\u0097\u0098\f\13\2\2\u0098\u009a\7\61\2\2\u0099")
        buf.write(u"\u009b\5\4\3\2\u009a\u0099\3\2\2\2\u009a\u009b\3\2\2")
        buf.write(u"\2\u009b\u009c\3\2\2\2\u009c\u00a6\7\62\2\2\u009d\u009e")
        buf.write(u"\f\n\2\2\u009e\u009f\7]\2\2\u009f\u00a6\7_\2\2\u00a0")
        buf.write(u"\u00a1\f\t\2\2\u00a1\u00a2\7\\\2\2\u00a2\u00a6\7_\2\2")
        buf.write(u"\u00a3\u00a4\f\b\2\2\u00a4\u00a6\t\2\2\2\u00a5\u0092")
        buf.write(u"\3\2\2\2\u00a5\u0097\3\2\2\2\u00a5\u009d\3\2\2\2\u00a5")
        buf.write(u"\u00a0\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a9\3\2\2")
        buf.write(u"\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\3\3")
        buf.write(u"\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00af\5\f\7\2\u00ab")
        buf.write(u"\u00ac\7N\2\2\u00ac\u00ae\5\f\7\2\u00ad\u00ab\3\2\2\2")
        buf.write(u"\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0")
        buf.write(u"\3\2\2\2\u00b0\5\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b9")
        buf.write(u"\5\2\2\2\u00b3\u00b4\7\61\2\2\u00b4\u00b5\5D#\2\u00b5")
        buf.write(u"\u00b6\7\62\2\2\u00b6\u00b7\5\6\4\2\u00b7\u00b9\3\2\2")
        buf.write(u"\2\u00b8\u00b2\3\2\2\2\u00b8\u00b3\3\2\2\2\u00b9\7\3")
        buf.write(u"\2\2\2\u00ba\u00bb\b\5\1\2\u00bb\u00bc\5\6\4\2\u00bc")
        buf.write(u"\u00dd\3\2\2\2\u00bd\u00be\f\f\2\2\u00be\u00bf\t\4\2")
        buf.write(u"\2\u00bf\u00dc\5\b\5\r\u00c0\u00c1\f\13\2\2\u00c1\u00c2")
        buf.write(u"\t\5\2\2\u00c2\u00dc\5\b\5\f\u00c3\u00c4\f\n\2\2\u00c4")
        buf.write(u"\u00c5\t\6\2\2\u00c5\u00dc\5\b\5\13\u00c6\u00c7\f\t\2")
        buf.write(u"\2\u00c7\u00c8\t\7\2\2\u00c8\u00dc\5\b\5\n\u00c9\u00ca")
        buf.write(u"\f\b\2\2\u00ca\u00cb\t\b\2\2\u00cb\u00dc\5\b\5\t\u00cc")
        buf.write(u"\u00cd\f\7\2\2\u00cd\u00ce\7D\2\2\u00ce\u00dc\5\b\5\b")
        buf.write(u"\u00cf\u00d0\f\6\2\2\u00d0\u00d1\7H\2\2\u00d1\u00dc\5")
        buf.write(u"\b\5\7\u00d2\u00d3\f\5\2\2\u00d3\u00d4\7E\2\2\u00d4\u00dc")
        buf.write(u"\5\b\5\6\u00d5\u00d6\f\4\2\2\u00d6\u00d7\7F\2\2\u00d7")
        buf.write(u"\u00dc\5\b\5\5\u00d8\u00d9\f\3\2\2\u00d9\u00da\7G\2\2")
        buf.write(u"\u00da\u00dc\5\b\5\4\u00db\u00bd\3\2\2\2\u00db\u00c0")
        buf.write(u"\3\2\2\2\u00db\u00c3\3\2\2\2\u00db\u00c6\3\2\2\2\u00db")
        buf.write(u"\u00c9\3\2\2\2\u00db\u00cc\3\2\2\2\u00db\u00cf\3\2\2")
        buf.write(u"\2\u00db\u00d2\3\2\2\2\u00db\u00d5\3\2\2\2\u00db\u00d8")
        buf.write(u"\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write(u"\u00de\3\2\2\2\u00de\t\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0")
        buf.write(u"\u00e8\5\b\5\2\u00e1\u00e2\5\b\5\2\u00e2\u00e3\7K\2\2")
        buf.write(u"\u00e3\u00e4\5\16\b\2\u00e4\u00e5\7L\2\2\u00e5\u00e6")
        buf.write(u"\5\n\6\2\u00e6\u00e8\3\2\2\2\u00e7\u00e0\3\2\2\2\u00e7")
        buf.write(u"\u00e1\3\2\2\2\u00e8\13\3\2\2\2\u00e9\u00ef\5\n\6\2\u00ea")
        buf.write(u"\u00eb\5\2\2\2\u00eb\u00ec\t\t\2\2\u00ec\u00ed\5\f\7")
        buf.write(u"\2\u00ed\u00ef\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ee\u00ea")
        buf.write(u"\3\2\2\2\u00ef\r\3\2\2\2\u00f0\u00f5\5\f\7\2\u00f1\u00f2")
        buf.write(u"\7N\2\2\u00f2\u00f4\5\f\7\2\u00f3\u00f1\3\2\2\2\u00f4")
        buf.write(u"\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2")
        buf.write(u"\2\u00f6\17\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9\5")
        buf.write(u"\n\6\2\u00f9\21\3\2\2\2\u00fa\u00fc\5\24\13\2\u00fb\u00fa")
        buf.write(u"\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd")
        buf.write(u"\u00fe\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff\u0101\5\26\f")
        buf.write(u"\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102")
        buf.write(u"\3\2\2\2\u0102\u0103\7M\2\2\u0103\u0106\3\2\2\2\u0104")
        buf.write(u"\u0106\5T+\2\u0105\u00fb\3\2\2\2\u0105\u0104\3\2\2\2")
        buf.write(u"\u0106\23\3\2\2\2\u0107\u010d\5\32\16\2\u0108\u010d\5")
        buf.write(u"\34\17\2\u0109\u010d\5\62\32\2\u010a\u010d\5\64\33\2")
        buf.write(u"\u010b\u010d\5\66\34\2\u010c\u0107\3\2\2\2\u010c\u0108")
        buf.write(u"\3\2\2\2\u010c\u0109\3\2\2\2\u010c\u010a\3\2\2\2\u010c")
        buf.write(u"\u010b\3\2\2\2\u010d\25\3\2\2\2\u010e\u0113\5\30\r\2")
        buf.write(u"\u010f\u0110\7N\2\2\u0110\u0112\5\30\r\2\u0111\u010f")
        buf.write(u"\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113")
        buf.write(u"\u0114\3\2\2\2\u0114\27\3\2\2\2\u0115\u0113\3\2\2\2\u0116")
        buf.write(u"\u011c\58\35\2\u0117\u0118\58\35\2\u0118\u0119\7O\2\2")
        buf.write(u"\u0119\u011a\5L\'\2\u011a\u011c\3\2\2\2\u011b\u0116\3")
        buf.write(u"\2\2\2\u011b\u0117\3\2\2\2\u011c\31\3\2\2\2\u011d\u011e")
        buf.write(u"\t\n\2\2\u011e\33\3\2\2\2\u011f\u0125\t\13\2\2\u0120")
        buf.write(u"\u0125\5\60\31\2\u0121\u0125\5\36\20\2\u0122\u0125\5")
        buf.write(u"*\26\2\u0123\u0125\5J&\2\u0124\u011f\3\2\2\2\u0124\u0120")
        buf.write(u"\3\2\2\2\u0124\u0121\3\2\2\2\u0124\u0122\3\2\2\2\u0124")
        buf.write(u"\u0123\3\2\2\2\u0125\35\3\2\2\2\u0126\u0128\5 \21\2\u0127")
        buf.write(u"\u0129\7_\2\2\u0128\u0127\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write(u"\u0129\u012a\3\2\2\2\u012a\u012c\7\65\2\2\u012b\u012d")
        buf.write(u"\5\"\22\2\u012c\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write(u"\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\3\2\2")
        buf.write(u"\2\u0130\u0131\7\66\2\2\u0131\u0136\3\2\2\2\u0132\u0133")
        buf.write(u"\5 \21\2\u0133\u0134\7_\2\2\u0134\u0136\3\2\2\2\u0135")
        buf.write(u"\u0126\3\2\2\2\u0135\u0132\3\2\2\2\u0136\37\3\2\2\2\u0137")
        buf.write(u"\u0138\t\f\2\2\u0138!\3\2\2\2\u0139\u013b\5$\23\2\u013a")
        buf.write(u"\u013c\5&\24\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2\2")
        buf.write(u"\2\u013c\u013d\3\2\2\2\u013d\u013e\7M\2\2\u013e\u0141")
        buf.write(u"\3\2\2\2\u013f\u0141\5T+\2\u0140\u0139\3\2\2\2\u0140")
        buf.write(u"\u013f\3\2\2\2\u0141#\3\2\2\2\u0142\u0144\5\34\17\2\u0143")
        buf.write(u"\u0145\5$\23\2\u0144\u0143\3\2\2\2\u0144\u0145\3\2\2")
        buf.write(u"\2\u0145\u014b\3\2\2\2\u0146\u0148\5\62\32\2\u0147\u0149")
        buf.write(u"\5$\23\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write(u"\u014b\3\2\2\2\u014a\u0142\3\2\2\2\u014a\u0146\3\2\2")
        buf.write(u"\2\u014b%\3\2\2\2\u014c\u0151\5(\25\2\u014d\u014e\7N")
        buf.write(u"\2\2\u014e\u0150\5(\25\2\u014f\u014d\3\2\2\2\u0150\u0153")
        buf.write(u"\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152")
        buf.write(u"\'\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u015b\58\35\2\u0155")
        buf.write(u"\u0157\58\35\2\u0156\u0155\3\2\2\2\u0156\u0157\3\2\2")
        buf.write(u"\2\u0157\u0158\3\2\2\2\u0158\u0159\7L\2\2\u0159\u015b")
        buf.write(u"\5\20\t\2\u015a\u0154\3\2\2\2\u015a\u0156\3\2\2\2\u015b")
        buf.write(u")\3\2\2\2\u015c\u015e\7\17\2\2\u015d\u015f\7_\2\2\u015e")
        buf.write(u"\u015d\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2")
        buf.write(u"\2\u0160\u0161\7\65\2\2\u0161\u0162\5,\27\2\u0162\u0163")
        buf.write(u"\7\66\2\2\u0163\u0170\3\2\2\2\u0164\u0166\7\17\2\2\u0165")
        buf.write(u"\u0167\7_\2\2\u0166\u0165\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write(u"\u0167\u0168\3\2\2\2\u0168\u0169\7\65\2\2\u0169\u016a")
        buf.write(u"\5,\27\2\u016a\u016b\7N\2\2\u016b\u016c\7\66\2\2\u016c")
        buf.write(u"\u0170\3\2\2\2\u016d\u016e\7\17\2\2\u016e\u0170\7_\2")
        buf.write(u"\2\u016f\u015c\3\2\2\2\u016f\u0164\3\2\2\2\u016f\u016d")
        buf.write(u"\3\2\2\2\u0170+\3\2\2\2\u0171\u0176\5.\30\2\u0172\u0173")
        buf.write(u"\7N\2\2\u0173\u0175\5.\30\2\u0174\u0172\3\2\2\2\u0175")
        buf.write(u"\u0178\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2")
        buf.write(u"\2\u0177-\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017c\7_")
        buf.write(u"\2\2\u017a\u017b\7O\2\2\u017b\u017d\5\20\t\2\u017c\u017a")
        buf.write(u"\3\2\2\2\u017c\u017d\3\2\2\2\u017d/\3\2\2\2\u017e\u017f")
        buf.write(u"\7)\2\2\u017f\u0180\7\61\2\2\u0180\u0181\5D#\2\u0181")
        buf.write(u"\u0182\7\62\2\2\u0182\61\3\2\2\2\u0183\u0184\t\r\2\2")
        buf.write(u"\u0184\63\3\2\2\2\u0185\u018b\t\16\2\2\u0186\u0187\7")
        buf.write(u"\4\2\2\u0187\u0188\7\61\2\2\u0188\u0189\7_\2\2\u0189")
        buf.write(u"\u018b\7\62\2\2\u018a\u0185\3\2\2\2\u018a\u0186\3\2\2")
        buf.write(u"\2\u018b\65\3\2\2\2\u018c\u018d\7\'\2\2\u018d\u018e\7")
        buf.write(u"\61\2\2\u018e\u018f\5D#\2\u018f\u0190\7\62\2\2\u0190")
        buf.write(u"\u0197\3\2\2\2\u0191\u0192\7\'\2\2\u0192\u0193\7\61\2")
        buf.write(u"\2\u0193\u0194\5\20\t\2\u0194\u0195\7\62\2\2\u0195\u0197")
        buf.write(u"\3\2\2\2\u0196\u018c\3\2\2\2\u0196\u0191\3\2\2\2\u0197")
        buf.write(u"\67\3\2\2\2\u0198\u019a\5<\37\2\u0199\u0198\3\2\2\2\u0199")
        buf.write(u"\u019a\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\5:\36")
        buf.write(u"\2\u019c9\3\2\2\2\u019d\u019e\b\36\1\2\u019e\u019f\7")
        buf.write(u"_\2\2\u019f\u01da\3\2\2\2\u01a0\u01a1\f\b\2\2\u01a1\u01a5")
        buf.write(u"\7\63\2\2\u01a2\u01a4\5\62\32\2\u01a3\u01a2\3\2\2\2\u01a4")
        buf.write(u"\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2")
        buf.write(u"\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01aa")
        buf.write(u"\5\f\7\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write(u"\u01ab\3\2\2\2\u01ab\u01d9\7\64\2\2\u01ac\u01ad\f\7\2")
        buf.write(u"\2\u01ad\u01ae\7\63\2\2\u01ae\u01b2\7\36\2\2\u01af\u01b1")
        buf.write(u"\5\62\32\2\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2")
        buf.write(u"\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2")
        buf.write(u"\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\5\f\7\2\u01b6\u01b7")
        buf.write(u"\7\64\2\2\u01b7\u01d9\3\2\2\2\u01b8\u01b9\f\6\2\2\u01b9")
        buf.write(u"\u01bb\7\63\2\2\u01ba\u01bc\5\62\32\2\u01bb\u01ba\3\2")
        buf.write(u"\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be")
        buf.write(u"\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\7\36\2\2\u01c0")
        buf.write(u"\u01c1\5\f\7\2\u01c1\u01c2\7\64\2\2\u01c2\u01d9\3\2\2")
        buf.write(u"\2\u01c3\u01c4\f\5\2\2\u01c4\u01c8\7\63\2\2\u01c5\u01c7")
        buf.write(u"\5\62\32\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8")
        buf.write(u"\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cb\3\2\2")
        buf.write(u"\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\7A\2\2\u01cc\u01d9")
        buf.write(u"\7\64\2\2\u01cd\u01ce\f\4\2\2\u01ce\u01cf\7\61\2\2\u01cf")
        buf.write(u"\u01d0\5> \2\u01d0\u01d1\7\62\2\2\u01d1\u01d9\3\2\2\2")
        buf.write(u"\u01d2\u01d3\f\3\2\2\u01d3\u01d5\7\61\2\2\u01d4\u01d6")
        buf.write(u"\5B\"\2\u01d5\u01d4\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write(u"\u01d7\3\2\2\2\u01d7\u01d9\7\62\2\2\u01d8\u01a0\3\2\2")
        buf.write(u"\2\u01d8\u01ac\3\2\2\2\u01d8\u01b8\3\2\2\2\u01d8\u01c3")
        buf.write(u"\3\2\2\2\u01d8\u01cd\3\2\2\2\u01d8\u01d2\3\2\2\2\u01d9")
        buf.write(u"\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2")
        buf.write(u"\2\u01db;\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01e1\7A")
        buf.write(u"\2\2\u01de\u01e0\5\62\32\2\u01df\u01de\3\2\2\2\u01e0")
        buf.write(u"\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2")
        buf.write(u"\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4\u01e6")
        buf.write(u"\5<\37\2\u01e5\u01e4\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6")
        buf.write(u"=\3\2\2\2\u01e7\u01ec\5@!\2\u01e8\u01e9\7N\2\2\u01e9")
        buf.write(u"\u01eb\5@!\2\u01ea\u01e8\3\2\2\2\u01eb\u01ee\3\2\2\2")
        buf.write(u"\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01f1")
        buf.write(u"\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f0\7N\2\2\u01f0")
        buf.write(u"\u01f2\7^\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write(u"\u01f2?\3\2\2\2\u01f3\u01f5\5\24\13\2\u01f4\u01f3\3\2")
        buf.write(u"\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7")
        buf.write(u"\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9\58\35\2\u01f9")
        buf.write(u"\u0203\3\2\2\2\u01fa\u01fc\5\24\13\2\u01fb\u01fa\3\2")
        buf.write(u"\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write(u"\3\2\2\2\u01fe\u0200\3\2\2\2\u01ff\u0201\5F$\2\u0200")
        buf.write(u"\u01ff\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0203\3\2\2")
        buf.write(u"\2\u0202\u01f4\3\2\2\2\u0202\u01fb\3\2\2\2\u0203A\3\2")
        buf.write(u"\2\2\u0204\u0209\7_\2\2\u0205\u0206\7N\2\2\u0206\u0208")
        buf.write(u"\7_\2\2\u0207\u0205\3\2\2\2\u0208\u020b\3\2\2\2\u0209")
        buf.write(u"\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020aC\3\2\2\2\u020b")
        buf.write(u"\u0209\3\2\2\2\u020c\u020e\5$\23\2\u020d\u020f\5F$\2")
        buf.write(u"\u020e\u020d\3\2\2\2\u020e\u020f\3\2\2\2\u020fE\3\2\2")
        buf.write(u"\2\u0210\u0216\5<\37\2\u0211\u0213\5<\37\2\u0212\u0211")
        buf.write(u"\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write(u"\u0216\5H%\2\u0215\u0210\3\2\2\2\u0215\u0212\3\2\2\2")
        buf.write(u"\u0216G\3\2\2\2\u0217\u0218\b%\1\2\u0218\u0219\7\61\2")
        buf.write(u"\2\u0219\u021a\5F$\2\u021a\u021b\7\62\2\2\u021b\u0246")
        buf.write(u"\3\2\2\2\u021c\u0220\7\63\2\2\u021d\u021f\5\62\32\2\u021e")
        buf.write(u"\u021d\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2")
        buf.write(u"\2\u0220\u0221\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220")
        buf.write(u"\3\2\2\2\u0223\u0225\5\f\7\2\u0224\u0223\3\2\2\2\u0224")
        buf.write(u"\u0225\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0246\7\64\2")
        buf.write(u"\2\u0227\u0228\7\63\2\2\u0228\u022c\7\36\2\2\u0229\u022b")
        buf.write(u"\5\62\32\2\u022a\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c")
        buf.write(u"\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022f\3\2\2")
        buf.write(u"\2\u022e\u022c\3\2\2\2\u022f\u0230\5\f\7\2\u0230\u0231")
        buf.write(u"\7\64\2\2\u0231\u0246\3\2\2\2\u0232\u0236\7\63\2\2\u0233")
        buf.write(u"\u0235\5\62\32\2\u0234\u0233\3\2\2\2\u0235\u0238\3\2")
        buf.write(u"\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0239")
        buf.write(u"\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023a\7\36\2\2\u023a")
        buf.write(u"\u023b\5\f\7\2\u023b\u023c\7\64\2\2\u023c\u0246\3\2\2")
        buf.write(u"\2\u023d\u023e\7\63\2\2\u023e\u023f\7A\2\2\u023f\u0246")
        buf.write(u"\7\64\2\2\u0240\u0242\7\61\2\2\u0241\u0243\5> \2\u0242")
        buf.write(u"\u0241\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0244\3\2\2")
        buf.write(u"\2\u0244\u0246\7\62\2\2\u0245\u0217\3\2\2\2\u0245\u021c")
        buf.write(u"\3\2\2\2\u0245\u0227\3\2\2\2\u0245\u0232\3\2\2\2\u0245")
        buf.write(u"\u023d\3\2\2\2\u0245\u0240\3\2\2\2\u0246\u0276\3\2\2")
        buf.write(u"\2\u0247\u0248\f\7\2\2\u0248\u024c\7\63\2\2\u0249\u024b")
        buf.write(u"\5\62\32\2\u024a\u0249\3\2\2\2\u024b\u024e\3\2\2\2\u024c")
        buf.write(u"\u024a\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u0250\3\2\2")
        buf.write(u"\2\u024e\u024c\3\2\2\2\u024f\u0251\5\f\7\2\u0250\u024f")
        buf.write(u"\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write(u"\u0275\7\64\2\2\u0253\u0254\f\6\2\2\u0254\u0255\7\63")
        buf.write(u"\2\2\u0255\u0259\7\36\2\2\u0256\u0258\5\62\32\2\u0257")
        buf.write(u"\u0256\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257\3\2\2")
        buf.write(u"\2\u0259\u025a\3\2\2\2\u025a\u025c\3\2\2\2\u025b\u0259")
        buf.write(u"\3\2\2\2\u025c\u025d\5\f\7\2\u025d\u025e\7\64\2\2\u025e")
        buf.write(u"\u0275\3\2\2\2\u025f\u0260\f\5\2\2\u0260\u0262\7\63\2")
        buf.write(u"\2\u0261\u0263\5\62\32\2\u0262\u0261\3\2\2\2\u0263\u0264")
        buf.write(u"\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265")
        buf.write(u"\u0266\3\2\2\2\u0266\u0267\7\36\2\2\u0267\u0268\5\f\7")
        buf.write(u"\2\u0268\u0269\7\64\2\2\u0269\u0275\3\2\2\2\u026a\u026b")
        buf.write(u"\f\4\2\2\u026b\u026c\7\63\2\2\u026c\u026d\7A\2\2\u026d")
        buf.write(u"\u0275\7\64\2\2\u026e\u026f\f\3\2\2\u026f\u0271\7\61")
        buf.write(u"\2\2\u0270\u0272\5> \2\u0271\u0270\3\2\2\2\u0271\u0272")
        buf.write(u"\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0275\7\62\2\2\u0274")
        buf.write(u"\u0247\3\2\2\2\u0274\u0253\3\2\2\2\u0274\u025f\3\2\2")
        buf.write(u"\2\u0274\u026a\3\2\2\2\u0274\u026e\3\2\2\2\u0275\u0278")
        buf.write(u"\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277")
        buf.write(u"I\3\2\2\2\u0278\u0276\3\2\2\2\u0279\u027a\7_\2\2\u027a")
        buf.write(u"K\3\2\2\2\u027b\u0284\5\f\7\2\u027c\u027d\7\65\2\2\u027d")
        buf.write(u"\u027f\5N(\2\u027e\u0280\7N\2\2\u027f\u027e\3\2\2\2\u027f")
        buf.write(u"\u0280\3\2\2\2\u0280\u0281\3\2\2\2\u0281\u0282\7\66\2")
        buf.write(u"\2\u0282\u0284\3\2\2\2\u0283\u027b\3\2\2\2\u0283\u027c")
        buf.write(u"\3\2\2\2\u0284M\3\2\2\2\u0285\u0287\b(\1\2\u0286\u0288")
        buf.write(u"\5P)\2\u0287\u0286\3\2\2\2\u0287\u0288\3\2\2\2\u0288")
        buf.write(u"\u0289\3\2\2\2\u0289\u028a\5L\'\2\u028a\u0293\3\2\2\2")
        buf.write(u"\u028b\u028c\f\3\2\2\u028c\u028e\7N\2\2\u028d\u028f\5")
        buf.write(u"P)\2\u028e\u028d\3\2\2\2\u028e\u028f\3\2\2\2\u028f\u0290")
        buf.write(u"\3\2\2\2\u0290\u0292\5L\'\2\u0291\u028b\3\2\2\2\u0292")
        buf.write(u"\u0295\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0294\3\2\2")
        buf.write(u"\2\u0294O\3\2\2\2\u0295\u0293\3\2\2\2\u0296\u0298\5R")
        buf.write(u"*\2\u0297\u0296\3\2\2\2\u0298\u0299\3\2\2\2\u0299\u0297")
        buf.write(u"\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u029b\3\2\2\2\u029b")
        buf.write(u"\u029c\7O\2\2\u029cQ\3\2\2\2\u029d\u029e\7\63\2\2\u029e")
        buf.write(u"\u029f\5\20\t\2\u029f\u02a0\7\64\2\2\u02a0\u02a4\3\2")
        buf.write(u"\2\2\u02a1\u02a2\7]\2\2\u02a2\u02a4\7_\2\2\u02a3\u029d")
        buf.write(u"\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a4S\3\2\2\2\u02a5\u02a6")
        buf.write(u"\7/\2\2\u02a6\u02a7\7\61\2\2\u02a7\u02a8\5\20\t\2\u02a8")
        buf.write(u"\u02aa\7N\2\2\u02a9\u02ab\7c\2\2\u02aa\u02a9\3\2\2\2")
        buf.write(u"\u02ab\u02ac\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ac\u02ad")
        buf.write(u"\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u02af\7\62\2\2\u02af")
        buf.write(u"\u02b0\7M\2\2\u02b0U\3\2\2\2\u02b1\u02b8\5X-\2\u02b2")
        buf.write(u"\u02b8\5Z.\2\u02b3\u02b8\5^\60\2\u02b4\u02b8\5`\61\2")
        buf.write(u"\u02b5\u02b8\5f\64\2\u02b6\u02b8\5h\65\2\u02b7\u02b1")
        buf.write(u"\3\2\2\2\u02b7\u02b2\3\2\2\2\u02b7\u02b3\3\2\2\2\u02b7")
        buf.write(u"\u02b4\3\2\2\2\u02b7\u02b5\3\2\2\2\u02b7\u02b6\3\2\2")
        buf.write(u"\2\u02b8W\3\2\2\2\u02b9\u02ba\7_\2\2\u02ba\u02bb\7L\2")
        buf.write(u"\2\u02bb\u02c5\5V,\2\u02bc\u02bd\7\7\2\2\u02bd\u02be")
        buf.write(u"\5\20\t\2\u02be\u02bf\7L\2\2\u02bf\u02c0\5V,\2\u02c0")
        buf.write(u"\u02c5\3\2\2\2\u02c1\u02c2\7\13\2\2\u02c2\u02c3\7L\2")
        buf.write(u"\2\u02c3\u02c5\5V,\2\u02c4\u02b9\3\2\2\2\u02c4\u02bc")
        buf.write(u"\3\2\2\2\u02c4\u02c1\3\2\2\2\u02c5Y\3\2\2\2\u02c6\u02ca")
        buf.write(u"\7\65\2\2\u02c7\u02c9\5\\/\2\u02c8\u02c7\3\2\2\2\u02c9")
        buf.write(u"\u02cc\3\2\2\2\u02ca\u02c8\3\2\2\2\u02ca\u02cb\3\2\2")
        buf.write(u"\2\u02cb\u02cd\3\2\2\2\u02cc\u02ca\3\2\2\2\u02cd\u02ce")
        buf.write(u"\7\66\2\2\u02ce[\3\2\2\2\u02cf\u02d2\5\22\n\2\u02d0\u02d2")
        buf.write(u"\5V,\2\u02d1\u02cf\3\2\2\2\u02d1\u02d0\3\2\2\2\u02d2")
        buf.write(u"]\3\2\2\2\u02d3\u02d5\5\16\b\2\u02d4\u02d3\3\2\2\2\u02d4")
        buf.write(u"\u02d5\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6\u02d7\7M\2\2")
        buf.write(u"\u02d7_\3\2\2\2\u02d8\u02d9\7\24\2\2\u02d9\u02da\7\61")
        buf.write(u"\2\2\u02da\u02db\5\16\b\2\u02db\u02dc\7\62\2\2\u02dc")
        buf.write(u"\u02df\5V,\2\u02dd\u02de\7\16\2\2\u02de\u02e0\5V,\2\u02df")
        buf.write(u"\u02dd\3\2\2\2\u02df\u02e0\3\2\2\2\u02e0\u02e8\3\2\2")
        buf.write(u"\2\u02e1\u02e2\7 \2\2\u02e2\u02e3\7\61\2\2\u02e3\u02e4")
        buf.write(u"\5\16\b\2\u02e4\u02e5\7\62\2\2\u02e5\u02e6\5V,\2\u02e6")
        buf.write(u"\u02e8\3\2\2\2\u02e7\u02d8\3\2\2\2\u02e7\u02e1\3\2\2")
        buf.write(u"\2\u02e8a\3\2\2\2\u02e9\u02ea\5\16\b\2\u02eac\3\2\2\2")
        buf.write(u"\u02eb\u02ec\5\16\b\2\u02ece\3\2\2\2\u02ed\u02ee\7&\2")
        buf.write(u"\2\u02ee\u02ef\7\61\2\2\u02ef\u02f0\5\16\b\2\u02f0\u02f1")
        buf.write(u"\7\62\2\2\u02f1\u02f2\5V,\2\u02f2\u0318\3\2\2\2\u02f3")
        buf.write(u"\u02f4\7\f\2\2\u02f4\u02f5\5V,\2\u02f5\u02f6\7&\2\2\u02f6")
        buf.write(u"\u02f7\7\61\2\2\u02f7\u02f8\5\16\b\2\u02f8\u02f9\7\62")
        buf.write(u"\2\2\u02f9\u02fa\7M\2\2\u02fa\u0318\3\2\2\2\u02fb\u02fc")
        buf.write(u"\7\22\2\2\u02fc\u02fe\7\61\2\2\u02fd\u02ff\5b\62\2\u02fe")
        buf.write(u"\u02fd\3\2\2\2\u02fe\u02ff\3\2\2\2\u02ff\u0300\3\2\2")
        buf.write(u"\2\u0300\u0302\7M\2\2\u0301\u0303\5\16\b\2\u0302\u0301")
        buf.write(u"\3\2\2\2\u0302\u0303\3\2\2\2\u0303\u0304\3\2\2\2\u0304")
        buf.write(u"\u0306\7M\2\2\u0305\u0307\5d\63\2\u0306\u0305\3\2\2\2")
        buf.write(u"\u0306\u0307\3\2\2\2\u0307\u0308\3\2\2\2\u0308\u0309")
        buf.write(u"\7\62\2\2\u0309\u0318\5V,\2\u030a\u030b\7\22\2\2\u030b")
        buf.write(u"\u030c\7\61\2\2\u030c\u030e\5\22\n\2\u030d\u030f\5\16")
        buf.write(u"\b\2\u030e\u030d\3\2\2\2\u030e\u030f\3\2\2\2\u030f\u0310")
        buf.write(u"\3\2\2\2\u0310\u0312\7M\2\2\u0311\u0313\5d\63\2\u0312")
        buf.write(u"\u0311\3\2\2\2\u0312\u0313\3\2\2\2\u0313\u0314\3\2\2")
        buf.write(u"\2\u0314\u0315\7\62\2\2\u0315\u0316\5V,\2\u0316\u0318")
        buf.write(u"\3\2\2\2\u0317\u02ed\3\2\2\2\u0317\u02f3\3\2\2\2\u0317")
        buf.write(u"\u02fb\3\2\2\2\u0317\u030a\3\2\2\2\u0318g\3\2\2\2\u0319")
        buf.write(u"\u031a\7\23\2\2\u031a\u031b\7_\2\2\u031b\u0326\7M\2\2")
        buf.write(u"\u031c\u031d\7\n\2\2\u031d\u0326\7M\2\2\u031e\u031f\7")
        buf.write(u"\6\2\2\u031f\u0326\7M\2\2\u0320\u0322\7\32\2\2\u0321")
        buf.write(u"\u0323\5\16\b\2\u0322\u0321\3\2\2\2\u0322\u0323\3\2\2")
        buf.write(u"\2\u0323\u0324\3\2\2\2\u0324\u0326\7M\2\2\u0325\u0319")
        buf.write(u"\3\2\2\2\u0325\u031c\3\2\2\2\u0325\u031e\3\2\2\2\u0325")
        buf.write(u"\u0320\3\2\2\2\u0326i\3\2\2\2\u0327\u0329\5l\67\2\u0328")
        buf.write(u"\u0327\3\2\2\2\u0329\u032c\3\2\2\2\u032a\u0328\3\2\2")
        buf.write(u"\2\u032a\u032b\3\2\2\2\u032b\u032d\3\2\2\2\u032c\u032a")
        buf.write(u"\3\2\2\2\u032d\u032e\7\2\2\3\u032ek\3\2\2\2\u032f\u0334")
        buf.write(u"\5n8\2\u0330\u0334\5\22\n\2\u0331\u0334\5p9\2\u0332\u0334")
        buf.write(u"\7M\2\2\u0333\u032f\3\2\2\2\u0333\u0330\3\2\2\2\u0333")
        buf.write(u"\u0331\3\2\2\2\u0333\u0332\3\2\2\2\u0334m\3\2\2\2\u0335")
        buf.write(u"\u0337\5\24\13\2\u0336\u0335\3\2\2\2\u0337\u033a\3\2")
        buf.write(u"\2\2\u0338\u0336\3\2\2\2\u0338\u0339\3\2\2\2\u0339\u033b")
        buf.write(u"\3\2\2\2\u033a\u0338\3\2\2\2\u033b\u033f\58\35\2\u033c")
        buf.write(u"\u033e\5\22\n\2\u033d\u033c\3\2\2\2\u033e\u0341\3\2\2")
        buf.write(u"\2\u033f\u033d\3\2\2\2\u033f\u0340\3\2\2\2\u0340\u0342")
        buf.write(u"\3\2\2\2\u0341\u033f\3\2\2\2\u0342\u0343\5Z.\2\u0343")
        buf.write(u"o\3\2\2\2\u0344\u0345\t\17\2\2\u0345q\3\2\2\2d~\u0090")
        buf.write(u"\u009a\u00a5\u00a7\u00af\u00b8\u00db\u00dd\u00e7\u00ee")
        buf.write(u"\u00f5\u00fd\u0100\u0105\u010c\u0113\u011b\u0124\u0128")
        buf.write(u"\u012e\u0135\u013b\u0140\u0144\u0148\u014a\u0151\u0156")
        buf.write(u"\u015a\u015e\u0166\u016f\u0176\u017c\u018a\u0196\u0199")
        buf.write(u"\u01a5\u01a9\u01b2\u01bd\u01c8\u01d5\u01d8\u01da\u01e1")
        buf.write(u"\u01e5\u01ec\u01f1\u01f6\u01fd\u0200\u0202\u0209\u020e")
        buf.write(u"\u0212\u0215\u0220\u0224\u022c\u0236\u0242\u0245\u024c")
        buf.write(u"\u0250\u0259\u0264\u0271\u0274\u0276\u027f\u0283\u0287")
        buf.write(u"\u028e\u0293\u0299\u02a3\u02ac\u02b7\u02c4\u02ca\u02d1")
        buf.write(u"\u02d4\u02df\u02e7\u02fe\u0302\u0306\u030e\u0312\u0317")
        buf.write(u"\u0322\u0325\u032a\u0333\u0338\u033f")
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
                      u"Identifier", u"IntegerConstant", u"FloatingConstant", 
                      u"CharacterConstant", u"StringLiteral", u"LineDirective", 
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
    IntegerConstant=94
    FloatingConstant=95
    CharacterConstant=96
    StringLiteral=97
    LineDirective=98
    PragmaDirective=99
    IncludeDirective=100
    DefineDirective=101
    Whitespace=102
    Newline=103
    BlockComment=104
    LineComment=105

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


    class FloatingLiteralExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.FloatingLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def FloatingConstant(self):
            return self.getToken(CParser.FloatingConstant, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterFloatingLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitFloatingLiteralExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitFloatingLiteralExpression(self)
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


    class CharacterLiteralExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.CharacterLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def CharacterConstant(self):
            return self.getToken(CParser.CharacterConstant, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterCharacterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitCharacterLiteralExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitCharacterLiteralExpression(self)
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


    class IntegerLiteralExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.IntegerLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def IntegerConstant(self):
            return self.getToken(CParser.IntegerConstant, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIntegerLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIntegerLiteralExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIntegerLiteralExpression(self)
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
            self.state = 142
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
                localctx = CParser.IntegerLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(CParser.IntegerConstant)
                pass

            elif la_ == 5:
                localctx = CParser.FloatingLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(CParser.FloatingConstant)
                pass

            elif la_ == 6:
                localctx = CParser.CharacterLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(CParser.CharacterConstant)
                pass

            elif la_ == 7:
                localctx = CParser.StringLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 121
                        self.match(CParser.StringLiteral)

                    else:
                        raise NoViableAltException(self)
                    self.state = 124 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass

            elif la_ == 8:
                localctx = CParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(CParser.LeftParen)
                self.state = 127
                self.expression()
                self.state = 128
                self.match(CParser.RightParen)
                pass

            elif la_ == 9:
                localctx = CParser.UnaryOperatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                _la = self._input.LA(1)
                if not(((((_la - 59)) & ~0x3f) == 0 and ((1 << (_la - 59)) & ((1 << (CParser.Plus - 59)) | (1 << (CParser.Minus - 59)) | (1 << (CParser.Star - 59)) | (1 << (CParser.And - 59)) | (1 << (CParser.Not - 59)) | (1 << (CParser.Tilde - 59)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 131
                self.castExpression()
                pass

            elif la_ == 10:
                localctx = CParser.SizeOfTypeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 132
                self.match(CParser.Sizeof)
                self.state = 133
                self.match(CParser.LeftParen)
                self.state = 134
                self.typeName()
                self.state = 135
                self.match(CParser.RightParen)
                pass

            elif la_ == 11:
                localctx = CParser.AlignOfTypeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(CParser.Alignof)
                self.state = 138
                self.match(CParser.LeftParen)
                self.state = 139
                self.typeName()
                self.state = 140
                self.match(CParser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 163
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CParser.IndexExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 144
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 145
                        self.match(CParser.LeftBracket)
                        self.state = 146
                        self.expression()
                        self.state = 147
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.FunctionExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 149
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 150
                        self.match(CParser.LeftParen)
                        self.state = 152
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                            self.state = 151
                            self.argumentExpressionList()


                        self.state = 154
                        self.match(CParser.RightParen)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DotExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 155
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 156
                        self.match(CParser.Dot)
                        self.state = 157
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ArrowExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 158
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 159
                        self.match(CParser.Arrow)
                        self.state = 160
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 5:
                        localctx = CParser.PostIncrementExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 161
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 162
                        _la = self._input.LA(1)
                        if not(_la==CParser.PlusPlus or _la==CParser.MinusMinus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        pass

             
                self.state = 167
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
            self.state = 168
            self.assignmentExpression()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 169
                self.match(CParser.Comma)
                self.state = 170
                self.assignmentExpression()
                self.state = 175
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
            self.state = 182
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.unaryExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(CParser.LeftParen)
                self.state = 178
                self.typeName()
                self.state = 179
                self.match(CParser.RightParen)
                self.state = 180
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
            self.state = 185
            self.castExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 217
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 187
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 188
                        _la = self._input.LA(1)
                        if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (CParser.Star - 63)) | (1 << (CParser.Div - 63)) | (1 << (CParser.Mod - 63)))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 189
                        self.logicalOrExpression(11)
                        pass

                    elif la_ == 2:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 190
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 191
                        _la = self._input.LA(1)
                        if not(_la==CParser.Plus or _la==CParser.Minus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 192
                        self.logicalOrExpression(10)
                        pass

                    elif la_ == 3:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 193
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 194
                        _la = self._input.LA(1)
                        if not(_la==CParser.LeftShift or _la==CParser.RightShift):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 195
                        self.logicalOrExpression(9)
                        pass

                    elif la_ == 4:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 196
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 197
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Less) | (1 << CParser.LessEqual) | (1 << CParser.Greater) | (1 << CParser.GreaterEqual))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 198
                        self.logicalOrExpression(8)
                        pass

                    elif la_ == 5:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 199
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 200
                        _la = self._input.LA(1)
                        if not(_la==CParser.Equal or _la==CParser.NotEqual):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 201
                        self.logicalOrExpression(7)
                        pass

                    elif la_ == 6:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 202
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 203
                        self.match(CParser.And)
                        self.state = 204
                        self.logicalOrExpression(6)
                        pass

                    elif la_ == 7:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 205
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 206
                        self.match(CParser.Caret)
                        self.state = 207
                        self.logicalOrExpression(5)
                        pass

                    elif la_ == 8:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 208
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 209
                        self.match(CParser.Or)
                        self.state = 210
                        self.logicalOrExpression(4)
                        pass

                    elif la_ == 9:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 211
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 212
                        self.match(CParser.AndAnd)
                        self.state = 213
                        self.logicalOrExpression(3)
                        pass

                    elif la_ == 10:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 214
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 215
                        self.match(CParser.OrOr)
                        self.state = 216
                        self.logicalOrExpression(2)
                        pass

             
                self.state = 221
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
            self.state = 229
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.logicalOrExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.logicalOrExpression(0)
                self.state = 224
                self.match(CParser.Question)
                self.state = 225
                self.expression()
                self.state = 226
                self.match(CParser.Colon)
                self.state = 227
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
            self.state = 236
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.unaryExpression(0)
                self.state = 233
                _la = self._input.LA(1)
                if not(((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & ((1 << (CParser.Assign - 77)) | (1 << (CParser.StarAssign - 77)) | (1 << (CParser.DivAssign - 77)) | (1 << (CParser.ModAssign - 77)) | (1 << (CParser.PlusAssign - 77)) | (1 << (CParser.MinusAssign - 77)) | (1 << (CParser.LeftShiftAssign - 77)) | (1 << (CParser.RightShiftAssign - 77)) | (1 << (CParser.AndAssign - 77)) | (1 << (CParser.XorAssign - 77)) | (1 << (CParser.OrAssign - 77)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 234
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
            self.state = 238
            self.assignmentExpression()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 239
                self.match(CParser.Comma)
                self.state = 240
                self.assignmentExpression()
                self.state = 245
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
            self.state = 246
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
            self.state = 259
            token = self._input.LA(1)
            if token in [CParser.T__0, CParser.T__1, CParser.Auto, CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Extern, CParser.Float, CParser.Inline, CParser.Int, CParser.Long, CParser.Register, CParser.Restrict, CParser.Short, CParser.Signed, CParser.Static, CParser.Struct, CParser.Typedef, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Volatile, CParser.Alignas, CParser.Atomic, CParser.Bool, CParser.Complex, CParser.Noreturn, CParser.ThreadLocal, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 248
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 251 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 254
                _la = self._input.LA(1)
                if _la==CParser.Star or _la==CParser.Identifier:
                    self.state = 253
                    self.initDeclaratorList()


                self.state = 256
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
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
            self.state = 266
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.storageClassSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.typeSpecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self.typeQualifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.functionSpecifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 265
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
            self.state = 268
            self.initDeclarator()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 269
                self.match(CParser.Comma)
                self.state = 270
                self.initDeclarator()
                self.state = 275
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
            self.state = 281
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.declarator()
                self.state = 278
                self.match(CParser.Assign)
                self.state = 279
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
            self.state = 283
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
            self.state = 290
            token = self._input.LA(1)
            if token in [CParser.Char, CParser.Double, CParser.Float, CParser.Int, CParser.Long, CParser.Short, CParser.Signed, CParser.Unsigned, CParser.Void, CParser.Bool, CParser.Complex]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Char) | (1 << CParser.Double) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [CParser.Atomic]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.atomicTypeSpecifier()

            elif token in [CParser.Struct, CParser.Union]:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.structOrUnionSpecifier()

            elif token in [CParser.Enum]:
                self.enterOuterAlt(localctx, 4)
                self.state = 288
                self.enumSpecifier()

            elif token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 5)
                self.state = 289
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
            self.state = 307
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.structOrUnion()
                self.state = 294
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 293
                    self.match(CParser.Identifier)


                self.state = 296
                self.match(CParser.LeftBrace)
                self.state = 298 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 297
                    self.structDeclaration()
                    self.state = 300 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Struct) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.StaticAssert))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 302
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.structOrUnion()
                self.state = 305
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
            self.state = 309
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
            self.state = 318
            token = self._input.LA(1)
            if token in [CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Float, CParser.Int, CParser.Long, CParser.Restrict, CParser.Short, CParser.Signed, CParser.Struct, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Volatile, CParser.Atomic, CParser.Bool, CParser.Complex, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.specifierQualifierList()
                self.state = 313
                _la = self._input.LA(1)
                if ((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (CParser.Star - 63)) | (1 << (CParser.Colon - 63)) | (1 << (CParser.Identifier - 63)))) != 0):
                    self.state = 312
                    self.structDeclaratorList()


                self.state = 315
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
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
            self.state = 328
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.typeSpecifier()
                self.state = 322
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 321
                    self.specifierQualifierList()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.typeQualifier()
                self.state = 326
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 325
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
            self.state = 330
            self.structDeclarator()
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 331
                self.match(CParser.Comma)
                self.state = 332
                self.structDeclarator()
                self.state = 337
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
            self.state = 344
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                _la = self._input.LA(1)
                if _la==CParser.Star or _la==CParser.Identifier:
                    self.state = 339
                    self.declarator()


                self.state = 342
                self.match(CParser.Colon)
                self.state = 343
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
            self.state = 365
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(CParser.Enum)
                self.state = 348
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 347
                    self.match(CParser.Identifier)


                self.state = 350
                self.match(CParser.LeftBrace)
                self.state = 351
                self.enumeratorList()
                self.state = 352
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(CParser.Enum)
                self.state = 356
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 355
                    self.match(CParser.Identifier)


                self.state = 358
                self.match(CParser.LeftBrace)
                self.state = 359
                self.enumeratorList()
                self.state = 360
                self.match(CParser.Comma)
                self.state = 361
                self.match(CParser.RightBrace)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                self.match(CParser.Enum)
                self.state = 364
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
            self.state = 367
            self.enumerator()
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 368
                    self.match(CParser.Comma)
                    self.state = 369
                    self.enumerator() 
                self.state = 374
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
            self.state = 375
            self.match(CParser.Identifier)
            self.state = 378
            _la = self._input.LA(1)
            if _la==CParser.Assign:
                self.state = 376
                self.match(CParser.Assign)
                self.state = 377
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
            self.state = 380
            self.match(CParser.Atomic)
            self.state = 381
            self.match(CParser.LeftParen)
            self.state = 382
            self.typeName()
            self.state = 383
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
            self.state = 385
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
            self.state = 392
            token = self._input.LA(1)
            if token in [CParser.T__0, CParser.Inline, CParser.Noreturn]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.Inline) | (1 << CParser.Noreturn))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [CParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(CParser.T__1)
                self.state = 389
                self.match(CParser.LeftParen)
                self.state = 390
                self.match(CParser.Identifier)
                self.state = 391
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
            self.state = 404
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(CParser.Alignas)
                self.state = 395
                self.match(CParser.LeftParen)
                self.state = 396
                self.typeName()
                self.state = 397
                self.match(CParser.RightParen)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.match(CParser.Alignas)
                self.state = 400
                self.match(CParser.LeftParen)
                self.state = 401
                self.constantExpression()
                self.state = 402
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
            self.state = 407
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 406
                self.pointer()


            self.state = 409
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
            self.state = 412
            self.match(CParser.Identifier)
            self._ctx.stop = self._input.LT(-1)
            self.state = 472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 470
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 414
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 415
                        self.match(CParser.LeftBracket)
                        self.state = 419
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 416
                            self.typeQualifier()
                            self.state = 421
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 423
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                            self.state = 422
                            self.assignmentExpression()


                        self.state = 425
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 426
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 427
                        self.match(CParser.LeftBracket)
                        self.state = 428
                        self.match(CParser.Static)
                        self.state = 432
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 429
                            self.typeQualifier()
                            self.state = 434
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 435
                        self.assignmentExpression()
                        self.state = 436
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 438
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 439
                        self.match(CParser.LeftBracket)
                        self.state = 441 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 440
                            self.typeQualifier()
                            self.state = 443 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                                break

                        self.state = 445
                        self.match(CParser.Static)
                        self.state = 446
                        self.assignmentExpression()
                        self.state = 447
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 4:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 449
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 450
                        self.match(CParser.LeftBracket)
                        self.state = 454
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 451
                            self.typeQualifier()
                            self.state = 456
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 457
                        self.match(CParser.Star)
                        self.state = 458
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 5:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 459
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 460
                        self.match(CParser.LeftParen)
                        self.state = 461
                        self.parameterTypeList()
                        self.state = 462
                        self.match(CParser.RightParen)
                        pass

                    elif la_ == 6:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 464
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 465
                        self.match(CParser.LeftParen)
                        self.state = 467
                        _la = self._input.LA(1)
                        if _la==CParser.Identifier:
                            self.state = 466
                            self.identifierList()


                        self.state = 469
                        self.match(CParser.RightParen)
                        pass

             
                self.state = 474
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
            self.state = 475
            self.match(CParser.Star)
            self.state = 479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                self.state = 476
                self.typeQualifier()
                self.state = 481
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 483
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 482
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
            self.state = 485
            self.parameterDeclaration()
            self.state = 490
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 486
                    self.match(CParser.Comma)
                    self.state = 487
                    self.parameterDeclaration() 
                self.state = 492
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

            self.state = 495
            _la = self._input.LA(1)
            if _la==CParser.Comma:
                self.state = 493
                self.match(CParser.Comma)
                self.state = 494
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
            self.state = 512
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 497
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 500 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

                self.state = 502
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 504
                    self.declarationSpecifier()
                    self.state = 507 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 510
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.LeftParen) | (1 << CParser.LeftBracket) | (1 << CParser.Star))) != 0):
                    self.state = 509
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
            self.state = 514
            self.match(CParser.Identifier)
            self.state = 519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 515
                self.match(CParser.Comma)
                self.state = 516
                self.match(CParser.Identifier)
                self.state = 521
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
            self.state = 522
            self.specifierQualifierList()
            self.state = 524
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.LeftParen) | (1 << CParser.LeftBracket) | (1 << CParser.Star))) != 0):
                self.state = 523
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
            self.state = 531
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.pointer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 528
                _la = self._input.LA(1)
                if _la==CParser.Star:
                    self.state = 527
                    self.pointer()


                self.state = 530
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
            self.state = 579
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 534
                self.match(CParser.LeftParen)
                self.state = 535
                self.abstractDeclarator()
                self.state = 536
                self.match(CParser.RightParen)
                pass

            elif la_ == 2:
                self.state = 538
                self.match(CParser.LeftBracket)
                self.state = 542
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 539
                    self.typeQualifier()
                    self.state = 544
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 546
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 545
                    self.assignmentExpression()


                self.state = 548
                self.match(CParser.RightBracket)
                pass

            elif la_ == 3:
                self.state = 549
                self.match(CParser.LeftBracket)
                self.state = 550
                self.match(CParser.Static)
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 551
                    self.typeQualifier()
                    self.state = 556
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 557
                self.assignmentExpression()
                self.state = 558
                self.match(CParser.RightBracket)
                pass

            elif la_ == 4:
                self.state = 560
                self.match(CParser.LeftBracket)
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 561
                    self.typeQualifier()
                    self.state = 566
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 567
                self.match(CParser.Static)
                self.state = 568
                self.assignmentExpression()
                self.state = 569
                self.match(CParser.RightBracket)
                pass

            elif la_ == 5:
                self.state = 571
                self.match(CParser.LeftBracket)
                self.state = 572
                self.match(CParser.Star)
                self.state = 573
                self.match(CParser.RightBracket)
                pass

            elif la_ == 6:
                self.state = 574
                self.match(CParser.LeftParen)
                self.state = 576
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                    self.state = 575
                    self.parameterTypeList()


                self.state = 578
                self.match(CParser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 628
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 626
                    la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                    if la_ == 1:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 581
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 582
                        self.match(CParser.LeftBracket)
                        self.state = 586
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 583
                            self.typeQualifier()
                            self.state = 588
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 590
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                            self.state = 589
                            self.assignmentExpression()


                        self.state = 592
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 593
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 594
                        self.match(CParser.LeftBracket)
                        self.state = 595
                        self.match(CParser.Static)
                        self.state = 599
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 596
                            self.typeQualifier()
                            self.state = 601
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 602
                        self.assignmentExpression()
                        self.state = 603
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 605
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 606
                        self.match(CParser.LeftBracket)
                        self.state = 608 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 607
                            self.typeQualifier()
                            self.state = 610 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                                break

                        self.state = 612
                        self.match(CParser.Static)
                        self.state = 613
                        self.assignmentExpression()
                        self.state = 614
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 4:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 616
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 617
                        self.match(CParser.LeftBracket)
                        self.state = 618
                        self.match(CParser.Star)
                        self.state = 619
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 5:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 620
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 621
                        self.match(CParser.LeftParen)
                        self.state = 623
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                            self.state = 622
                            self.parameterTypeList()


                        self.state = 625
                        self.match(CParser.RightParen)
                        pass

             
                self.state = 630
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
            self.state = 631
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
            self.state = 641
            token = self._input.LA(1)
            if token in [CParser.Sizeof, CParser.Alignof, CParser.LeftParen, CParser.Plus, CParser.PlusPlus, CParser.Minus, CParser.MinusMinus, CParser.Star, CParser.And, CParser.Not, CParser.Tilde, CParser.Identifier, CParser.IntegerConstant, CParser.FloatingConstant, CParser.CharacterConstant, CParser.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 633
                self.assignmentExpression()

            elif token in [CParser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 634
                self.match(CParser.LeftBrace)
                self.state = 635
                self.initializerList(0)
                self.state = 637
                _la = self._input.LA(1)
                if _la==CParser.Comma:
                    self.state = 636
                    self.match(CParser.Comma)


                self.state = 639
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
            self.state = 645
            _la = self._input.LA(1)
            if _la==CParser.LeftBracket or _la==CParser.Dot:
                self.state = 644
                self.designation()


            self.state = 647
            self.initializer()
            self._ctx.stop = self._input.LT(-1)
            self.state = 657
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.InitializerListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerList)
                    self.state = 649
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 650
                    self.match(CParser.Comma)
                    self.state = 652
                    _la = self._input.LA(1)
                    if _la==CParser.LeftBracket or _la==CParser.Dot:
                        self.state = 651
                        self.designation()


                    self.state = 654
                    self.initializer() 
                self.state = 659
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
            self.state = 661 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 660
                self.designator()
                self.state = 663 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.LeftBracket or _la==CParser.Dot):
                    break

            self.state = 665
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
            self.state = 673
            token = self._input.LA(1)
            if token in [CParser.LeftBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 667
                self.match(CParser.LeftBracket)
                self.state = 668
                self.constantExpression()
                self.state = 669
                self.match(CParser.RightBracket)

            elif token in [CParser.Dot]:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.match(CParser.Dot)
                self.state = 672
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
            self.state = 675
            self.match(CParser.StaticAssert)
            self.state = 676
            self.match(CParser.LeftParen)
            self.state = 677
            self.constantExpression()
            self.state = 678
            self.match(CParser.Comma)
            self.state = 680 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 679
                self.match(CParser.StringLiteral)
                self.state = 682 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.StringLiteral):
                    break

            self.state = 684
            self.match(CParser.RightParen)
            self.state = 685
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
            self.state = 693
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 687
                self.labeledStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 688
                self.compoundStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 689
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 690
                self.selectionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 691
                self.iterationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 692
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
            self.state = 706
            token = self._input.LA(1)
            if token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 695
                self.match(CParser.Identifier)
                self.state = 696
                self.match(CParser.Colon)
                self.state = 697
                self.statement()

            elif token in [CParser.Case]:
                self.enterOuterAlt(localctx, 2)
                self.state = 698
                self.match(CParser.Case)
                self.state = 699
                self.constantExpression()
                self.state = 700
                self.match(CParser.Colon)
                self.state = 701
                self.statement()

            elif token in [CParser.Default]:
                self.enterOuterAlt(localctx, 3)
                self.state = 703
                self.match(CParser.Default)
                self.state = 704
                self.match(CParser.Colon)
                self.state = 705
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
            self.state = 708
            self.match(CParser.LeftBrace)
            self.state = 712
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Break) | (1 << CParser.Case) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Continue) | (1 << CParser.Default) | (1 << CParser.Do) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.For) | (1 << CParser.Goto) | (1 << CParser.If) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Return) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Sizeof) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Switch) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.While) | (1 << CParser.Alignas) | (1 << CParser.Alignof) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal) | (1 << CParser.LeftParen) | (1 << CParser.LeftBrace) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Semi - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                self.state = 709
                self.blockItem()
                self.state = 714
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 715
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
            self.state = 719
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 717
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 718
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
            self.state = 722
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                self.state = 721
                self.expression()


            self.state = 724
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
            self.state = 741
            token = self._input.LA(1)
            if token in [CParser.If]:
                localctx = CParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 726
                self.match(CParser.If)
                self.state = 727
                self.match(CParser.LeftParen)
                self.state = 728
                self.expression()
                self.state = 729
                self.match(CParser.RightParen)
                self.state = 730
                self.statement()
                self.state = 733
                la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
                if la_ == 1:
                    self.state = 731
                    self.match(CParser.Else)
                    self.state = 732
                    self.statement()



            elif token in [CParser.Switch]:
                localctx = CParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 735
                self.match(CParser.Switch)
                self.state = 736
                self.match(CParser.LeftParen)
                self.state = 737
                self.expression()
                self.state = 738
                self.match(CParser.RightParen)
                self.state = 739
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
            self.state = 743
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
            self.state = 745
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
            self.state = 789
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                localctx = CParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 747
                self.match(CParser.While)
                self.state = 748
                self.match(CParser.LeftParen)
                self.state = 749
                self.expression()
                self.state = 750
                self.match(CParser.RightParen)
                self.state = 751
                self.statement()
                pass

            elif la_ == 2:
                localctx = CParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 753
                self.match(CParser.Do)
                self.state = 754
                self.statement()
                self.state = 755
                self.match(CParser.While)
                self.state = 756
                self.match(CParser.LeftParen)
                self.state = 757
                self.expression()
                self.state = 758
                self.match(CParser.RightParen)
                self.state = 759
                self.match(CParser.Semi)
                pass

            elif la_ == 3:
                localctx = CParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 761
                self.match(CParser.For)
                self.state = 762
                self.match(CParser.LeftParen)
                self.state = 764
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 763
                    self.initExpression()


                self.state = 766
                self.match(CParser.Semi)
                self.state = 768
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 767
                    self.expression()


                self.state = 770
                self.match(CParser.Semi)
                self.state = 772
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 771
                    self.iterationExpression()


                self.state = 774
                self.match(CParser.RightParen)
                self.state = 775
                self.statement()
                pass

            elif la_ == 4:
                localctx = CParser.DeclForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 776
                self.match(CParser.For)
                self.state = 777
                self.match(CParser.LeftParen)
                self.state = 778
                self.declaration()
                self.state = 780
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 779
                    self.expression()


                self.state = 782
                self.match(CParser.Semi)
                self.state = 784
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 783
                    self.iterationExpression()


                self.state = 786
                self.match(CParser.RightParen)
                self.state = 787
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
            self.state = 803
            token = self._input.LA(1)
            if token in [CParser.Goto]:
                localctx = CParser.GotoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 791
                self.match(CParser.Goto)
                self.state = 792
                self.match(CParser.Identifier)
                self.state = 793
                self.match(CParser.Semi)

            elif token in [CParser.Continue]:
                localctx = CParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 794
                self.match(CParser.Continue)
                self.state = 795
                self.match(CParser.Semi)

            elif token in [CParser.Break]:
                localctx = CParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 796
                self.match(CParser.Break)
                self.state = 797
                self.match(CParser.Semi)

            elif token in [CParser.Return]:
                localctx = CParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 798
                self.match(CParser.Return)
                self.state = 800
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 799
                    self.expression()


                self.state = 802
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
            self.state = 808
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal) | (1 << CParser.Star))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CParser.Semi - 75)) | (1 << (CParser.Identifier - 75)) | (1 << (CParser.LineDirective - 75)) | (1 << (CParser.PragmaDirective - 75)) | (1 << (CParser.IncludeDirective - 75)) | (1 << (CParser.DefineDirective - 75)))) != 0):
                self.state = 805
                self.externalDeclaration()
                self.state = 810
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 811
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
            self.state = 817
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 813
                self.functionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 814
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 815
                self.preprocessorDirective()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 816
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
            self.state = 822
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,96,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 819
                    self.declarationSpecifier() 
                self.state = 824
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,96,self._ctx)

            self.state = 825
            self.declarator()
            self.state = 829
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                self.state = 826
                self.declaration()
                self.state = 831
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 832
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
            self.state = 834
            _la = self._input.LA(1)
            if not(((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (CParser.LineDirective - 98)) | (1 << (CParser.PragmaDirective - 98)) | (1 << (CParser.IncludeDirective - 98)) | (1 << (CParser.DefineDirective - 98)))) != 0)):
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
         



