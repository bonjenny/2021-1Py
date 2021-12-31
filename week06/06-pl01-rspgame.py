# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:53:55 2021

@author: bonje
"""

from random import choice
dcs = {'가위':'보오', '바위':'가위', '보오':'바위'}
rsp = ('가위', '바위', '보오')

print('*'*17)
print('{:4} {:4} {:4}'.format('철수', '영희', '승자'))
print('*'*17)

for i in range(10):
    cs = choice(rsp) # 철수 결정
    yh = choice(rsp) # 영희 결정
    
    # 철수와 영희의 결정 출력
    print('{:4} {:4}'.format(cs, yh), end=' ')
    
    if (cs == yh):             # 비기는 조건
        print('{:4}'.format('비김'))
    elif (dcs[cs] == yh):      # 철수가 이기는 조건
        print('{:4}'.format('철수'))
    else:                      # 영희가 이기는 조건
        print('{:4}'.format('영희'))