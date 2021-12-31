# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:11:40 2021

@author: 엄지희
"""

import turtle as t
t.shape('turtle') # 거북이모양 펜

# 삼각형 그리기
t.forward(100)
t.left(120)
t.fd(100) # t.forward()
t.lt(120) # t.left()
t.fd(100)
t.lt(120)

# 사각형 그리기
t.pencolor('blue')
for _ in range(4):
    t.lt(90)
    t.fd(150)

# 삼각형 그리기
t.pencolor('green')
t.goto(100, -100) # t.setpos(x,y)
t.goto(-100, -100) # t.setposition(x,y)
t.home()

# t.setheading(), t.seth()는 절대각도로 방향 지정