# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:46:57 2021

@author: bonje
"""

winnumber = 11, 17, 28, 30, 33, 35
print('모의 로또 당첨 번호'.center(28, '='))
print(winnumber)
print()
print('내 번호 확인'.center(30, '-'))
cnt = 0

# import random
from random import randint
# from 모듈 import 변수, 모듈 없이 바로 함수() 사용 가능

for i in range(6):
    n = randint(1, 45)
    if n in winnumber:
        print(n, '0', end = ' ')
        cnt += 1
    else:
        print(n, 'X', end=' ')

print()
print(cnt, '개 맞음')