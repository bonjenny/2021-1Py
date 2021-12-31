# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:05:37 2021

@author: bonje
"""

def ctofahrenheit(cels):
    # 인자인 섭씨 온도 cels을 화씨 온도로 변환해 반환
    return cels * 9/5 + 32

def ftocelsius(fahr):
    # 인자인 화씨 온도 fahr을 섭씨 온도로 변환해 반환
    return (fahr - 32) * 5/9

for cels in range(28, 35, 2):
    print('섭씨: {}, 화씨: {:.2f}'.format(cels, ctofahrenheit(cels)))

for fahr in range(90, 103, 3):
    print('섭씨: {:.2f}, 화씨: {}'.format(ftocelsius(fahr), fahr))