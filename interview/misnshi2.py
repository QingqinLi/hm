# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# python脚本， 路径 /home/test.py 统计行数


def get_line():
    file_path = '/Users/qing.li/PycharmProjects/hm/interview/lines.py'
    f = open(file_path)
    lines = f.readlines()
    count = 0
    flag = False
    for line in lines:
        if line.startswith("#"):
            continue
        if line == '\n':
            continue
        if line.startswith("'''") or line.startswith('"""'):
            if flag:
                flag = False
            else:
                flag = True
        if not flag:
            count += 1
    return count

print(get_line())


