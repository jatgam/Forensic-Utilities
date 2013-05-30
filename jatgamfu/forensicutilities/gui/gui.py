#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# gui.py
# Part of Jatgam Forensic Utilites
# 
# Created: 06/13/2011
# Modified: 06/13/2011
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
import os

from tkinter import *
from tkinter import tix
from tkinter.constants import *

from forensicutilities.gui import FocusedDialog
from forensicutilities.disk import DiskAnalyzer
from forensicutilities.math.Conversions import *

class JatgamFUgui:
    def __init__(self, root):
        self.root = root
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0, takefocus=0)
        filemenu.add_command(label="Open .img (dd)", command=self.__openDDImg)
        filemenu.add_command(label="Open Physical Disk", command=self.__openDisk)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        editmenu = Menu(menubar, tearoff=0, takefocus=0)
        editmenu.add_command(label="Copy", command=self.__copy)
        editmenu.add_command(label="Cut", command=self.__cut)
        editmenu.add_command(label="Paste", command=self.__paste)
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        helpmenu = Menu(menubar, tearoff=0, takefocus=0)
        helpmenu.add_command(label="About", command=self.__displayAbout)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        self.root.config(menu=menubar)
        
        toolbar = Frame(self.root)

        b = Button(toolbar, text="new", width=6, command=self.__callback)
        b.pack(side=LEFT, padx=2, pady=2)

        b = Button(toolbar, text="open", width=6, command=self.__callback)
        b.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)


        frame = Frame(self.root)
        frame.pack()
                
        self.t = Text(frame, height=10, width=100)
        self.t.pack()

        
        statusFrame = Frame(self.root)
        statusFrame.pack(side=BOTTOM, anchor=W)
        status = StatusBar(statusFrame, 10)
        status.pack(side=LEFT, fill=X)
        status.set("test")
        status1 = StatusBar(statusFrame, 10)
        status1.pack(side=LEFT, fill=X)
        status1.set("test1")
    
    def __callback(self):
        return

    def __openDDImg(self):
        return

    def __openDisk(self):
        ChooseDevice(self.root, "Choose a disk drive...")
        
    def __displayAbout(self):
        AboutDialog(self.root,"About Jatgam Forensic Utilities")
        
        return
    
    def __copy(self):
        if not self.t.tag_ranges(SEL):
            pass
        else:
            self.t.clipboard_clear()
            text = self.t.get(SEL_FIRST, SEL_LAST)
            self.t.clipboard_append(text)
    def __cut(self):
        if not self.t.tag_ranges(SEL):
            pass
        else:
            self.__copy()
            self.t.delete(SEL_FIRST, SEL_LAST)
    def __paste(self):
        try:
            text = self.t.selection_get(selection='CLIPBOARD')
        except:
            return
        self.t.insert(INSERT, text)
        self.t.tag_remove(SEL, '1.0', END)
        self.t.tag_add(SEL, INSERT+'-%dc' % len(text), INSERT)
        self.t.see(INSERT)
        
class StatusBar(Frame):
    def __init__(self, master, width):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W, width=width)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

class AboutDialog(FocusedDialog.FocusedDialog):
    def body(self, master):
        aboutlabel = Label(master, text="Jatgam Forensic Utilities\nVersion 0.0.1\nCopyright 2011-2013 Jatgam Technical Solutions")
        aboutlabel.pack()
        
    def buttonbox(self):
        box = Frame(self)
        w = Button(box, text="Close", width=10, command=self.cancel, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.cancel)
        self.bind("<Escape>", self.cancel)
        box.pack()
        
class ChooseDevice(FocusedDialog.FocusedDialog):
    def __createEntryField(self, parent, caption, width=None, row=None, column=0, **options):
        Label(parent, text=caption).grid(row=row, column=column, sticky=E)
        entry = Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.grid(row=row, column=column+1)
        return entry
    
    def __updateDeviceInfo(self, device):
        for d in self.disks:
            if d["Disk"] == device:
                self.vdiskpath.set(d["Disk"])
                self.vsize.set("%.2f" % DecimalUtilities.bytesToGB(d["DiskSize"]))
                self.vtpc.set(d["TracksPerCylinder"])
                self.vcyl.set(d["Cylinders"])
                self.vbps.set(d["BytesPerSector"])
                self.vmtype.set(d["MediaType"])
                self.vspt.set(d["SectorsPerTrack"])
                return
            else:
                pass
        return -1
        
    
    def body(self, master):
        self.disks = DiskAnalyzer.PhysicalDiskAnalyzer().disks
        if self.disks == -1:
            pass
        else:
            list = tix.ComboBox(master, label="Drive: ", command=self.__updateDeviceInfo, dropdown=1, editable=0, options='listbox.height 6 label.width 10 label.anchor e')
            
            list.pack(side=tix.TOP, anchor=tix.W)
            
            for d in self.disks:
                list.insert(tix.END, d["Disk"])
            
            diskInfoFrame = Frame(master)
            diskInfoFrame.pack()
            
            self.vdiskpath = StringVar()
            self.vsize = StringVar()
            self.vtpc = StringVar()
            self.vcyl = StringVar()
            self.vbps = StringVar()
            self.vmtype = StringVar()
            self.vspt = StringVar()
            
            diskpath = self.__createEntryField(diskInfoFrame, "Disk Path: ", row=0, state="readonly", textvariable=self.vdiskpath)
            size = self.__createEntryField(diskInfoFrame, "Size in GB: ", row=1, state="readonly", textvariable=self.vsize)
            tpc = self.__createEntryField(diskInfoFrame, "Tracks Per Cylinder: ", row=2, state="readonly", textvariable=self.vtpc)
            cyl = self.__createEntryField(diskInfoFrame, "Cylinders: ", row=3, state="readonly", textvariable=self.vcyl)
            bps = self.__createEntryField(diskInfoFrame, "Bytes Per Sector: ", row=4, state="readonly", textvariable=self.vbps)
            mtype = self.__createEntryField(diskInfoFrame, "Media Type: ", row=5, state="readonly", textvariable=self.vmtype)
            spt = self.__createEntryField(diskInfoFrame, "Sectors Per Track: ", row=6, state="readonly", textvariable=self.vspt)
            
def run_gui():
    root = tix.Tk()
    root.title('Jatgam Forensic Utilities')
    root.resizable(True, True)
    root.minsize(300, 300)
    JatgamFUgui(root)
    root.mainloop()
    return 0

if __name__ == '__main__':
    run_gui()