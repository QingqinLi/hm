# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


def add_color(arg):
    def inner():
        print("add color")
        arg()
        print("test end")
    return inner


@add_color
def create_people():
    print("test create_people")


"""
顺序必须在引用的前面
相当于
create_people = add_color(create_people)
create_people()

"""
create_people()

