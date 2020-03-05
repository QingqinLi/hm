# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
    需要的数据：
        邮箱 用户名 密码 雅正吗 错误信息定位元素 错误提示信息
"""
import ddt
import unittest
import sys
sys.path.append('..')
from selenium import webdriver
import time
import os
from business.register_business import RegisterBusiness
from base.register_function import RegisterFunction
import unittest
import HTMLTestRunner
from util.get_code import GetCode
from util.excel_util import ExcelUtil


@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    ex = ExcelUtil()
    data = ex.get_data()

    # 某一条case的前置条件, 装饰漆
    code_file = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/code.png"

    @classmethod
    def setUpClass(cls):
        # cls.code_file = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/code.png"
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后的后置")

    def setUp(self):
        print("每条case执行之前")
        self.file_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_code_%s.png" % (time.time())
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        self.register = RegisterBusiness(self.driver)
        # self.register_function = RegisterFunction(self.driver, self.file_path)
        self.register_code = GetCode(self.driver, self.file_path)

    def tearDown(self):
        print("每条case执行之后")
        # py2看case有没有异常
        # if sys.exc_info()[0]:
        #     self.driver.save_screenshot()
        # py3中使用_outcome.errors, self._outcome.errors结果是一个list
        print(self._outcome.errors)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                error_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_%s_%s.png" % (
                    case_name, time.time())
                self.driver.save_screenshot(error_path)

        self.driver.close()

    # @ddt.data(
    #     ['email', 'user11188', '111111', code_file, "register_email_error", "请输入有效的电子邮件地址"],
    #     ['email@', 'user11188', '111111', code_file, "register_email_error", "请输入有效的电子邮件地址"],
    #     ['email@111.com', 'user1188', '911111', code_file, "register_email_error", "请输入有效的电子邮件地址"]
    #
    # )
    # @ddt.unpack
    # case名称尽量见名知意
    # def test_register_error(self, email, username, password, code_file, assert_code, assert_text):
    #     # 此方法应该封装在handle中
    #     # if not self.register.login_email_error('email', 'user11188', '111111', 'test1'):
    #     #     error_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_email_error_%s.png" % (time.time())
    #     #     self.driver.save_screenshot(error_path)
    #     # AssertionError 通过assert判断是否为error
    #     email_error = self.register.register_function(email, username, password, code_file, assert_code, assert_text)
    #     self.assertTrue(email_error, "邮箱用例")

    @ddt.data(*data)
    def test_register_error(self, data):
        email, username, password, code, assert_code, assert_text = data
        # 此方法应该封装在handle中
        # if not self.register.login_email_error('email', 'user11188', '111111', 'test1'):
        #     error_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_email_error_%s.png" % (time.time())
        #     self.driver.save_screenshot(error_path)
        # AssertionError 通过assert判断是否为error
        email_error = self.register.register_function(email, username, password, self.code_file, assert_code, assert_text)
        self.assertTrue(email_error, "邮箱用例")


if __name__ == '__main__':
    # unittest.main()/Users/qing.li/PycharmProjects/hm/selenium_/imooc/report/first_case_1.html
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("base_dir:;", base_dir)
    file_path = os.path.join(base_dir, "report/first_case_1.html")
    print("filepath", file_path)
    f = open(file_path, 'wb')
    loader = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is  register page report", description="描述ddt")
    runner.run(loader)