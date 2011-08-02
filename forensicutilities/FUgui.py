#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# gui.py
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
# 06/13/2011        v0.0.1 - Initial script creation.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
from tkinter import *
from forensicutilities.gui import FocusedDialog

class JatgamFUgui:
    def __init__(self, root):
        self.root = root
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0, takefocus=0)
        filemenu.add_command(label="Open .img (dd)", command=self.__openDDImg)
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

    def __displayAbout(self):
        # aboutwin = Toplevel()
        # aboutwin.title('About JatgamFU')
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
        pass
        
    def buttonbox(self):
        box = Frame(self)
        w = Button(box, text="Close", width=10, command=self.cancel, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.cancel)
        self.bind("<Escape>", self.cancel)
        box.pack()
        
def run_gui():
    root = Tk()
    root.title('Jatgam Forensic Utilities')
    root.resizable(True, True)
    root.minsize(300, 300)
    JatgamFUgui(root)
    root.mainloop()
    return 0

if __name__ == '__main__':
    run_gui()