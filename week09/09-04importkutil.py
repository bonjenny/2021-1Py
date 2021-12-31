# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:40:02 2021

@author: 엄지희
"""

from kutil import nrandom

for i in range(5):
    print('로또 복권 %d' % (i+1), nrandom(1, 45, 6))
print()
print('주사위 4번: ', nrandom(1, 6, 4, True))