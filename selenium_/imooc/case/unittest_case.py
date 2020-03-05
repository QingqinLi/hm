# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import unittest


# 定义测试类，继承unittest.TestCase
class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("所有用例执行的前置")

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行的后置")

    # case必须以test开始
    def test_first01(self):
        print("this is first case")

    @unittest.skip("跳过")
    def test_first02(self):
        print("this is second case")

    # 前置
    def setUp(self):
        print("case的前置条件")

    # 后置
    def tearDown(self):
        print("case的后置case")


if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('test_first01'))
    suite.addTest(FirstCase01('test_first02'))
    unittest.TextTestRunner().run(suite)
