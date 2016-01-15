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

import os

from smartanthill_phc import api
from smartanthill_phc.parse_write import ZeptoPlugin, write_composer_file


def composer_test(prefix):

    h_file = "%s_parser.h" % prefix
    xml_file = "manifest.xml"

    print os.getcwd()
    os.chdir("tests/%s" % prefix)
    try:
        plugin = ZeptoPlugin(xml_file)
        code = write_composer_file(prefix, plugin)

        f = open(h_file, 'rb')
        assert code == f.read()
    finally:
        os.chdir("../..")


def non_blocking_test(prefix, split_all):

    c_file = "%s.c" % prefix
    nb_file = "%s_non_blocking.c" % prefix
    h_file = "%s_state.h" % prefix

    print os.getcwd()

    os.chdir("tests/%s" % prefix)
    try:
        code, header, c2 = api.process_file(c_file, prefix, split_all, False)

        f = open(nb_file, 'rb')
        assert code.splitlines() == f.read().splitlines()

        h = open(h_file, 'rb')
        assert header.splitlines() == h.read().splitlines()
    finally:
        os.chdir("../..")


def test_blink():

    composer_test('blink')
    non_blocking_test('blink', False)


def test_debug():

    non_blocking_test('debug', True)


def test_expression():

    non_blocking_test('expression', False)


def test_loop():

    non_blocking_test('loop', False)


def test_sleep():

    non_blocking_test('sleep', False)


def test_spi():

    non_blocking_test('spi', False)


def test_stateless():

    non_blocking_test('stateless', False)


def test_sub_machine():

    non_blocking_test('sub_machine', True)


def test_sub_machine2():

    non_blocking_test('sub_machine2', True)


def test_write_digital_pin():

    composer_test('write_digital_pin')
