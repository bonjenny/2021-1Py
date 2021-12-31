# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:07:06 2021

@author: bonje
"""

coffee = ['에스프레소', '아메리카노', '카페라테', '카페모카']
print(coffee)
print(type(coffee))

num = 0
for s in coffee:
    num += 1
    print('%d. %s' % (num, s))