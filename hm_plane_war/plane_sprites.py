# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import random
import pygame
SCREEN_RECT = pygame.Rect(0, 0, 501, 834)
# 定义刷新帧率的常量
FRAME_PER_SEC = 30
ENEMY_EVENT = pygame.USEREVENT
HREO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战游戏精灵
    """
    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 重写update，在屏幕的垂直方向运动
        self.rect.y += self.speed


class BackGround(GameSprite):

    def __init__(self, is_alt = False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1、调用父类的方法实现
        super().update()
        # 2、判断是否移出屏幕。，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    def __init__(self):
        super().__init__("./images/plane_small.png")
        self.speed = random.randint(1, 6)
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("kill")
        pass


class Hero(GameSprite):

    def __init__(self):
        super().__init__("./images/plane.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    # pygame捕获键盘按键：遍历事件列表，event判断类型 event.type == pygame.KEYDOWN；pygame的键盘模块，用户按下，对应的值为1，所有按键的元祖，用户可以按下不放
    # pygame.key.get_pressed 返回所有按键元祖
    def update(self):
        # 获取用户动作
        self.rect.x += self.speed
        # 设置不可超出屏幕
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

    def fire(self):
        for i in range(3):
            # 创建子弹精灵
            bullet = Bullet()
            # 设置精灵的初始位置
            bullet.rect.bottom = self.rect.y - 20 * i
            bullet.rect.centerx = self.rect.centerx
            # 将精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        pass
