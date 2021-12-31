# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:30:44 2021

@author: bonje
"""

stocks = {'삼성에스디에스': 242000, '삼성전자': 47000,
          '엔씨소프트': 52600, '핸디소프트': 5120}
stocks.pop('엔씨소프트') # 딕셔너리 삭제
stocks.pop('핸디소프트') # 딕셔너리 삭제
stocks['엔씨소프트'] = 52600
stocks['핸디소프트'] = 5120
stocks.update(dict(골프존=215000, 기아=56300))

print(stocks)

while True:
    s = input('주식 이름 ? ')
    if s in stocks:
        print('%s: %d' % (s, stocks[s]))
    else:
        print('주식 이름이 없습니다.')
        break