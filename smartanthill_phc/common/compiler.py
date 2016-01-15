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

from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.tree.Tree import TerminalNodeImpl

from smartanthill_phc.common.errors import CompilerError
from smartanthill_phc.common.visitor import NodeWalker
import xml.etree.ElementTree as ET


class BuiltinCtx(object):

    '''
    This class is used as context on built in code, to allow format_location
    '''

    def __init__(self, text):
        self.text = text


class Ctx(object):

    '''
    Static built in contexts
    '''

    BUILTIN = BuiltinCtx('<builtin>')
    PARAM = BuiltinCtx('<parameter>')
    BODYPART = BuiltinCtx('<bodypart>')
    TARGET = BuiltinCtx('<target>')
    ROOT = BuiltinCtx('<root>')
    NONE = BuiltinCtx('<none>')


def format_location(ctx):
    '''
    Returns formated string with location in source code of given ctx
    '''

    if isinstance(ctx, BuiltinCtx):
        return ctx.text + ', '
    elif isinstance(ctx, TerminalNodeImpl):  # ctx.symbol is CommonToken
        return 'line %s, ' % str(ctx.symbol.line)
    elif isinstance(ctx, ParserRuleContext):
        if ctx.start.line == ctx.stop.line:
            return 'line %s, ' % str(ctx.start.line)
        else:
            return 'lines %s-%s, ' % (str(ctx.start.line), str(ctx.stop.line))
    elif isinstance(ctx, ET.ElementTree):
        if ctx.start.line == ctx.stop.line:
            return 'line %s, ' % str(ctx.start.line)
    else:
        return '<unknown>'


class Compiler(object):

    '''
    Holds common information about a compilation and
    provides some helper methods
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.next_node_id = 0
        self.removed_nodes = []
        self.error_flag = False
        self.error_message = []

    def init_node(self, node, ctx):
        '''
        Initializes a node by setting its node_id
        '''
        node.node_id = self.next_node_id
        self.next_node_id += 1
        node.ctx = ctx

        return node

    def remove_nodes(self, node):
        '''
        Keeps a record of removed node_id
        Later checks may try to verify no refereces are kept
        '''
        walker = _NodeIdsWalker()
        walker.walk_node(node)

        self.removed_nodes.extend(walker.node_ids)

    def report_error(self, ctx, text):
        '''
        Reports an error
        '''
        self.error_flag = True
        self.error_message.append(format_location(ctx) + text)
        print self.error_message[-1]

    def syntax_error(self):
        '''
        Reports an error from the parser,
        currently the parser reports the error itself because I can not make
        Antlr to stop printing to console
        '''
#   print("line " + str(line) + ":" + str(column) + " " + msg, file=sys.stderr)
        self.error_flag = True

    def check_stage(self, name):
        '''
        Raises CompilerError if any error was reported on this stage
        '''
        if self.error_flag:
            print "Stage '%s' giving up" % name
            self.raise_error()

    def raise_error(self):
        '''
        Raises CompilerError
        '''
        # pylint: disable=no-self-use
        raise CompilerError(self.error_message)


class _NodeIdsWalker(NodeWalker):

    '''
    Walker class that will remove all child nodes
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(_NodeIdsWalker, self).__init__()
        self.node_ids = []

    def walk_node(self, node):
        assert node
        self.node_ids.append(node.node_id)
        self.walk_childs(node)
