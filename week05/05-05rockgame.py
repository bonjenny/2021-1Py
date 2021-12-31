# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:17:23 2021

@author: bonje
"""

rsp = ['가위', '바위', '보']
for i in range(len(rsp)):
    print(rsp[i], end=' ')
print()

from random import choice
print('컴퓨터의 가위 바위 보 5개')
for i in range(5):
    print(choice(rsp))