# -*-coding:utf-8-*-

import pygame,re,sys,time,random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('打字测速小游戏')

# 设置当前要打的单词是什么
font1 = pygame.font.Font('./meng.ttf',60)
# 设置当前打字的速度
font2 = pygame.font.Font('./meng.ttf',30)

white = (255,255,255)
key_flag = False
num = random.randint(65,90)
correctNum = 0
time = 0
endScore = None
while True:
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            print(eventList)
            print('num:',num)
            print(time)
            if event.key == num +32:
                print('按键正确')
                correctNum = correctNum + 1
                num = random.randint(65,90)
            pass
        elif event.type == KEYUP:
            pass

    # 随机出68-90的整数

    s1 = chr(num)
    time = pygame.time.get_ticks()

    if time < 10000:
        fontText = font1.render('请快速打出--> %s <--字母'%s1,True,(0,0,0))
        fontV = font2.render('当前打字速度是{}字/分钟'.format(correctNum*60000/time),True,(0,0,0))

        screen.fill(white)
        screen.blit(fontText,(100,200))
        screen.blit(fontV,(10,10))
        pygame.display.update()

    else:
        if not endScore:
            endScore = correctNum
        fontText = font1.render('game over',True,(0,0,0))
        fontV = font2.render('当前打字速度是{}字/分钟'.format(endScore*6),True,(0,0,0))

        screen.fill(white)
        screen.blit(fontText, (100, 200))
        screen.blit(fontV, (130, 300))
        pygame.display.update()