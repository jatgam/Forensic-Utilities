#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# jatgamFU.py
# Version: 0.0.1
# By: Shawn Silva (shawn at jatgam dot com)
# Jatgam Forensic Utilites
# 
# Created: 06/27/2011
# Modified: 06/27/2011
# 
# A collection of utilities to help gather information on digital
# evidence.
# -----------------------------------------------------------------
#
# 
# REQUIREMENTS:
# Python 3.2.x
# 
# Copyright (C) 2011  Shawn Silva
# -------------------------------
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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                               TODO                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  - 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                             CHANGELOG                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 06/27/2011        v0.0.1 - Initial creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
appversion = "0.0.1"

import argparse

from forensicutilities.gui import gui
from forensicutilities.cli import cli


def gui_main():
    gui.run_gui()

def cli_main():
    cli.run_cli()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(version=appversion, description="Jatgam Forensic Utilities")
    
    parser.add_argument('-G', action='store_false', default=True, dest='gui', help='Disable GUI and run in CLI mode')
    
    arguments = parser.parse_args()
    
    if arguments.gui:
        gui_main()
    else:
        cli_main()
