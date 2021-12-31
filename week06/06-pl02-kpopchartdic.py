# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:22:27 2021

@author: bonje
"""

# K-pop 가수와 곡을 차트 순위에 맞춰 입력
singer = ['BTS', '볼빨간사춘기', 'BTS', '블랙핑크', '태연', 'BTS']
song = ['작은 것들을 위한 시', '나만 봄', '소우주', 'Kill This Love', '사계']
kpop = list(zip(singer, song)) # zip() 함수로 가수와 곡을 조합
print(kpop)

# dict()와 enumeratezip() 함수로 순위를 키로 가수와 곡을 사전으로 구성
kpchart = dict(enumerate(kpop, start = 1))

# 일반 출력
print(kpchart); print()

# 모듈 pprint의 pprint()함수 활용
from pprint import pprint
pprint(kpchart)