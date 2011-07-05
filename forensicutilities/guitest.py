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
#  - Display Images. Thumbnails. PIL. ImageTk
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                             CHANGELOG                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 06/13/2011        v0.1.0 - Initial script creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import tkinter, tkinter.filedialog, tkinter.messagebox, tkinter.constants

class ADSApp:
    def __init__(self, root):
        
        
        menubar = tkinter.Menu(root)
        filemenu = tkinter.Menu(menubar, tearoff=0, takefocus=0)
        filemenu.add_command(label="Open .img (dd)", command=self.__openDDImg)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        editmenu = tkinter.Menu(menubar, tearoff=0, takefocus=0)
        editmenu.add_command(label="Copy", command=self.__copy)
        editmenu.add_command(label="Cut", command=self.__cut)
        editmenu.add_command(label="Paste", command=self.__paste)
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        helpmenu = tkinter.Menu(menubar, tearoff=0, takefocus=0)
        helpmenu.add_command(label="About", command=self.__displayAbout)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        root.config(menu=menubar)
        
        toolbar = tkinter.Frame(root)

        b = tkinter.Button(toolbar, text="new", width=6, command=self.__callback)
        b.pack(side=tkinter.LEFT, padx=2, pady=2)

        b = tkinter.Button(toolbar, text="open", width=6, command=self.__callback)
        b.pack(side=tkinter.LEFT, padx=2, pady=2)

        toolbar.pack(side=tkinter.TOP, fill=tkinter.X)


        frame = tkinter.Frame(root)
        frame.pack()
                
        self.t = tkinter.Text(frame, height=10, width=100)
        self.t.pack()

        
        statusFrame = tkinter.Frame(root)
        statusFrame.pack(side=tkinter.BOTTOM, anchor=tkinter.W)
        status = StatusBar(statusFrame, 10)
        status.pack(side=tkinter.LEFT, fill=tkinter.X)
        status.set("test")
        status1 = StatusBar(statusFrame, 10)
        status1.pack(side=tkinter.LEFT, fill=tkinter.X)
        status1.set("test1")
    
    def __callback(self):
        return

    def __openDDImg(self):
        return

    def __displayAbout(self):
        return
    
    def __copy(self):
        if not self.t.tag_ranges(tkinter.SEL):
            pass
        else:
            self.t.clipboard_clear()
            text = self.t.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
            self.t.clipboard_append(text)
    def __cut(self):
        if not self.t.tag_ranges(tkinter.SEL):
            pass
        else:
            self.__copy()
            self.t.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    def __paste(self):
        try:
            text = self.t.selection_get(selection='CLIPBOARD')
        except:
            return
        self.t.insert(tkinter.INSERT, text)
        self.t.tag_remove(tkinter.SEL, '1.0', tkinter.END)
        self.t.tag_add(tkinter.SEL, tkinter.INSERT+'-%dc' % len(text), tkinter.INSERT)
        self.t.see(tkinter.INSERT)
        
class StatusBar(tkinter.Frame):
    def __init__(self, master, width):
        tkinter.Frame.__init__(self, master)
        self.label = tkinter.Label(self, bd=1, relief=tkinter.SUNKEN, anchor=tkinter.W, width=width)
        self.label.pack(fill=tkinter.X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

def listPhysicalDisks():
    physicalDriveList = []
    driveprefix=r"\\.\PhysicalDrive"
    for i in range(64):
        try:
            drive = open(driveprefix+str(i))
            physicalDriveList.append(driveprefix+str(i))
        except:
            pass
    print(physicalDriveList)

        
def gui_main():
    root = tkinter.Tk()
    root.title('Jatgam Alternate Data Streams')
    root.resizable(True, True)
    root.minsize(300, 0)
    ADSApp(root)
    root.mainloop()
    return 0

if __name__ == '__main__':
    gui_main()
    listPhysicalDisks()