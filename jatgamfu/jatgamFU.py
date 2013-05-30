#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# jatgamFU.py
# Jatgam Forensic Utilites
# 
# Created: 06/27/2011
# Modified: 05/30/2013
# 
# Copyright (C) 2011-2013  Jatgam Technical Solutions
# ---------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
appversion = "0.0.1.005"

PY_MIN_VERSION = 0x30202f0

import argparse
import sys

import_error = False
try:
    from forensicutilities.gui import gui
    from forensicutilities.cli import cli
except ImportError as ex:
    print("Fatal Error during import process: " + str(ex))
    import_error = True


def check_system():
    """Makes sure version and imports worked before starting"""
    if sys.hexversion < PY_MIN_VERSION:
        try:
            print("You must use Python 3.2.2 or greater!")
        except:
            exec('print "You must use Python 3.2.2 or greater!"')
        sys.exit()
    if import_error:
        sys.exit()
    return
    
def gui_main():
    gui.run_gui()

def cli_main():
    cli.run_cli()

if __name__ == "__main__":
    check_system()
    
    parser = argparse.ArgumentParser(description="Jatgam Forensic Utilities")
    
    parser.add_argument('-v', action='store_true', default=False, dest='printversion', help='Print the application version and Exit')
    parser.add_argument('-c', action='store_true', default=False, dest='cli', help='Run a CLI')
    parser.add_argument('-g', action='store_true', default=False, dest='gui', help='Run a GUI')
    
    arguments = parser.parse_args()
    
    if arguments.gui:
        gui_main()
    elif arguments.cli:
        cli_main()
    elif arguments.printversion:
        print(appversion)
    else:
        parser.print_help()
