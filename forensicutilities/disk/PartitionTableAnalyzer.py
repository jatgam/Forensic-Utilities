#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PartitionTableAnalyzer.py
# Version: 0.0.1
# By: Shawn Silva (shawn at jatgam dot com)
# Part of Jatgam Forensic Utilites
# 
# Created: 06/23/2011
# Modified: 06/23/2011
# 
# Will grab the first sector from physical disks and images and
# parse out partition information.
# -----------------------------------------------------------------
#
# 
# REQUIREMENTS:
# Python 2.7.x
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
#  - Locate and Parse Extended Partitions.
#  - Compute Sector Size Instead of requesting user input.
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                             CHANGELOG                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 06/23/2011        v0.0.1 - Initial creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import binascii
from forensicutilities.math.conversions import *

PARTITION1 = 446, 461
PARTITION2 = 462, 477
PARTITION3 = 478, 493
PARTITION4 = 494, 509

PARTITIONTYPES = {"00" : "Empty", "01" : "FAT12, CHS", "02" : "XENIX root", "03" : "XENIX /usr", "04" : "FAT16, 16-32 MB, CHS", 
                    "05" : "Microsoft Extended, CHS", "06" : "FAT16, 32 MB-2GB, CHS", "07" : "NTFS", "0B" : "FAT32, CHS", 
                    "0C" : "FAT32, LBA", "0E" : "FAT16, 32 MB-2GB, LBA", "0F" : "Microsoft Extended, LBA", "11" : "Hidden FAT12, CHS",
                    "12" : "Configuration/Diagnostics", "14" : "Hidden FAT16, 16-32 MB, CHS", "16" : "Hidden FAT16, 32 MB-2GB, CHS", 
                    "1B" : "Hidden FAT32, CHS", "1C" : "Hidden FAT32, LBA", "1E" : "Hidden FAT16, 32 MB-2GB, LBA", "27" : "PQservice/Rescue Partition",
                    "42" : "Microsoft MBR. Dynamic Disk", "51" : "Novell", "63" : "Unix System V", "64" : "Novell Netware 286, 2.xx",
                    "65" : "Novell Netware 386, 3.xx or 4.xx", "66" : "Novell Netware SMS", "67" : "Novell", "68" : "Novell",
                    "69" : "Novell Netware 5+, Novell Netware NSS", "80" : "MINIX until 1.4a", "81" : "MINIX since 1.4b|Early Linux",
                    "82" : "Solaris x86|Linux Swap", "83" : "Linux", "84" : "Hibernation", "85" : "Linux Extended", "86" : "FAT16 Volume Set", 
                    "87" : "NTFS Volume Set", "8E" : "Linux LVM", "9F" : "BSD/OS", "A0" : "Hibernation", "A1" : "Hibernation", "A5" : "FreeBSD", 
                    "A6" : "OpenBSD", "A8" : "Mac OSX", "A9" : "NetBSD", "AB" : "Mac OSX Boot", "B7" : "BSDI", "B8" : "BSDI Swap", 
                    "BC" : "Acronis Backup", "BE" : "Solaris 8 Boot", "BF" : "New Solaris x86", "DE" : "Dell PowerEdge Server Utilities",
                    "E8" : "LUKS", "EB" : "BeOS BFS", "EC" : "SkyOS SkyFS", "EE" : "EFI GPT Disk", "EF" : "EFI System Partition",
                    "FB" : "Vmware File System", "FC" : "Vmware Swap", "FD" : "Linux Raid Partition", "FE" : "Old Linux LVM"}


class PartitionTableAnalyzer:
    def __init__(self, disk, sectorsize):
        self.disk = disk
        self.sectorsize = sectorsize
        self.MBRdata = self.__readMBR(self.disk, self.sectorsize)
        self.MBRhexlist = self.__listifyMBR(self.MBRdata)
        self.partitions = self.__primaryPartitionParse(self.MBRhexlist)
    
    #def __determineSectorSize(self):
    
    
    def __readMBR(self, disk, sectorsize):
        with open(disk, 'rb') as f:
            f.seek(0)
            MBRdata = f.read(sectorsize)
        return MBRdata
    
    def __listifyMBR(self, MBRdata):
        MBRhexlist = []
        for byte in MBRdata:
            MBRhexlist.append(binascii.hexlify(byte).upper())
        return MBRhexlist
    
    def __primaryPartitionParse(self, MBRhexlist):
        partitions = []
        
        return
        
    def __printPartitionTable(self, byterange, partitionnum):
        print "-" * 77
        print "PARTITION TABLE: PARTITION " + partitionnum + ": MBR Byte Range = " + str(byterange[0]) + "-" + str(byterange[1])
        print "-" * 77
        print " ".join(self.MBRhexlist[byterange[0]:byterange[1]+1])
        print "." * 77
        print "Bootable Flag:\t\t" + self.MBRhexlist[byterange[0]]
        print "Starting CHS Address:\t" + " ".join(self.MBRhexlist[byterange[0]+1:byterange[0]+3+1])
        print "Partition Type:\t\t" + self.MBRhexlist[byterange[0]+4] + " - " + PARTITIONTYPES[self.MBRhexlist[byterange[0]+4]]
        print "Ending CHS Address:\t" + " ".join(self.MBRhexlist[byterange[0]+5:byterange[0]+7+1])
        print "Starting LBA Address:\t" + " ".join(self.MBRhexlist[byterange[0]+8:byterange[0]+11+1])
        print "Size in Sectors:\t" + " ".join(self.MBRhexlist[byterange[0]+12:byterange[0]+15+1])
        return
    
    def printMBR(self):
        numlines = self.sectorsize / 16
        print "-" * 77
        print "Master Boot Record: SECTOR 0"
        print "-" * 77
        for line in range(numlines):
            asciidata = ""
            offset = hex(line+0*32)[2:].upper().zfill(7)[-7:] + '0'
            hexdata = " ".join(self.MBRhexlist[line*16:(line+1)*16])
            for byte in self.MBRhexlist[line*16:(line+1)*16]:
                if len(repr(chr(int(byte, 16)))) == 3 or int(byte, 16) == ord('\\'):
                    asciidata += chr(int(byte, 16))
                else:
                    asciidata += "."
            print offset + " | " + hexdata + " | " + asciidata
        print "-" * 77
        
    def printAllParts(self):
        """
        0-0 Bootable Flag
        1-3 Starting CHS Address
        4-4 Partition Type
        5-7 Ending CHS Address
        8-11 Starting LBA Address
        12-15 Size in Sectors
        """
        self.__printPartitionTable(PARTITION1, "1")
        self.__printPartitionTable(PARTITION2, "2")
        self.__printPartitionTable(PARTITION3, "3")
        self.__printPartitionTable(PARTITION4, "4")

    
    #def listAllNTFSParts(self):