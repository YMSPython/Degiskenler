import tkinter
from tkinter import *

top = tkinter.Tk()
# Code to add widgets will go here...


L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)


top.mainloop()