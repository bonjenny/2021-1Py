# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:20:42 2021

@author: bonje
"""

from random import randint
correct = randint(1, 10)

user = int(input('1에서 10사이의 수를 입력하세요. >> '))
while True:
    if user == correct:
        print()
        print('축하합니다, {}: 정답입니다.'.format(correct))
        print()
        break;
    elif user < correct:
        query = '{}보다 더 큰 수로 다시 입력하세요. >> '.format(user)
    elif user > correct:
        query = '{}보다 더 작은 수로 다시 입력하세요. >> '.format(user)
    user = int(input(query))

print(" 종료 ".center(40, '*'))