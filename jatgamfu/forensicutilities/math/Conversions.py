#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# conversions.py
# Version: 0.0.2
# By: Shawn Silva (shawn at jatgam dot com)
# Part of Jatgam Forensic Utilites
# 
# Created: 06/27/2011
# Modified: 05/09/2012
# 
# Various functions for working with HEX/Decimal/Binary
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
#  -  Need to completely redo the structure as this isn't sane.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                  CHANGELOG                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 05/09/2012        v0.0.2 - Added littleEndianToDecimal
# 06/27/2011        v0.0.1 - Initial creation.
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
        hex = self.swapEndianess()
        return int(hex, 16)
        
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
        
    