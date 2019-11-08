# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
大批量运行case
所有case的主入口
"""
import unittest
import os


class RunCase(unittest.TestCase):
    def test_case01(self):
        # 需要一个路径, 当前case的路径
        case_path = os.getcwd()
        print("path", case_path)
        suite = unittest.defaultTestLoader.discover(case_path, 'unittest_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    print("path", os.getcwd())
    unittest.main()