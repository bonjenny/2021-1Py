# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:41:43 2021

@author: 동양미래대학교
"""

import matplotlib.pyplot as plt

objects = ('Python', 'Java', 'C++', 'C#', 'C', 'Kotlin')
performance = [10, 8, 6, 4, 7, 2]

plt.title('Programming language usage') # 제목
plt.xlabel('Usage') # x축 레이블
plt.ylabel('Programming language') # y축 레이블
plt.barh(objects, performance, height=0.5, color='yellow') # 가로바 그리기
plt.show()