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


def run_test(prefix, split_all):

    c_file = "tests/%s.c" % prefix
    nb_file = "tests/%s_non_blocking.c" % prefix
    h_file = "tests/%s_state.h" % prefix
    (async, header) = api.process_file(c_file, prefix, split_all, False)

    f = open(nb_file, 'rb')
    assert async == f.read()

    h = open(h_file, 'rb')
    assert header == h.read()


def test_sleep():

    run_test('sleep', False)


def test_spi():

    run_test('spi', False)
