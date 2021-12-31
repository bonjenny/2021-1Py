# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:26:20 2021

@author: 엄지희
"""

from tkinter import *
win = Tk()

btn1 = Button(win, text='left')
btn1.pack(side="left")
btn2 = Button(win, text='right')
btn2.pack(side="right", expand=True, fill='x')

win.mainloop()