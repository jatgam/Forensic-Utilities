#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# cli.py
# Version: 0.0.1.1
# By: Shawn Silva (shawn at jatgam dot com)
# Part of Jatgam Forensic Utilities
# 
# Created: 06/13/2011
# Modified: 05/14/2012
# 
# A CLI to Jatgam Forensic Utilities.
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
# 05/14/2012        v0.0.1.1 - Actually creating a CLI, instead of just
#                           dumping test information.    
# 08/02/2011        v0.0.1 - Initial script creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import cmd

from forensicutilities.disk.PartitionTableAnalyzer import *
from forensicutilities.disk.DiskAnalyzer import PhysicalDiskAnalyzer
from forensicutilities.math.Conversions import *

class JatgamFUcli(cmd.Cmd):
    prompt = "fu: "
    intro = "\nJatgam Forensic Utilities\nA collection of utilities to help gather information on digital evidence.\n"
    
    disks = PhysicalDiskAnalyzer().disks
    selecteddisk = None
    disktable = None
    
    def do_listdisks(self, line):
        """List available disks to analyze."""
        if self.disks == -1:
            print("Not disks found; possibly not running on a supported system")
            return
        elif self.disks == []:
            print("No disks found.")
            return
        print("\nDisk ID\t\tOS Identifier\t\tSize\t\tMedia Type")
        print("-"*77)
        count = 0
        for disk in self.disks:
            disksize = "%.2f" % DecimalUtilities.bytesToGB(disk["DiskSize"])
            print(str(count) + "\t\t" + disk["Disk"] + "\t" + str(disksize) + " GB" + "\t" + str(disk["MediaType"]))
            count += 1
        print("\n")
        
    def do_selectdisk(self, line):
        """Select a disk (by Disk ID) to perform operations on."""
        try:
            self.disks[int(line)]
            self.selecteddisk = int(line)
            self.disktable = PartitionTableAnalyzer(self.disks[int(line)]["Disk"], self.disks[int(line)]["BytesPerSector"])
        except:
            print("Invalid Disk!")
            
    def do_diskinfo(self, line):
        """Print information on the selected disk."""
        if self.selecteddisk != None:
            print("\nDisk ID:\t\t" + str(self.selecteddisk))
            print("OS Identifier:\t\t" + self.disks[self.selecteddisk]["Disk"])
            print("Media Type:\t\t" + str(self.disks[self.selecteddisk]["MediaType"]))
            print("Sectors Per Track:\t" + str(self.disks[self.selecteddisk]["SectorsPerTrack"]))
            print("Tracks Per Cylinder:\t" + str(self.disks[self.selecteddisk]["TracksPerCylinder"]))
            print("Cylinders:\t\t" + str(self.disks[self.selecteddisk]["Cylinders"]))
            print("Bytes Per Sector:\t" + str(self.disks[self.selecteddisk]["BytesPerSector"]))
            print("Size (bytes):\t\t" + str(self.disks[self.selecteddisk]["DiskSize"]))
            print("Size (GB):\t\t" + "%.2f" % DecimalUtilities.bytesToGB(self.disks[self.selecteddisk]["DiskSize"]))
            print("\n")
        else:
            print("You haven't selected a disk yet!")
    
    def do_printmbr(self, line):
        """Print the MBR of the selected disk."""
        if self.selecteddisk != None:
            self.disktable.printMBR()
        else:
            print("You haven't selected a disk yet!")
            
    def do_listpartitions(self, line):
        """List all partitions on the selected disk."""
        if self.selecteddisk != None:
            self.disktable.printAllPartitions()
        else:
            print("You haven't selected a disk yet!")
    
    def do_exit(self, line):
        """Exit the program."""
        return True
    
def run_cli():
    JatgamFUcli().cmdloop()
