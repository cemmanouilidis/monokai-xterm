#!/usr/bin/env python

import sys
import os
import shutil
from datetime import datetime


if __name__ == "__main__":
    config = 'xtermcontrol'
    script_dir = os.path.abspath(os.path.dirname(__file__))

    src = os.path.join(script_dir, config)
    dest = os.path.join(os.environ["HOME"], ".%s" % config)

    if os.path.exists(dest):
        now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        backup = '%s-%s.backup' % (dest, now)
        print("Create backup file %s" % backup)
        shutil.move(dest, backup)

    shutil.copy(src, dest)

    if 'bash' in os.environ['SHELL']:
        run_xtermcontrol = "xtermcontrol # added by monokai-xterm"

        bashrc = os.path.join(os.environ["HOME"], ".bashrc")

        bashrc_content = open(bashrc, 'r').readlines()

        is_xtermcontrol_is_setup = False
        for line in bashrc_content:
            if run_xtermcontrol in line:
                is_xtermcontrol_is_setup = True
                break

        if not is_xtermcontrol_is_setup:
            print("Setup xtermcontrol for bash: ")
            print(" Adding \"%s\" to your bashrc file " % run_xtermcontrol)
            bashrc_content = open(bashrc, 'a')
            bashrc_content.write('\n%s\n' % run_xtermcontrol)
            bashrc_content.close()

    sys.exit(0)
