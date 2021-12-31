# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:29:03 2021

@author: bonje
"""

# for문으로 리스트 생성
a = []
for i in range(10):
    a.append(i)
print(a)

# 컴프리헨션으로 리스트 생성
seq = [i for i in range(10)]
print(seq)

# for문으로 리스트 생성
s = []
for i in range(10):
    if i%2 == 1:
        s.append(i**2)
print(s)

# 컴프리헨션 리스트 생성
squares = [i**2 for i in range(10) if i%2 == 1]
print(squares)