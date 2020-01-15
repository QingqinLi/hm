# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class Stack:
    def __init__(self):
        # _表示数据不被外界访问
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pull(self):
        return self._data.pop()


class TestStack:
    def setup(self):
        self.stack = Stack()

    def test_demo(self):
        self.stack.push(3)
        self.stack.push(1)
        self.stack.pull()
        print(self.stack)

