# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:12:59 2021

@author: 엄지희
"""
# import sys
# sys.path.pop(6)
# sys.path.insert(6, 'C:\Program Files\Python37\Lib\site-packages')

import pygame

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 윈도 초기화
pygame.init()

# 윈도 크기 정의
size = [300, 200]
screen = pygame.display.set_mode(size)
# 제목인 캡션 지정
pygame.display.set_caption("Hello, pygame!")

# 폰트 생성과 출력할 문자열 지정
font = pygame.font.SysFont('malgungothic', 32)
outstr = '졸려잉'

# 메인 루프
done = False
while not done:
    for event in pygame.event.get(): # 여러 이벤트를 받아 처리
        if event.type == pygame.QUIT: # 윈도 종료 버튼을 누르면
            done = True # 프로그램을 종료하기 위해 True 지정
    
    screen.fill(WHITE) # 스크린 색상을 흰색으로 지정
    
    # 지정된 문자열 글씨를 그린 화면을 반환해 text에 저장
    text = font.render(outstr, True, BLUE)
    # 글씨가 그려진 화면인 text를 윈도 스크린 위치 [x, y]에 그리기
    screen.blit(text, [100, 80])
    
    pygame.display.update() # 화면의 필요한 부분만을 수정, flip으로도 가능

# 메인 루프를 빠져나오면 프로그램 종료
pygame.quit()