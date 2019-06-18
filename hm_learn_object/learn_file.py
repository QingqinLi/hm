# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import os
# 打开文件
# file = open('readme.txt')
#
# # 文件操作
# text = file.read()
# print(text)
#
# # 关闭文件(一般打开文件后就执行关闭动作，避免忘记关闭文件）
# file.close()


def read_big_file():
    # 读取大文件
    file = open('readme.txt')

    while True:
        # 判断是否读取到内容
        text = file.readline()
        if not text:
            break
        print(text)
        pass

    file.close()


def copy_file():
    """
    复制小文件
    :return:
    """
    file_source = open('readme.txt', 'r')
    file_target = open('readme_copy.txt', 'w')

    text = file_source.read()
    file_target.write(text)

    file_source.close()
    file_target.close()


def copy_big_file():
    """
    复制大文件
    :return:
    """
    file_source = open('readme.txt', 'r')
    file_target = open('readme_copy.txt', 'w')

    while True:
        text = file_source.readline()
        if not text:
            break
        file_target.write(text)

    file_source.close()
    file_target.close()


def file_operation():
    # os.rename('readme.txt', 'readme2.txt')
    os.remove('readme_copy.txt')
#     os.list


if __name__ == '__main__':
    file_operation()