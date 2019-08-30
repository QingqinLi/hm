# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import time
import datetime
# 1. 把一个自字符串格式的时间转化成结构化的时间
t1 = time.strptime('2019-01-01', '%Y-%m-%d')
print(t1, t1.tm_year)

# 2. 把结构化的时间格式转换成指定格式字符串: 2018.10.01
t2 = time.localtime()
t3 = time.strftime('%Y-%m-%d %H:%M:%S', t2)
print(t3)

# 3. 时间间隔
t4 = datetime.datetime.now()
print(t4, type(t4))
t5 = t4 + datetime.timedelta(days=2)
print(t5)