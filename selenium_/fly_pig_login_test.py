# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

fly_index = "https://www.fliggy.com/?ttid=sem.000000736&hlreferid=baidu.082076&route_source=seo"
fly_login = ""

driver = webdriver.Chrome()
driver.get(fly_index)

# chrome f12 元素copy-full-xpath可以复制xpath
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul[1]/li[2]/div/a[1]").click()
"""
"""
# 超时时间为30s，每隔0.2秒检查一次
WebDriverWait(driver, 30, 0.2).until(lambda x: x.find_element_by_id("J_Quick2Static")).click()
# driver.find_element_by_id("TPL_username_1").click() 需要先找到input框，再输入文字
driver.find_element_by_id("TPL_username_1").send_keys("13263106808")
# driver.find_element_by_id("TPL_password_1").click()
driver.find_element_by_id("TPL_password_1").send_keys("291518lq")

driver.find_element_by_id("J_SubmitStatic").click()

# driver.quit()
