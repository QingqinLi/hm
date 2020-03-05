# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class Dog(object):

    # 不需要访问类属性和实例熟悉，定义静态方法
    @staticmethod
    def run():
        print("dog run...")


# 通过类名.的方法调用静态方法，不需要创建对象
Dog.run()
