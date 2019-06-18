# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import hm_message


def hello():
    print("hello")


print(__name__)

hm_message.send_message.send("hello")
# 测试模块
if __name__ == "__main__":
    hello()