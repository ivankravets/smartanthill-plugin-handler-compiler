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


def test_code_1():

    async = api.process_file(
        'tests/test_code_1.c', 'my_plugin_handler', False)

    f = open('tests/test_code_1.async.c', 'r')

    assert async == f.read()


def test_code_2():

    async = api.process_file(
        'tests/test_code_2.c', 'my_plugin_handler', False)

    f = open('tests/test_code_2.async.c', 'r')

    assert async == f.read()
