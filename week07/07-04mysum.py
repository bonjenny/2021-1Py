# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:50:40 2021

@author: bonje
"""

def mysum(x, y = 0): # 인자가 2개
    """두 수의 합 반환 함수"""
    return x + y # 두 인자의 합으로 반환

hap = mysum(5) # y는 기본값이 0으로
print(hap)

hap = mysum(5, 10)
print(hap)