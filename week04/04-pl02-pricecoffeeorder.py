# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:26:29 2021

@author: bonje
"""

coffee = ['아메리카노', '카페라테', '카푸치노', '캐러멜마키아또']
order = '''
Coffee menu!
    1. 아메리카노       2000
    2. 카페라테         2500
    3. 카푸치노         3000
    4. 캐러멜마키아또   4000
    0. 주문 종료
'''
price = 0

print('환영합니다. 음료를 선택하세요.')
while True:
    print(order)
    sort = int(input('종류 ? '))
    
    if sort == 0:
        print()
        print(' 주문 종료 '.center(40, '*'))
        break
    elif sort == 1:
        amount = int(input('수량 ? '))
        price += 2000 * amount
    elif sort == 2:
        amount = int(input('수량 ? '))
        price += 2500 * amount
    elif sort == 3:
        amount = int(input('수량 ? '))
        price += 3000 * amount
    elif sort == 4:
        amount = int(input('수량 ? '))
        price += 4000 * amount
    else:
        print('모르겠어요.')
        continue
    
    print()
    print('%s %d개 주문' % (coffee[sort-1], amount))
    print('현재 주문 가격: %d원' % price)

else:
    print('사용되지 않는 구간입니다.')
    
print('총 주문 가격: %d원' % price)
print(' 안녕! '.center(40, '='))