# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import sys
sys.path.append('..')
from selenium import webdriver
import time
from business.register_business import RegisterBusiness


class FirstCase:

    def __init__(self, driver):
        self.driver = driver
        self.register = RegisterBusiness(driver)

    # case名称尽量见名知意
    def test_login_email_error(self):
        # 此方法应该封装在handle中
        if not self.register.login_email_error('email', 'user11188', '111111', 'test1'):
            error_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_error_%s.png" % (time.time())
            self.driver.save_screenshot(error_path)
        # AssertionError 通过assert判断是否为error


    def test_login_username_error(self):
        pass

    def test_login_code_error(self):
        pass

    def test_login_success(self):
        pass


if __name__ == '__main__':
    url = "http://www.5itest.cn/register"
    driver = webdriver.Chrome()
    driver.get(url)
    first_case = FirstCase(driver)
    first_case.test_login_email_error()
    driver.close()