# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:32:44 2021

@author: bonje
"""

daysA = {'월', '화', '수', '목'}
daysB = set(['수', '목', '금', '토', '일'])
weekends = set(('토', '일'))

alldays = daysA | daysB
print(alldays)

workdays = alldays - weekends
print(workdays)

print(daysA & daysB)
print(daysA.symmetric_difference(daysB))