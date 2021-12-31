# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:25:16 2021

@author: bonje
"""

f = open('pyzen.txt', 'r')

while True:
    line = f.readline()
    if not line: break
    print(line, end = '')
    # print(line.strip('\n'))

f.close()
