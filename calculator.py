from tkinter import *
from tkinter import ttk

WIDTH = 68
HEIDTH = 50

class Display(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGTH)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        self.label = ttk.Label(self, text="0", anchor=E, background='black', forenground='white', font='Helvetica 36')
        self.label.pack(side=TOP, fill=BOTH, expand=True)

class CalcButton(ttk.Frame):
    def __init__(self, parent, label, command):
        ttkFrame.__init__(self, parent, width=WIDTH, height=HEIGHT)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        btn = ttk.Button(self, text=text, command=command)
