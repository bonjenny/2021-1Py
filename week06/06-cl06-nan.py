# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:02:03 2021

@author: bonje
"""

from random import sample

A = set(sample(list(range(1, 21)), 5))
B = set(sample(list(range(1, 21)), 5))
print('A = {} '.format(A))
print('B = {} '.format(B))
print()

print('A | B = {} '.format(A | B))
print('A & B = {} '.format(A & B))
print('A - B = {} '.format(A - B))
print('A ^ B = {} '.format(A ^ B))