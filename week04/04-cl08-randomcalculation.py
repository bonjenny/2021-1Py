# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:48:57 2021

@author: bonje
"""

from random import randint
pre = randint(1, 100)
print('첫 값은 %d 입니다.' % pre)

while True:
    opr = input('산술 연산의 종류를 입력하세요. >> ')
    opd = int(input('두 번째 피연산자를 입력하세요. >> '))
    if opr == '+':
        pst = pre + opd
        break
    elif opr == '-':
        pst = pre - opd
        break
    elif opr == '*':
        pst = pre * opd
        break
    elif opr == '/':
        pst = pre / opd
        break
    elif opr == '%':
        pst = pre % opd
        break
    else:
        print('연산자를 다시 입력해주세요. (+, -, *, /, % 중)')
        continue
print()
print(' 연산 결과 '.center(35, '*'))
print('{} {} {} = {}'.format(pre, opr, opd, pst))
print(' 연산을 종료합니다. '.center(32, '='))