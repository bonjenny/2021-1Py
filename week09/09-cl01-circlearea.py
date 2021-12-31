# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:12:36 2021

@author: 엄지희
"""

import math
from random import random

def getarea(r):
    return round(math.pi, 2)*r*r

r = random()*10
print('원의 반지름: %3.2f' % r)
print('원주율 pi: %5.4f' % (math.pi))
print('반지름 %3.2f인 원의 면적은 %5.2f' % (r, getarea(r)))
