#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# winioctl.py
# Version: 0.0.1
# By: Shawn Silva (shawn at jatgam dot com)
# Part of Jatgam Forensic Utilites
# 
# Created: 07/08/2011
# Modified: 07/08/2011
# 
# Variables and structures found in WinIoCtl.h
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
#  - Pieces will be added as they are needed in the project.
# 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                  CHANGELOG                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 07/08/2011        v0.0.1 - Initial creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import ctypes
from ctypes import wintypes

def CTL_CODE(deviceType, function, method, access):
    return (deviceType << 16) | (access << 14) | (function << 2) | method
    
def DEVICE_TYPE_FROM_CTL_CODE(ctrlCode):
    return (ctrlCode & 0xffff0000) >> 16

FILE_DEVICE_DISK = 0x00000007
IOCTL_DISK_BASE = FILE_DEVICE_DISK

METHOD_BUFFERED = 0
METHOD_IN_DIRECT = 1
METHOD_OUT_DIRECT = 2
METHOD_NEITHER = 3

METHOD_DIRECT_TO_HARDWARE = METHOD_IN_DIRECT
METHOD_DIRECT_FROM_HARDWARE = METHOD_OUT_DIRECT

FILE_ANY_ACCESS = 0
FILE_SPECIAL_ACCESS = FILE_ANY_ACCESS
FILE_READ_ACCESS = 0x0001
FILE_WRITE_ACCESS = 0x0002

#IOCTL_DISK_GET_DRIVE_GEOMETRY_EX = 0x700a0
IOCTL_DISK_GET_DRIVE_GEOMETRY_EX = CTL_CODE(IOCTL_DISK_BASE, 0x0028, METHOD_BUFFERED, FILE_ANY_ACCESS)


class DISK_GEOMETRY(ctypes.Structure):
    '''
    Disk Geometry Data Structure
    http://msdn.microsoft.com/en-us/library/aa363972(v=vs.85).aspx
    '''
    _fields_ = [("Cylinders", wintypes.LARGE_INTEGER),
                ("MediaType", wintypes.BYTE), #MEDIA_TYPE
                ("TracksPerCylinder", wintypes.DWORD),
                ("SectorsPerTrack", wintypes.DWORD),
                ("BytesPerSector", wintypes.DWORD)]


class DISK_GEOMETRY_EX(ctypes.Structure):
    '''
    Disk Geometry EX Data Structure
    http://msdn.microsoft.com/en-us/library/aa363970(v=vs.85).aspx
    '''
    _fields_ = [("Geometry", DISK_GEOMETRY),
                ("DiskSize", wintypes.LARGE_INTEGER),
                ("Data[1]", wintypes.BYTE)]


MEDIA_TYPE = {0x00 : "Unknown",
            0x01 : "F5_1Pt2_512", #A 5.25" floppy, with 1.2MB and 512 bytes/sector.
            0x02 : "F3_1Pt44_512", #A 3.5" floppy, with 1.44MB and 512 bytes/sector.
            0x03 : "F3_2Pt88_512", #A 3.5" floppy, with 2.88MB and 512 bytes/sector.
            0x04 : "F3_20Pt8_512", #A 3.5" floppy, with 20.8MB and 512 bytes/sector.
            0x05 : "F3_720_512", #A 3.5" floppy, with 720KB and 512 bytes/sector.
            0x06 : "F5_360_512", #A 5.25" floppy, with 360KB and 512 bytes/sector.
            0x07 : "F5_320_512", #A 5.25" floppy, with 320KB and 512 bytes/sector.
            0x08 : "F5_320_1024", #A 5.25" floppy, with 320KB and 1024 bytes/sector.
            0x09 : "F5_180_512", #A 5.25" floppy, with 180KB and 512 bytes/sector.
            0x0a : "F5_160_512", #A 5.25" floppy, with 160KB and 512 bytes/sector.
            0x0b : "RemovableMedia", #Removable media other than floppy.
            0x0c : "FixedMedia", #Fixed hard disk media.
            0x0d : "F3_120M_512", #A 3.5" floppy, with 120MB and 512 bytes/sector.
            0x0e : "F3_640_512", #A 3.5" floppy, with 640KB and 512 bytes/sector.
            0x0f : "F5_640_512", #A 5.25" floppy, with 640KB and 512 bytes/sector.
            0x10 : "F5_720_512", #A 5.25" floppy, with 720KB and 512 bytes/sector.
            0x11 : "F3_1Pt2_512", #A 3.5" floppy, with 1.2MB and 512 bytes/sector.
            0x12 : "F3_1Pt23_1024", #A 3.5" floppy, with 1.23MB and 1024 bytes/sector.
            0x13 : "F5_1Pt23_1024", #A 5.25" floppy, with 1.23MB and 1024 bytes/sector.
            0x14 : "F3_128Mb_512", #A 3.5" floppy, with 128MB and 512 bytes/sector.
            0x15 : "F3_230Mb_512", #A 3.5" floppy, with 230MB and 512 bytes/sector.
            0x16 : "F8_256_128", #An 8" floppy, with 256KB and 128 bytes/sector.
            0x17 : "F3_200Mb_512", #A 3.5" floppy, with 200MB and 512 bytes/sector. (HiFD).
            0x18 : "F3_240M_512", #A 3.5" floppy, with 240MB and 512 bytes/sector. (HiFD).
            0x19 : "F3_32M_512"} #A 3.5" floppy, with 32MB and 512 bytes/sector.