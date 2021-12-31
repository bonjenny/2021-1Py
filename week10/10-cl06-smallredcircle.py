# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:48:35 2021

@author: bonje
"""

import sys
# sys.path.pop(6)
sys.path.insert(6, 'C:\Program Files\Python37\Lib\site-packages')

import pygame

pygame.init() # 게임 엔진 초기화
RED = [255, 0, 0]
WHITE = [255, 255, 255]
screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption("마우스로 그림 그리기")

mpos = []
clock = pygame.time.Clock()

done = False
mdown = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mdown = True
        elif event.type == pygame.MOUSEMOTION:
            if mdown:
                mpos.append(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            mdown = False
    
    screen.fill(WHITE)
    
    for i in range(len(mpos)):
        x = mpos[i][0]
        y = mpos[i][1]
        pygame.draw.circle(screen, RED, [x, y], 2)
    
    pygame.display.update()
    # 초당 수정될 프레임 수 지정, 초당 100 프레임 화면이 수정됨
    clock.tick(1000)
