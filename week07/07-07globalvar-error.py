# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:24:27 2021

@author: bonje
"""

def addone():
    # 대입이 있는 변수가 참조되면 지역 변수로 인식
    # "지역 변수 i에 값을 대입하기도 전에 참조했다"라는 오류 메시지 출력
    print('\t 전역 변수 i 읽기, i + 1: ', i + 1)
    i += 1 # 수정이 있으므로 i는 지역 변수로 인지

i = 20 # 전역 변수
print('i = ', i)
addone() # 함수 호출로 함수 내부 4번 줄에서 오류
print('i = ', i)