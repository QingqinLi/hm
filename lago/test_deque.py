# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# import queue
# def test_queue():
#     queue.heappop()


# 自定义实现队列
class Queue:
    def __init__(self):
        self._data = []

    def put(self, item):
        self._data.append(item)

    def get(self):
        return self._data.pop(0)
