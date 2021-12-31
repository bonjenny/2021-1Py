# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:16:24 2021

@author: bonje
"""

day = dict([]) # 빈 딕셔너리
day = dict(()) # 빈 딕셔너리

day = dict([['월', 'monday'], ['화', 'tuesday'], ['수', 'wendsday']])
day = dict([('월', 'monday'), ('화', 'tuesday'), ('수', 'wendsday')])
day = dict((['월', 'monday'], ['화', 'tuesday'], ['수', 'wendsday']))
day = dict((('월', 'monday'), ('화', 'tuesday'), ('수', 'wendsday')))
print(day)

day = dict(월='monday', 화='tuesday', 수='wendsday')
print(day)

bts1 = {'그룹명' : '방탄소년단', '인원수' : 7, '리더' : '김남준'}
bts1['소속사'] = '빅히트엔턴테인먼트';
print(bts1)

bts2 = dict([['그룹명', '방탄소년단'], ['인원수', 7]])
print(bts2)

bts3 = dict((('리더', '김남준'), ('소속사', '빅히트엔터테인먼트')))
print(bts3)

bts = dict(그룹명='방탄소년단', 인원수=7, 리더='김남준', 소속사='빅히트엔터테인먼트')
# 구성원 추가
bts['구성원'] = ['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']

print(bts) # 전체 출력
print(bts['구성원']) # 구성원 출력