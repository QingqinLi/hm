# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
a, b, c = 10, 5, 1

if a > b > c:
    print("this is true")
else:
    print("this is false")


# 在django的模板语言中不能使用连续判断的语法，类似于在js中会先判断10> 5 结果为True， 替换为1后与后面的算式继续比较