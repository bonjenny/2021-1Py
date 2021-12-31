# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:06:58 2021

@author: bonje
"""

from random import randint
LUCKY = 7

while True:
    n = randint(0, 9)
    if n == LUCKY:
        print('드디어 %d, 종료!' % n)
        break
    else:
        print('%d, %d 나올 때까지 계속!' % (n, LUCKY))
else:
    print('여기는 실행되지 않습니다.')