# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# 实现线程安全的单例模式
import threading


class Singleton:
    lock = threading.Lock
    _isinstance = None

    # 多线程下不安全
    def __new__(cls, *args, **kwargs):
        if not cls._isinstance:
            with cls.lock:
                if not cls._isinstance:
                    cls._isinstance = super().__new__(cls, *args, **kwargs)
        return cls._isinstance


