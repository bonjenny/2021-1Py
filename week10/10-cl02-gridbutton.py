# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:36:30 2021

@author: bonje
"""

from tkinter import *

win = Tk()
win.title('그리드에 배치한 버튼의 다양한 모습')
rtype = ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken']
txt = ['(0, 0)', '(0, 1)', '(1, 0)', '(1, 1)', '(2, 0)', '(2, 1)']


b1 = Button(win, text="(0, 0)", width="30")
b1.grid(row = 0, column = 0)

b2 = Button(win, text="(0, 1)", width="30")
b2.grid(row = 0, column = 1)

b3 = Button(win, text="(1, 0)", width="30")
b3.grid(row = 1, column = 0)

b4 = Button(win, text="(1, 1)", width="30")
b4.grid(row = 1, column = 1)

b5 = Button(win, text="(2, 0)", width="30")
b5.grid(row = 2, column = 0)

b6 = Button(win, text="(2, 1)", width="30")
b6.grid(row = 2, column = 1)

for i, t in enumerate(rtype):
    btn = Button(win, text=txt[i], width="30", relief=rtype[i])
    btn.grid(row = int(i/2), column = int(i%2))

win.mainloop()
