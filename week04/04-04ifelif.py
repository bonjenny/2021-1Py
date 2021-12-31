# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:54:03 2021

@author: bonje
"""

point = int(input('성적을 입력하시오>>> ')) # 성적
if 90 <= point:
    print('점수 {}, 성적 {}'.format(point, 'A'))
elif 80 <= point:
    print('점수 {}, 성적 {}'.format(point, 'B'))
elif 70 <= point:
    print('점수 {}, 성적 {}'.format(point, 'C'))
elif 60 <= point:
    print('점수 {}, 성적 {}'.format(point, 'D'))
else:
    print('점수 {}, 성적 {}'.format(point, 'F'))