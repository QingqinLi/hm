# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
一个小坑，不要把自己的文件／文件夹命名为selenium,会导入自己的模块出错
下载webdriver到/usr/local/bin中
firefox webdriver下载地址：https://github.com/mozilla/geckodriver/releases
"""
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

print(driver.title)

driver.quit()