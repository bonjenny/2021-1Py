# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:42:24 2021

@author: bonje
"""

for i in range(2, 10):
    for j in range(1, 10):
        print('%d * %d = %2d' % (i, j, i * j), end = '  ')
    print()