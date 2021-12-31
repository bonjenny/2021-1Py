# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:23:41 2021

@author: 엄지희
"""

from tkinter import *
 
win = Tk()
win.title('라인 그리기')
win.geometry('640x400+100+100') # 너비와 높이, 좌측 상단 x, y좌표

def click1(event):
    global sX, sY
    print("클릭 위치", event.x, event.y)
    sX, sY = event.x, event.y
    
def release1(event):
    global eX, eY
    print("릴리즈 위치", event.x, event.y)
    eX, eY = event.x, event.y
    # 직선 라인 그리기
    canvas.create_line(sX, sY, eX, eY, fill="blue", width=2)

def click2(event):
    global sX, sY
    print("클릭 위치", event.x, event.y)
    sX, sY = event.x, event.y
    
def release2(event):
    global eX, eY
    print("릴리즈 위치", event.x, event.y)
    eX, eY = event.x, event.y
    # 직선 라인 그리기
    canvas.create_line(sX, sY, eX, eY, fill="red", width=2)

def click3(event):
    global sX, sY
    print("클릭 위치", event.x, event.y)
    sX, sY = event.x, event.y
    
def release3(event):
    global eX, eY
    print("릴리즈 위치", event.x, event.y)
    eX, eY = event.x, event.y
    # 직선 라인 그리기
    canvas.create_line(sX, sY, eX, eY, fill="green", width=2)

canvas = Canvas(win, relief='solid', bd=2)
canvas.pack(expand=True, fill='both')

# 왼쪽 마우스 버튼 클릭 바인딩
canvas.bind("<Button-1>", click1)
# 왼쪽 마우스 버튼 릴리즈 바인딩
canvas.bind("<ButtonRelease-1>", release1)

# 마우스 중간 버튼 클릭 바인딩
canvas.bind("<Button-2>", click2)
# 마우스 중간 버튼 릴리즈 바인딩
canvas.bind("<ButtonRelease-2>", release2)

# 오른쪽 마우스 버튼 클릭 바인딩
canvas.bind("<Button-3>", click3)
# 오른쪽 마우스 버튼 릴리즈 바인딩
canvas.bind("<ButtonRelease-3>", release3)

win.mainloop()