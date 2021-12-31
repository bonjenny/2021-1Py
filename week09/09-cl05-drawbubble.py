# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:48:33 2021

@author: 엄지희
"""

import turtle as t
from random import randint
from random import choice

tshs = ['arrow', 'circle', 'turtle', 'square', 'triangle', 'classic']
han = ['화살', '원', '거북이', '사각형', '삼각형', '전통']
cols = ['red', 'blue', 'green', 'purple', 'magenta', 'black', 
        'gray', 'yellow', 'cyan', 'orange', 'aqua']

t.setup(800, 500)

for i in range(20):
    t.pu()
    x = randint(-300, 300)
    y = randint(-200, 200)
    t.goto(x, y)
    t.pd()
    
    t.shape(tshs[i % len(tshs)])
    t.pencolor(cols[i % len(cols)])
    t.fillcolor(cols[i % len(cols)])
    t.begin_fill() # 칠하기 시작
    t.circle(randint(3, 50))
    t.end_fill() # 칠하기 종료
    
    t.pencolor(choice(cols))
    t.write(han[i % len(han)])
