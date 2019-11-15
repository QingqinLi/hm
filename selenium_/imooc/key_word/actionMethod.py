# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from selenium import webdriver
from base.find_element import FindElement
import time


class ActionMethod:
    def __init__(self):
        pass

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Safari()

        self.driver = driver

    # 输入地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, element):
        find_element = FindElement(self.driver)
        return find_element.get_element(element)

    # 输入元素
    def element_send_keys(self, key, value):
        element = self.get_element(key)
        element.send_keys(value)

    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()

    # 等待
    def sleep_time(self, sec):
        time.sleep(sec)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title



