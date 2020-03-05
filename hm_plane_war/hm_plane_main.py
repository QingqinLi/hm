import pygame
import time
from hm_plane_war.plane_sprites import *


def play_game():
    pygame.init()

    # 操作部分

    # 创建游戏窗口
    screen = pygame.display.set_mode((506, 846))
    # 绘制背景图片
    """
    1、加载图片数据
    2、屏幕对象blit绘制图像
    3、update 更新屏幕的显示(可以在所有的绘制工作完成之后，调用一次）
    """
    bg = pygame.image.load("./images/background1.png")
    screen.blit(bg, (0, 0))
    # pygame.display.update()

    # 绘制英雄图像
    hero = pygame.image.load("./images/plane.png")
    screen.blit(hero, (300, 700))

    # 创建时钟对象
    clock = pygame.time.Clock()

    # 记录飞机的初始位置rect(起点，宽度，高度）
    hero_rect = pygame.Rect(300, 700, 104, 166)

    sprite = GameSprite("./images/plane_small.png", speed=5)
    sprite2 = GameSprite("./images/plane_small.png", speed=10)
    sprite_group = pygame.sprite.Group(sprite, sprite2)

    pygame.display.update()

    while True:
        # 设置每秒刷新频率，指定循环体内部执行频率
        clock.tick(10)

        sprite_group.update()
        # 捕获事件
        event_list = pygame.event.get()
        # print(event_list)
        # 事件监听
        for event in event_list:
            if event.type == pygame.QUIT:
                # 停止游戏的代码（大多数pygame游戏使用）
                # quit()卸载所有的模块
                pygame.quit()
                # 直接退出系统,exit()内置函数，终止当前程序
                exit()

        if hero_rect.y + 166 <= 0:
            hero_rect.y = 650
        # 修改飞机的位置
        hero_rect.y -= 20
        # 解决飞机图像多个的问题：重新绘制背景
        screen.blit(bg, (0, 0))
        # 调用blit绘制图像
        screen.blit(hero, hero_rect)
        # 调用update更新显示
        sprite_group.draw(screen)
        pygame.display.update()


    pygame.quit()


def hero_learn():
    hero_rect = pygame.Rect(100, 200, 120, 150)
    print(hero_rect.x, hero_rect.width, hero_rect.size)


play_game()