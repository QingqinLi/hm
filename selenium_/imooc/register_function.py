# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
# 改造代码，避免元素信息暴露
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from util.find_element import FindElement


class RegisterFunction(object):

    def __init__(self, url, file_path, i):
        self.i = i
        self.driver = self.get_driver(url)
        self.file_path = file_path

    # 获取driver，并且打开url
    def get_driver(self, url):
        if self.i == 0:
            driver = webdriver.Chrome()
        elif self.i == 1:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Safari()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_user(self, str, num):

        return ''.join(random.sample(str, num))

    def get_picture(self, file_path):
        self.driver.save_screenshot(file_path)
        code_image = self.get_user_element("code_image")
        left = code_image.location['x']
        top = code_image.location['y']
        right = code_image.size['width'] + left
        bottom = code_image.size['height'] + top
        im = Image.open(file_path)
        img = im.crop((left, top, right, bottom))
        img.save(file_path)
        return file_path

    # 获取验证码图片
    def get_code_picture(self):
        file_path = self.get_picture(self.file_path)
        r = ShowapiRequest("http://route.showapi.com/184-4", "110187", "31fead27b6414c27b467e278ec3a62ed")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_path)
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text

    # 验证
    # def

    def run_main(self):
        user_email = "132" + self.get_user("1234567890", 8) + "@163.com"
        user_name = self.get_user("abcdefjhjklmnopqituvwxyz", 6)
        code = self.get_code_picture()
        self.send_user_info("register_email", user_email)
        self.send_user_info("register_name", user_name)
        self.send_user_info("register_password", "123456liqing")
        self.send_user_info("register_captcha", code)
        self.get_user_element("rgister_btn").click()
        code_error = self.get_user_element("code_text_error")
        if code_error:
            error_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_error_%s.png" % (time.time())
            self.driver.save_screenshot(error_path)
            # print("register failed")
        # else:
        #     print("register success")
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    url = "http://www.5itest.cn/register"
    # 可以使用多线程多进程同时运行
    for i in range(3):
        file_path = "/Users/qing.li/PycharmProjects/hm/selenium_/imooc/image/imooc_%s.png" % (time.time())
        register = RegisterFunction(url, file_path, i)
        register.run_main()