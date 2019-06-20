# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from hm_plane_war.plane_sprites import *


class PlaneMain(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_RECT.width, SCREEN_RECT.height))
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        print("yesy")

    def __create_sprites(self):
        # 创建北京精灵和精灵组
        bg = BackGround()
        bg2 = BackGround(True)
        sprite = GameSprite('./images/plane_small.png', 3)
        self.sprite_group = pygame.sprite.Group(bg, bg2, sprite)
        self.__update_sprites()

    def start_game(self):
        while True:
            # 设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collidate()
            # 更新绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    @staticmethod
    def __event_handler():
        # 判断是否退出游戏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneMain.__game_over()

    def __check_collidate(self):
        pass

    def __update_sprites(self):
        self.sprite_group.update()
        self.sprite_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


plane = PlaneMain()
plane.start_game()
# x = {}
