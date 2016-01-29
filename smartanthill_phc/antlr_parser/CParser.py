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
        buf.write(u"k\u036a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\6\2\u0085\n\2\r\2\16\2\u0086\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\5\2\u0099\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5")
        buf.write(u"\2\u00a3\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2")
        buf.write(u"\u00ae\n\2\f\2\16\2\u00b1\13\2\3\3\3\3\3\3\7\3\u00b6")
        buf.write(u"\n\3\f\3\16\3\u00b9\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write(u"\u00c1\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u00e4\n\5")
        buf.write(u"\f\5\16\5\u00e7\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write(u"\u00f0\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u00f7\n\7\3\b\3\b")
        buf.write(u"\3\b\7\b\u00fc\n\b\f\b\16\b\u00ff\13\b\3\t\3\t\3\n\6")
        buf.write(u"\n\u0104\n\n\r\n\16\n\u0105\3\n\5\n\u0109\n\n\3\n\3\n")
        buf.write(u"\3\n\5\n\u010e\n\n\3\13\3\13\3\13\3\13\3\13\5\13\u0115")
        buf.write(u"\n\13\3\f\3\f\3\f\7\f\u011a\n\f\f\f\16\f\u011d\13\f\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\5\r\u0124\n\r\3\16\3\16\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\5\17\u012d\n\17\3\20\3\20\5\20\u0131")
        buf.write(u"\n\20\3\20\3\20\6\20\u0135\n\20\r\20\16\20\u0136\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\5\20\u013e\n\20\3\21\3\21\3\22\3")
        buf.write(u"\22\5\22\u0144\n\22\3\22\3\22\3\22\5\22\u0149\n\22\3")
        buf.write(u"\23\3\23\5\23\u014d\n\23\3\23\3\23\5\23\u0151\n\23\5")
        buf.write(u"\23\u0153\n\23\3\24\3\24\3\24\7\24\u0158\n\24\f\24\16")
        buf.write(u"\24\u015b\13\24\3\25\3\25\5\25\u015f\n\25\3\25\3\25\5")
        buf.write(u"\25\u0163\n\25\3\26\3\26\5\26\u0167\n\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\5\26\u016f\n\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\5\26\u0178\n\26\3\27\3\27\3\27\7\27\u017d")
        buf.write(u"\n\27\f\27\16\27\u0180\13\27\3\30\3\30\3\30\5\30\u0185")
        buf.write(u"\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\5\33\u0193\n\33\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\5\34\u019f\n\34\3\35\5\35\u01a2")
        buf.write(u"\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u01ac")
        buf.write(u"\n\36\f\36\16\36\u01af\13\36\3\36\5\36\u01b2\n\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\7\36\u01b9\n\36\f\36\16\36\u01bc")
        buf.write(u"\13\36\3\36\3\36\3\36\3\36\3\36\3\36\6\36\u01c4\n\36")
        buf.write(u"\r\36\16\36\u01c5\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\7\36\u01cf\n\36\f\36\16\36\u01d2\13\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u01de\n\36\3")
        buf.write(u"\36\7\36\u01e1\n\36\f\36\16\36\u01e4\13\36\3\37\3\37")
        buf.write(u"\7\37\u01e8\n\37\f\37\16\37\u01eb\13\37\3\37\5\37\u01ee")
        buf.write(u"\n\37\3 \3 \3 \7 \u01f3\n \f \16 \u01f6\13 \3 \3 \5 ")
        buf.write(u"\u01fa\n \3!\6!\u01fd\n!\r!\16!\u01fe\3!\3!\3!\6!\u0204")
        buf.write(u"\n!\r!\16!\u0205\3!\5!\u0209\n!\5!\u020b\n!\3\"\3\"\3")
        buf.write(u"\"\7\"\u0210\n\"\f\"\16\"\u0213\13\"\3#\3#\5#\u0217\n")
        buf.write(u"#\3$\3$\5$\u021b\n$\3$\5$\u021e\n$\3%\3%\3%\3%\3%\3%")
        buf.write(u"\3%\7%\u0227\n%\f%\16%\u022a\13%\3%\5%\u022d\n%\3%\3")
        buf.write(u"%\3%\3%\7%\u0233\n%\f%\16%\u0236\13%\3%\3%\3%\3%\3%\7")
        buf.write(u"%\u023d\n%\f%\16%\u0240\13%\3%\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write(u"%\5%\u024b\n%\3%\5%\u024e\n%\3%\3%\3%\7%\u0253\n%\f%")
        buf.write(u"\16%\u0256\13%\3%\5%\u0259\n%\3%\3%\3%\3%\3%\7%\u0260")
        buf.write(u"\n%\f%\16%\u0263\13%\3%\3%\3%\3%\3%\3%\6%\u026b\n%\r")
        buf.write(u"%\16%\u026c\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u027a")
        buf.write(u"\n%\3%\7%\u027d\n%\f%\16%\u0280\13%\3&\3&\3\'\3\'\3\'")
        buf.write(u"\3\'\5\'\u0288\n\'\3\'\3\'\5\'\u028c\n\'\3(\3(\5(\u0290")
        buf.write(u"\n(\3(\3(\3(\3(\3(\5(\u0297\n(\3(\7(\u029a\n(\f(\16(")
        buf.write(u"\u029d\13(\3)\6)\u02a0\n)\r)\16)\u02a1\3)\3)\3*\3*\3")
        buf.write(u"*\3*\3*\3*\5*\u02ac\n*\3+\3+\3+\3+\3+\6+\u02b3\n+\r+")
        buf.write(u"\16+\u02b4\3+\3+\3+\3,\3,\3,\3,\3,\3,\5,\u02c0\n,\3-")
        buf.write(u"\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u02cd\n-\3.\3.\7.\u02d1")
        buf.write(u"\n.\f.\16.\u02d4\13.\3.\3.\3/\3/\5/\u02da\n/\3\60\5\60")
        buf.write(u"\u02dd\n\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\5\61\u02e8\n\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61")
        buf.write(u"\u02f0\n\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\3\64\3\64\5\64\u0307\n\64\3\64\3\64\5\64\u030b\n\64")
        buf.write(u"\3\64\3\64\5\64\u030f\n\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\5\64\u0317\n\64\3\64\3\64\5\64\u031b\n\64\3\64\3")
        buf.write(u"\64\3\64\5\64\u0320\n\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write(u"\3\65\3\65\3\65\5\65\u032b\n\65\3\65\5\65\u032e\n\65")
        buf.write(u"\3\66\7\66\u0331\n\66\f\66\16\66\u0334\13\66\3\66\3\66")
        buf.write(u"\3\67\3\67\3\67\3\67\5\67\u033c\n\67\38\78\u033f\n8\f")
        buf.write(u"8\168\u0342\138\38\38\78\u0346\n8\f8\168\u0349\138\3")
        buf.write(u"8\38\39\39\39\39\39\59\u0352\n9\3:\3:\3:\3;\3;\3;\3;")
        buf.write(u"\3<\3<\3<\3<\6<\u035f\n<\r<\16<\u0360\3<\3<\3=\3=\3=")
        buf.write(u"\3=\3=\3=\2\7\2\b:HN>\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write(u"\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdf")
        buf.write(u"hjlnprtvx\2\17\4\2@@BB\7\2??AACCFFKL\3\2CE\4\2??AA\3")
        buf.write(u"\2=>\3\29<\3\2\\]\3\2Q[\b\2\7\7\22\22\32\32  ##\62\62")
        buf.write(u"\t\2\n\n\17\17\23\23\30\31\35\36%&,-\4\2!!$$\6\2\13\13")
        buf.write(u"\33\33\'\'++\5\2\3\3\27\27\60\60\u03c5\2\u0098\3\2\2")
        buf.write(u"\2\4\u00b2\3\2\2\2\6\u00c0\3\2\2\2\b\u00c2\3\2\2\2\n")
        buf.write(u"\u00ef\3\2\2\2\f\u00f6\3\2\2\2\16\u00f8\3\2\2\2\20\u0100")
        buf.write(u"\3\2\2\2\22\u010d\3\2\2\2\24\u0114\3\2\2\2\26\u0116\3")
        buf.write(u"\2\2\2\30\u0123\3\2\2\2\32\u0125\3\2\2\2\34\u012c\3\2")
        buf.write(u"\2\2\36\u013d\3\2\2\2 \u013f\3\2\2\2\"\u0148\3\2\2\2")
        buf.write(u"$\u0152\3\2\2\2&\u0154\3\2\2\2(\u0162\3\2\2\2*\u0177")
        buf.write(u"\3\2\2\2,\u0179\3\2\2\2.\u0181\3\2\2\2\60\u0186\3\2\2")
        buf.write(u"\2\62\u018b\3\2\2\2\64\u0192\3\2\2\2\66\u019e\3\2\2\2")
        buf.write(u"8\u01a1\3\2\2\2:\u01a5\3\2\2\2<\u01e5\3\2\2\2>\u01ef")
        buf.write(u"\3\2\2\2@\u020a\3\2\2\2B\u020c\3\2\2\2D\u0214\3\2\2\2")
        buf.write(u"F\u021d\3\2\2\2H\u024d\3\2\2\2J\u0281\3\2\2\2L\u028b")
        buf.write(u"\3\2\2\2N\u028d\3\2\2\2P\u029f\3\2\2\2R\u02ab\3\2\2\2")
        buf.write(u"T\u02ad\3\2\2\2V\u02bf\3\2\2\2X\u02cc\3\2\2\2Z\u02ce")
        buf.write(u"\3\2\2\2\\\u02d9\3\2\2\2^\u02dc\3\2\2\2`\u02ef\3\2\2")
        buf.write(u"\2b\u02f1\3\2\2\2d\u02f3\3\2\2\2f\u031f\3\2\2\2h\u032d")
        buf.write(u"\3\2\2\2j\u0332\3\2\2\2l\u033b\3\2\2\2n\u0340\3\2\2\2")
        buf.write(u"p\u0351\3\2\2\2r\u0353\3\2\2\2t\u0356\3\2\2\2v\u035a")
        buf.write(u"\3\2\2\2x\u0364\3\2\2\2z{\b\2\1\2{|\t\2\2\2|\u0099\5")
        buf.write(u"\2\2\7}~\7\37\2\2~\u0099\5\2\2\5\177\u0099\7a\2\2\u0080")
        buf.write(u"\u0099\7b\2\2\u0081\u0099\7c\2\2\u0082\u0099\7d\2\2\u0083")
        buf.write(u"\u0085\7e\2\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write(u"\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0099")
        buf.write(u"\3\2\2\2\u0088\u0089\7\63\2\2\u0089\u008a\5\16\b\2\u008a")
        buf.write(u"\u008b\7\64\2\2\u008b\u0099\3\2\2\2\u008c\u008d\t\3\2")
        buf.write(u"\2\u008d\u0099\5\6\4\2\u008e\u008f\7\37\2\2\u008f\u0090")
        buf.write(u"\7\63\2\2\u0090\u0091\5D#\2\u0091\u0092\7\64\2\2\u0092")
        buf.write(u"\u0099\3\2\2\2\u0093\u0094\7*\2\2\u0094\u0095\7\63\2")
        buf.write(u"\2\u0095\u0096\5D#\2\u0096\u0097\7\64\2\2\u0097\u0099")
        buf.write(u"\3\2\2\2\u0098z\3\2\2\2\u0098}\3\2\2\2\u0098\177\3\2")
        buf.write(u"\2\2\u0098\u0080\3\2\2\2\u0098\u0081\3\2\2\2\u0098\u0082")
        buf.write(u"\3\2\2\2\u0098\u0084\3\2\2\2\u0098\u0088\3\2\2\2\u0098")
        buf.write(u"\u008c\3\2\2\2\u0098\u008e\3\2\2\2\u0098\u0093\3\2\2")
        buf.write(u"\2\u0099\u00af\3\2\2\2\u009a\u009b\f\f\2\2\u009b\u009c")
        buf.write(u"\7\65\2\2\u009c\u009d\5\16\b\2\u009d\u009e\7\66\2\2\u009e")
        buf.write(u"\u00ae\3\2\2\2\u009f\u00a0\f\13\2\2\u00a0\u00a2\7\63")
        buf.write(u"\2\2\u00a1\u00a3\5\4\3\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3")
        buf.write(u"\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00ae\7\64\2\2\u00a5")
        buf.write(u"\u00a6\f\n\2\2\u00a6\u00a7\7_\2\2\u00a7\u00ae\7a\2\2")
        buf.write(u"\u00a8\u00a9\f\t\2\2\u00a9\u00aa\7^\2\2\u00aa\u00ae\7")
        buf.write(u"a\2\2\u00ab\u00ac\f\b\2\2\u00ac\u00ae\t\2\2\2\u00ad\u009a")
        buf.write(u"\3\2\2\2\u00ad\u009f\3\2\2\2\u00ad\u00a5\3\2\2\2\u00ad")
        buf.write(u"\u00a8\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b1\3\2\2")
        buf.write(u"\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\3\3")
        buf.write(u"\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b7\5\f\7\2\u00b3")
        buf.write(u"\u00b4\7P\2\2\u00b4\u00b6\5\f\7\2\u00b5\u00b3\3\2\2\2")
        buf.write(u"\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8")
        buf.write(u"\3\2\2\2\u00b8\5\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00c1")
        buf.write(u"\5\2\2\2\u00bb\u00bc\7\63\2\2\u00bc\u00bd\5D#\2\u00bd")
        buf.write(u"\u00be\7\64\2\2\u00be\u00bf\5\6\4\2\u00bf\u00c1\3\2\2")
        buf.write(u"\2\u00c0\u00ba\3\2\2\2\u00c0\u00bb\3\2\2\2\u00c1\7\3")
        buf.write(u"\2\2\2\u00c2\u00c3\b\5\1\2\u00c3\u00c4\5\6\4\2\u00c4")
        buf.write(u"\u00e5\3\2\2\2\u00c5\u00c6\f\f\2\2\u00c6\u00c7\t\4\2")
        buf.write(u"\2\u00c7\u00e4\5\b\5\r\u00c8\u00c9\f\13\2\2\u00c9\u00ca")
        buf.write(u"\t\5\2\2\u00ca\u00e4\5\b\5\f\u00cb\u00cc\f\n\2\2\u00cc")
        buf.write(u"\u00cd\t\6\2\2\u00cd\u00e4\5\b\5\13\u00ce\u00cf\f\t\2")
        buf.write(u"\2\u00cf\u00d0\t\7\2\2\u00d0\u00e4\5\b\5\n\u00d1\u00d2")
        buf.write(u"\f\b\2\2\u00d2\u00d3\t\b\2\2\u00d3\u00e4\5\b\5\t\u00d4")
        buf.write(u"\u00d5\f\7\2\2\u00d5\u00d6\7F\2\2\u00d6\u00e4\5\b\5\b")
        buf.write(u"\u00d7\u00d8\f\6\2\2\u00d8\u00d9\7J\2\2\u00d9\u00e4\5")
        buf.write(u"\b\5\7\u00da\u00db\f\5\2\2\u00db\u00dc\7G\2\2\u00dc\u00e4")
        buf.write(u"\5\b\5\6\u00dd\u00de\f\4\2\2\u00de\u00df\7H\2\2\u00df")
        buf.write(u"\u00e4\5\b\5\5\u00e0\u00e1\f\3\2\2\u00e1\u00e2\7I\2\2")
        buf.write(u"\u00e2\u00e4\5\b\5\4\u00e3\u00c5\3\2\2\2\u00e3\u00c8")
        buf.write(u"\3\2\2\2\u00e3\u00cb\3\2\2\2\u00e3\u00ce\3\2\2\2\u00e3")
        buf.write(u"\u00d1\3\2\2\2\u00e3\u00d4\3\2\2\2\u00e3\u00d7\3\2\2")
        buf.write(u"\2\u00e3\u00da\3\2\2\2\u00e3\u00dd\3\2\2\2\u00e3\u00e0")
        buf.write(u"\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5")
        buf.write(u"\u00e6\3\2\2\2\u00e6\t\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8")
        buf.write(u"\u00f0\5\b\5\2\u00e9\u00ea\5\b\5\2\u00ea\u00eb\7M\2\2")
        buf.write(u"\u00eb\u00ec\5\16\b\2\u00ec\u00ed\7N\2\2\u00ed\u00ee")
        buf.write(u"\5\n\6\2\u00ee\u00f0\3\2\2\2\u00ef\u00e8\3\2\2\2\u00ef")
        buf.write(u"\u00e9\3\2\2\2\u00f0\13\3\2\2\2\u00f1\u00f7\5\n\6\2\u00f2")
        buf.write(u"\u00f3\5\2\2\2\u00f3\u00f4\t\t\2\2\u00f4\u00f5\5\f\7")
        buf.write(u"\2\u00f5\u00f7\3\2\2\2\u00f6\u00f1\3\2\2\2\u00f6\u00f2")
        buf.write(u"\3\2\2\2\u00f7\r\3\2\2\2\u00f8\u00fd\5\f\7\2\u00f9\u00fa")
        buf.write(u"\7P\2\2\u00fa\u00fc\5\f\7\2\u00fb\u00f9\3\2\2\2\u00fc")
        buf.write(u"\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2")
        buf.write(u"\2\u00fe\17\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101\5")
        buf.write(u"\n\6\2\u0101\21\3\2\2\2\u0102\u0104\5\24\13\2\u0103\u0102")
        buf.write(u"\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0103\3\2\2\2\u0105")
        buf.write(u"\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107\u0109\5\26\f")
        buf.write(u"\2\u0108\u0107\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a")
        buf.write(u"\3\2\2\2\u010a\u010b\7O\2\2\u010b\u010e\3\2\2\2\u010c")
        buf.write(u"\u010e\5T+\2\u010d\u0103\3\2\2\2\u010d\u010c\3\2\2\2")
        buf.write(u"\u010e\23\3\2\2\2\u010f\u0115\5\32\16\2\u0110\u0115\5")
        buf.write(u"\34\17\2\u0111\u0115\5\62\32\2\u0112\u0115\5\64\33\2")
        buf.write(u"\u0113\u0115\5\66\34\2\u0114\u010f\3\2\2\2\u0114\u0110")
        buf.write(u"\3\2\2\2\u0114\u0111\3\2\2\2\u0114\u0112\3\2\2\2\u0114")
        buf.write(u"\u0113\3\2\2\2\u0115\25\3\2\2\2\u0116\u011b\5\30\r\2")
        buf.write(u"\u0117\u0118\7P\2\2\u0118\u011a\5\30\r\2\u0119\u0117")
        buf.write(u"\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b")
        buf.write(u"\u011c\3\2\2\2\u011c\27\3\2\2\2\u011d\u011b\3\2\2\2\u011e")
        buf.write(u"\u0124\58\35\2\u011f\u0120\58\35\2\u0120\u0121\7Q\2\2")
        buf.write(u"\u0121\u0122\5L\'\2\u0122\u0124\3\2\2\2\u0123\u011e\3")
        buf.write(u"\2\2\2\u0123\u011f\3\2\2\2\u0124\31\3\2\2\2\u0125\u0126")
        buf.write(u"\t\n\2\2\u0126\33\3\2\2\2\u0127\u012d\t\13\2\2\u0128")
        buf.write(u"\u012d\5\60\31\2\u0129\u012d\5\36\20\2\u012a\u012d\5")
        buf.write(u"*\26\2\u012b\u012d\5J&\2\u012c\u0127\3\2\2\2\u012c\u0128")
        buf.write(u"\3\2\2\2\u012c\u0129\3\2\2\2\u012c\u012a\3\2\2\2\u012c")
        buf.write(u"\u012b\3\2\2\2\u012d\35\3\2\2\2\u012e\u0130\5 \21\2\u012f")
        buf.write(u"\u0131\7a\2\2\u0130\u012f\3\2\2\2\u0130\u0131\3\2\2\2")
        buf.write(u"\u0131\u0132\3\2\2\2\u0132\u0134\7\67\2\2\u0133\u0135")
        buf.write(u"\5\"\22\2\u0134\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write(u"\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2")
        buf.write(u"\2\u0138\u0139\78\2\2\u0139\u013e\3\2\2\2\u013a\u013b")
        buf.write(u"\5 \21\2\u013b\u013c\7a\2\2\u013c\u013e\3\2\2\2\u013d")
        buf.write(u"\u012e\3\2\2\2\u013d\u013a\3\2\2\2\u013e\37\3\2\2\2\u013f")
        buf.write(u"\u0140\t\f\2\2\u0140!\3\2\2\2\u0141\u0143\5$\23\2\u0142")
        buf.write(u"\u0144\5&\24\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2\2")
        buf.write(u"\2\u0144\u0145\3\2\2\2\u0145\u0146\7O\2\2\u0146\u0149")
        buf.write(u"\3\2\2\2\u0147\u0149\5T+\2\u0148\u0141\3\2\2\2\u0148")
        buf.write(u"\u0147\3\2\2\2\u0149#\3\2\2\2\u014a\u014c\5\34\17\2\u014b")
        buf.write(u"\u014d\5$\23\2\u014c\u014b\3\2\2\2\u014c\u014d\3\2\2")
        buf.write(u"\2\u014d\u0153\3\2\2\2\u014e\u0150\5\62\32\2\u014f\u0151")
        buf.write(u"\5$\23\2\u0150\u014f\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write(u"\u0153\3\2\2\2\u0152\u014a\3\2\2\2\u0152\u014e\3\2\2")
        buf.write(u"\2\u0153%\3\2\2\2\u0154\u0159\5(\25\2\u0155\u0156\7P")
        buf.write(u"\2\2\u0156\u0158\5(\25\2\u0157\u0155\3\2\2\2\u0158\u015b")
        buf.write(u"\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write(u"\'\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u0163\58\35\2\u015d")
        buf.write(u"\u015f\58\35\2\u015e\u015d\3\2\2\2\u015e\u015f\3\2\2")
        buf.write(u"\2\u015f\u0160\3\2\2\2\u0160\u0161\7N\2\2\u0161\u0163")
        buf.write(u"\5\20\t\2\u0162\u015c\3\2\2\2\u0162\u015e\3\2\2\2\u0163")
        buf.write(u")\3\2\2\2\u0164\u0166\7\21\2\2\u0165\u0167\7a\2\2\u0166")
        buf.write(u"\u0165\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\3\2\2")
        buf.write(u"\2\u0168\u0169\7\67\2\2\u0169\u016a\5,\27\2\u016a\u016b")
        buf.write(u"\78\2\2\u016b\u0178\3\2\2\2\u016c\u016e\7\21\2\2\u016d")
        buf.write(u"\u016f\7a\2\2\u016e\u016d\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write(u"\u016f\u0170\3\2\2\2\u0170\u0171\7\67\2\2\u0171\u0172")
        buf.write(u"\5,\27\2\u0172\u0173\7P\2\2\u0173\u0174\78\2\2\u0174")
        buf.write(u"\u0178\3\2\2\2\u0175\u0176\7\21\2\2\u0176\u0178\7a\2")
        buf.write(u"\2\u0177\u0164\3\2\2\2\u0177\u016c\3\2\2\2\u0177\u0175")
        buf.write(u"\3\2\2\2\u0178+\3\2\2\2\u0179\u017e\5.\30\2\u017a\u017b")
        buf.write(u"\7P\2\2\u017b\u017d\5.\30\2\u017c\u017a\3\2\2\2\u017d")
        buf.write(u"\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2")
        buf.write(u"\2\u017f-\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0184\7a")
        buf.write(u"\2\2\u0182\u0183\7Q\2\2\u0183\u0185\5\20\t\2\u0184\u0182")
        buf.write(u"\3\2\2\2\u0184\u0185\3\2\2\2\u0185/\3\2\2\2\u0186\u0187")
        buf.write(u"\7+\2\2\u0187\u0188\7\63\2\2\u0188\u0189\5D#\2\u0189")
        buf.write(u"\u018a\7\64\2\2\u018a\61\3\2\2\2\u018b\u018c\t\r\2\2")
        buf.write(u"\u018c\63\3\2\2\2\u018d\u0193\t\16\2\2\u018e\u018f\7")
        buf.write(u"\4\2\2\u018f\u0190\7\63\2\2\u0190\u0191\7a\2\2\u0191")
        buf.write(u"\u0193\7\64\2\2\u0192\u018d\3\2\2\2\u0192\u018e\3\2\2")
        buf.write(u"\2\u0193\65\3\2\2\2\u0194\u0195\7)\2\2\u0195\u0196\7")
        buf.write(u"\63\2\2\u0196\u0197\5D#\2\u0197\u0198\7\64\2\2\u0198")
        buf.write(u"\u019f\3\2\2\2\u0199\u019a\7)\2\2\u019a\u019b\7\63\2")
        buf.write(u"\2\u019b\u019c\5\20\t\2\u019c\u019d\7\64\2\2\u019d\u019f")
        buf.write(u"\3\2\2\2\u019e\u0194\3\2\2\2\u019e\u0199\3\2\2\2\u019f")
        buf.write(u"\67\3\2\2\2\u01a0\u01a2\5<\37\2\u01a1\u01a0\3\2\2\2\u01a1")
        buf.write(u"\u01a2\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\5:\36")
        buf.write(u"\2\u01a49\3\2\2\2\u01a5\u01a6\b\36\1\2\u01a6\u01a7\7")
        buf.write(u"a\2\2\u01a7\u01e2\3\2\2\2\u01a8\u01a9\f\b\2\2\u01a9\u01ad")
        buf.write(u"\7\65\2\2\u01aa\u01ac\5\62\32\2\u01ab\u01aa\3\2\2\2\u01ac")
        buf.write(u"\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2")
        buf.write(u"\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b2")
        buf.write(u"\5\f\7\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write(u"\u01b3\3\2\2\2\u01b3\u01e1\7\66\2\2\u01b4\u01b5\f\7\2")
        buf.write(u"\2\u01b5\u01b6\7\65\2\2\u01b6\u01ba\7 \2\2\u01b7\u01b9")
        buf.write(u"\5\62\32\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba")
        buf.write(u"\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd\3\2\2")
        buf.write(u"\2\u01bc\u01ba\3\2\2\2\u01bd\u01be\5\f\7\2\u01be\u01bf")
        buf.write(u"\7\66\2\2\u01bf\u01e1\3\2\2\2\u01c0\u01c1\f\6\2\2\u01c1")
        buf.write(u"\u01c3\7\65\2\2\u01c2\u01c4\5\62\32\2\u01c3\u01c2\3\2")
        buf.write(u"\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6")
        buf.write(u"\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\7 \2\2\u01c8")
        buf.write(u"\u01c9\5\f\7\2\u01c9\u01ca\7\66\2\2\u01ca\u01e1\3\2\2")
        buf.write(u"\2\u01cb\u01cc\f\5\2\2\u01cc\u01d0\7\65\2\2\u01cd\u01cf")
        buf.write(u"\5\62\32\2\u01ce\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0")
        buf.write(u"\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d3\3\2\2")
        buf.write(u"\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\7C\2\2\u01d4\u01e1")
        buf.write(u"\7\66\2\2\u01d5\u01d6\f\4\2\2\u01d6\u01d7\7\63\2\2\u01d7")
        buf.write(u"\u01d8\5> \2\u01d8\u01d9\7\64\2\2\u01d9\u01e1\3\2\2\2")
        buf.write(u"\u01da\u01db\f\3\2\2\u01db\u01dd\7\63\2\2\u01dc\u01de")
        buf.write(u"\5B\"\2\u01dd\u01dc\3\2\2\2\u01dd\u01de\3\2\2\2\u01de")
        buf.write(u"\u01df\3\2\2\2\u01df\u01e1\7\64\2\2\u01e0\u01a8\3\2\2")
        buf.write(u"\2\u01e0\u01b4\3\2\2\2\u01e0\u01c0\3\2\2\2\u01e0\u01cb")
        buf.write(u"\3\2\2\2\u01e0\u01d5\3\2\2\2\u01e0\u01da\3\2\2\2\u01e1")
        buf.write(u"\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2")
        buf.write(u"\2\u01e3;\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e9\7C")
        buf.write(u"\2\2\u01e6\u01e8\5\62\32\2\u01e7\u01e6\3\2\2\2\u01e8")
        buf.write(u"\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2")
        buf.write(u"\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9\3\2\2\2\u01ec\u01ee")
        buf.write(u"\5<\37\2\u01ed\u01ec\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee")
        buf.write(u"=\3\2\2\2\u01ef\u01f4\5@!\2\u01f0\u01f1\7P\2\2\u01f1")
        buf.write(u"\u01f3\5@!\2\u01f2\u01f0\3\2\2\2\u01f3\u01f6\3\2\2\2")
        buf.write(u"\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f9")
        buf.write(u"\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8\7P\2\2\u01f8")
        buf.write(u"\u01fa\7`\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2")
        buf.write(u"\u01fa?\3\2\2\2\u01fb\u01fd\5\24\13\2\u01fc\u01fb\3\2")
        buf.write(u"\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff")
        buf.write(u"\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0201\58\35\2\u0201")
        buf.write(u"\u020b\3\2\2\2\u0202\u0204\5\24\13\2\u0203\u0202\3\2")
        buf.write(u"\2\2\u0204\u0205\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206")
        buf.write(u"\3\2\2\2\u0206\u0208\3\2\2\2\u0207\u0209\5F$\2\u0208")
        buf.write(u"\u0207\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020b\3\2\2")
        buf.write(u"\2\u020a\u01fc\3\2\2\2\u020a\u0203\3\2\2\2\u020bA\3\2")
        buf.write(u"\2\2\u020c\u0211\7a\2\2\u020d\u020e\7P\2\2\u020e\u0210")
        buf.write(u"\7a\2\2\u020f\u020d\3\2\2\2\u0210\u0213\3\2\2\2\u0211")
        buf.write(u"\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212C\3\2\2\2\u0213")
        buf.write(u"\u0211\3\2\2\2\u0214\u0216\5$\23\2\u0215\u0217\5F$\2")
        buf.write(u"\u0216\u0215\3\2\2\2\u0216\u0217\3\2\2\2\u0217E\3\2\2")
        buf.write(u"\2\u0218\u021e\5<\37\2\u0219\u021b\5<\37\2\u021a\u0219")
        buf.write(u"\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021c\3\2\2\2\u021c")
        buf.write(u"\u021e\5H%\2\u021d\u0218\3\2\2\2\u021d\u021a\3\2\2\2")
        buf.write(u"\u021eG\3\2\2\2\u021f\u0220\b%\1\2\u0220\u0221\7\63\2")
        buf.write(u"\2\u0221\u0222\5F$\2\u0222\u0223\7\64\2\2\u0223\u024e")
        buf.write(u"\3\2\2\2\u0224\u0228\7\65\2\2\u0225\u0227\5\62\32\2\u0226")
        buf.write(u"\u0225\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2")
        buf.write(u"\2\u0228\u0229\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228")
        buf.write(u"\3\2\2\2\u022b\u022d\5\f\7\2\u022c\u022b\3\2\2\2\u022c")
        buf.write(u"\u022d\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u024e\7\66\2")
        buf.write(u"\2\u022f\u0230\7\65\2\2\u0230\u0234\7 \2\2\u0231\u0233")
        buf.write(u"\5\62\32\2\u0232\u0231\3\2\2\2\u0233\u0236\3\2\2\2\u0234")
        buf.write(u"\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0237\3\2\2")
        buf.write(u"\2\u0236\u0234\3\2\2\2\u0237\u0238\5\f\7\2\u0238\u0239")
        buf.write(u"\7\66\2\2\u0239\u024e\3\2\2\2\u023a\u023e\7\65\2\2\u023b")
        buf.write(u"\u023d\5\62\32\2\u023c\u023b\3\2\2\2\u023d\u0240\3\2")
        buf.write(u"\2\2\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0241")
        buf.write(u"\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0242\7 \2\2\u0242")
        buf.write(u"\u0243\5\f\7\2\u0243\u0244\7\66\2\2\u0244\u024e\3\2\2")
        buf.write(u"\2\u0245\u0246\7\65\2\2\u0246\u0247\7C\2\2\u0247\u024e")
        buf.write(u"\7\66\2\2\u0248\u024a\7\63\2\2\u0249\u024b\5> \2\u024a")
        buf.write(u"\u0249\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024c\3\2\2")
        buf.write(u"\2\u024c\u024e\7\64\2\2\u024d\u021f\3\2\2\2\u024d\u0224")
        buf.write(u"\3\2\2\2\u024d\u022f\3\2\2\2\u024d\u023a\3\2\2\2\u024d")
        buf.write(u"\u0245\3\2\2\2\u024d\u0248\3\2\2\2\u024e\u027e\3\2\2")
        buf.write(u"\2\u024f\u0250\f\7\2\2\u0250\u0254\7\65\2\2\u0251\u0253")
        buf.write(u"\5\62\32\2\u0252\u0251\3\2\2\2\u0253\u0256\3\2\2\2\u0254")
        buf.write(u"\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0258\3\2\2")
        buf.write(u"\2\u0256\u0254\3\2\2\2\u0257\u0259\5\f\7\2\u0258\u0257")
        buf.write(u"\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025a\3\2\2\2\u025a")
        buf.write(u"\u027d\7\66\2\2\u025b\u025c\f\6\2\2\u025c\u025d\7\65")
        buf.write(u"\2\2\u025d\u0261\7 \2\2\u025e\u0260\5\62\32\2\u025f\u025e")
        buf.write(u"\3\2\2\2\u0260\u0263\3\2\2\2\u0261\u025f\3\2\2\2\u0261")
        buf.write(u"\u0262\3\2\2\2\u0262\u0264\3\2\2\2\u0263\u0261\3\2\2")
        buf.write(u"\2\u0264\u0265\5\f\7\2\u0265\u0266\7\66\2\2\u0266\u027d")
        buf.write(u"\3\2\2\2\u0267\u0268\f\5\2\2\u0268\u026a\7\65\2\2\u0269")
        buf.write(u"\u026b\5\62\32\2\u026a\u0269\3\2\2\2\u026b\u026c\3\2")
        buf.write(u"\2\2\u026c\u026a\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u026e")
        buf.write(u"\3\2\2\2\u026e\u026f\7 \2\2\u026f\u0270\5\f\7\2\u0270")
        buf.write(u"\u0271\7\66\2\2\u0271\u027d\3\2\2\2\u0272\u0273\f\4\2")
        buf.write(u"\2\u0273\u0274\7\65\2\2\u0274\u0275\7C\2\2\u0275\u027d")
        buf.write(u"\7\66\2\2\u0276\u0277\f\3\2\2\u0277\u0279\7\63\2\2\u0278")
        buf.write(u"\u027a\5> \2\u0279\u0278\3\2\2\2\u0279\u027a\3\2\2\2")
        buf.write(u"\u027a\u027b\3\2\2\2\u027b\u027d\7\64\2\2\u027c\u024f")
        buf.write(u"\3\2\2\2\u027c\u025b\3\2\2\2\u027c\u0267\3\2\2\2\u027c")
        buf.write(u"\u0272\3\2\2\2\u027c\u0276\3\2\2\2\u027d\u0280\3\2\2")
        buf.write(u"\2\u027e\u027c\3\2\2\2\u027e\u027f\3\2\2\2\u027fI\3\2")
        buf.write(u"\2\2\u0280\u027e\3\2\2\2\u0281\u0282\7a\2\2\u0282K\3")
        buf.write(u"\2\2\2\u0283\u028c\5\f\7\2\u0284\u0285\7\67\2\2\u0285")
        buf.write(u"\u0287\5N(\2\u0286\u0288\7P\2\2\u0287\u0286\3\2\2\2\u0287")
        buf.write(u"\u0288\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a\78\2\2")
        buf.write(u"\u028a\u028c\3\2\2\2\u028b\u0283\3\2\2\2\u028b\u0284")
        buf.write(u"\3\2\2\2\u028cM\3\2\2\2\u028d\u028f\b(\1\2\u028e\u0290")
        buf.write(u"\5P)\2\u028f\u028e\3\2\2\2\u028f\u0290\3\2\2\2\u0290")
        buf.write(u"\u0291\3\2\2\2\u0291\u0292\5L\'\2\u0292\u029b\3\2\2\2")
        buf.write(u"\u0293\u0294\f\3\2\2\u0294\u0296\7P\2\2\u0295\u0297\5")
        buf.write(u"P)\2\u0296\u0295\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0298")
        buf.write(u"\3\2\2\2\u0298\u029a\5L\'\2\u0299\u0293\3\2\2\2\u029a")
        buf.write(u"\u029d\3\2\2\2\u029b\u0299\3\2\2\2\u029b\u029c\3\2\2")
        buf.write(u"\2\u029cO\3\2\2\2\u029d\u029b\3\2\2\2\u029e\u02a0\5R")
        buf.write(u"*\2\u029f\u029e\3\2\2\2\u02a0\u02a1\3\2\2\2\u02a1\u029f")
        buf.write(u"\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u02a3\3\2\2\2\u02a3")
        buf.write(u"\u02a4\7Q\2\2\u02a4Q\3\2\2\2\u02a5\u02a6\7\65\2\2\u02a6")
        buf.write(u"\u02a7\5\20\t\2\u02a7\u02a8\7\66\2\2\u02a8\u02ac\3\2")
        buf.write(u"\2\2\u02a9\u02aa\7_\2\2\u02aa\u02ac\7a\2\2\u02ab\u02a5")
        buf.write(u"\3\2\2\2\u02ab\u02a9\3\2\2\2\u02acS\3\2\2\2\u02ad\u02ae")
        buf.write(u"\7\61\2\2\u02ae\u02af\7\63\2\2\u02af\u02b0\5\20\t\2\u02b0")
        buf.write(u"\u02b2\7P\2\2\u02b1\u02b3\7e\2\2\u02b2\u02b1\3\2\2\2")
        buf.write(u"\u02b3\u02b4\3\2\2\2\u02b4\u02b2\3\2\2\2\u02b4\u02b5")
        buf.write(u"\3\2\2\2\u02b5\u02b6\3\2\2\2\u02b6\u02b7\7\64\2\2\u02b7")
        buf.write(u"\u02b8\7O\2\2\u02b8U\3\2\2\2\u02b9\u02c0\5X-\2\u02ba")
        buf.write(u"\u02c0\5Z.\2\u02bb\u02c0\5^\60\2\u02bc\u02c0\5`\61\2")
        buf.write(u"\u02bd\u02c0\5f\64\2\u02be\u02c0\5h\65\2\u02bf\u02b9")
        buf.write(u"\3\2\2\2\u02bf\u02ba\3\2\2\2\u02bf\u02bb\3\2\2\2\u02bf")
        buf.write(u"\u02bc\3\2\2\2\u02bf\u02bd\3\2\2\2\u02bf\u02be\3\2\2")
        buf.write(u"\2\u02c0W\3\2\2\2\u02c1\u02c2\7a\2\2\u02c2\u02c3\7N\2")
        buf.write(u"\2\u02c3\u02cd\5V,\2\u02c4\u02c5\7\t\2\2\u02c5\u02c6")
        buf.write(u"\5\20\t\2\u02c6\u02c7\7N\2\2\u02c7\u02c8\5V,\2\u02c8")
        buf.write(u"\u02cd\3\2\2\2\u02c9\u02ca\7\r\2\2\u02ca\u02cb\7N\2\2")
        buf.write(u"\u02cb\u02cd\5V,\2\u02cc\u02c1\3\2\2\2\u02cc\u02c4\3")
        buf.write(u"\2\2\2\u02cc\u02c9\3\2\2\2\u02cdY\3\2\2\2\u02ce\u02d2")
        buf.write(u"\7\67\2\2\u02cf\u02d1\5\\/\2\u02d0\u02cf\3\2\2\2\u02d1")
        buf.write(u"\u02d4\3\2\2\2\u02d2\u02d0\3\2\2\2\u02d2\u02d3\3\2\2")
        buf.write(u"\2\u02d3\u02d5\3\2\2\2\u02d4\u02d2\3\2\2\2\u02d5\u02d6")
        buf.write(u"\78\2\2\u02d6[\3\2\2\2\u02d7\u02da\5\22\n\2\u02d8\u02da")
        buf.write(u"\5V,\2\u02d9\u02d7\3\2\2\2\u02d9\u02d8\3\2\2\2\u02da")
        buf.write(u"]\3\2\2\2\u02db\u02dd\5\16\b\2\u02dc\u02db\3\2\2\2\u02dc")
        buf.write(u"\u02dd\3\2\2\2\u02dd\u02de\3\2\2\2\u02de\u02df\7O\2\2")
        buf.write(u"\u02df_\3\2\2\2\u02e0\u02e1\7\26\2\2\u02e1\u02e2\7\63")
        buf.write(u"\2\2\u02e2\u02e3\5\16\b\2\u02e3\u02e4\7\64\2\2\u02e4")
        buf.write(u"\u02e7\5V,\2\u02e5\u02e6\7\20\2\2\u02e6\u02e8\5V,\2\u02e7")
        buf.write(u"\u02e5\3\2\2\2\u02e7\u02e8\3\2\2\2\u02e8\u02f0\3\2\2")
        buf.write(u"\2\u02e9\u02ea\7\"\2\2\u02ea\u02eb\7\63\2\2\u02eb\u02ec")
        buf.write(u"\5\16\b\2\u02ec\u02ed\7\64\2\2\u02ed\u02ee\5V,\2\u02ee")
        buf.write(u"\u02f0\3\2\2\2\u02ef\u02e0\3\2\2\2\u02ef\u02e9\3\2\2")
        buf.write(u"\2\u02f0a\3\2\2\2\u02f1\u02f2\5\16\b\2\u02f2c\3\2\2\2")
        buf.write(u"\u02f3\u02f4\5\16\b\2\u02f4e\3\2\2\2\u02f5\u02f6\7(\2")
        buf.write(u"\2\u02f6\u02f7\7\63\2\2\u02f7\u02f8\5\16\b\2\u02f8\u02f9")
        buf.write(u"\7\64\2\2\u02f9\u02fa\5V,\2\u02fa\u0320\3\2\2\2\u02fb")
        buf.write(u"\u02fc\7\16\2\2\u02fc\u02fd\5V,\2\u02fd\u02fe\7(\2\2")
        buf.write(u"\u02fe\u02ff\7\63\2\2\u02ff\u0300\5\16\b\2\u0300\u0301")
        buf.write(u"\7\64\2\2\u0301\u0302\7O\2\2\u0302\u0320\3\2\2\2\u0303")
        buf.write(u"\u0304\7\24\2\2\u0304\u0306\7\63\2\2\u0305\u0307\5b\62")
        buf.write(u"\2\u0306\u0305\3\2\2\2\u0306\u0307\3\2\2\2\u0307\u0308")
        buf.write(u"\3\2\2\2\u0308\u030a\7O\2\2\u0309\u030b\5\16\b\2\u030a")
        buf.write(u"\u0309\3\2\2\2\u030a\u030b\3\2\2\2\u030b\u030c\3\2\2")
        buf.write(u"\2\u030c\u030e\7O\2\2\u030d\u030f\5d\63\2\u030e\u030d")
        buf.write(u"\3\2\2\2\u030e\u030f\3\2\2\2\u030f\u0310\3\2\2\2\u0310")
        buf.write(u"\u0311\7\64\2\2\u0311\u0320\5V,\2\u0312\u0313\7\24\2")
        buf.write(u"\2\u0313\u0314\7\63\2\2\u0314\u0316\5\22\n\2\u0315\u0317")
        buf.write(u"\5\16\b\2\u0316\u0315\3\2\2\2\u0316\u0317\3\2\2\2\u0317")
        buf.write(u"\u0318\3\2\2\2\u0318\u031a\7O\2\2\u0319\u031b\5d\63\2")
        buf.write(u"\u031a\u0319\3\2\2\2\u031a\u031b\3\2\2\2\u031b\u031c")
        buf.write(u"\3\2\2\2\u031c\u031d\7\64\2\2\u031d\u031e\5V,\2\u031e")
        buf.write(u"\u0320\3\2\2\2\u031f\u02f5\3\2\2\2\u031f\u02fb\3\2\2")
        buf.write(u"\2\u031f\u0303\3\2\2\2\u031f\u0312\3\2\2\2\u0320g\3\2")
        buf.write(u"\2\2\u0321\u0322\7\25\2\2\u0322\u0323\7a\2\2\u0323\u032e")
        buf.write(u"\7O\2\2\u0324\u0325\7\f\2\2\u0325\u032e\7O\2\2\u0326")
        buf.write(u"\u0327\7\b\2\2\u0327\u032e\7O\2\2\u0328\u032a\7\34\2")
        buf.write(u"\2\u0329\u032b\5\16\b\2\u032a\u0329\3\2\2\2\u032a\u032b")
        buf.write(u"\3\2\2\2\u032b\u032c\3\2\2\2\u032c\u032e\7O\2\2\u032d")
        buf.write(u"\u0321\3\2\2\2\u032d\u0324\3\2\2\2\u032d\u0326\3\2\2")
        buf.write(u"\2\u032d\u0328\3\2\2\2\u032ei\3\2\2\2\u032f\u0331\5l")
        buf.write(u"\67\2\u0330\u032f\3\2\2\2\u0331\u0334\3\2\2\2\u0332\u0330")
        buf.write(u"\3\2\2\2\u0332\u0333\3\2\2\2\u0333\u0335\3\2\2\2\u0334")
        buf.write(u"\u0332\3\2\2\2\u0335\u0336\7\2\2\3\u0336k\3\2\2\2\u0337")
        buf.write(u"\u033c\5n8\2\u0338\u033c\5\22\n\2\u0339\u033c\5p9\2\u033a")
        buf.write(u"\u033c\7O\2\2\u033b\u0337\3\2\2\2\u033b\u0338\3\2\2\2")
        buf.write(u"\u033b\u0339\3\2\2\2\u033b\u033a\3\2\2\2\u033cm\3\2\2")
        buf.write(u"\2\u033d\u033f\5\24\13\2\u033e\u033d\3\2\2\2\u033f\u0342")
        buf.write(u"\3\2\2\2\u0340\u033e\3\2\2\2\u0340\u0341\3\2\2\2\u0341")
        buf.write(u"\u0343\3\2\2\2\u0342\u0340\3\2\2\2\u0343\u0347\58\35")
        buf.write(u"\2\u0344\u0346\5\22\n\2\u0345\u0344\3\2\2\2\u0346\u0349")
        buf.write(u"\3\2\2\2\u0347\u0345\3\2\2\2\u0347\u0348\3\2\2\2\u0348")
        buf.write(u"\u034a\3\2\2\2\u0349\u0347\3\2\2\2\u034a\u034b\5Z.\2")
        buf.write(u"\u034bo\3\2\2\2\u034c\u0352\7f\2\2\u034d\u0352\7g\2\2")
        buf.write(u"\u034e\u0352\5r:\2\u034f\u0352\5t;\2\u0350\u0352\5x=")
        buf.write(u"\2\u0351\u034c\3\2\2\2\u0351\u034d\3\2\2\2\u0351\u034e")
        buf.write(u"\3\2\2\2\u0351\u034f\3\2\2\2\u0351\u0350\3\2\2\2\u0352")
        buf.write(u"q\3\2\2\2\u0353\u0354\7\5\2\2\u0354\u0355\7e\2\2\u0355")
        buf.write(u"s\3\2\2\2\u0356\u0357\7\6\2\2\u0357\u0358\7a\2\2\u0358")
        buf.write(u"\u0359\5\16\b\2\u0359u\3\2\2\2\u035a\u035b\7\63\2\2\u035b")
        buf.write(u"\u035e\7a\2\2\u035c\u035d\7P\2\2\u035d\u035f\7a\2\2\u035e")
        buf.write(u"\u035c\3\2\2\2\u035f\u0360\3\2\2\2\u0360\u035e\3\2\2")
        buf.write(u"\2\u0360\u0361\3\2\2\2\u0361\u0362\3\2\2\2\u0362\u0363")
        buf.write(u"\7\64\2\2\u0363w\3\2\2\2\u0364\u0365\7\6\2\2\u0365\u0366")
        buf.write(u"\7a\2\2\u0366\u0367\5v<\2\u0367\u0368\5\16\b\2\u0368")
        buf.write(u"y\3\2\2\2f\u0086\u0098\u00a2\u00ad\u00af\u00b7\u00c0")
        buf.write(u"\u00e3\u00e5\u00ef\u00f6\u00fd\u0105\u0108\u010d\u0114")
        buf.write(u"\u011b\u0123\u012c\u0130\u0136\u013d\u0143\u0148\u014c")
        buf.write(u"\u0150\u0152\u0159\u015e\u0162\u0166\u016e\u0177\u017e")
        buf.write(u"\u0184\u0192\u019e\u01a1\u01ad\u01b1\u01ba\u01c5\u01d0")
        buf.write(u"\u01dd\u01e0\u01e2\u01e9\u01ed\u01f4\u01f9\u01fe\u0205")
        buf.write(u"\u0208\u020a\u0211\u0216\u021a\u021d\u0228\u022c\u0234")
        buf.write(u"\u023e\u024a\u024d\u0254\u0258\u0261\u026c\u0279\u027c")
        buf.write(u"\u027e\u0287\u028b\u028f\u0296\u029b\u02a1\u02ab\u02b4")
        buf.write(u"\u02bf\u02cc\u02d2\u02d9\u02dc\u02e7\u02ef\u0306\u030a")
        buf.write(u"\u030e\u0316\u031a\u031f\u032a\u032d\u0332\u033b\u0340")
        buf.write(u"\u0347\u0351\u0360")
        return buf.getvalue()


class CParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'__stdcall'", u"'__declspec'", u"'#include'", 
                     u"'#define'", u"'auto'", u"'break'", u"'case'", u"'char'", 
                     u"'const'", u"'continue'", u"'default'", u"'do'", u"'double'", 
                     u"'else'", u"'enum'", u"'extern'", u"'float'", u"'for'", 
                     u"'goto'", u"'if'", u"'inline'", u"'int'", u"'long'", 
                     u"'register'", u"'restrict'", u"'return'", u"'short'", 
                     u"'signed'", u"'sizeof'", u"'static'", u"'struct'", 
                     u"'switch'", u"'typedef'", u"'union'", u"'unsigned'", 
                     u"'void'", u"'volatile'", u"'while'", u"'_Alignas'", 
                     u"'_Alignof'", u"'_Atomic'", u"'_Bool'", u"'_Complex'", 
                     u"'_Generic'", u"'_Imaginary'", u"'_Noreturn'", u"'_Static_assert'", 
                     u"'_Thread_local'", u"'('", u"')'", u"'['", u"']'", 
                     u"'{'", u"'}'", u"'<'", u"'<='", u"'>'", u"'>='", u"'<<'", 
                     u"'>>'", u"'+'", u"'++'", u"'-'", u"'--'", u"'*'", 
                     u"'/'", u"'%'", u"'&'", u"'|'", u"'&&'", u"'||'", u"'^'", 
                     u"'!'", u"'~'", u"'?'", u"':'", u"';'", u"','", u"'='", 
                     u"'*='", u"'/='", u"'%='", u"'+='", u"'-='", u"'<<='", 
                     u"'>>='", u"'&='", u"'^='", u"'|='", u"'=='", u"'!='", 
                     u"'->'", u"'.'", u"'...'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"Auto", u"Break", u"Case", u"Char", 
                      u"Const", u"Continue", u"Default", u"Do", u"Double", 
                      u"Else", u"Enum", u"Extern", u"Float", u"For", u"Goto", 
                      u"If", u"Inline", u"Int", u"Long", u"Register", u"Restrict", 
                      u"Return", u"Short", u"Signed", u"Sizeof", u"Static", 
                      u"Struct", u"Switch", u"Typedef", u"Union", u"Unsigned", 
                      u"Void", u"Volatile", u"While", u"Alignas", u"Alignof", 
                      u"Atomic", u"Bool", u"Complex", u"Generic", u"Imaginary", 
                      u"Noreturn", u"StaticAssert", u"ThreadLocal", u"LeftParen", 
                      u"RightParen", u"LeftBracket", u"RightBracket", u"LeftBrace", 
                      u"RightBrace", u"Less", u"LessEqual", u"Greater", 
                      u"GreaterEqual", u"LeftShift", u"RightShift", u"Plus", 
                      u"PlusPlus", u"Minus", u"MinusMinus", u"Star", u"Div", 
                      u"Mod", u"And", u"Or", u"AndAnd", u"OrOr", u"Caret", 
                      u"Not", u"Tilde", u"Question", u"Colon", u"Semi", 
                      u"Comma", u"Assign", u"StarAssign", u"DivAssign", 
                      u"ModAssign", u"PlusAssign", u"MinusAssign", u"LeftShiftAssign", 
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
    RULE_includeDirective = 56
    RULE_defineConstantDirective = 57
    RULE_defineFunctionArgs = 58
    RULE_defineFunctionDirective = 59

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
                   u"externalDeclaration", u"functionDefinition", u"preprocessorDirective", 
                   u"includeDirective", u"defineConstantDirective", u"defineFunctionArgs", 
                   u"defineFunctionDirective" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    Auto=5
    Break=6
    Case=7
    Char=8
    Const=9
    Continue=10
    Default=11
    Do=12
    Double=13
    Else=14
    Enum=15
    Extern=16
    Float=17
    For=18
    Goto=19
    If=20
    Inline=21
    Int=22
    Long=23
    Register=24
    Restrict=25
    Return=26
    Short=27
    Signed=28
    Sizeof=29
    Static=30
    Struct=31
    Switch=32
    Typedef=33
    Union=34
    Unsigned=35
    Void=36
    Volatile=37
    While=38
    Alignas=39
    Alignof=40
    Atomic=41
    Bool=42
    Complex=43
    Generic=44
    Imaginary=45
    Noreturn=46
    StaticAssert=47
    ThreadLocal=48
    LeftParen=49
    RightParen=50
    LeftBracket=51
    RightBracket=52
    LeftBrace=53
    RightBrace=54
    Less=55
    LessEqual=56
    Greater=57
    GreaterEqual=58
    LeftShift=59
    RightShift=60
    Plus=61
    PlusPlus=62
    Minus=63
    MinusMinus=64
    Star=65
    Div=66
    Mod=67
    And=68
    Or=69
    AndAnd=70
    OrOr=71
    Caret=72
    Not=73
    Tilde=74
    Question=75
    Colon=76
    Semi=77
    Comma=78
    Assign=79
    StarAssign=80
    DivAssign=81
    ModAssign=82
    PlusAssign=83
    MinusAssign=84
    LeftShiftAssign=85
    RightShiftAssign=86
    AndAssign=87
    XorAssign=88
    OrAssign=89
    Equal=90
    NotEqual=91
    Arrow=92
    Dot=93
    Ellipsis=94
    Identifier=95
    IntegerConstant=96
    FloatingConstant=97
    CharacterConstant=98
    StringLiteral=99
    LineDirective=100
    PragmaDirective=101
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
            self.state = 150
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CParser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 121
                _la = self._input.LA(1)
                if not(_la==CParser.PlusPlus or _la==CParser.MinusMinus):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 122
                self.unaryExpression(5)
                pass

            elif la_ == 2:
                localctx = CParser.SizeOfExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                self.match(CParser.Sizeof)
                self.state = 124
                self.unaryExpression(3)
                pass

            elif la_ == 3:
                localctx = CParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 125
                self.match(CParser.Identifier)
                pass

            elif la_ == 4:
                localctx = CParser.IntegerLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(CParser.IntegerConstant)
                pass

            elif la_ == 5:
                localctx = CParser.FloatingLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 127
                self.match(CParser.FloatingConstant)
                pass

            elif la_ == 6:
                localctx = CParser.CharacterLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                self.match(CParser.CharacterConstant)
                pass

            elif la_ == 7:
                localctx = CParser.StringLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 129
                        self.match(CParser.StringLiteral)

                    else:
                        raise NoViableAltException(self)
                    self.state = 132 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass

            elif la_ == 8:
                localctx = CParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.match(CParser.LeftParen)
                self.state = 135
                self.expression()
                self.state = 136
                self.match(CParser.RightParen)
                pass

            elif la_ == 9:
                localctx = CParser.UnaryOperatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                _la = self._input.LA(1)
                if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & ((1 << (CParser.Plus - 61)) | (1 << (CParser.Minus - 61)) | (1 << (CParser.Star - 61)) | (1 << (CParser.And - 61)) | (1 << (CParser.Not - 61)) | (1 << (CParser.Tilde - 61)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 139
                self.castExpression()
                pass

            elif la_ == 10:
                localctx = CParser.SizeOfTypeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(CParser.Sizeof)
                self.state = 141
                self.match(CParser.LeftParen)
                self.state = 142
                self.typeName()
                self.state = 143
                self.match(CParser.RightParen)
                pass

            elif la_ == 11:
                localctx = CParser.AlignOfTypeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.match(CParser.Alignof)
                self.state = 146
                self.match(CParser.LeftParen)
                self.state = 147
                self.typeName()
                self.state = 148
                self.match(CParser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 171
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CParser.IndexExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 152
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 153
                        self.match(CParser.LeftBracket)
                        self.state = 154
                        self.expression()
                        self.state = 155
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.FunctionExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 157
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 158
                        self.match(CParser.LeftParen)
                        self.state = 160
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                            self.state = 159
                            self.argumentExpressionList()


                        self.state = 162
                        self.match(CParser.RightParen)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DotExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 163
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 164
                        self.match(CParser.Dot)
                        self.state = 165
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 4:
                        localctx = CParser.ArrowExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 166
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 167
                        self.match(CParser.Arrow)
                        self.state = 168
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 5:
                        localctx = CParser.PostIncrementExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 169
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 170
                        _la = self._input.LA(1)
                        if not(_la==CParser.PlusPlus or _la==CParser.MinusMinus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        pass

             
                self.state = 175
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
            self.state = 176
            self.assignmentExpression()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 177
                self.match(CParser.Comma)
                self.state = 178
                self.assignmentExpression()
                self.state = 183
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
            self.state = 190
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.unaryExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(CParser.LeftParen)
                self.state = 186
                self.typeName()
                self.state = 187
                self.match(CParser.RightParen)
                self.state = 188
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
            self.state = 193
            self.castExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 225
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 195
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 196
                        _la = self._input.LA(1)
                        if not(((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CParser.Star - 65)) | (1 << (CParser.Div - 65)) | (1 << (CParser.Mod - 65)))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 197
                        self.logicalOrExpression(11)
                        pass

                    elif la_ == 2:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 198
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 199
                        _la = self._input.LA(1)
                        if not(_la==CParser.Plus or _la==CParser.Minus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 200
                        self.logicalOrExpression(10)
                        pass

                    elif la_ == 3:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 201
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 202
                        _la = self._input.LA(1)
                        if not(_la==CParser.LeftShift or _la==CParser.RightShift):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 203
                        self.logicalOrExpression(9)
                        pass

                    elif la_ == 4:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 204
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 205
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Less) | (1 << CParser.LessEqual) | (1 << CParser.Greater) | (1 << CParser.GreaterEqual))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 206
                        self.logicalOrExpression(8)
                        pass

                    elif la_ == 5:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 207
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 208
                        _la = self._input.LA(1)
                        if not(_la==CParser.Equal or _la==CParser.NotEqual):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 209
                        self.logicalOrExpression(7)
                        pass

                    elif la_ == 6:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 210
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 211
                        self.match(CParser.And)
                        self.state = 212
                        self.logicalOrExpression(6)
                        pass

                    elif la_ == 7:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 213
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 214
                        self.match(CParser.Caret)
                        self.state = 215
                        self.logicalOrExpression(5)
                        pass

                    elif la_ == 8:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 216
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 217
                        self.match(CParser.Or)
                        self.state = 218
                        self.logicalOrExpression(4)
                        pass

                    elif la_ == 9:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 219
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 220
                        self.match(CParser.AndAnd)
                        self.state = 221
                        self.logicalOrExpression(3)
                        pass

                    elif la_ == 10:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 222
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 223
                        self.match(CParser.OrOr)
                        self.state = 224
                        self.logicalOrExpression(2)
                        pass

             
                self.state = 229
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
            self.state = 237
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.logicalOrExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.logicalOrExpression(0)
                self.state = 232
                self.match(CParser.Question)
                self.state = 233
                self.expression()
                self.state = 234
                self.match(CParser.Colon)
                self.state = 235
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
            self.state = 244
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.unaryExpression(0)
                self.state = 241
                _la = self._input.LA(1)
                if not(((((_la - 79)) & ~0x3f) == 0 and ((1 << (_la - 79)) & ((1 << (CParser.Assign - 79)) | (1 << (CParser.StarAssign - 79)) | (1 << (CParser.DivAssign - 79)) | (1 << (CParser.ModAssign - 79)) | (1 << (CParser.PlusAssign - 79)) | (1 << (CParser.MinusAssign - 79)) | (1 << (CParser.LeftShiftAssign - 79)) | (1 << (CParser.RightShiftAssign - 79)) | (1 << (CParser.AndAssign - 79)) | (1 << (CParser.XorAssign - 79)) | (1 << (CParser.OrAssign - 79)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 242
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
            self.state = 246
            self.assignmentExpression()
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 247
                self.match(CParser.Comma)
                self.state = 248
                self.assignmentExpression()
                self.state = 253
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
            self.state = 254
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
            self.state = 267
            token = self._input.LA(1)
            if token in [CParser.T__0, CParser.T__1, CParser.Auto, CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Extern, CParser.Float, CParser.Inline, CParser.Int, CParser.Long, CParser.Register, CParser.Restrict, CParser.Short, CParser.Signed, CParser.Static, CParser.Struct, CParser.Typedef, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Volatile, CParser.Alignas, CParser.Atomic, CParser.Bool, CParser.Complex, CParser.Noreturn, CParser.ThreadLocal, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 256
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 259 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 262
                _la = self._input.LA(1)
                if _la==CParser.Star or _la==CParser.Identifier:
                    self.state = 261
                    self.initDeclaratorList()


                self.state = 264
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
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
            self.state = 274
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.storageClassSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.typeSpecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.typeQualifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.functionSpecifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 273
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
            self.state = 276
            self.initDeclarator()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 277
                self.match(CParser.Comma)
                self.state = 278
                self.initDeclarator()
                self.state = 283
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
            self.state = 289
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.declarator()
                self.state = 286
                self.match(CParser.Assign)
                self.state = 287
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
            self.state = 291
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
            self.state = 298
            token = self._input.LA(1)
            if token in [CParser.Char, CParser.Double, CParser.Float, CParser.Int, CParser.Long, CParser.Short, CParser.Signed, CParser.Unsigned, CParser.Void, CParser.Bool, CParser.Complex]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Char) | (1 << CParser.Double) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [CParser.Atomic]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.atomicTypeSpecifier()

            elif token in [CParser.Struct, CParser.Union]:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.structOrUnionSpecifier()

            elif token in [CParser.Enum]:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                self.enumSpecifier()

            elif token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 5)
                self.state = 297
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
            self.state = 315
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.structOrUnion()
                self.state = 302
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 301
                    self.match(CParser.Identifier)


                self.state = 304
                self.match(CParser.LeftBrace)
                self.state = 306 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 305
                    self.structDeclaration()
                    self.state = 308 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Struct) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.StaticAssert))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 310
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.structOrUnion()
                self.state = 313
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
            self.state = 317
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
            self.state = 326
            token = self._input.LA(1)
            if token in [CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Float, CParser.Int, CParser.Long, CParser.Restrict, CParser.Short, CParser.Signed, CParser.Struct, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Volatile, CParser.Atomic, CParser.Bool, CParser.Complex, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.specifierQualifierList()
                self.state = 321
                _la = self._input.LA(1)
                if ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CParser.Star - 65)) | (1 << (CParser.Colon - 65)) | (1 << (CParser.Identifier - 65)))) != 0):
                    self.state = 320
                    self.structDeclaratorList()


                self.state = 323
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
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
            self.state = 336
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.typeSpecifier()
                self.state = 330
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 329
                    self.specifierQualifierList()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.typeQualifier()
                self.state = 334
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 333
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
            self.state = 338
            self.structDeclarator()
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 339
                self.match(CParser.Comma)
                self.state = 340
                self.structDeclarator()
                self.state = 345
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
            self.state = 352
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                _la = self._input.LA(1)
                if _la==CParser.Star or _la==CParser.Identifier:
                    self.state = 347
                    self.declarator()


                self.state = 350
                self.match(CParser.Colon)
                self.state = 351
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
            self.state = 373
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
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
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(CParser.Enum)
                self.state = 364
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 363
                    self.match(CParser.Identifier)


                self.state = 366
                self.match(CParser.LeftBrace)
                self.state = 367
                self.enumeratorList()
                self.state = 368
                self.match(CParser.Comma)
                self.state = 369
                self.match(CParser.RightBrace)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.match(CParser.Enum)
                self.state = 372
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
            self.state = 375
            self.enumerator()
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 376
                    self.match(CParser.Comma)
                    self.state = 377
                    self.enumerator() 
                self.state = 382
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
            self.state = 383
            self.match(CParser.Identifier)
            self.state = 386
            _la = self._input.LA(1)
            if _la==CParser.Assign:
                self.state = 384
                self.match(CParser.Assign)
                self.state = 385
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
            self.state = 388
            self.match(CParser.Atomic)
            self.state = 389
            self.match(CParser.LeftParen)
            self.state = 390
            self.typeName()
            self.state = 391
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
            self.state = 393
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
            self.state = 400
            token = self._input.LA(1)
            if token in [CParser.T__0, CParser.Inline, CParser.Noreturn]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.Inline) | (1 << CParser.Noreturn))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [CParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.match(CParser.T__1)
                self.state = 397
                self.match(CParser.LeftParen)
                self.state = 398
                self.match(CParser.Identifier)
                self.state = 399
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
            self.state = 412
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.match(CParser.Alignas)
                self.state = 403
                self.match(CParser.LeftParen)
                self.state = 404
                self.typeName()
                self.state = 405
                self.match(CParser.RightParen)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(CParser.Alignas)
                self.state = 408
                self.match(CParser.LeftParen)
                self.state = 409
                self.constantExpression()
                self.state = 410
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
            self.state = 415
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 414
                self.pointer()


            self.state = 417
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
            self.state = 420
            self.match(CParser.Identifier)
            self._ctx.stop = self._input.LT(-1)
            self.state = 480
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 478
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 422
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 423
                        self.match(CParser.LeftBracket)
                        self.state = 427
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 424
                            self.typeQualifier()
                            self.state = 429
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 431
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                            self.state = 430
                            self.assignmentExpression()


                        self.state = 433
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 434
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 435
                        self.match(CParser.LeftBracket)
                        self.state = 436
                        self.match(CParser.Static)
                        self.state = 440
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 437
                            self.typeQualifier()
                            self.state = 442
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 443
                        self.assignmentExpression()
                        self.state = 444
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 446
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 447
                        self.match(CParser.LeftBracket)
                        self.state = 449 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 448
                            self.typeQualifier()
                            self.state = 451 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                                break

                        self.state = 453
                        self.match(CParser.Static)
                        self.state = 454
                        self.assignmentExpression()
                        self.state = 455
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 4:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 457
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 458
                        self.match(CParser.LeftBracket)
                        self.state = 462
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 459
                            self.typeQualifier()
                            self.state = 464
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 465
                        self.match(CParser.Star)
                        self.state = 466
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 5:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 467
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 468
                        self.match(CParser.LeftParen)
                        self.state = 469
                        self.parameterTypeList()
                        self.state = 470
                        self.match(CParser.RightParen)
                        pass

                    elif la_ == 6:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 472
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 473
                        self.match(CParser.LeftParen)
                        self.state = 475
                        _la = self._input.LA(1)
                        if _la==CParser.Identifier:
                            self.state = 474
                            self.identifierList()


                        self.state = 477
                        self.match(CParser.RightParen)
                        pass

             
                self.state = 482
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
            self.state = 483
            self.match(CParser.Star)
            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                self.state = 484
                self.typeQualifier()
                self.state = 489
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 491
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 490
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
            self.state = 493
            self.parameterDeclaration()
            self.state = 498
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 494
                    self.match(CParser.Comma)
                    self.state = 495
                    self.parameterDeclaration() 
                self.state = 500
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

            self.state = 503
            _la = self._input.LA(1)
            if _la==CParser.Comma:
                self.state = 501
                self.match(CParser.Comma)
                self.state = 502
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
            self.state = 520
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 505
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 508 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

                self.state = 510
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 512
                    self.declarationSpecifier()
                    self.state = 515 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 518
                _la = self._input.LA(1)
                if ((((_la - 49)) & ~0x3f) == 0 and ((1 << (_la - 49)) & ((1 << (CParser.LeftParen - 49)) | (1 << (CParser.LeftBracket - 49)) | (1 << (CParser.Star - 49)))) != 0):
                    self.state = 517
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
            self.state = 522
            self.match(CParser.Identifier)
            self.state = 527
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 523
                self.match(CParser.Comma)
                self.state = 524
                self.match(CParser.Identifier)
                self.state = 529
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
            self.state = 530
            self.specifierQualifierList()
            self.state = 532
            _la = self._input.LA(1)
            if ((((_la - 49)) & ~0x3f) == 0 and ((1 << (_la - 49)) & ((1 << (CParser.LeftParen - 49)) | (1 << (CParser.LeftBracket - 49)) | (1 << (CParser.Star - 49)))) != 0):
                self.state = 531
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
            self.state = 539
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.pointer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                _la = self._input.LA(1)
                if _la==CParser.Star:
                    self.state = 535
                    self.pointer()


                self.state = 538
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
            self.state = 587
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 542
                self.match(CParser.LeftParen)
                self.state = 543
                self.abstractDeclarator()
                self.state = 544
                self.match(CParser.RightParen)
                pass

            elif la_ == 2:
                self.state = 546
                self.match(CParser.LeftBracket)
                self.state = 550
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 547
                    self.typeQualifier()
                    self.state = 552
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 554
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 553
                    self.assignmentExpression()


                self.state = 556
                self.match(CParser.RightBracket)
                pass

            elif la_ == 3:
                self.state = 557
                self.match(CParser.LeftBracket)
                self.state = 558
                self.match(CParser.Static)
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
                self.assignmentExpression()
                self.state = 566
                self.match(CParser.RightBracket)
                pass

            elif la_ == 4:
                self.state = 568
                self.match(CParser.LeftBracket)
                self.state = 572
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 569
                    self.typeQualifier()
                    self.state = 574
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 575
                self.match(CParser.Static)
                self.state = 576
                self.assignmentExpression()
                self.state = 577
                self.match(CParser.RightBracket)
                pass

            elif la_ == 5:
                self.state = 579
                self.match(CParser.LeftBracket)
                self.state = 580
                self.match(CParser.Star)
                self.state = 581
                self.match(CParser.RightBracket)
                pass

            elif la_ == 6:
                self.state = 582
                self.match(CParser.LeftParen)
                self.state = 584
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                    self.state = 583
                    self.parameterTypeList()


                self.state = 586
                self.match(CParser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 636
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 634
                    la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                    if la_ == 1:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 589
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 590
                        self.match(CParser.LeftBracket)
                        self.state = 594
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 591
                            self.typeQualifier()
                            self.state = 596
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 598
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                            self.state = 597
                            self.assignmentExpression()


                        self.state = 600
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 601
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 602
                        self.match(CParser.LeftBracket)
                        self.state = 603
                        self.match(CParser.Static)
                        self.state = 607
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 604
                            self.typeQualifier()
                            self.state = 609
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 610
                        self.assignmentExpression()
                        self.state = 611
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 613
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 614
                        self.match(CParser.LeftBracket)
                        self.state = 616 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 615
                            self.typeQualifier()
                            self.state = 618 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                                break

                        self.state = 620
                        self.match(CParser.Static)
                        self.state = 621
                        self.assignmentExpression()
                        self.state = 622
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 4:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 624
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 625
                        self.match(CParser.LeftBracket)
                        self.state = 626
                        self.match(CParser.Star)
                        self.state = 627
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 5:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 628
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 629
                        self.match(CParser.LeftParen)
                        self.state = 631
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                            self.state = 630
                            self.parameterTypeList()


                        self.state = 633
                        self.match(CParser.RightParen)
                        pass

             
                self.state = 638
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
            self.state = 639
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
            self.state = 649
            token = self._input.LA(1)
            if token in [CParser.Sizeof, CParser.Alignof, CParser.LeftParen, CParser.Plus, CParser.PlusPlus, CParser.Minus, CParser.MinusMinus, CParser.Star, CParser.And, CParser.Not, CParser.Tilde, CParser.Identifier, CParser.IntegerConstant, CParser.FloatingConstant, CParser.CharacterConstant, CParser.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 641
                self.assignmentExpression()

            elif token in [CParser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 642
                self.match(CParser.LeftBrace)
                self.state = 643
                self.initializerList(0)
                self.state = 645
                _la = self._input.LA(1)
                if _la==CParser.Comma:
                    self.state = 644
                    self.match(CParser.Comma)


                self.state = 647
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
            self.state = 653
            _la = self._input.LA(1)
            if _la==CParser.LeftBracket or _la==CParser.Dot:
                self.state = 652
                self.designation()


            self.state = 655
            self.initializer()
            self._ctx.stop = self._input.LT(-1)
            self.state = 665
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,75,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.InitializerListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerList)
                    self.state = 657
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 658
                    self.match(CParser.Comma)
                    self.state = 660
                    _la = self._input.LA(1)
                    if _la==CParser.LeftBracket or _la==CParser.Dot:
                        self.state = 659
                        self.designation()


                    self.state = 662
                    self.initializer() 
                self.state = 667
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
            self.state = 669 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 668
                self.designator()
                self.state = 671 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.LeftBracket or _la==CParser.Dot):
                    break

            self.state = 673
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
            self.state = 681
            token = self._input.LA(1)
            if token in [CParser.LeftBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 675
                self.match(CParser.LeftBracket)
                self.state = 676
                self.constantExpression()
                self.state = 677
                self.match(CParser.RightBracket)

            elif token in [CParser.Dot]:
                self.enterOuterAlt(localctx, 2)
                self.state = 679
                self.match(CParser.Dot)
                self.state = 680
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
            self.state = 683
            self.match(CParser.StaticAssert)
            self.state = 684
            self.match(CParser.LeftParen)
            self.state = 685
            self.constantExpression()
            self.state = 686
            self.match(CParser.Comma)
            self.state = 688 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 687
                self.match(CParser.StringLiteral)
                self.state = 690 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.StringLiteral):
                    break

            self.state = 692
            self.match(CParser.RightParen)
            self.state = 693
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
            self.state = 701
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 695
                self.labeledStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 696
                self.compoundStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 697
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 698
                self.selectionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 699
                self.iterationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 700
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
            self.state = 714
            token = self._input.LA(1)
            if token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 703
                self.match(CParser.Identifier)
                self.state = 704
                self.match(CParser.Colon)
                self.state = 705
                self.statement()

            elif token in [CParser.Case]:
                self.enterOuterAlt(localctx, 2)
                self.state = 706
                self.match(CParser.Case)
                self.state = 707
                self.constantExpression()
                self.state = 708
                self.match(CParser.Colon)
                self.state = 709
                self.statement()

            elif token in [CParser.Default]:
                self.enterOuterAlt(localctx, 3)
                self.state = 711
                self.match(CParser.Default)
                self.state = 712
                self.match(CParser.Colon)
                self.state = 713
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
            self.state = 716
            self.match(CParser.LeftBrace)
            self.state = 720
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Break) | (1 << CParser.Case) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Continue) | (1 << CParser.Default) | (1 << CParser.Do) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.For) | (1 << CParser.Goto) | (1 << CParser.If) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Return) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Sizeof) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Switch) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.While) | (1 << CParser.Alignas) | (1 << CParser.Alignof) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal) | (1 << CParser.LeftParen) | (1 << CParser.LeftBrace) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Semi - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                self.state = 717
                self.blockItem()
                self.state = 722
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 723
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
            self.state = 727
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 725
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 726
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
            self.state = 730
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                self.state = 729
                self.expression()


            self.state = 732
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
            self.state = 749
            token = self._input.LA(1)
            if token in [CParser.If]:
                localctx = CParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 734
                self.match(CParser.If)
                self.state = 735
                self.match(CParser.LeftParen)
                self.state = 736
                self.expression()
                self.state = 737
                self.match(CParser.RightParen)
                self.state = 738
                self.statement()
                self.state = 741
                la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
                if la_ == 1:
                    self.state = 739
                    self.match(CParser.Else)
                    self.state = 740
                    self.statement()



            elif token in [CParser.Switch]:
                localctx = CParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 743
                self.match(CParser.Switch)
                self.state = 744
                self.match(CParser.LeftParen)
                self.state = 745
                self.expression()
                self.state = 746
                self.match(CParser.RightParen)
                self.state = 747
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
            self.state = 751
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
            self.state = 753
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
            self.state = 797
            la_ = self._interp.adaptivePredict(self._input,91,self._ctx)
            if la_ == 1:
                localctx = CParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 755
                self.match(CParser.While)
                self.state = 756
                self.match(CParser.LeftParen)
                self.state = 757
                self.expression()
                self.state = 758
                self.match(CParser.RightParen)
                self.state = 759
                self.statement()
                pass

            elif la_ == 2:
                localctx = CParser.DoWhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 761
                self.match(CParser.Do)
                self.state = 762
                self.statement()
                self.state = 763
                self.match(CParser.While)
                self.state = 764
                self.match(CParser.LeftParen)
                self.state = 765
                self.expression()
                self.state = 766
                self.match(CParser.RightParen)
                self.state = 767
                self.match(CParser.Semi)
                pass

            elif la_ == 3:
                localctx = CParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 769
                self.match(CParser.For)
                self.state = 770
                self.match(CParser.LeftParen)
                self.state = 772
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 771
                    self.initExpression()


                self.state = 774
                self.match(CParser.Semi)
                self.state = 776
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 775
                    self.expression()


                self.state = 778
                self.match(CParser.Semi)
                self.state = 780
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 779
                    self.iterationExpression()


                self.state = 782
                self.match(CParser.RightParen)
                self.state = 783
                self.statement()
                pass

            elif la_ == 4:
                localctx = CParser.DeclForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 784
                self.match(CParser.For)
                self.state = 785
                self.match(CParser.LeftParen)
                self.state = 786
                self.declaration()
                self.state = 788
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 787
                    self.expression()


                self.state = 790
                self.match(CParser.Semi)
                self.state = 792
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 791
                    self.iterationExpression()


                self.state = 794
                self.match(CParser.RightParen)
                self.state = 795
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
            self.state = 811
            token = self._input.LA(1)
            if token in [CParser.Goto]:
                localctx = CParser.GotoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 799
                self.match(CParser.Goto)
                self.state = 800
                self.match(CParser.Identifier)
                self.state = 801
                self.match(CParser.Semi)

            elif token in [CParser.Continue]:
                localctx = CParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 802
                self.match(CParser.Continue)
                self.state = 803
                self.match(CParser.Semi)

            elif token in [CParser.Break]:
                localctx = CParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 804
                self.match(CParser.Break)
                self.state = 805
                self.match(CParser.Semi)

            elif token in [CParser.Return]:
                localctx = CParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 806
                self.match(CParser.Return)
                self.state = 808
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus) | (1 << CParser.PlusPlus) | (1 << CParser.Minus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.IntegerConstant - 64)) | (1 << (CParser.FloatingConstant - 64)) | (1 << (CParser.CharacterConstant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 807
                    self.expression()


                self.state = 810
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
            self.state = 816
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2) | (1 << CParser.T__3) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CParser.Star - 65)) | (1 << (CParser.Semi - 65)) | (1 << (CParser.Identifier - 65)) | (1 << (CParser.LineDirective - 65)) | (1 << (CParser.PragmaDirective - 65)))) != 0):
                self.state = 813
                self.externalDeclaration()
                self.state = 818
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 819
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
            self.state = 825
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 821
                self.functionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 822
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 823
                self.preprocessorDirective()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 824
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
            self.state = 830
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,96,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 827
                    self.declarationSpecifier() 
                self.state = 832
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,96,self._ctx)

            self.state = 833
            self.declarator()
            self.state = 837
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                self.state = 834
                self.declaration()
                self.state = 839
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 840
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
        self.enterRule(localctx, 110, self.RULE_preprocessorDirective)
        try:
            self.state = 847
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 842
                self.match(CParser.LineDirective)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 843
                self.match(CParser.PragmaDirective)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 844
                self.includeDirective()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 845
                self.defineConstantDirective()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 846
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
        self.enterRule(localctx, 112, self.RULE_includeDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 849
            self.match(CParser.T__2)
            self.state = 850
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
        self.enterRule(localctx, 114, self.RULE_defineConstantDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 852
            self.match(CParser.T__3)
            self.state = 853
            self.match(CParser.Identifier)
            self.state = 854
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
        self.enterRule(localctx, 116, self.RULE_defineFunctionArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 856
            self.match(CParser.LeftParen)
            self.state = 857
            self.match(CParser.Identifier)
            self.state = 860 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 858
                self.match(CParser.Comma)
                self.state = 859
                self.match(CParser.Identifier)
                self.state = 862 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.Comma):
                    break

            self.state = 864
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
        self.enterRule(localctx, 118, self.RULE_defineFunctionDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 866
            self.match(CParser.T__3)
            self.state = 867
            self.match(CParser.Identifier)
            self.state = 868
            self.defineFunctionArgs()
            self.state = 869
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
         



