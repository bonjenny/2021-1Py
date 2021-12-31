# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 21:06:03 2021

@author: bonje
"""

# 1. []를 이용한 리스트 만들기
sports = ['축구', '야구', '농구', '배구']
# 위 종목에 대응하는 팀원 수를 항목으로 구성
num = [11, 9, 5, 6]
print(sports)
print(num)

# 1차원 리스트에서의 출력
for i in range(len(sports)):
    print('%s: %d명' % (sports[i], num[i]), end = ' ')
print(); print()

# 2. 2차원 리스트 만들기
sportsnum = [sports, num]
print(sportsnum)
'''
# 다른 방법 (1). +를 이용한 리스트 만들기
sportsnum = [sports] + [num]
print(sportsnum)

# 다른 방법 (2). insert를 이용한 리스트 만들기
sportsnum = []
sportsnum.insert(0, sports)
sportsnum.insert(1, num)
print(sportsnum)

# 다른 방법 (3). list()와 append()를 이용한 리스트 만들기
sportsnum = list()
sportsnum.append(sports)
sportsnum.append(num)
print(sportsnum)
'''

# 2차원 리스트에서의 출력
for i in range(4):
    print('%s: %d명' % (sportsnum[0][i], sportsnum[1][i]), end = ' ')
print(); print()
'''
# 다른 방법. range()와 len()을 이용하여 출력
for i in range(len(sportsnum[0])):
    print('%s: %d명' % (sportsnum[0][i], sportsnum[1][i]), end = ' ')
print()
'''

# 3. 컴프리헨션을 이용한 리스트 만들기
sportsnum = [[sports[i], num[i]] for i in range(4)]
print(sportsnum)

for i in range(4):
    print('{}: {}명'.format(sportsnum[i][0], sportsnum[i][1]), end = ' ')
'''
# 다른 방법 (1). range()와 len()을 이용하여 출력
for i in range(len(sportsnum)):
    print('{}: {}명'.format(sportsnum[i][0], sportsnum[i][1]), end = ' ')

# 다른 방법 (2). 리스트 자체를 이용하여 출력
for one in sportsnum:
    print('{}: {}명'.format(one[0], one[1]), end = ' ')
print()
'''