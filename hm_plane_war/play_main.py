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
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        pygame.time.set_timer(HREO_FIRE_EVENT, 500)
        self.__create_sprites()

    def __create_sprites(self):
        # 创建北京精灵和精灵组
        bg = BackGround()
        bg2 = BackGround(True)
        sprite = GameSprite('./images/plane_small.png', 3)
        self.background_group = pygame.sprite.Group(bg, bg2, sprite)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

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

    def __event_handler(self):
        # 判断是否退出游戏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneMain.__game_over()
            elif event.type == ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HREO_FIRE_EVENT:
                self.hero.fire()
        #     # 事件监听模式
        #     elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        #         print("move right")
        # 事件键盘事件,判断元祖对应的索引,用户可以按下某个键不放
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collidate(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemies) > 0:
            self.hero.kill()
            print("英雄牺牲，游戏结束")
            PlaneMain.__game_over()

    def __update_sprites(self):
        self.background_group.update()
        self.background_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


plane = PlaneMain()
plane.start_game()
# x = {}
