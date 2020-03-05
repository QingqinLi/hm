# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import ddt
import unittest


@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("this is setup")

    def tearDown(self):
        print("this is tear down")



    """
    需要的数据：
        邮箱 用户名 密码 雅正吗 错误信息定位元素 错误提示信息
    """

    # 有很多测试数据，1，2   3，4    5，6 可以放在文件中／数据库中
    @ddt.data(
        ["1", "2"],
        [3, 4],
        [5, 6],
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a+b)


if __name__ == '__main__':
    unittest.main()
