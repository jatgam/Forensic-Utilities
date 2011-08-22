#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# DiskAnalyzer.py
# Version: 0.0.1
# By: Shawn Silva (shawn at jatgam dot com)
# Part of Jatgam Forensic Utilites
# 
# Created: 06/27/2011
# Modified: 06/27/2011
# 
# Locates and gathers information on Physical Disks.
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
#   - 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                             CHANGELOG                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 06/27/2011        v0.0.1 - Initial creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import platform
from forensicutilities.windows.ioctl.DeviceIoControl import DeviceIoControl

class PhysicalDiskAnalyzer:
    def __init__(self):
        self.ostype = platform.system()
        if self.ostype == "Windows":
            self.disks = self.__windowsListPhysicalDisks()
        elif self.ostype == "Linux":
            self.disks = self.__linuxListPhysicalDisks()
        else:
            return -1

    def __windowsListPhysicalDisks(self):
        physicalDriveList = []
        driveprefix=r"\\.\PhysicalDrive"
        for i in range(0,64):
            try:
                drive = open(driveprefix+str(i))
                diskinfo = DeviceIoControl(driveprefix+str(i)).GetDriveGeometry()
                diskinfo['Disk'] = driveprefix+str(i)
                physicalDriveList.append(diskinfo)
            except:
                pass
        return physicalDriveList
    
    def __linuxListPhysicalDisks(self):
        return -1
    
class ImageDiskAnalyzer:
    def __init__(self, image):
        return
