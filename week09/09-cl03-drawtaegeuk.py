# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:08:05 2021

@author: 엄지희
"""

import turtle as t

# 선 색상에 사용할 이름 리스트
col = ['yellow', 'red', 'blue']
t.setup(500, 500)
t.bgcolor('black')
t.speed(0)

for i in range(200):
    t.pencolor(col[i % len(col)])
    t.width(i/200 + 1)
    t.fd(i*2)
    t.lt(119)
