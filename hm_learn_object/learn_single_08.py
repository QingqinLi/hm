# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class MusicPlayer(object):

    # 定义一个类属性，记录单例对象的引用，初始值设置为None
    instance = None

    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 创建方法时，new会被自动调用
        print("创建对象，分配空间")
        #
        # 为对象分配空间，返回对象的引用 不返回，解释器得不到内存地址,调用父类的new方法，new是静态方法，调用需要传递cls的参数
        # return super().__new__(cls)

        if MusicPlayer.instance is None:
            MusicPlayer.instance = super().__new__(cls)

        return MusicPlayer.instance

    def __init__(self):
        # 只执行一次初始化方法
        if MusicPlayer.init_flag:
            return
        print("播放器创建")
        MusicPlayer.init_flag = True


player = MusicPlayer()
player1 = MusicPlayer()
print(player, player1)