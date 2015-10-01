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


def run_test(prefix):

    (async, header) = api.process_file('tests/' + prefix + '.c', prefix, False)

    f = open('tests/' + prefix + '_non_blocking.c', 'r')
    assert async == f.read()

    h = open('tests/' + prefix + '_state.h', 'r')
    assert header == h.read()


def test_sleep():

    run_test('sleep')


def test_spi():

    run_test('spi')
