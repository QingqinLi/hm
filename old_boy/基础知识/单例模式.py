# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton._instance:
            Singleton._instance = object.__new__(cls)
        return Singleton._instance


s1 = Singleton()
s2 = Singleton()
print(id(s1), id(s2))