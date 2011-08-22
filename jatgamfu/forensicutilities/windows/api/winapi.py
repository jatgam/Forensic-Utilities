#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# winapi.py
# Version: 0.0.1
# By: Shawn Silva (shawn at jatgam dot com)
# Part of Jatgam Forensic Utilites
# 
# Created: 07/08/2011
# Modified: 07/08/2011
# 
# Various Windows functions called using ctypes.
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
#  - Pieces will be added as they are needed in the project.
# 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                             CHANGELOG                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 07/08/2011        v0.0.1 - Initial creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import ctypes
from ctypes import wintypes

class SECURITY_ATTRIBUTES(ctypes.Structure):
    '''
    Security Attribute Data Structure
    http://msdn.microsoft.com/en-us/library/aa379560(v=vs.85).aspx
    '''
    _fields_ = [('nLength', wintypes.DWORD),
            ('lpSecurityDescriptor', wintypes.LPVOID),
            ('bInheritHandle', wintypes.BOOLEAN)]

LPSECURITY_ATTRIBUTES = ctypes.POINTER(SECURITY_ATTRIBUTES)

'''
File Creation Attributes
'''
FILE_SHARE_READ = 0x00000001
FILE_SHARE_WRITE = 0x00000002
FILE_SHARE_DELETE = 0x00000004
NULL = 0
OPEN_EXISTING = 3
FILE_ATTRIBUTE_READONLY = 0x1
FILE_ATTRIBUTE_DIRECTORY = 0x10
FILE_ATTRIBUTE_NORMAL = 0x80
FILE_ATTRIBUTE_REPARSE_POINT = 0x400
GENERIC_READ = 0x80000000
FILE_READ_ATTRIBUTES = 0x80
INVALID_HANDLE_VALUE = wintypes.HANDLE(-1).value

'''
Create File Function
http://msdn.microsoft.com/en-us/library/aa363858(v=vs.85).aspx

http://msdn.microsoft.com/en-us/library/aa363874(v=vs.85).aspx
'''
CreateHandle = ctypes.windll.kernel32.CreateFileW
CreateHandle.argtypes = [
    wintypes.LPWSTR, #LPCTSTR lpFileName
    wintypes.DWORD, #DWORD dwDesiredAccess
    wintypes.DWORD, #DWORD dwShareMode
    LPSECURITY_ATTRIBUTES, #LPSECURITY_ATTRIBUTES lpSecurityAttributes
    wintypes.DWORD, #DWORD dwCreationDisposition
    wintypes.DWORD, #DWORD dwFlagsAndAttributes
    wintypes.HANDLE] #HANDLE hTemplateFile
CreateHandle.restype = wintypes.HANDLE


'''
Close Handle Function
'''
CloseHandle = ctypes.windll.kernel32.CloseHandle
CloseHandle.argtypes = (wintypes.HANDLE,)
CloseHandle.restype = wintypes.BOOLEAN