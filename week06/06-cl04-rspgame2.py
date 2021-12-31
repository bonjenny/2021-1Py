# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:44:39 2021

@author: bonje
"""

from random import choice
# 한글의 format 출력 문제로 '보'를 '보오'로
dcs = {'가위':'보오', '바위':'가위', '보오':'바위'}
rsp = ('가위', '바위', '보오')
tit = ['비김', '철수', '영희', '승자'] # 출력에 필요

# 승리 횟수를 저장
cnt = {tit[0]: 0, tit[1]: 0, tit[2]: 0}

print('*'*20)
print('{:4} {:4} {:^5}'.format(tit[1], tit[2], tit[3]))
print('*'*20)

# 총 게임 횟수
numgame = 20
for i in range(numgame):
    cs = choice(rsp) # 철수 결정
    yh = choice(rsp) # 영희 결정
    
    # 철수와 영희의 결정 출력
    print('{:4} {:4}'.format(cs, yh), end=' ')
    
    # 비기는 조건
    if (cs == yh):
        index = 0 # 비김 출력
    # 철수가 이기는 조건
    elif (dcs[cs] == yh):
        index = 1 # 철수 출력
    # 영희가 이기는 조건
    else:
        index = 2 # 영희 출력
    
    cnt[tit[index]] += 1
    print('{:3} {}'.format(tit[index], cnt[tit[index]]))
print()
print('총 게임 횟수: %d  비긴 회수: %d' % (numgame, cnt[tit[0]]))

vgame = cnt[tit[1]] + cnt[tit[2]]
print('철수 승률: {:.2f}'.format(cnt[tit[1]]/vgame))
print('영희 승률: {:.2f}'.format(cnt[tit[2]]/vgame))

'''
from random import choice
dcs = {'가위':'보오', '바위':'가위', '보오':'바위'}
rsp = ('가위', '바위', '보오')

print('*'*17)
print('{:4} {:4} {:4}'.format('철수', '영희', '승자'))
print('*'*17)

ci, yi = 0, 0
for i in range(20):
    cs = choice(rsp) # 철수 결정
    yh = choice(rsp) # 영희 결정
    
    # 철수와 영희의 결정 출력
    print('{:4} {:4}'.format(cs, yh), end=' ')
    
    if (cs == yh):        # 비기는 조건
        print('{:4}'.format('비김'))
    elif (dcs[cs] == yh): # 철수가 이기는 조건
        ci += 1
        print('{:4} {}'.format('철수', ci))
    else:                 # 영희가 이기는 조건
        yi += 1
        print('{:4} {}'.format('영희', yi))
print(); print()

print('총 게임 회수: {}  비긴회수: {}'.format(i, i-(ci+yi)))
print('철수 승률: %.2f' % (ci/i))
print('영희 승률: %.2f' % (yi/i))
'''