# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 00:06:27 2021

@author: bonje
"""

try:
    data = int('3.67')
except Exception as e:
    print('예외 발생 이름: {}'.format(type(e)))
    print('예외 발생 이유: {}'.format(e))
