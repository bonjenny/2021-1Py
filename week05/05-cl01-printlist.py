# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:50:27 2021

@author: bonje
"""

#%% 1 Challenge Pragramming 05-cl01-printlist.py

from random import randint
lst = []
for _ in range(10):
    lst.append(randint(1, 99))
    
print('리스트', lst)
print('정렬 리스트', sorted(lst))
print('내림차순 리스트', sorted(lst, reverse=True))