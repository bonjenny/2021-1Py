# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:53:22 2021

@author: bonje
"""

#%% 3 Challenge Pragramming 05-cl08-nanlisttuple.py

from random import randint
lst = []
for _ in range(10):
    lst.append(randint(1, 99))
tpl = tuple(lst)
    
print('리스트', lst)
print('튜플', tpl)
print('정렬된 리스트', sorted(tpl))
print()

sum = 0
for i in range(len(lst)):
    sum += lst[i]
print('정렬된 리스트의 합', sum)

print('항목수', len(lst))
print('최대값', max(tpl))
print('최소값', min(tpl))
print('평균값', sum/len(lst))