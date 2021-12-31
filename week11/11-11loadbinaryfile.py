# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:34:58 2021

@author: bonje
"""

import pickle as pk

# 바이너리 파일 읽기
try:
    with open('dicmonth.pic', mode='rb') as f:
        dmon = pk.load(f)
        pl = pk.load(f)

except FileNotFoundError as e:
    print(e)
    print(' 파일 읽기 실패! '.center(30, '*'))
else:
    print(dmon)
    print(pl)
    print(' 바이너리 파일 읽기 완료! '.center(30, '*'))
finally:
    print(' 프로그램 종료! '.center(30, '*'))
