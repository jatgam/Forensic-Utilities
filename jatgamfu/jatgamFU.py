#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# jatgamFU.py
# Version: 0.0.1.1
# By: Shawn Silva (shawn at jatgam dot com)
# Jatgam Forensic Utilites
# 
# Created: 06/27/2011
# Modified: 05/11/2012
# 
# A collection of utilities to help gather information on digital evidence.
# -----------------------------------------------------------------------------
#
# 
# REQUIREMENTS:
# Python 3.2.x
# 
# Copyright (C) 2011-2012  Jatgam Technical Solutions
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
#                                    TODO                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  - 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                  CHANGELOG                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 05/11/2012        v0.0.1.1 - Changed command line options to run.
# 06/27/2011        v0.0.1 - Initial creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
appversion = "0.0.1"

import argparse
import sys

from forensicutilities.gui import gui
from forensicutilities.cli import cli


def gui_main():
    gui.run_gui()

def cli_main():
    cli.run_cli()

if __name__ == "__main__":

    if sys.hexversion < 0x30202f0:
        try:
            print("You must use Python 3.2.2 or greater!")
            sys.exit()
        except:
            print "You must use Python 3.2.2 or greater!"
            sys.exit()
    
    parser = argparse.ArgumentParser(version=appversion, description="Jatgam Forensic Utilities")
    
    parser.add_argument('-C', action='store_true', default=False, dest='cli', help='Run a CLI')
    parser.add_argument('-G', action='store_true', default=False, dest='gui', help='Run a GUI')
    
    arguments = parser.parse_args()
    
    if arguments.gui:
        gui_main()
    elif arguments.cli:
        cli_main()
    else:
        parser.print_help()
