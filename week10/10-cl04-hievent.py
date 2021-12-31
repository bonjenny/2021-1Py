# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:11:01 2021

@author: bonje
"""

from tkinter import *

def ebnd(event):
    global str
    str = str + 'bind: 안녕!\n'
    lbl['text'] = str
    lbl.pack()
    print('bind: 안녕!')

def ecmd():
    global str
    str = str + 'command: 안녕!'
    lbl['text'] = str
    lbl.pack()
    print('command: 안녕!')

win = Tk()
win.title('반가워요, Tkinter!')
win.geometry('640x400+100+100') # 너비와 높이, 좌측 상단 x, y좌표

str = ''
lbl = Label(win, text=str)

btn = Button(win, text='인사 이벤트 처리') # 버튼
btn.pack(expand=True, fill='both')
btn.bind('<Button-1>', ebnd)
btn['command'] = ecmd

win.mainloop()
