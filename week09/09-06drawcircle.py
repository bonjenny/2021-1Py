# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:37:12 2021

@author: 엄지희
"""

import turtle as t
t.setup(500, 400) # 초기 윈도의 크기 조정
t.speed(1) # 1에서 10까지 거북이 속도 증가, 0이면 초고속
t.shape('classic') # 기본 모양, turtle, arrow, circle, square, triangle

t.home()
t.write('좌표 (0, 0)') # 좌표 (0, 0)이라고 표시

t.pu() # 이동에 선이 그려지지 않도록, penup(), up()
t.goto(0, -100) # 이동

t.pd() # 이동에 선이 그려지도록, pendown(), down()
t.hideturtle() # 거북이는 보이지 않도록, ht()
t.fillcolor('aqua') # 내부 칠할 색 지정
t.begin_fill() # 칠하기 시작
t.circle(100) # 원 그리기
t.end_fill() # 칠하기 종료