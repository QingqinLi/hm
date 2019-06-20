# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import pygame
SCREEN_RECT = pygame.Rect(0, 0, 506, 846)
# 定义刷新帧率的常量
FRAME_PER_SEC = 30


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
        if self.rect.y >= 700:
            self.rect.y = 0


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



