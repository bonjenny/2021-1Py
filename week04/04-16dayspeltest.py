# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:12:16 2021

@author: bonje
"""

days = ['monday', 'tuesday', 'wendsday']

while True:
    user = input('월, 화, 수 중 하나 영어 단어 입력 >> ')
    if user not in days:
        print('잘못 입력했어요!')
        continue
    print('입력: %s, 철자가 맞습니다.' % user)
    break

print('종료'.center(15, '*'))