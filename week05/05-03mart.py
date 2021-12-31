# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:13:55 2021

@author: bonje
"""

goods = []
for i in range(3):
    item = input('구입할 품목은 ? ')
    goods.append(item)
    print(goods)
print('길이: %d' % len(goods))