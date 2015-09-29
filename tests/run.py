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


def _build_and_run(f, exe_file, plugin_file):

    f.write('--- Build ---\n')
    cmd = "gcc -fno-exceptions -g -Os -Wall -ffunction-sections -fdata-sections "\
        "-o %s test.c %s" % (exe_file, plugin_file)
    f.write("%s\n" % cmd)
    sp = subprocess.Popen(
        cmd,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    f.write('\n'.join(sp.communicate()))
    if sp.returncode != 0:
        f.write('Failed with code %d\n' % sp.returncode)
        return
    else:
        f.write('Ok\n')

    f.write('\n---  Run  ---\n')
    sp = subprocess.Popen(
        exe_file,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    f.write('\n'.join(sp.communicate()))
    if sp.returncode != 0:
        f.write('Failed with code %d\n' % sp.returncode)


def _run(prefix):
    log_file = '%s.log' % prefix
    exe_file = '%s.exe' % prefix
#    plugin_file = '%s.c' % prefix
    plugin_file = '%s_non_blocking.c' % prefix

    try:
        os.unlink(exe_file)
    except:
        pass
    try:
        os.unlink(log_file)
    except:
        pass

    f = open(log_file, 'wb')
    _build_and_run(f, exe_file, plugin_file)
    f.close()
    try:
        os.unlink(exe_file)
    except:
        pass


def main():

    _run('my_1')

# temporary entrance
if __name__ == "__main__":
    main()
    sys.exit()
