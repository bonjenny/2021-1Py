# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:40:49 2021

@author: 엄지희
"""

import math
import statistics

s = [1, 6, 11, 16]
st = [80, 99, 77, 65, 92, 74, 82]

if __name__ == '__main__':
    for i in s:
        print('%2d! = %d' % (i, math.factorial(i)))
    print()
    print(st)
    print('중앙 값: %5.2f' % statistics.median(st))
    print('평균: %5.2f' % statistics.mean(st))
    print('분산: %5.2f' % statistics.variance(st))
    print('표준편차: %5.2f' % statistics.stdev(st))
