# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""

"""
一个楼梯有50个台阶，每一步可以走一个台阶，也可以走两个台阶，请问走完这个楼梯共有多少种方法？
"""
# 类似汉诺塔问题, 分治，由小到大的分解问题
# https://blog.csdn.net/wangdq_1989/article/details/40151049


def fstep(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return(fstep(n-1) + fstep(n-1))


print(fstep(10))