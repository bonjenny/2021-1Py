# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:38:37 2021

@author: bonje
"""

while True:
    month = int(input('월 입력 ? >> '))
    if 11 <= month <= 12 or 1 <= month <= 3:
        print('{}월은 겨울입니다.'.format(month))
        break
    elif 4 <= month <= 5:
        print('{}월은 봄입니다.'.format(month))
        break
    elif 6 <= month <= 8:
        print('{}월은 여름입니다.'.format(month))
        break
    elif 9 <= month <= 10:
        print('{}월은 가을입니다.'.format(month))
        break
    else:
        print('{}월은 존재하지 않습니다.'.format(month))
        continue
    
else:
    print('사용되지 않는 구간입니다.')