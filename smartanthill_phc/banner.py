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


def get_copyright_banner():
    '''
    Returns the copyright header/banner text
    '''

    txt = "/*" + (76 * "*") + "\n"

    txt += "    Copyright (C) 2015 OLogN Technologies AG\n\n"

    for each in _gpl2_banner:
        txt += "    " + each + "\n"

    txt += (76 * "*") + "*/\n"

    return txt


def get_copyright_banner2():
    '''
    Returns the copyright header/banner text
    '''

    banner = []

    banner.append("/*" + (76 * "*"))

    banner.append("    Copyright (C) 2015 OLogN Technologies AG")
    banner.append("    ")

    for each in _gpl2_banner:
        banner.append("    " + each)

    banner.append((76 * "*") + "*/")

    return banner

_gpl2_banner = [
    "This program is free software; you can redistribute it and/or modify",
    "it under the terms of the GNU General Public License version 2 as",
    "published by the Free Software Foundation.",
    "",
    "This program is distributed in the hope that it will be useful,",
    "but WITHOUT ANY WARRANTY; without even the implied warranty of",
    "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the",
    "GNU General Public License for more details.",
    "",
    "You should have received a copy of the GNU General Public License along",
    "with this program; if not, write to the Free Software Foundation, Inc.,",
    "51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA",
    "",
]
