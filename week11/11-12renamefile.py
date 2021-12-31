# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:37:46 2021

@author: bonje
"""

import os

try:
    with open('pyfile.txt', mode='w') as file:
        file.write('파일 이름 수정과 삭제')
    
    os.rename('pyfile.txt', '파일수정삭제.txt') # 파일 이름 수정
    os.remove('파일수정삭제.txt') # 파일 삭제

except Exception as e:
    print('예외 발생: ', e)
else:
    print('파일 수정 삭제 성공!')
