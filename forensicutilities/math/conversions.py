#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# conversions.py
# Version: 0.0.1
# By: Shawn Silva (shawn at jatgam dot com)
# Part of Jatgam Forensic Utilites
# 
# Created: 06/27/2011
# Modified: 06/27/2011
# 
# Various functions for working with HEX/Decimal/Binary
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
#  -  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                             CHANGELOG                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 06/27/2011        v0.0.1 - Initial creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


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
        
class DecimalUtilities:
    def __init__(self):
        return
        
    def toBinaryStr(self):
        binarystr = ""
        for i in reversed(range(8)):
            binarystr += str((n & (1 << i)) and 1)
        return binarystr

class BinaryNumUtilities:
    def __init__(self):
        return

class BinaryDataUtilities:
    def __init__(self, data):
        self.data = data
        return
        
    