# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""

# 异常捕获
# try:
#     num = int(input("请输入一个整数："))
#     result = 8 / num
#     print(result)
# except ZeroDivisionError:
#     print("1")
# except ValueError:
#     pass
# 错误类型
# 捕获未知错误
# try:
#     num = int(input("请输入一个整数："))
#     result = 8 / num
#     print(result)
# except Exception as e:
#     print("exception info:", e)


def get_password():
    password = input("please input your password:")

    if len(password) > 8:
        print("密码苏护乳正确")
        return

    ex = Exception("密码长度错误")
    raise ex


try:
    get_password()
except Exception as result:
    print(result)