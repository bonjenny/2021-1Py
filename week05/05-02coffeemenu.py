# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:10:07 2021

@author: bonje
"""

menu = ['COFFEE', 'BEVERAGE', 'ADE']
coffee = ['에스프레소', '아메리카노', '카페라테', '카페모카']

print('=' * 45)
for category in menu:
    print('{:^15s}'.format(category), end=' ')
print()
print('=' * 45)

for ckind in coffee:
    print('{:^10s}'.format(ckind))