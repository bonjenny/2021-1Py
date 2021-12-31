# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:11:17 2021

@author: bonje
"""

dates = int(input('한 달 최대 일수 입력 >> '))
day = int(input('''첫 날 1일의 시작 요일 입력
0=일, 1=월, ... , 6=토) >> '''))
day = day % 7 # 7이 넘어가면 재설정

print('''\n일 월 화 수 목 금 토''')

cnt = 0
# 공백 출력
if day != 0:
    print('   ' * day, end = '')
    cnt += day

# 날짜 출력
for i in range(1, dates + 1):
    print('%2d' % i, end = ' ')
    cnt += 1
    if (cnt % 7 == 0): # 한 주가 다시 돌아옴
        print()

else:
    print()