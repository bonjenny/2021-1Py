# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:46:47 2021

@author: 엄지희
"""

'''
import sys
print(sys.path)
['', 'C:\\Program Files\\Spyder\\Python\\python37.zip', 
 'C:\\Program Files\\Spyder\\Python', 
 'C:\\Program Files\\Spyder\\pkgs', 
 'C:\\Program Files\\Spyder\\pkgs\\IPython\\extensions', 
 'C:\\Users\\동양미래대학교\\.ipython']
'''

import random
def nrandom(start, end, n, duplicated = False):
    '''
    start와 end 사이의 정수 난수를 n개 생성해 반환

    Parameters
    ----------
    start : 시작 정수
    end : 마지막 정수
    n : 난수 개수
    duplicated : 중복 허용 여부, The default is False.

    '''
    lst = [] # 반환할 난수 리스트
    if duplicated:
        for _ in range(n):
            lst.append(random.randint(start, end))
    else:
        lst = list(random.sample(range(start, end+1), n))
    
    # 모두 정렬해 반환
    return sorted(lst)

if __name__ == '__main__':
    print('로또 복권: ', nrandom(1, 45, 6))
    print('주사위 3번: ', nrandom(1, 6, 3, True))
        