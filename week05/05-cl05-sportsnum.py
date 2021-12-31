# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:03:22 2021

@author: bonje
"""

#%% 2 Challenge Pragramming 05-cl05-sportsnum.py

# 1. 메소드 insert()로 팀원 수 삽입
sports = ['축구', '야구', '농구', '배구']
sports.insert(1, 11)
sports.insert(3, 9)
sports.insert(5, 5)
sports.insert(7, 6)

print('메소드 insert()로 팀원 수 삽입')
print(sports); print()


# 2. for문에서 메소드 insert()로 팀원 수 삽입
sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]
for i in range(1, len(sports)*2, 2):
    sports.insert(i, num[int((i+1)/2-1)])
    
print("for문에서 메소드 insert()로 팀원 수 삽입")
print(sports); print()


# 3. sports[1::2]에 num을 대입

num = [11, 9, 5, 6]
sports[1::2] = num
print("슬라이스 sports[1::2]에 num을 대입")
print(sports); print()