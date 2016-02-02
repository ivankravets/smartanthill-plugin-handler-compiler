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
        buf.write(u"i\u02c0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\6\2}\n\2\r")
        buf.write(u"\2\16\2~\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\5\2\u008c\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0096")
        buf.write(u"\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\u00a1\n")
        buf.write(u"\2\f\2\16\2\u00a4\13\2\3\3\3\3\3\3\7\3\u00a9\n\3\f\3")
        buf.write(u"\16\3\u00ac\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00b4\n")
        buf.write(u"\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u00d7\n\5\f\5\16\5")
        buf.write(u"\u00da\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00e3\n\6")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\5\7\u00ea\n\7\3\b\3\b\3\b\7\b\u00ef")
        buf.write(u"\n\b\f\b\16\b\u00f2\13\b\3\t\3\t\3\n\6\n\u00f7\n\n\r")
        buf.write(u"\n\16\n\u00f8\3\n\5\n\u00fc\n\n\3\n\3\n\3\n\5\n\u0101")
        buf.write(u"\n\n\3\13\3\13\3\13\3\13\5\13\u0107\n\13\3\f\3\f\3\f")
        buf.write(u"\7\f\u010c\n\f\f\f\16\f\u010f\13\f\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\5\r\u0116\n\r\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u011e")
        buf.write(u"\n\17\3\20\3\20\5\20\u0122\n\20\3\20\3\20\6\20\u0126")
        buf.write(u"\n\20\r\20\16\20\u0127\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write(u"\u012f\n\20\3\21\3\21\3\22\3\22\5\22\u0135\n\22\3\22")
        buf.write(u"\3\22\3\22\5\22\u013a\n\22\3\23\3\23\5\23\u013e\n\23")
        buf.write(u"\3\23\3\23\5\23\u0142\n\23\5\23\u0144\n\23\3\24\3\24")
        buf.write(u"\3\24\7\24\u0149\n\24\f\24\16\24\u014c\13\24\3\25\3\25")
        buf.write(u"\5\25\u0150\n\25\3\25\3\25\5\25\u0154\n\25\3\26\3\26")
        buf.write(u"\5\26\u0158\n\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0160")
        buf.write(u"\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0169\n")
        buf.write(u"\26\3\27\3\27\3\27\7\27\u016e\n\27\f\27\16\27\u0171\13")
        buf.write(u"\27\3\30\3\30\3\30\5\30\u0176\n\30\3\31\3\31\3\32\3\32")
        buf.write(u"\3\33\5\33\u017d\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\5\34\u0187\n\34\3\34\7\34\u018a\n\34\f\34\16")
        buf.write(u"\34\u018d\13\34\3\35\3\35\7\35\u0191\n\35\f\35\16\35")
        buf.write(u"\u0194\13\35\3\35\5\35\u0197\n\35\3\36\3\36\3\36\7\36")
        buf.write(u"\u019c\n\36\f\36\16\36\u019f\13\36\3\36\3\36\5\36\u01a3")
        buf.write(u"\n\36\3\37\6\37\u01a6\n\37\r\37\16\37\u01a7\3\37\3\37")
        buf.write(u"\3\37\6\37\u01ad\n\37\r\37\16\37\u01ae\3\37\5\37\u01b2")
        buf.write(u"\n\37\5\37\u01b4\n\37\3 \3 \5 \u01b8\n \3!\3!\5!\u01bc")
        buf.write(u"\n!\3!\5!\u01bf\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01c8")
        buf.write(u"\n\"\3\"\5\"\u01cb\n\"\3\"\3\"\3\"\5\"\u01d0\n\"\3\"")
        buf.write(u"\7\"\u01d3\n\"\f\"\16\"\u01d6\13\"\3#\3#\3$\3$\3$\3$")
        buf.write(u"\5$\u01de\n$\3$\3$\5$\u01e2\n$\3%\3%\5%\u01e6\n%\3%\3")
        buf.write(u"%\3%\3%\3%\5%\u01ed\n%\3%\7%\u01f0\n%\f%\16%\u01f3\13")
        buf.write(u"%\3&\6&\u01f6\n&\r&\16&\u01f7\3&\3&\3\'\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\5\'\u0202\n\'\3(\3(\3(\3(\3(\6(\u0209\n(\r(\16")
        buf.write(u"(\u020a\3(\3(\3(\3)\3)\3)\3)\3)\3)\5)\u0216\n)\3*\3*")
        buf.write(u"\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u0223\n*\3+\3+\7+\u0227")
        buf.write(u"\n+\f+\16+\u022a\13+\3+\3+\3,\3,\5,\u0230\n,\3-\5-\u0233")
        buf.write(u"\n-\3-\3-\3.\3.\3.\3.\3.\3.\3.\5.\u023e\n.\3.\3.\3.\3")
        buf.write(u".\3.\3.\5.\u0246\n.\3/\3/\3\60\3\60\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\61\5\61\u025d\n\61\3\61\3\61\5\61\u0261")
        buf.write(u"\n\61\3\61\3\61\5\61\u0265\n\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\3\61\5\61\u026d\n\61\3\61\3\61\5\61\u0271\n\61\3")
        buf.write(u"\61\3\61\3\61\5\61\u0276\n\61\3\62\3\62\3\62\3\62\3\62")
        buf.write(u"\3\62\3\62\3\62\3\62\5\62\u0281\n\62\3\62\5\62\u0284")
        buf.write(u"\n\62\3\63\7\63\u0287\n\63\f\63\16\63\u028a\13\63\3\63")
        buf.write(u"\3\63\3\64\3\64\3\64\3\64\5\64\u0292\n\64\3\65\7\65\u0295")
        buf.write(u"\n\65\f\65\16\65\u0298\13\65\3\65\3\65\7\65\u029c\n\65")
        buf.write(u"\f\65\16\65\u029f\13\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write(u"\3\66\5\66\u02a8\n\66\3\67\3\67\3\67\38\38\38\38\39\3")
        buf.write(u"9\39\39\69\u02b5\n9\r9\169\u02b6\39\39\3:\3:\3:\3:\3")
        buf.write(u":\3:\2\7\2\b\66BH;\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write(u"\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl")
        buf.write(u"npr\2\16\4\2>>@@\7\2==??AADDIJ\3\2AC\4\2==??\3\2;<\3")
        buf.write(u"\2\67:\3\2Z[\3\2OY\b\2\5\5\20\20\30\30\36\36!!\60\60")
        buf.write(u"\t\2\b\b\r\r\21\21\26\27\33\34#$*+\4\2\37\37\"\"\4\2")
        buf.write(u"\25\25..\u02fd\2\u008b\3\2\2\2\4\u00a5\3\2\2\2\6\u00b3")
        buf.write(u"\3\2\2\2\b\u00b5\3\2\2\2\n\u00e2\3\2\2\2\f\u00e9\3\2")
        buf.write(u"\2\2\16\u00eb\3\2\2\2\20\u00f3\3\2\2\2\22\u0100\3\2\2")
        buf.write(u"\2\24\u0106\3\2\2\2\26\u0108\3\2\2\2\30\u0115\3\2\2\2")
        buf.write(u"\32\u0117\3\2\2\2\34\u011d\3\2\2\2\36\u012e\3\2\2\2 ")
        buf.write(u"\u0130\3\2\2\2\"\u0139\3\2\2\2$\u0143\3\2\2\2&\u0145")
        buf.write(u"\3\2\2\2(\u0153\3\2\2\2*\u0168\3\2\2\2,\u016a\3\2\2\2")
        buf.write(u".\u0172\3\2\2\2\60\u0177\3\2\2\2\62\u0179\3\2\2\2\64")
        buf.write(u"\u017c\3\2\2\2\66\u0180\3\2\2\28\u018e\3\2\2\2:\u0198")
        buf.write(u"\3\2\2\2<\u01b3\3\2\2\2>\u01b5\3\2\2\2@\u01be\3\2\2\2")
        buf.write(u"B\u01ca\3\2\2\2D\u01d7\3\2\2\2F\u01e1\3\2\2\2H\u01e3")
        buf.write(u"\3\2\2\2J\u01f5\3\2\2\2L\u0201\3\2\2\2N\u0203\3\2\2\2")
        buf.write(u"P\u0215\3\2\2\2R\u0222\3\2\2\2T\u0224\3\2\2\2V\u022f")
        buf.write(u"\3\2\2\2X\u0232\3\2\2\2Z\u0245\3\2\2\2\\\u0247\3\2\2")
        buf.write(u"\2^\u0249\3\2\2\2`\u0275\3\2\2\2b\u0283\3\2\2\2d\u0288")
        buf.write(u"\3\2\2\2f\u0291\3\2\2\2h\u0296\3\2\2\2j\u02a7\3\2\2\2")
        buf.write(u"l\u02a9\3\2\2\2n\u02ac\3\2\2\2p\u02b0\3\2\2\2r\u02ba")
        buf.write(u"\3\2\2\2tu\b\2\1\2uv\t\2\2\2v\u008c\5\2\2\5w\u008c\7")
        buf.write(u"_\2\2x\u008c\7`\2\2y\u008c\7a\2\2z\u008c\7b\2\2{}\7c")
        buf.write(u"\2\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u008c")
        buf.write(u"\3\2\2\2\u0080\u0081\7\61\2\2\u0081\u0082\5\16\b\2\u0082")
        buf.write(u"\u0083\7\62\2\2\u0083\u008c\3\2\2\2\u0084\u0085\t\3\2")
        buf.write(u"\2\u0085\u008c\5\6\4\2\u0086\u0087\7\35\2\2\u0087\u0088")
        buf.write(u"\7\61\2\2\u0088\u0089\5> \2\u0089\u008a\7\62\2\2\u008a")
        buf.write(u"\u008c\3\2\2\2\u008bt\3\2\2\2\u008bw\3\2\2\2\u008bx\3")
        buf.write(u"\2\2\2\u008by\3\2\2\2\u008bz\3\2\2\2\u008b|\3\2\2\2\u008b")
        buf.write(u"\u0080\3\2\2\2\u008b\u0084\3\2\2\2\u008b\u0086\3\2\2")
        buf.write(u"\2\u008c\u00a2\3\2\2\2\u008d\u008e\f\n\2\2\u008e\u008f")
        buf.write(u"\7\63\2\2\u008f\u0090\5\16\b\2\u0090\u0091\7\64\2\2\u0091")
        buf.write(u"\u00a1\3\2\2\2\u0092\u0093\f\t\2\2\u0093\u0095\7\61\2")
        buf.write(u"\2\u0094\u0096\5\4\3\2\u0095\u0094\3\2\2\2\u0095\u0096")
        buf.write(u"\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u00a1\7\62\2\2\u0098")
        buf.write(u"\u0099\f\b\2\2\u0099\u009a\7]\2\2\u009a\u00a1\7_\2\2")
        buf.write(u"\u009b\u009c\f\7\2\2\u009c\u009d\7\\\2\2\u009d\u00a1")
        buf.write(u"\7_\2\2\u009e\u009f\f\6\2\2\u009f\u00a1\t\2\2\2\u00a0")
        buf.write(u"\u008d\3\2\2\2\u00a0\u0092\3\2\2\2\u00a0\u0098\3\2\2")
        buf.write(u"\2\u00a0\u009b\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a4")
        buf.write(u"\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write(u"\3\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00aa\5\f\7\2\u00a6")
        buf.write(u"\u00a7\7N\2\2\u00a7\u00a9\5\f\7\2\u00a8\u00a6\3\2\2\2")
        buf.write(u"\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab")
        buf.write(u"\3\2\2\2\u00ab\5\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00b4")
        buf.write(u"\5\2\2\2\u00ae\u00af\7\61\2\2\u00af\u00b0\5> \2\u00b0")
        buf.write(u"\u00b1\7\62\2\2\u00b1\u00b2\5\6\4\2\u00b2\u00b4\3\2\2")
        buf.write(u"\2\u00b3\u00ad\3\2\2\2\u00b3\u00ae\3\2\2\2\u00b4\7\3")
        buf.write(u"\2\2\2\u00b5\u00b6\b\5\1\2\u00b6\u00b7\5\6\4\2\u00b7")
        buf.write(u"\u00d8\3\2\2\2\u00b8\u00b9\f\f\2\2\u00b9\u00ba\t\4\2")
        buf.write(u"\2\u00ba\u00d7\5\b\5\r\u00bb\u00bc\f\13\2\2\u00bc\u00bd")
        buf.write(u"\t\5\2\2\u00bd\u00d7\5\b\5\f\u00be\u00bf\f\n\2\2\u00bf")
        buf.write(u"\u00c0\t\6\2\2\u00c0\u00d7\5\b\5\13\u00c1\u00c2\f\t\2")
        buf.write(u"\2\u00c2\u00c3\t\7\2\2\u00c3\u00d7\5\b\5\n\u00c4\u00c5")
        buf.write(u"\f\b\2\2\u00c5\u00c6\t\b\2\2\u00c6\u00d7\5\b\5\t\u00c7")
        buf.write(u"\u00c8\f\7\2\2\u00c8\u00c9\7D\2\2\u00c9\u00d7\5\b\5\b")
        buf.write(u"\u00ca\u00cb\f\6\2\2\u00cb\u00cc\7H\2\2\u00cc\u00d7\5")
        buf.write(u"\b\5\7\u00cd\u00ce\f\5\2\2\u00ce\u00cf\7E\2\2\u00cf\u00d7")
        buf.write(u"\5\b\5\6\u00d0\u00d1\f\4\2\2\u00d1\u00d2\7F\2\2\u00d2")
        buf.write(u"\u00d7\5\b\5\5\u00d3\u00d4\f\3\2\2\u00d4\u00d5\7G\2\2")
        buf.write(u"\u00d5\u00d7\5\b\5\4\u00d6\u00b8\3\2\2\2\u00d6\u00bb")
        buf.write(u"\3\2\2\2\u00d6\u00be\3\2\2\2\u00d6\u00c1\3\2\2\2\u00d6")
        buf.write(u"\u00c4\3\2\2\2\u00d6\u00c7\3\2\2\2\u00d6\u00ca\3\2\2")
        buf.write(u"\2\u00d6\u00cd\3\2\2\2\u00d6\u00d0\3\2\2\2\u00d6\u00d3")
        buf.write(u"\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8")
        buf.write(u"\u00d9\3\2\2\2\u00d9\t\3\2\2\2\u00da\u00d8\3\2\2\2\u00db")
        buf.write(u"\u00e3\5\b\5\2\u00dc\u00dd\5\b\5\2\u00dd\u00de\7K\2\2")
        buf.write(u"\u00de\u00df\5\16\b\2\u00df\u00e0\7L\2\2\u00e0\u00e1")
        buf.write(u"\5\n\6\2\u00e1\u00e3\3\2\2\2\u00e2\u00db\3\2\2\2\u00e2")
        buf.write(u"\u00dc\3\2\2\2\u00e3\13\3\2\2\2\u00e4\u00ea\5\n\6\2\u00e5")
        buf.write(u"\u00e6\5\2\2\2\u00e6\u00e7\t\t\2\2\u00e7\u00e8\5\f\7")
        buf.write(u"\2\u00e8\u00ea\3\2\2\2\u00e9\u00e4\3\2\2\2\u00e9\u00e5")
        buf.write(u"\3\2\2\2\u00ea\r\3\2\2\2\u00eb\u00f0\5\f\7\2\u00ec\u00ed")
        buf.write(u"\7N\2\2\u00ed\u00ef\5\f\7\2\u00ee\u00ec\3\2\2\2\u00ef")
        buf.write(u"\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2")
        buf.write(u"\2\u00f1\17\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\5")
        buf.write(u"\n\6\2\u00f4\21\3\2\2\2\u00f5\u00f7\5\24\13\2\u00f6\u00f5")
        buf.write(u"\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write(u"\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00fc\5\26\f")
        buf.write(u"\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd")
        buf.write(u"\3\2\2\2\u00fd\u00fe\7M\2\2\u00fe\u0101\3\2\2\2\u00ff")
        buf.write(u"\u0101\5N(\2\u0100\u00f6\3\2\2\2\u0100\u00ff\3\2\2\2")
        buf.write(u"\u0101\23\3\2\2\2\u0102\u0107\5\32\16\2\u0103\u0107\5")
        buf.write(u"\34\17\2\u0104\u0107\5\60\31\2\u0105\u0107\5\62\32\2")
        buf.write(u"\u0106\u0102\3\2\2\2\u0106\u0103\3\2\2\2\u0106\u0104")
        buf.write(u"\3\2\2\2\u0106\u0105\3\2\2\2\u0107\25\3\2\2\2\u0108\u010d")
        buf.write(u"\5\30\r\2\u0109\u010a\7N\2\2\u010a\u010c\5\30\r\2\u010b")
        buf.write(u"\u0109\3\2\2\2\u010c\u010f\3\2\2\2\u010d\u010b\3\2\2")
        buf.write(u"\2\u010d\u010e\3\2\2\2\u010e\27\3\2\2\2\u010f\u010d\3")
        buf.write(u"\2\2\2\u0110\u0116\5\64\33\2\u0111\u0112\5\64\33\2\u0112")
        buf.write(u"\u0113\7O\2\2\u0113\u0114\5F$\2\u0114\u0116\3\2\2\2\u0115")
        buf.write(u"\u0110\3\2\2\2\u0115\u0111\3\2\2\2\u0116\31\3\2\2\2\u0117")
        buf.write(u"\u0118\t\n\2\2\u0118\33\3\2\2\2\u0119\u011e\t\13\2\2")
        buf.write(u"\u011a\u011e\5\36\20\2\u011b\u011e\5*\26\2\u011c\u011e")
        buf.write(u"\5D#\2\u011d\u0119\3\2\2\2\u011d\u011a\3\2\2\2\u011d")
        buf.write(u"\u011b\3\2\2\2\u011d\u011c\3\2\2\2\u011e\35\3\2\2\2\u011f")
        buf.write(u"\u0121\5 \21\2\u0120\u0122\7_\2\2\u0121\u0120\3\2\2\2")
        buf.write(u"\u0121\u0122\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125")
        buf.write(u"\7\65\2\2\u0124\u0126\5\"\22\2\u0125\u0124\3\2\2\2\u0126")
        buf.write(u"\u0127\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2")
        buf.write(u"\2\u0128\u0129\3\2\2\2\u0129\u012a\7\66\2\2\u012a\u012f")
        buf.write(u"\3\2\2\2\u012b\u012c\5 \21\2\u012c\u012d\7_\2\2\u012d")
        buf.write(u"\u012f\3\2\2\2\u012e\u011f\3\2\2\2\u012e\u012b\3\2\2")
        buf.write(u"\2\u012f\37\3\2\2\2\u0130\u0131\t\f\2\2\u0131!\3\2\2")
        buf.write(u"\2\u0132\u0134\5$\23\2\u0133\u0135\5&\24\2\u0134\u0133")
        buf.write(u"\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write(u"\u0137\7M\2\2\u0137\u013a\3\2\2\2\u0138\u013a\5N(\2\u0139")
        buf.write(u"\u0132\3\2\2\2\u0139\u0138\3\2\2\2\u013a#\3\2\2\2\u013b")
        buf.write(u"\u013d\5\34\17\2\u013c\u013e\5$\23\2\u013d\u013c\3\2")
        buf.write(u"\2\2\u013d\u013e\3\2\2\2\u013e\u0144\3\2\2\2\u013f\u0141")
        buf.write(u"\5\60\31\2\u0140\u0142\5$\23\2\u0141\u0140\3\2\2\2\u0141")
        buf.write(u"\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143\u013b\3\2\2")
        buf.write(u"\2\u0143\u013f\3\2\2\2\u0144%\3\2\2\2\u0145\u014a\5(")
        buf.write(u"\25\2\u0146\u0147\7N\2\2\u0147\u0149\5(\25\2\u0148\u0146")
        buf.write(u"\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a")
        buf.write(u"\u014b\3\2\2\2\u014b\'\3\2\2\2\u014c\u014a\3\2\2\2\u014d")
        buf.write(u"\u0154\5\64\33\2\u014e\u0150\5\64\33\2\u014f\u014e\3")
        buf.write(u"\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write(u"\u0152\7L\2\2\u0152\u0154\5\20\t\2\u0153\u014d\3\2\2")
        buf.write(u"\2\u0153\u014f\3\2\2\2\u0154)\3\2\2\2\u0155\u0157\7\17")
        buf.write(u"\2\2\u0156\u0158\7_\2\2\u0157\u0156\3\2\2\2\u0157\u0158")
        buf.write(u"\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\7\65\2\2\u015a")
        buf.write(u"\u015b\5,\27\2\u015b\u015c\7\66\2\2\u015c\u0169\3\2\2")
        buf.write(u"\2\u015d\u015f\7\17\2\2\u015e\u0160\7_\2\2\u015f\u015e")
        buf.write(u"\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write(u"\u0162\7\65\2\2\u0162\u0163\5,\27\2\u0163\u0164\7N\2")
        buf.write(u"\2\u0164\u0165\7\66\2\2\u0165\u0169\3\2\2\2\u0166\u0167")
        buf.write(u"\7\17\2\2\u0167\u0169\7_\2\2\u0168\u0155\3\2\2\2\u0168")
        buf.write(u"\u015d\3\2\2\2\u0168\u0166\3\2\2\2\u0169+\3\2\2\2\u016a")
        buf.write(u"\u016f\5.\30\2\u016b\u016c\7N\2\2\u016c\u016e\5.\30\2")
        buf.write(u"\u016d\u016b\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d")
        buf.write(u"\3\2\2\2\u016f\u0170\3\2\2\2\u0170-\3\2\2\2\u0171\u016f")
        buf.write(u"\3\2\2\2\u0172\u0175\7_\2\2\u0173\u0174\7O\2\2\u0174")
        buf.write(u"\u0176\5\20\t\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2")
        buf.write(u"\2\u0176/\3\2\2\2\u0177\u0178\7\t\2\2\u0178\61\3\2\2")
        buf.write(u"\2\u0179\u017a\t\r\2\2\u017a\63\3\2\2\2\u017b\u017d\5")
        buf.write(u"8\35\2\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write(u"\u017e\3\2\2\2\u017e\u017f\5\66\34\2\u017f\65\3\2\2\2")
        buf.write(u"\u0180\u0181\b\34\1\2\u0181\u0182\7_\2\2\u0182\u018b")
        buf.write(u"\3\2\2\2\u0183\u0184\f\3\2\2\u0184\u0186\7\61\2\2\u0185")
        buf.write(u"\u0187\5:\36\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2")
        buf.write(u"\2\u0187\u0188\3\2\2\2\u0188\u018a\7\62\2\2\u0189\u0183")
        buf.write(u"\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b")
        buf.write(u"\u018c\3\2\2\2\u018c\67\3\2\2\2\u018d\u018b\3\2\2\2\u018e")
        buf.write(u"\u0192\7A\2\2\u018f\u0191\5\60\31\2\u0190\u018f\3\2\2")
        buf.write(u"\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193")
        buf.write(u"\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0195")
        buf.write(u"\u0197\58\35\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2")
        buf.write(u"\2\u01979\3\2\2\2\u0198\u019d\5<\37\2\u0199\u019a\7N")
        buf.write(u"\2\2\u019a\u019c\5<\37\2\u019b\u0199\3\2\2\2\u019c\u019f")
        buf.write(u"\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write(u"\u01a2\3\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a1\7N\2\2")
        buf.write(u"\u01a1\u01a3\7^\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3")
        buf.write(u"\2\2\2\u01a3;\3\2\2\2\u01a4\u01a6\5\24\13\2\u01a5\u01a4")
        buf.write(u"\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write(u"\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\5\64\33")
        buf.write(u"\2\u01aa\u01b4\3\2\2\2\u01ab\u01ad\5\24\13\2\u01ac\u01ab")
        buf.write(u"\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae")
        buf.write(u"\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01b2\5@!\2")
        buf.write(u"\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b4")
        buf.write(u"\3\2\2\2\u01b3\u01a5\3\2\2\2\u01b3\u01ac\3\2\2\2\u01b4")
        buf.write(u"=\3\2\2\2\u01b5\u01b7\5$\23\2\u01b6\u01b8\5@!\2\u01b7")
        buf.write(u"\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8?\3\2\2\2\u01b9")
        buf.write(u"\u01bf\58\35\2\u01ba\u01bc\58\35\2\u01bb\u01ba\3\2\2")
        buf.write(u"\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01bf")
        buf.write(u"\5B\"\2\u01be\u01b9\3\2\2\2\u01be\u01bb\3\2\2\2\u01bf")
        buf.write(u"A\3\2\2\2\u01c0\u01c1\b\"\1\2\u01c1\u01c2\7\61\2\2\u01c2")
        buf.write(u"\u01c3\5@!\2\u01c3\u01c4\7\62\2\2\u01c4\u01cb\3\2\2\2")
        buf.write(u"\u01c5\u01c7\7\61\2\2\u01c6\u01c8\5:\36\2\u01c7\u01c6")
        buf.write(u"\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write(u"\u01cb\7\62\2\2\u01ca\u01c0\3\2\2\2\u01ca\u01c5\3\2\2")
        buf.write(u"\2\u01cb\u01d4\3\2\2\2\u01cc\u01cd\f\3\2\2\u01cd\u01cf")
        buf.write(u"\7\61\2\2\u01ce\u01d0\5:\36\2\u01cf\u01ce\3\2\2\2\u01cf")
        buf.write(u"\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d3\7\62\2")
        buf.write(u"\2\u01d2\u01cc\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2")
        buf.write(u"\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5C\3\2\2\2\u01d6\u01d4")
        buf.write(u"\3\2\2\2\u01d7\u01d8\7_\2\2\u01d8E\3\2\2\2\u01d9\u01e2")
        buf.write(u"\5\f\7\2\u01da\u01db\7\65\2\2\u01db\u01dd\5H%\2\u01dc")
        buf.write(u"\u01de\7N\2\2\u01dd\u01dc\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write(u"\u01de\u01df\3\2\2\2\u01df\u01e0\7\66\2\2\u01e0\u01e2")
        buf.write(u"\3\2\2\2\u01e1\u01d9\3\2\2\2\u01e1\u01da\3\2\2\2\u01e2")
        buf.write(u"G\3\2\2\2\u01e3\u01e5\b%\1\2\u01e4\u01e6\5J&\2\u01e5")
        buf.write(u"\u01e4\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\3\2\2")
        buf.write(u"\2\u01e7\u01e8\5F$\2\u01e8\u01f1\3\2\2\2\u01e9\u01ea")
        buf.write(u"\f\3\2\2\u01ea\u01ec\7N\2\2\u01eb\u01ed\5J&\2\u01ec\u01eb")
        buf.write(u"\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee")
        buf.write(u"\u01f0\5F$\2\u01ef\u01e9\3\2\2\2\u01f0\u01f3\3\2\2\2")
        buf.write(u"\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2I\3\2\2")
        buf.write(u"\2\u01f3\u01f1\3\2\2\2\u01f4\u01f6\5L\'\2\u01f5\u01f4")
        buf.write(u"\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7")
        buf.write(u"\u01f8\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa\7O\2\2")
        buf.write(u"\u01faK\3\2\2\2\u01fb\u01fc\7\63\2\2\u01fc\u01fd\5\20")
        buf.write(u"\t\2\u01fd\u01fe\7\64\2\2\u01fe\u0202\3\2\2\2\u01ff\u0200")
        buf.write(u"\7]\2\2\u0200\u0202\7_\2\2\u0201\u01fb\3\2\2\2\u0201")
        buf.write(u"\u01ff\3\2\2\2\u0202M\3\2\2\2\u0203\u0204\7/\2\2\u0204")
        buf.write(u"\u0205\7\61\2\2\u0205\u0206\5\20\t\2\u0206\u0208\7N\2")
        buf.write(u"\2\u0207\u0209\7c\2\2\u0208\u0207\3\2\2\2\u0209\u020a")
        buf.write(u"\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b")
        buf.write(u"\u020c\3\2\2\2\u020c\u020d\7\62\2\2\u020d\u020e\7M\2")
        buf.write(u"\2\u020eO\3\2\2\2\u020f\u0216\5R*\2\u0210\u0216\5T+\2")
        buf.write(u"\u0211\u0216\5X-\2\u0212\u0216\5Z.\2\u0213\u0216\5`\61")
        buf.write(u"\2\u0214\u0216\5b\62\2\u0215\u020f\3\2\2\2\u0215\u0210")
        buf.write(u"\3\2\2\2\u0215\u0211\3\2\2\2\u0215\u0212\3\2\2\2\u0215")
        buf.write(u"\u0213\3\2\2\2\u0215\u0214\3\2\2\2\u0216Q\3\2\2\2\u0217")
        buf.write(u"\u0218\7_\2\2\u0218\u0219\7L\2\2\u0219\u0223\5P)\2\u021a")
        buf.write(u"\u021b\7\7\2\2\u021b\u021c\5\20\t\2\u021c\u021d\7L\2")
        buf.write(u"\2\u021d\u021e\5P)\2\u021e\u0223\3\2\2\2\u021f\u0220")
        buf.write(u"\7\13\2\2\u0220\u0221\7L\2\2\u0221\u0223\5P)\2\u0222")
        buf.write(u"\u0217\3\2\2\2\u0222\u021a\3\2\2\2\u0222\u021f\3\2\2")
        buf.write(u"\2\u0223S\3\2\2\2\u0224\u0228\7\65\2\2\u0225\u0227\5")
        buf.write(u"V,\2\u0226\u0225\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226")
        buf.write(u"\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022b\3\2\2\2\u022a")
        buf.write(u"\u0228\3\2\2\2\u022b\u022c\7\66\2\2\u022cU\3\2\2\2\u022d")
        buf.write(u"\u0230\5\22\n\2\u022e\u0230\5P)\2\u022f\u022d\3\2\2\2")
        buf.write(u"\u022f\u022e\3\2\2\2\u0230W\3\2\2\2\u0231\u0233\5\16")
        buf.write(u"\b\2\u0232\u0231\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234")
        buf.write(u"\3\2\2\2\u0234\u0235\7M\2\2\u0235Y\3\2\2\2\u0236\u0237")
        buf.write(u"\7\24\2\2\u0237\u0238\7\61\2\2\u0238\u0239\5\16\b\2\u0239")
        buf.write(u"\u023a\7\62\2\2\u023a\u023d\5P)\2\u023b\u023c\7\16\2")
        buf.write(u"\2\u023c\u023e\5P)\2\u023d\u023b\3\2\2\2\u023d\u023e")
        buf.write(u"\3\2\2\2\u023e\u0246\3\2\2\2\u023f\u0240\7 \2\2\u0240")
        buf.write(u"\u0241\7\61\2\2\u0241\u0242\5\16\b\2\u0242\u0243\7\62")
        buf.write(u"\2\2\u0243\u0244\5P)\2\u0244\u0246\3\2\2\2\u0245\u0236")
        buf.write(u"\3\2\2\2\u0245\u023f\3\2\2\2\u0246[\3\2\2\2\u0247\u0248")
        buf.write(u"\5\16\b\2\u0248]\3\2\2\2\u0249\u024a\5\16\b\2\u024a_")
        buf.write(u"\3\2\2\2\u024b\u024c\7&\2\2\u024c\u024d\7\61\2\2\u024d")
        buf.write(u"\u024e\5\16\b\2\u024e\u024f\7\62\2\2\u024f\u0250\5P)")
        buf.write(u"\2\u0250\u0276\3\2\2\2\u0251\u0252\7\f\2\2\u0252\u0253")
        buf.write(u"\5P)\2\u0253\u0254\7&\2\2\u0254\u0255\7\61\2\2\u0255")
        buf.write(u"\u0256\5\16\b\2\u0256\u0257\7\62\2\2\u0257\u0258\7M\2")
        buf.write(u"\2\u0258\u0276\3\2\2\2\u0259\u025a\7\22\2\2\u025a\u025c")
        buf.write(u"\7\61\2\2\u025b\u025d\5\\/\2\u025c\u025b\3\2\2\2\u025c")
        buf.write(u"\u025d\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0260\7M\2\2")
        buf.write(u"\u025f\u0261\5\16\b\2\u0260\u025f\3\2\2\2\u0260\u0261")
        buf.write(u"\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u0264\7M\2\2\u0263")
        buf.write(u"\u0265\5^\60\2\u0264\u0263\3\2\2\2\u0264\u0265\3\2\2")
        buf.write(u"\2\u0265\u0266\3\2\2\2\u0266\u0267\7\62\2\2\u0267\u0276")
        buf.write(u"\5P)\2\u0268\u0269\7\22\2\2\u0269\u026a\7\61\2\2\u026a")
        buf.write(u"\u026c\5\22\n\2\u026b\u026d\5\16\b\2\u026c\u026b\3\2")
        buf.write(u"\2\2\u026c\u026d\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u0270")
        buf.write(u"\7M\2\2\u026f\u0271\5^\60\2\u0270\u026f\3\2\2\2\u0270")
        buf.write(u"\u0271\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0273\7\62\2")
        buf.write(u"\2\u0273\u0274\5P)\2\u0274\u0276\3\2\2\2\u0275\u024b")
        buf.write(u"\3\2\2\2\u0275\u0251\3\2\2\2\u0275\u0259\3\2\2\2\u0275")
        buf.write(u"\u0268\3\2\2\2\u0276a\3\2\2\2\u0277\u0278\7\23\2\2\u0278")
        buf.write(u"\u0279\7_\2\2\u0279\u0284\7M\2\2\u027a\u027b\7\n\2\2")
        buf.write(u"\u027b\u0284\7M\2\2\u027c\u027d\7\6\2\2\u027d\u0284\7")
        buf.write(u"M\2\2\u027e\u0280\7\32\2\2\u027f\u0281\5\16\b\2\u0280")
        buf.write(u"\u027f\3\2\2\2\u0280\u0281\3\2\2\2\u0281\u0282\3\2\2")
        buf.write(u"\2\u0282\u0284\7M\2\2\u0283\u0277\3\2\2\2\u0283\u027a")
        buf.write(u"\3\2\2\2\u0283\u027c\3\2\2\2\u0283\u027e\3\2\2\2\u0284")
        buf.write(u"c\3\2\2\2\u0285\u0287\5f\64\2\u0286\u0285\3\2\2\2\u0287")
        buf.write(u"\u028a\3\2\2\2\u0288\u0286\3\2\2\2\u0288\u0289\3\2\2")
        buf.write(u"\2\u0289\u028b\3\2\2\2\u028a\u0288\3\2\2\2\u028b\u028c")
        buf.write(u"\7\2\2\3\u028ce\3\2\2\2\u028d\u0292\5h\65\2\u028e\u0292")
        buf.write(u"\5\22\n\2\u028f\u0292\5j\66\2\u0290\u0292\7M\2\2\u0291")
        buf.write(u"\u028d\3\2\2\2\u0291\u028e\3\2\2\2\u0291\u028f\3\2\2")
        buf.write(u"\2\u0291\u0290\3\2\2\2\u0292g\3\2\2\2\u0293\u0295\5\24")
        buf.write(u"\13\2\u0294\u0293\3\2\2\2\u0295\u0298\3\2\2\2\u0296\u0294")
        buf.write(u"\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0299\3\2\2\2\u0298")
        buf.write(u"\u0296\3\2\2\2\u0299\u029d\5\64\33\2\u029a\u029c\5\22")
        buf.write(u"\n\2\u029b\u029a\3\2\2\2\u029c\u029f\3\2\2\2\u029d\u029b")
        buf.write(u"\3\2\2\2\u029d\u029e\3\2\2\2\u029e\u02a0\3\2\2\2\u029f")
        buf.write(u"\u029d\3\2\2\2\u02a0\u02a1\5T+\2\u02a1i\3\2\2\2\u02a2")
        buf.write(u"\u02a8\7d\2\2\u02a3\u02a8\7e\2\2\u02a4\u02a8\5l\67\2")
        buf.write(u"\u02a5\u02a8\5n8\2\u02a6\u02a8\5r:\2\u02a7\u02a2\3\2")
        buf.write(u"\2\2\u02a7\u02a3\3\2\2\2\u02a7\u02a4\3\2\2\2\u02a7\u02a5")
        buf.write(u"\3\2\2\2\u02a7\u02a6\3\2\2\2\u02a8k\3\2\2\2\u02a9\u02aa")
        buf.write(u"\7\3\2\2\u02aa\u02ab\7c\2\2\u02abm\3\2\2\2\u02ac\u02ad")
        buf.write(u"\7\4\2\2\u02ad\u02ae\7_\2\2\u02ae\u02af\5\16\b\2\u02af")
        buf.write(u"o\3\2\2\2\u02b0\u02b1\7\61\2\2\u02b1\u02b4\7_\2\2\u02b2")
        buf.write(u"\u02b3\7N\2\2\u02b3\u02b5\7_\2\2\u02b4\u02b2\3\2\2\2")
        buf.write(u"\u02b5\u02b6\3\2\2\2\u02b6\u02b4\3\2\2\2\u02b6\u02b7")
        buf.write(u"\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02b9\7\62\2\2\u02b9")
        buf.write(u"q\3\2\2\2\u02ba\u02bb\7\4\2\2\u02bb\u02bc\7_\2\2\u02bc")
        buf.write(u"\u02bd\5p9\2\u02bd\u02be\5\16\b\2\u02bes\3\2\2\2T~\u008b")
        buf.write(u"\u0095\u00a0\u00a2\u00aa\u00b3\u00d6\u00d8\u00e2\u00e9")
        buf.write(u"\u00f0\u00f8\u00fb\u0100\u0106\u010d\u0115\u011d\u0121")
        buf.write(u"\u0127\u012e\u0134\u0139\u013d\u0141\u0143\u014a\u014f")
        buf.write(u"\u0153\u0157\u015f\u0168\u016f\u0175\u017c\u0186\u018b")
        buf.write(u"\u0192\u0196\u019d\u01a2\u01a7\u01ae\u01b1\u01b3\u01b7")
        buf.write(u"\u01bb\u01be\u01c7\u01ca\u01cf\u01d4\u01dd\u01e1\u01e5")
        buf.write(u"\u01ec\u01f1\u01f7\u0201\u020a\u0215\u0222\u0228\u022f")
        buf.write(u"\u0232\u023d\u0245\u025c\u0260\u0264\u026c\u0270\u0275")
        buf.write(u"\u0280\u0283\u0288\u0291\u0296\u029d\u02a7\u02b6")
        return buf.getvalue()


class CParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'#include'", u"'#define'", u"'auto'", 
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
                      u"PragmaDirective", u"Whitespace", u"Newline", u"BlockComment", 
                      u"LineComment" ]

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
    RULE_typeQualifier = 23
    RULE_functionSpecifier = 24
    RULE_declarator = 25
    RULE_directDeclarator = 26
    RULE_pointer = 27
    RULE_parameterTypeList = 28
    RULE_parameterDeclaration = 29
    RULE_typeName = 30
    RULE_abstractDeclarator = 31
    RULE_directAbstractDeclarator = 32
    RULE_typedefName = 33
    RULE_initializer = 34
    RULE_initializerList = 35
    RULE_designation = 36
    RULE_designator = 37
    RULE_staticAssertDeclaration = 38
    RULE_statement = 39
    RULE_labeledStatement = 40
    RULE_compoundStatement = 41
    RULE_blockItem = 42
    RULE_expressionStatement = 43
    RULE_selectionStatement = 44
    RULE_initExpression = 45
    RULE_iterationExpression = 46
    RULE_iterationStatement = 47
    RULE_jumpStatement = 48
    RULE_compilationUnit = 49
    RULE_externalDeclaration = 50
    RULE_functionDefinition = 51
    RULE_preprocessorDirective = 52
    RULE_includeDirective = 53
    RULE_defineConstantDirective = 54
    RULE_defineFunctionArgs = 55
    RULE_defineFunctionDirective = 56

    ruleNames =  [ u"unaryExpression", u"argumentExpressionList", u"castExpression", 
                   u"logicalOrExpression", u"conditionalExpression", u"assignmentExpression", 
                   u"expression", u"constantExpression", u"declaration", 
                   u"declarationSpecifier", u"initDeclaratorList", u"initDeclarator", 
                   u"storageClassSpecifier", u"typeSpecifier", u"structOrUnionSpecifier", 
                   u"structOrUnion", u"structDeclaration", u"specifierQualifierList", 
                   u"structDeclaratorList", u"structDeclarator", u"enumSpecifier", 
                   u"enumeratorList", u"enumerator", u"typeQualifier", u"functionSpecifier", 
                   u"declarator", u"directDeclarator", u"pointer", u"parameterTypeList", 
                   u"parameterDeclaration", u"typeName", u"abstractDeclarator", 
                   u"directAbstractDeclarator", u"typedefName", u"initializer", 
                   u"initializerList", u"designation", u"designator", u"staticAssertDeclaration", 
                   u"statement", u"labeledStatement", u"compoundStatement", 
                   u"blockItem", u"expressionStatement", u"selectionStatement", 
                   u"initExpression", u"iterationExpression", u"iterationStatement", 
                   u"jumpStatement", u"compilationUnit", u"externalDeclaration", 
                   u"functionDefinition", u"preprocessorDirective", u"includeDirective", 
                   u"defineConstantDirective", u"defineFunctionArgs", u"defineFunctionDirective" ]

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
            self.state = 137
            token = self._input.LA(1)
            if token in [CParser.PlusPlus, CParser.MinusMinus]:
                localctx = CParser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 115
                _la = self._input.LA(1)
                if not(_la==CParser.PlusPlus or _la==CParser.MinusMinus):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 116
                self.unaryExpression(3)

            elif token in [CParser.Identifier]:
                localctx = CParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.match(CParser.Identifier)

            elif token in [CParser.IntegerConstant]:
                localctx = CParser.IntegerLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(CParser.IntegerConstant)

            elif token in [CParser.FloatingConstant]:
                localctx = CParser.FloatingLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(CParser.FloatingConstant)

            elif token in [CParser.CharacterConstant]:
                localctx = CParser.CharacterLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(CParser.CharacterConstant)

            elif token in [CParser.StringLiteral]:
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


            elif token in [CParser.LeftParen]:
                localctx = CParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(CParser.LeftParen)
                self.state = 127
                self.expression()
                self.state = 128
                self.match(CParser.RightParen)

            elif token in [CParser.Plus, CParser.Minus, CParser.Star, CParser.And, CParser.Not, CParser.Tilde]:
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

            elif token in [CParser.Sizeof]:
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

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 158
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CParser.IndexExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 139
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 140
                        self.match(CParser.LeftBracket)
                        self.state = 141
                        self.expression()
                        self.state = 142
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.FunctionExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 144
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 145
                        self.match(CParser.LeftParen)
                        self.state = 147
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                            self.state = 146
                            self.argumentExpressionList()


                        self.state = 149
                        self.match(CParser.RightParen)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DotExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 150
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 151
                        self.match(CParser.Dot)
                        self.state = 152
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ArrowExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 153
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 154
                        self.match(CParser.Arrow)
                        self.state = 155
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 5:
                        localctx = CParser.PostIncrementExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 156
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 157
                        _la = self._input.LA(1)
                        if not(_la==CParser.PlusPlus or _la==CParser.MinusMinus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        pass

             
                self.state = 162
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
            self.state = 163
            self.assignmentExpression()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 164
                self.match(CParser.Comma)
                self.state = 165
                self.assignmentExpression()
                self.state = 170
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
            self.state = 177
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.unaryExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(CParser.LeftParen)
                self.state = 173
                self.typeName()
                self.state = 174
                self.match(CParser.RightParen)
                self.state = 175
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
            self.state = 180
            self.castExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 212
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 182
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 183
                        _la = self._input.LA(1)
                        if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (CParser.Star - 63)) | (1 << (CParser.Div - 63)) | (1 << (CParser.Mod - 63)))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 184
                        self.logicalOrExpression(11)
                        pass

                    elif la_ == 2:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 185
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 186
                        _la = self._input.LA(1)
                        if not(_la==CParser.Plus or _la==CParser.Minus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 187
                        self.logicalOrExpression(10)
                        pass

                    elif la_ == 3:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 188
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 189
                        _la = self._input.LA(1)
                        if not(_la==CParser.LeftShift or _la==CParser.RightShift):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 190
                        self.logicalOrExpression(9)
                        pass

                    elif la_ == 4:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 191
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 192
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Less) | (1 << CParser.LessEqual) | (1 << CParser.Greater) | (1 << CParser.GreaterEqual))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 193
                        self.logicalOrExpression(8)
                        pass

                    elif la_ == 5:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 194
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 195
                        _la = self._input.LA(1)
                        if not(_la==CParser.Equal or _la==CParser.NotEqual):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 196
                        self.logicalOrExpression(7)
                        pass

                    elif la_ == 6:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 197
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 198
                        self.match(CParser.And)
                        self.state = 199
                        self.logicalOrExpression(6)
                        pass

                    elif la_ == 7:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 200
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 201
                        self.match(CParser.Caret)
                        self.state = 202
                        self.logicalOrExpression(5)
                        pass

                    elif la_ == 8:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 203
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 204
                        self.match(CParser.Or)
                        self.state = 205
                        self.logicalOrExpression(4)
                        pass

                    elif la_ == 9:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 206
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 207
                        self.match(CParser.AndAnd)
                        self.state = 208
                        self.logicalOrExpression(3)
                        pass

                    elif la_ == 10:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 209
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 210
                        self.match(CParser.OrOr)
                        self.state = 211
                        self.logicalOrExpression(2)
                        pass

             
                self.state = 216
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
            self.state = 224
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.logicalOrExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.logicalOrExpression(0)
                self.state = 219
                self.match(CParser.Question)
                self.state = 220
                self.expression()
                self.state = 221
                self.match(CParser.Colon)
                self.state = 222
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
            self.state = 231
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.unaryExpression(0)
                self.state = 228
                _la = self._input.LA(1)
                if not(((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & ((1 << (CParser.Assign - 77)) | (1 << (CParser.StarAssign - 77)) | (1 << (CParser.DivAssign - 77)) | (1 << (CParser.ModAssign - 77)) | (1 << (CParser.PlusAssign - 77)) | (1 << (CParser.MinusAssign - 77)) | (1 << (CParser.LeftShiftAssign - 77)) | (1 << (CParser.RightShiftAssign - 77)) | (1 << (CParser.AndAssign - 77)) | (1 << (CParser.XorAssign - 77)) | (1 << (CParser.OrAssign - 77)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 229
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
            self.state = 233
            self.assignmentExpression()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 234
                self.match(CParser.Comma)
                self.state = 235
                self.assignmentExpression()
                self.state = 240
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
            self.state = 241
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
            self.state = 254
            token = self._input.LA(1)
            if token in [CParser.Auto, CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Extern, CParser.Float, CParser.Inline, CParser.Int, CParser.Long, CParser.Register, CParser.Short, CParser.Signed, CParser.Static, CParser.Struct, CParser.Typedef, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Bool, CParser.Complex, CParser.Noreturn, CParser.ThreadLocal, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 243
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 246 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 249
                _la = self._input.LA(1)
                if _la==CParser.Star or _la==CParser.Identifier:
                    self.state = 248
                    self.initDeclaratorList()


                self.state = 251
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
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
            self.state = 260
            token = self._input.LA(1)
            if token in [CParser.Auto, CParser.Extern, CParser.Register, CParser.Static, CParser.Typedef, CParser.ThreadLocal]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.storageClassSpecifier()

            elif token in [CParser.Char, CParser.Double, CParser.Enum, CParser.Float, CParser.Int, CParser.Long, CParser.Short, CParser.Signed, CParser.Struct, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Bool, CParser.Complex, CParser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.typeSpecifier()

            elif token in [CParser.Const]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.typeQualifier()

            elif token in [CParser.Inline, CParser.Noreturn]:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.functionSpecifier()

            else:
                raise NoViableAltException(self)

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
            self.state = 262
            self.initDeclarator()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 263
                self.match(CParser.Comma)
                self.state = 264
                self.initDeclarator()
                self.state = 269
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
            self.state = 275
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.declarator()
                self.state = 272
                self.match(CParser.Assign)
                self.state = 273
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
            self.state = 277
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
            self.state = 283
            token = self._input.LA(1)
            if token in [CParser.Char, CParser.Double, CParser.Float, CParser.Int, CParser.Long, CParser.Short, CParser.Signed, CParser.Unsigned, CParser.Void, CParser.Bool, CParser.Complex]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Char) | (1 << CParser.Double) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [CParser.Struct, CParser.Union]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.structOrUnionSpecifier()

            elif token in [CParser.Enum]:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.enumSpecifier()

            elif token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
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
            self.state = 300
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.structOrUnion()
                self.state = 287
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 286
                    self.match(CParser.Identifier)


                self.state = 289
                self.match(CParser.LeftBrace)
                self.state = 291 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 290
                    self.structDeclaration()
                    self.state = 293 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Struct) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.StaticAssert))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 295
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.structOrUnion()
                self.state = 298
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
            self.state = 302
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
            self.state = 311
            token = self._input.LA(1)
            if token in [CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Float, CParser.Int, CParser.Long, CParser.Short, CParser.Signed, CParser.Struct, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Bool, CParser.Complex, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.specifierQualifierList()
                self.state = 306
                _la = self._input.LA(1)
                if ((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (CParser.Star - 63)) | (1 << (CParser.Colon - 63)) | (1 << (CParser.Identifier - 63)))) != 0):
                    self.state = 305
                    self.structDeclaratorList()


                self.state = 308
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
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
            self.state = 321
            token = self._input.LA(1)
            if token in [CParser.Char, CParser.Double, CParser.Enum, CParser.Float, CParser.Int, CParser.Long, CParser.Short, CParser.Signed, CParser.Struct, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Bool, CParser.Complex, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.typeSpecifier()
                self.state = 315
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 314
                    self.specifierQualifierList()



            elif token in [CParser.Const]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.typeQualifier()
                self.state = 319
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 318
                    self.specifierQualifierList()



            else:
                raise NoViableAltException(self)

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
            self.state = 323
            self.structDeclarator()
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 324
                self.match(CParser.Comma)
                self.state = 325
                self.structDeclarator()
                self.state = 330
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
            self.state = 337
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                _la = self._input.LA(1)
                if _la==CParser.Star or _la==CParser.Identifier:
                    self.state = 332
                    self.declarator()


                self.state = 335
                self.match(CParser.Colon)
                self.state = 336
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
            self.state = 358
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(CParser.Enum)
                self.state = 341
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 340
                    self.match(CParser.Identifier)


                self.state = 343
                self.match(CParser.LeftBrace)
                self.state = 344
                self.enumeratorList()
                self.state = 345
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(CParser.Enum)
                self.state = 349
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 348
                    self.match(CParser.Identifier)


                self.state = 351
                self.match(CParser.LeftBrace)
                self.state = 352
                self.enumeratorList()
                self.state = 353
                self.match(CParser.Comma)
                self.state = 354
                self.match(CParser.RightBrace)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.match(CParser.Enum)
                self.state = 357
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
            self.state = 360
            self.enumerator()
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 361
                    self.match(CParser.Comma)
                    self.state = 362
                    self.enumerator() 
                self.state = 367
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
            self.state = 368
            self.match(CParser.Identifier)
            self.state = 371
            _la = self._input.LA(1)
            if _la==CParser.Assign:
                self.state = 369
                self.match(CParser.Assign)
                self.state = 370
                self.constantExpression()


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
        self.enterRule(localctx, 46, self.RULE_typeQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(CParser.Const)
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
        self.enterRule(localctx, 48, self.RULE_functionSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            _la = self._input.LA(1)
            if not(_la==CParser.Inline or _la==CParser.Noreturn):
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
        self.enterRule(localctx, 50, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 377
                self.pointer()


            self.state = 380
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


        def parameterTypeList(self):
            return self.getTypedRuleContext(CParser.ParameterTypeListContext,0)


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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_directDeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(CParser.Identifier)
            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                    self.state = 385
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 386
                    self.match(CParser.LeftParen)
                    self.state = 388
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                        self.state = 387
                        self.parameterTypeList()


                    self.state = 390
                    self.match(CParser.RightParen) 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(CParser.Star)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Const:
                self.state = 397
                self.typeQualifier()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 404
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 403
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
        self.enterRule(localctx, 56, self.RULE_parameterTypeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.parameterDeclaration()
            self.state = 411
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 407
                    self.match(CParser.Comma)
                    self.state = 408
                    self.parameterDeclaration() 
                self.state = 413
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 416
            _la = self._input.LA(1)
            if _la==CParser.Comma:
                self.state = 414
                self.match(CParser.Comma)
                self.state = 415
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
        self.enterRule(localctx, 58, self.RULE_parameterDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 433
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 418
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 421 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                self.state = 423
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 425
                    self.declarationSpecifier()
                    self.state = 428 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 431
                _la = self._input.LA(1)
                if _la==CParser.LeftParen or _la==CParser.Star:
                    self.state = 430
                    self.abstractDeclarator()


                pass


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
        self.enterRule(localctx, 60, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.specifierQualifierList()
            self.state = 437
            _la = self._input.LA(1)
            if _la==CParser.LeftParen or _la==CParser.Star:
                self.state = 436
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
        self.enterRule(localctx, 62, self.RULE_abstractDeclarator)
        self._la = 0 # Token type
        try:
            self.state = 444
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.pointer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                _la = self._input.LA(1)
                if _la==CParser.Star:
                    self.state = 440
                    self.pointer()


                self.state = 443
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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_directAbstractDeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 447
                self.match(CParser.LeftParen)
                self.state = 448
                self.abstractDeclarator()
                self.state = 449
                self.match(CParser.RightParen)
                pass

            elif la_ == 2:
                self.state = 451
                self.match(CParser.LeftParen)
                self.state = 453
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                    self.state = 452
                    self.parameterTypeList()


                self.state = 455
                self.match(CParser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                    self.state = 458
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 459
                    self.match(CParser.LeftParen)
                    self.state = 461
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                        self.state = 460
                        self.parameterTypeList()


                    self.state = 463
                    self.match(CParser.RightParen) 
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        self.enterRule(localctx, 66, self.RULE_typedefName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
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
        self.enterRule(localctx, 68, self.RULE_initializer)
        self._la = 0 # Token type
        try:
            self.state = 479
            token = self._input.LA(1)
            if token in [CParser.Sizeof, CParser.LeftParen, CParser.Plus, CParser.PlusPlus, CParser.Minus, CParser.MinusMinus, CParser.Star, CParser.And, CParser.Not, CParser.Tilde, CParser.Identifier, CParser.IntegerConstant, CParser.FloatingConstant, CParser.CharacterConstant, CParser.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.assignmentExpression()

            elif token in [CParser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.match(CParser.LeftBrace)
                self.state = 473
                self.initializerList(0)
                self.state = 475
                _la = self._input.LA(1)
                if _la==CParser.Comma:
                    self.state = 474
                    self.match(CParser.Comma)


                self.state = 477
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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_initializerList, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            _la = self._input.LA(1)
            if _la==CParser.LeftBracket or _la==CParser.Dot:
                self.state = 482
                self.designation()


            self.state = 485
            self.initializer()
            self._ctx.stop = self._input.LT(-1)
            self.state = 495
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.InitializerListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerList)
                    self.state = 487
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 488
                    self.match(CParser.Comma)
                    self.state = 490
                    _la = self._input.LA(1)
                    if _la==CParser.LeftBracket or _la==CParser.Dot:
                        self.state = 489
                        self.designation()


                    self.state = 492
                    self.initializer() 
                self.state = 497
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

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
        self.enterRule(localctx, 72, self.RULE_designation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 498
                self.designator()
                self.state = 501 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.LeftBracket or _la==CParser.Dot):
                    break

            self.state = 503
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
        self.enterRule(localctx, 74, self.RULE_designator)
        try:
            self.state = 511
            token = self._input.LA(1)
            if token in [CParser.LeftBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.match(CParser.LeftBracket)
                self.state = 506
                self.constantExpression()
                self.state = 507
                self.match(CParser.RightBracket)

            elif token in [CParser.Dot]:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.match(CParser.Dot)
                self.state = 510
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
        self.enterRule(localctx, 76, self.RULE_staticAssertDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(CParser.StaticAssert)
            self.state = 514
            self.match(CParser.LeftParen)
            self.state = 515
            self.constantExpression()
            self.state = 516
            self.match(CParser.Comma)
            self.state = 518 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 517
                self.match(CParser.StringLiteral)
                self.state = 520 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.StringLiteral):
                    break

            self.state = 522
            self.match(CParser.RightParen)
            self.state = 523
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
        self.enterRule(localctx, 78, self.RULE_statement)
        try:
            self.state = 531
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.labeledStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.compoundStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 527
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 528
                self.selectionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 529
                self.iterationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 530
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
        self.enterRule(localctx, 80, self.RULE_labeledStatement)
        try:
            self.state = 544
            token = self._input.LA(1)
            if token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.match(CParser.Identifier)
                self.state = 534
                self.match(CParser.Colon)
                self.state = 535
                self.statement()

            elif token in [CParser.Case]:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.match(CParser.Case)
                self.state = 537
                self.constantExpression()
                self.state = 538
                self.match(CParser.Colon)
                self.state = 539
                self.statement()

            elif token in [CParser.Default]:
                self.enterOuterAlt(localctx, 3)
                self.state = 541
                self.match(CParser.Default)
                self.state = 542
                self.match(CParser.Colon)
                self.state = 543
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
        self.enterRule(localctx, 82, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.match(CParser.LeftBrace)
            self.state = 550
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Auto) | (1 << CParser.Break) | (1 << CParser.Case) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Continue) | (1 << CParser.Default) | (1 << CParser.Do) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.For) | (1 << CParser.Goto) | (1 << CParser.If) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Return) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Sizeof) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Switch) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.While) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal) | (1 << CParser.LeftParen) | (1 << CParser.LeftBrace) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Semi - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                self.state = 547
                self.blockItem()
                self.state = 552
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 553
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
        self.enterRule(localctx, 84, self.RULE_blockItem)
        try:
            self.state = 557
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
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
        self.enterRule(localctx, 86, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                self.state = 559
                self.expression()


            self.state = 562
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
        self.enterRule(localctx, 88, self.RULE_selectionStatement)
        try:
            self.state = 579
            token = self._input.LA(1)
            if token in [CParser.If]:
                localctx = CParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.match(CParser.If)
                self.state = 565
                self.match(CParser.LeftParen)
                self.state = 566
                self.expression()
                self.state = 567
                self.match(CParser.RightParen)
                self.state = 568
                self.statement()
                self.state = 571
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 569
                    self.match(CParser.Else)
                    self.state = 570
                    self.statement()



            elif token in [CParser.Switch]:
                localctx = CParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                self.match(CParser.Switch)
                self.state = 574
                self.match(CParser.LeftParen)
                self.state = 575
                self.expression()
                self.state = 576
                self.match(CParser.RightParen)
                self.state = 577
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
        self.enterRule(localctx, 90, self.RULE_initExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
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
        self.enterRule(localctx, 92, self.RULE_iterationExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
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
        self.enterRule(localctx, 94, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 627
            la_ = self._interp.adaptivePredict(self._input,73,self._ctx)
            if la_ == 1:
                localctx = CParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 585
                self.match(CParser.While)
                self.state = 586
                self.match(CParser.LeftParen)
                self.state = 587
                self.expression()
                self.state = 588
                self.match(CParser.RightParen)
                self.state = 589
                self.statement()
                pass

            elif la_ == 2:
                localctx = CParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 591
                self.match(CParser.Do)
                self.state = 592
                self.statement()
                self.state = 593
                self.match(CParser.While)
                self.state = 594
                self.match(CParser.LeftParen)
                self.state = 595
                self.expression()
                self.state = 596
                self.match(CParser.RightParen)
                self.state = 597
                self.match(CParser.Semi)
                pass

            elif la_ == 3:
                localctx = CParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 599
                self.match(CParser.For)
                self.state = 600
                self.match(CParser.LeftParen)
                self.state = 602
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 601
                    self.initExpression()


                self.state = 604
                self.match(CParser.Semi)
                self.state = 606
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 605
                    self.expression()


                self.state = 608
                self.match(CParser.Semi)
                self.state = 610
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 609
                    self.iterationExpression()


                self.state = 612
                self.match(CParser.RightParen)
                self.state = 613
                self.statement()
                pass

            elif la_ == 4:
                localctx = CParser.DeclForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 614
                self.match(CParser.For)
                self.state = 615
                self.match(CParser.LeftParen)
                self.state = 616
                self.declaration()
                self.state = 618
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 617
                    self.expression()


                self.state = 620
                self.match(CParser.Semi)
                self.state = 622
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 621
                    self.iterationExpression()


                self.state = 624
                self.match(CParser.RightParen)
                self.state = 625
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
        self.enterRule(localctx, 96, self.RULE_jumpStatement)
        self._la = 0 # Token type
        try:
            self.state = 641
            token = self._input.LA(1)
            if token in [CParser.Goto]:
                localctx = CParser.GotoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.match(CParser.Goto)
                self.state = 630
                self.match(CParser.Identifier)
                self.state = 631
                self.match(CParser.Semi)

            elif token in [CParser.Continue]:
                localctx = CParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 632
                self.match(CParser.Continue)
                self.state = 633
                self.match(CParser.Semi)

            elif token in [CParser.Break]:
                localctx = CParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 634
                self.match(CParser.Break)
                self.state = 635
                self.match(CParser.Semi)

            elif token in [CParser.Return]:
                localctx = CParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 636
                self.match(CParser.Return)
                self.state = 638
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus) | (1 << CParser.MinusMinus) | (1 << CParser.Star))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (CParser.And - 66)) | (1 << (CParser.Not - 66)) | (1 << (CParser.Tilde - 66)) | (1 << (CParser.Identifier - 66)) | (1 << (CParser.IntegerConstant - 66)) | (1 << (CParser.FloatingConstant - 66)) | (1 << (CParser.CharacterConstant - 66)) | (1 << (CParser.StringLiteral - 66)))) != 0):
                    self.state = 637
                    self.expression()


                self.state = 640
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
        self.enterRule(localctx, 98, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal) | (1 << CParser.Star))) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & ((1 << (CParser.Semi - 75)) | (1 << (CParser.Identifier - 75)) | (1 << (CParser.LineDirective - 75)) | (1 << (CParser.PragmaDirective - 75)))) != 0):
                self.state = 643
                self.externalDeclaration()
                self.state = 648
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 649
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
        self.enterRule(localctx, 100, self.RULE_externalDeclaration)
        try:
            self.state = 655
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 651
                self.functionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 652
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 653
                self.preprocessorDirective()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 654
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
        self.enterRule(localctx, 102, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,78,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 657
                    self.declarationSpecifier() 
                self.state = 662
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,78,self._ctx)

            self.state = 663
            self.declarator()
            self.state = 667
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                self.state = 664
                self.declaration()
                self.state = 669
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 670
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

        def includeDirective(self):
            return self.getTypedRuleContext(CParser.IncludeDirectiveContext,0)


        def defineConstantDirective(self):
            return self.getTypedRuleContext(CParser.DefineConstantDirectiveContext,0)


        def defineFunctionDirective(self):
            return self.getTypedRuleContext(CParser.DefineFunctionDirectiveContext,0)


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
        self.enterRule(localctx, 104, self.RULE_preprocessorDirective)
        try:
            self.state = 677
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 672
                self.match(CParser.LineDirective)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 673
                self.match(CParser.PragmaDirective)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 674
                self.includeDirective()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 675
                self.defineConstantDirective()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 676
                self.defineFunctionDirective()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncludeDirectiveContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.IncludeDirectiveContext, self).__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(CParser.StringLiteral, 0)

        def getRuleIndex(self):
            return CParser.RULE_includeDirective

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIncludeDirective(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIncludeDirective(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIncludeDirective(self)
            else:
                return visitor.visitChildren(self)




    def includeDirective(self):

        localctx = CParser.IncludeDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_includeDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            self.match(CParser.T__0)
            self.state = 680
            self.match(CParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefineConstantDirectiveContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DefineConstantDirectiveContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_defineConstantDirective

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDefineConstantDirective(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDefineConstantDirective(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDefineConstantDirective(self)
            else:
                return visitor.visitChildren(self)




    def defineConstantDirective(self):

        localctx = CParser.DefineConstantDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_defineConstantDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            self.match(CParser.T__1)
            self.state = 683
            self.match(CParser.Identifier)
            self.state = 684
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefineFunctionArgsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DefineFunctionArgsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i=None):
            if i is None:
                return self.getTokens(CParser.Identifier)
            else:
                return self.getToken(CParser.Identifier, i)

        def getRuleIndex(self):
            return CParser.RULE_defineFunctionArgs

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDefineFunctionArgs(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDefineFunctionArgs(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDefineFunctionArgs(self)
            else:
                return visitor.visitChildren(self)




    def defineFunctionArgs(self):

        localctx = CParser.DefineFunctionArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_defineFunctionArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 686
            self.match(CParser.LeftParen)
            self.state = 687
            self.match(CParser.Identifier)
            self.state = 690 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 688
                self.match(CParser.Comma)
                self.state = 689
                self.match(CParser.Identifier)
                self.state = 692 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.Comma):
                    break

            self.state = 694
            self.match(CParser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefineFunctionDirectiveContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DefineFunctionDirectiveContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def defineFunctionArgs(self):
            return self.getTypedRuleContext(CParser.DefineFunctionArgsContext,0)


        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_defineFunctionDirective

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDefineFunctionDirective(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDefineFunctionDirective(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDefineFunctionDirective(self)
            else:
                return visitor.visitChildren(self)




    def defineFunctionDirective(self):

        localctx = CParser.DefineFunctionDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_defineFunctionDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 696
            self.match(CParser.T__1)
            self.state = 697
            self.match(CParser.Identifier)
            self.state = 698
            self.defineFunctionArgs()
            self.state = 699
            self.expression()
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
        self._predicates[26] = self.directDeclarator_sempred
        self._predicates[32] = self.directAbstractDeclarator_sempred
        self._predicates[35] = self.initializerList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unaryExpression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

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
                return self.precpred(self._ctx, 1)
         

    def directAbstractDeclarator_sempred(self, localctx, predIndex):
            if predIndex == 16:
                return self.precpred(self._ctx, 1)
         

    def initializerList_sempred(self, localctx, predIndex):
            if predIndex == 17:
                return self.precpred(self._ctx, 1)
         



