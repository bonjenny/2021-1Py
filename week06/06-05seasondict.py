# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:39:54 2021

@author: bonje
"""

season = {'봄': 'spring', '여름': 'summer', '가을': 'autumn', '겨울': 'winter'}
print(season.keys())
print(season.items())
print(season.values())

# 메소드 keys() 항목 순회
for key in season.keys():
    print(('%s %s ') % (key, season[key]))
    
for item in season.items():
    print('{} {} '.format(item[0], item[1]), end=' ')
print()
# 메소드 items()의 반환 값인 튜플을 한 변수에 저장한 경우, 항목 순회 2
for item in season.items():
    print('{} {} '.format(*item), end=' ')
# 매개변수의 개수가 가변적일 경우 *을 붙임
print()