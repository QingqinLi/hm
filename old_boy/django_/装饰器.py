# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


def wrapper(fn):  # 装饰器函数
    def inner(*args, **kwargs):
        print("before fn")
        ret = fn(*args, **kwargs)  # 真正执行的函数接收参数的过程
        print("after fn")
        return ret  # 返回只想函数的返回值
    return inner


@wrapper  # python语法糖的使用
def yue(tool):
    return "use %s learn english" % tool


# 不改变原函数调用方式的前提下，改变内部的执行的方式
print(yue("百词斩"))