# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:14:09 2021

@author: bonje
"""

s = set()
print(type(s)) # 집합의 자료형 이름 set
print(s) # 공집합을 출력하면 set()

d = {}
print(type(d)) # {}는 빈 딕셔너리

planets = set('해달별')
print(planets)

fruits = set(['감', '귤'])
print(fruits)
# 수정가능한 리스트와 딕셔너리는 집합의 원소로 사용 불가
# 단, 이 경우는 set()의 argument로 리스트를 준 것

nuts = {'밤', '잣'}
things = {('밤', '잣'), ('감', '귤'), '해달'}
# things = {['밤', '잣'], ('감', '귤'), '해달'} 은 오류 발생
print(nuts)
print(things)