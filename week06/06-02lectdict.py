# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:03:20 2021

@author: bonje
"""
groupnumber = {} # 빈 딕셔너리
groupnumber = {'잔나비':5, '트와이스':9, '블랙핑크':4, '방탄소년단':7}

lect = dict() # 빈 딕셔너리
lect['강좌명'] = '파이썬 기초';
lect['개설년도'] = [2020, 1];
lect['학점시수']= (3, 3);
lect['교수'] = '김민국';

print(lect)
print(len(lect)) # lect의 항목 개수
print(type(lect)) # lect의 type : dict
print()
# 딕셔너리의 항목 참조
print(lect['개설년도'], lect['학점시수'])
print(lect['강좌명'], lect['교수'])