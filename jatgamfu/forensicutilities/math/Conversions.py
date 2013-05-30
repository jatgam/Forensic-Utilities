#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# conversions.py
# Part of Jatgam Forensic Utilites
# 
# Created: 06/27/2011
# Modified: 05/09/2012
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

class HexUtilities:
    def __init__(self, hexstr):
        self.hexstr = hexstr
        return

    def swapEndianess(self):
        if len(self.hexstr)%2 != 0:
                return -1

        swapList = []
        for i in range(0, len(self.hexstr), 2):
            swapList.insert(0, self.hexstr[i:i+2])

        return ''.join(swapList)
        
    def littleEndianToDecimal(self):
        hexs = self.swapEndianess()
        return int(hexs, 16)
        
class DecimalUtilities:
    def toBinaryStr(num):
        binarystr = ""
        for i in reversed(list(range(8))):
            binarystr += str((num & (1 << i)) and 1)
        return binarystr
        
    def bytesToGB(bytes):
        return bytes/1024/1024/1024
        

class BinaryNumUtilities:
    def __init__(self):
        return

class BinaryDataUtilities:
    def __init__(self, data):
        self.data = data
        return
        
    