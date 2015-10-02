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
import subprocess
import sys
from smartanthill_phc import api

'''
This python script needs to be run with environment path for gcc to work.
I use a shell script to set PATH for specific gcc instance to test,
and then run this script
'''


def main():

    build_and_run('debug')


def run_test(prefix, split_all):

    c_file = "tests/%s/%s.c" % (prefix, prefix)
    nb_file = "tests/%s/%s_non_blocking.c" % (prefix, prefix)
    h_file = "tests/%s/%s_state.h" % (prefix, prefix)
    code, header = api.process_file(c_file, prefix, split_all, False)

    f = open(nb_file, 'rb')
    assert code == f.read()

    h = open(h_file, 'rb')
    assert header == h.read()


def make_non_blocking(prefix, split_all):

    c_file = "%s.c" % prefix
    nb_file = "%s_non_blocking.c" % prefix
    h_file = "%s_state.h" % prefix

    code, header = api.process_file(c_file, prefix, split_all, False)

    f = open(nb_file, 'wb')
    f.write(code)

    h = open(h_file, 'wb')
    h.write(header)


def build_and_run(prefix):

    log_file = '%s.log' % prefix

    try:
        os.unlink(log_file)
    except:
        pass

    f = open(log_file, 'wb')

    _build_and_run2(f, prefix, prefix)
    f.write('\n\n*** Non Blocking ***\n')
    _build_and_run2(f, prefix, prefix + "_non_blocking")
    f.close()


def _build_and_run2(f, prefix, file_prefix):

    exe_file = file_prefix + '.exe'

    try:
        os.unlink(exe_file)
    except:
        pass

    _build_and_run(f, prefix, file_prefix)

    try:
        os.unlink(exe_file)
    except:
        pass


def _build_and_run(f, prefix, file_prefix):

    f.write('--- Build ---\n')
    cmd = "gcc -fno-exceptions -g -Os -Wall -ffunction-sections "\
        "-fdata-sections -I.. -DSA_PLUGIN_ID=%s "\
        "-include %s.h -include %s_state.h "\
        "-o %s.exe ../runner.c %s.c" % (prefix, prefix,
                                        prefix, file_prefix, file_prefix)
    f.write("%s\n" % cmd)
    sp = subprocess.Popen(
        cmd,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    f.write(sp.communicate()[0])
    if sp.returncode != 0:
        f.write('Failed with code %d\n' % sp.returncode)
        return
    else:
        f.write('Ok\n')

    f.write('\n---  Run  ---\n')
    sp = subprocess.Popen(
        file_prefix + ".exe",
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

    f.write(sp.communicate()[0])
    if sp.returncode != 0:
        f.write('Failed with code %d\n' % sp.returncode)


# temporary entrance
if __name__ == "__main__":
    main()
    sys.exit()
