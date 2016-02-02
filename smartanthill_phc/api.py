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

import antlr4

from smartanthill_phc import writer
from smartanthill_phc.antlr_parser import CLexer, CParser
from smartanthill_phc.builtin import create_builtins
from smartanthill_phc.common.antlr_helper import dump_antlr_tree
from smartanthill_phc.common.compiler import Compiler, Ctx
from smartanthill_phc.common.visitor import dump_tree,\
    check_all_nodes_reachables
from smartanthill_phc.manifest import create_manifest
from smartanthill_phc.parser import c_parse_tree_to_syntax_tree
from smartanthill_phc.resolve import resolve_tree
from smartanthill_phc.rewrite import rewrite_code
from smartanthill_phc.root import RootNode
from smartanthill_phc.state import create_states


class _Helper(object):
    '''
    Agregate helper class to create and hold parser related stuff
    '''

    def __init__(self, file_name):
        '''
        Constructor
        '''
        self.file_stream = antlr4.FileStream(file_name)
        self.clexer = CLexer.CLexer(self.file_stream)
        self.token_stream = antlr4.CommonTokenStream(self.clexer)
        self.cparser = CParser.CParser(self.token_stream)


def process_file(file_name, zepto_plugin, prefix, split_all, dump, papi=None):
    '''
    Process a c input file, and returns an string with output text
    '''
    # pylint: disable=too-many-locals

    c = Compiler()
    root = c.init_node(RootNode(), Ctx.ROOT)
    builtin = create_builtins(c, Ctx.BUILTIN)
    root.builtins.set(builtin)

    if papi is not None:
        papi_helper = _Helper(papi)
        papi_tree = papi_helper.cparser.compilationUnit()

        if dump:
            print '\n'.join(dump_antlr_tree(papi_tree))

        papi = c_parse_tree_to_syntax_tree(c, papi_tree, prefix)
        root.papi.set(papi)

    manif = create_manifest(c, Ctx.MANIFEST, prefix, zepto_plugin)
    root.manifest.set(manif)

    helper = _Helper(file_name)
    ptree = helper.cparser.compilationUnit()
    if dump:
        print '\n'.join(dump_antlr_tree(ptree))
    source = c_parse_tree_to_syntax_tree(c, ptree, prefix)
    root.source.set(source)

    if dump:
        print
        print '\n'.join(dump_tree(root))

    check_all_nodes_reachables(c, root)
    resolve_tree(c, root)

    create_states(c, root, prefix, split_all)

    if dump:
        print
        print '\n'.join(dump_tree(root))

    async2 = rewrite_code(c, root, helper.token_stream)
    header = writer.write_header(c, root, file_name)
    async = writer.write_code(c, root, file_name)
    parser = writer.write_parser(c, root)
    return (async, header, async2, parser)


def process_manifest(zepto_plugin, prefix, dump, papi=None):
    '''
    Process a c input file, and returns an string with output text
    '''

    c = Compiler()
    root = c.init_node(RootNode(), Ctx.ROOT)
    builtin = create_builtins(c, Ctx.BUILTIN)
    root.builtins.set(builtin)

    if papi is not None:
        papi_helper = _Helper(papi)
        papi_tree = papi_helper.cparser.compilationUnit()

        if dump:
            print '\n'.join(dump_antlr_tree(papi_tree))

        papi = c_parse_tree_to_syntax_tree(c, papi_tree, prefix)
        root.papi.set(papi)

    manif = create_manifest(c, Ctx.MANIFEST, prefix, zepto_plugin)
    root.manifest.set(manif)

    if dump:
        print
        print '\n'.join(dump_tree(root))

    check_all_nodes_reachables(c, root)
    resolve_tree(c, root)

    if dump:
        print
        print '\n'.join(dump_tree(root))

    parser = writer.write_parser(c, root)
    return parser
