# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""

# os和sys模块都是干什么的
"""
os模块是和操作系统相关的
os.path.join("a", "n") 会根据不同系统的sep去拼接路径
os.path.sep/os.sep 操作系统的路径分割符
os.path.abspath(__file__) 获取当前文件的绝对路径
os.path.dirname(filename) 获取当前文件的文件夹名
os.path.exists(filepath) 判断文件是否存在
os.path.getsize() 获取文件大小
os.mkdir(filename) 创建文件夹

sys是和python解释器相关的
sys.path 是python的搜索模块的路径集，是一个list
sys.moudles 获取python解释器加载的所有模块
sys.argv 获取脚本运行时候的参数,是一个list，第一个是文件的名字，第二个开始是参数
sys.exit() 停止运行
"""
import os
import sys

# print(os.path.sep, os.sep)
# print(os.path.abspath(__file__))
# print(os.path.dirname(__file__))
# print(os.path.exists(__file__))
# print(os.path.getsize(__file__))
# os.mkdir("123")

# print(sys.path)
# print(sys.modules)
# sys.exit()
# print(sys.argv)
#

# 常用的内置模块有哪些
"""
time
re
json
hashlib
random
socket
collection
functools
"""

# functools

# import functools
from functools import partial, reduce, wraps

from collections import namedtuple

"""
namedtuple 命名元组
partial 便函数 指定一个默认参数，包装成另外一个参数

"""
# print(bin(10))  # 十进制转二进制
# print(oct(10))  # 十进制转八进制

print(int("1000", base=2))  # 把二进制的字符传类型的数字转换成十进制的数字
print(int('1000', base=8))

int2 = partial(int, base=2)
print(int2('1000'))


"""
collection模块
functools模块
"""



