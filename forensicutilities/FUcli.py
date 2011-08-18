#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# FUcli.py
# Version: 0.0.1
# By: Shawn Silva (shawn at jatgam dot com)
# 
# Created: 06/13/2011
# Modified: 06/13/2011
# 
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
# 08/02/2011        v0.0.1 - Initial script creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from forensicutilities.disk.PartitionTableAnalyzer import *
from forensicutilities.disk.DiskAnalyzer import PhysicalDiskAnalyzer
from forensicutilities.windows.ioctl.DeviceIoControl import DeviceIoControl

def run_cli():
    device = DeviceIoControl(r"\\.\PhysicalDrive0")
    devicegeo = device.GetDriveGeometry()
    
    table = PartitionTableAnalyzer(r"\\.\PhysicalDrive0", devicegeo["BytesPerSector"])
    table.printMBR()
    table.printAllParts()
    physicaldisk = PhysicalDiskAnalyzer()
    print(physicaldisk.disks)