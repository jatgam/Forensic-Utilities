#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# guitest.py
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
#  - Display Images. Thumbnails. PIL. ImageTk
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                             CHANGELOG                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 06/13/2011        v0.1.0 - Initial script creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import Tkinter, tkFileDialog, tkMessageBox, Tkconstants

class ADSApp:
    def __init__(self, root):
        
        
        menubar = Tkinter.Menu(root)
        filemenu = Tkinter.Menu(menubar, tearoff=0, takefocus=0)
        filemenu.add_command(label="Open .img (dd)", command=self.__openDDImg)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        editmenu = Tkinter.Menu(menubar, tearoff=0, takefocus=0)
        editmenu.add_command(label="Copy", command=self.__copy)
        editmenu.add_command(label="Cut", command=self.__cut)
        editmenu.add_command(label="Paste", command=self.__paste)
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        helpmenu = Tkinter.Menu(menubar, tearoff=0, takefocus=0)
        helpmenu.add_command(label="About", command=self.__displayAbout)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        root.config(menu=menubar)
        
        toolbar = Tkinter.Frame(root)

        b = Tkinter.Button(toolbar, text="new", width=6, command=self.__callback)
        b.pack(side=Tkinter.LEFT, padx=2, pady=2)

        b = Tkinter.Button(toolbar, text="open", width=6, command=self.__callback)
        b.pack(side=Tkinter.LEFT, padx=2, pady=2)

        toolbar.pack(side=Tkinter.TOP, fill=Tkinter.X)


        frame = Tkinter.Frame(root)
        frame.pack()
                
        self.t = Tkinter.Text(frame, height=10, width=100)
        self.t.pack()

        
        statusFrame = Tkinter.Frame(root)
        statusFrame.pack(side=Tkinter.BOTTOM, anchor=Tkinter.W)
        status = StatusBar(statusFrame, 10)
        status.pack(side=Tkinter.LEFT, fill=Tkinter.X)
        status.set("test")
        status1 = StatusBar(statusFrame, 10)
        status1.pack(side=Tkinter.LEFT, fill=Tkinter.X)
        status1.set("test1")
    
    def __callback(self):
        return

    def __openDDImg(self):
        return

    def __displayAbout(self):
        return
    
    def __copy(self):
        if not self.t.tag_ranges(Tkinter.SEL):
            pass
        else:
            self.t.clipboard_clear()
            text = self.t.get(Tkinter.SEL_FIRST, Tkinter.SEL_LAST)
            self.t.clipboard_append(text)
    def __cut(self):
        if not self.t.tag_ranges(Tkinter.SEL):
            pass
        else:
            self.__copy()
            self.t.delete(Tkinter.SEL_FIRST, Tkinter.SEL_LAST)
    def __paste(self):
        try:
            text = self.t.selection_get(selection='CLIPBOARD')
        except:
            return
        self.t.insert(Tkinter.INSERT, text)
        self.t.tag_remove(Tkinter.SEL, '1.0', Tkinter.END)
        self.t.tag_add(Tkinter.SEL, Tkinter.INSERT+'-%dc' % len(text), Tkinter.INSERT)
        self.t.see(Tkinter.INSERT)
        
class StatusBar(Tkinter.Frame):
    def __init__(self, master, width):
        Tkinter.Frame.__init__(self, master)
        self.label = Tkinter.Label(self, bd=1, relief=Tkinter.SUNKEN, anchor=Tkinter.W, width=width)
        self.label.pack(fill=Tkinter.X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

def listPhysicalDisks():
    physicalDriveList = []
    driveprefix=r"\\.\PhysicalDrive"
    for i in range(0,64):
        try:
            drive = file(driveprefix+str(i))
            physicalDriveList.append(driveprefix+str(i))
        except:
            pass
    print physicalDriveList

        
def gui_main():
    root = Tkinter.Tk()
    root.title('Jatgam Alternate Data Streams')
    root.resizable(True, True)
    root.minsize(300, 0)
    ADSApp(root)
    root.mainloop()
    return 0

if __name__ == '__main__':
    #gui_main()
    listPhysicalDisks()