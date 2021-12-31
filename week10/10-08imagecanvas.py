# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:04:02 2021

@author: 엄지희
"""

from tkinter import *

win = Tk()
win.title("그림 로드")
win.geometry("310x439")

# 캔버스 생성
canvas = Canvas(win, bg='Yellow')
# 캔버스를 윈도에 배치, 가로 세로로 확장되게
canvas.pack(expand=YES, fill=BOTH)

# 사진 생성
img = PhotoImage(file="imitation.gif")

# 사진을 캔버스 위에 생성
canvas.create_image(10, 10, anchor=NW, image=img)

win.mainloop()