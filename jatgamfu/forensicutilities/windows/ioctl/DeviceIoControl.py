#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# DeviceIoControl.py
# Version: 0.0.1
# By: Shawn Silva (shawn at jatgam dot com)
# Part of Jatgam Forensic Utilites
# 
# Created: 07/08/2011
# Modified: 07/08/2011
# 
# Uses the Windows function DeviceIoControl to communicate with
# hardware and recieve device status/information.
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
from forensicutilities.windows.api import winapi
from forensicutilities.windows.ioctl import winioctl

class DeviceIoControl:
    def __init__(self, path):
        self.path = path
        
    def __DeviceIoControl(self, devicehandle, IoControlCode, input, output):
        '''
        DeviceIoControl Function
        http://msdn.microsoft.com/en-us/library/aa363216(v=vs.85).aspx
        '''
        DevIoCtl = ctypes.windll.kernel32.DeviceIoControl
        DevIoCtl.argtypes = [
            wintypes.HANDLE, #HANDLE hDevice
            wintypes.DWORD, #DWORD dwIoControlCode
            wintypes.LPVOID, #LPVOID lpInBuffer
            wintypes.DWORD, #DWORD nInBufferSize
            wintypes.LPVOID, #LPVOID lpOutBuffer
            wintypes.DWORD, #DWORD nOutBufferSize
            ctypes.POINTER(wintypes.DWORD), #LPDWORD lpBytesReturned
            wintypes.LPVOID] #LPOVERLAPPED lpOverlapped
        DevIoCtl.restype = wintypes.BOOL
        
        if isinstance(output, int):
            output = ctypes.create_string_buffer(output)

        input_size = len(input) if input is not None else 0
        output_size = len(output)
        assert isinstance(output, ctypes.Array)

        BytesReturned = wintypes.DWORD()
        
        status = DevIoCtl(devicehandle, IoControlCode, input, input_size, output, output_size, ctypes.byref(BytesReturned), None)
        return output[:BytesReturned.value] if status is not 0 else 0
        
    def GetDriveGeometry(self):
        diskhandle = winapi.CreateHandle(
                self.path,
                winapi.NULL,
                winapi.FILE_SHARE_READ|winapi.FILE_SHARE_WRITE,
                winapi.LPSECURITY_ATTRIBUTES(),
                winapi.OPEN_EXISTING,
                winapi.FILE_ATTRIBUTE_NORMAL,
                winapi.NULL)
        if diskhandle == winapi.INVALID_HANDLE_VALUE:
            return -1

        devicegeobytes = self.__DeviceIoControl(diskhandle, winioctl.IOCTL_DISK_GET_DRIVE_GEOMETRY_EX, None, 1024)
        temp = ctypes.cast(devicegeobytes, ctypes.POINTER(winioctl.DISK_GEOMETRY_EX)).contents
        devicegeo = {"DiskSize" : temp.DiskSize, "Cylinders" : temp.Geometry.Cylinders, "MediaType" : temp.Geometry.MediaType, "TracksPerCylinder" : temp.Geometry.TracksPerCylinder, "SectorsPerTrack" : temp.Geometry.SectorsPerTrack, "BytesPerSector" : temp.Geometry.BytesPerSector}
        winapi.CloseHandle(diskhandle)
        return devicegeo