# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import sys
sys.path.append('..')
from selenium import webdriver
import time
import os
from business.register_business import RegisterBusiness
from base.register_function import RegisterFunction
import unittest
import HTMLTestRunner


class FirstCase(unittest.TestCase):

    # 某一条case的前置条件, 装饰漆
    @classmethod
    def setUpClass(cls):
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
        self.register_function = RegisterFunction(self.driver, self.file_path)

    def tearDown(self):
        print("每条case执行之后")
        self.driver.close()

    # def __init__(self, driver):
    #     self.file_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_code_%s.png" % (time.time())
    #     self.driver = driver
    #     self.register = RegisterBusiness(driver)
    #     self.register_function = RegisterFunction(driver, self.file_path)

    # case名称尽量见名知意
    def test_login_email_error(self):
        # 此方法应该封装在handle中
        # if not self.register.login_email_error('email', 'user11188', '111111', 'test1'):
        #     error_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_email_error_%s.png" % (time.time())
        #     self.driver.save_screenshot(error_path)
        # AssertionError 通过assert判断是否为error
        email_error = self.register.login_email_error('email', 'user11188', '111111', 'test1')
        self.assertFalse(email_error, "case执行了")

    @unittest.skip("不执行username用例")
    def test_login_username_error(self):
        if not self.register.login_name_error('132606808@163.com', '11', '111111', 'test1'):
            error_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_user_name_error_%s.png" % (time.time())
            self.driver.save_screenshot(error_path)

    def test_login_code_error(self):
        if not self.register.login_password_error('132631808@163.com', 'user111d88', '1', 'test1'):
            error_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_password_error_%s.png" % (time.time())
            self.driver.save_screenshot(error_path)

    def test_login_success(self):
        code = self.register_function.get_code_picture()
        print("code", code)
        if not self.register.register_success('132638@163.com', '3buu837', '123456', code):
            error_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_error_%s.png" % (time.time())
            self.driver.save_screenshot(error_path)
        else:
            print("校验成功")

    # def run_main(self):
    #     self.test_login_email_error()
    #     self.register_function.clear_element()
    #     self.test_login_username_error()
    #     self.register_function.clear_element()
    #     self.test_login_code_error()
    #     self.register_function.clear_element()
    #     self.test_login_success()
    #     self.driver.close()


if __name__ == '__main__':
    # unittest.main()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("path", base_dir)
    file_path = os.path.join(base_dir, "report/first_case.html")
    print(file_path)
    f = open(file_path, 'wb')


    # 管理执行case
    # 容器
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_code_error'))
    # unittest.TextTestRunner().run(suite)

    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is 5itest register page report", description="描述")
    runner.run(suite)
    # 控制case的执行顺序，以及跳过case
    """
    unitest.main()中case的执行顺序，数字或字母的升序执行
    使用容器的方式：按照添加的顺序
    
    跳过：
        @unittest.skip()
        
    大批量运行case：
        用统一的入口类
    
    assert：
        
    生成测试报告：
    
        python3.x 使用的htmltestrunner代码 https://github.com/linyuli861/Automated-Test
    
首先，我们要知道如果要利用HTMLTestRunnerNew生成测试报告的话，就需要对其进行导入：
        HTMLTestRunnerNew下载地址：链接:https://pan.baidu.com/s/1DO8_0HrNx_UtVPzqCEJ8CQ  密码:5yoy
        下载好了之后需要把这个文件复制到python的lib目录下面，操作步骤如下：
        在访达中command+shift+G，在弹出的输入框中输入：/资源库/Frameworks/Python.framework/Versions/3.6/lib/python3.6，找到这个目录后把文件放在这个文件夹里面就可以了
        
        下载htmltestrunner.py文件，安装到python中
        python unittest HTMLTestRunner
        路径：file_path = os.path.join(os.getcwd(), "/report/", 'first_case.html')
        open(file_path, 'wb')
        运行case
        suite = 
        suite.add()
        runner = HTMLTesyRunner.HTMLTestRunner(stream=f, title='this is first report', description=u'first report',
        runner.run(suite)
    """
