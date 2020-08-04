# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:45:07 2017

@author: samarth
"""

import tkinter
import tkinter.messagebox
top = tkinter.Tk(className = 'samarth')

def hello():
    tkinter.messagebox.showinfo( "Learn ML","Hello samarth")
B = tkinter.Button(top , text = "Hello",command = hello)
B.pack()    
    
top.mainloop()
