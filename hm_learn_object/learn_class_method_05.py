# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class Tool(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具类对象的数量为:%d" % Tool.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
Tool.show_tool_count()