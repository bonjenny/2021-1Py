# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:23:24 2021

@author: bonje
"""

f = open('pyzen.txt', 'wt')
f.write('파이썬 철학\n')
f.write('아름다움이 추한 것보다 낫다.\n')
f.write('명시적인 것이 암묵적인 것보다 낫다.\n')
f.close()

f = open('pyzen.txt', mode='r')
s = f.read()
print(s)
f.close()
