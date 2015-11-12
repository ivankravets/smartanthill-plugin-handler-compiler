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

from smartanthill_phc import api
from smartanthill_phc.parse_write import ZeptoPlugin, write_composer_file


def composer_test(prefix):

    h_file = "tests/%s/%s_parser.h" % (prefix, prefix)
    xml_file = "tests/%s/manifest.xml" % prefix
    plugin = ZeptoPlugin(xml_file)

    code = write_composer_file(prefix, plugin)

    f = open(h_file, 'rb')
    assert code == f.read()


def non_blocking_test(prefix, split_all):

    c_file = "tests/%s/%s.c" % (prefix, prefix)
    nb_file = "tests/%s/%s_non_blocking.c" % (prefix, prefix)
    h_file = "tests/%s/%s_state.h" % (prefix, prefix)
    code, header = api.process_file(c_file, prefix, split_all, False)

    f = open(nb_file, 'rb')
    assert code.splitlines() == f.read().splitlines()

    h = open(h_file, 'rb')
    assert header.splitlines() == h.read().splitlines()


def test_blink():

    composer_test('blink')
    non_blocking_test('blink', False)


def test_debug():

    non_blocking_test('debug', True)


def test_sleep():

    non_blocking_test('sleep', False)


def test_spi():

    non_blocking_test('spi', False)


def test_sub_machine():

    non_blocking_test('sub_machine', True)


def test_sub_machine2():

    non_blocking_test('sub_machine2', True)


def test_write_digital_pin():

    composer_test('write_digital_pin')
