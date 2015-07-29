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

import sys

import antlr4

from smartanthill_pc.antlr_helper import dump_antlr_tree
from smartanthill_pc.antlr_parser import CLexer, CParser
from smartanthill_pc.antlr_parser.TokenStreamRewriter import TokenStreamRewriter


def main():

    istream = antlr4.FileStream("test_code_1.c")
    lexer = CLexer.CLexer(istream)
    stream = antlr4.CommonTokenStream(lexer)
    rewriter = TokenStreamRewriter(stream)
#     stream.fill()
#     toks = stream.getTokens(0, 1000)
#     for each in toks:
#         print "%s, %s : %s" % (each.tokenIndex, each.channel, each.text)

    parser = CParser.CParser(stream)
    tree = parser.compilationUnit()

    rewriter.delete(50, 60)
    rewriter.insertAfter(80, u"*****************")
    rewriter.replace(90, 100, u"///////////////////")

    print rewriter.getIntervalText(30, 110)
    text = dump_antlr_tree(tree)
    print '\n'.join(text)

# temporary entrance
if __name__ == "__main__":
    #    cProfile.run("main()")
    main()
    sys.exit()
