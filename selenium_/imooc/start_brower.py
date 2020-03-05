# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from selenium import webdriver
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from ShowapiRequest import ShowapiRequest

import time
from PIL import Image
import pytesseract

URL = "http://www.5itest.cn/register"
driver = webdriver.Chrome()


driver.get(URL)
driver.maximize_window()
# driver.quit()

# 生成随机手机号
# random.sample("1234567890", 9)
user_name = ''.join(random.sample("abcdefjhjklmnopqituvwxyz", 6))
user_email = "132"+''.join(random.sample("1234567890", 8)) + "@163.com"


# EC用法：https://www.cnblogs.com/surewing/p/9639855.html
# time.sleep(5)
# 获取验证码截图
# WebDriverWait(driver, 10, 1).until(EC.visibility_of(driver.find_element_by_xpath("/html/body/div[5]/div/div[1]")))
# driver.find_element_by_xpath("/html/body/div[5]/div/div[1]").click()

WebDriverWait(driver, 10, 1).until(EC.title_contains("注册"))
file_path = "imooc_%s.png" % (time.time())
driver.save_screenshot(file_path)
code_image = driver.find_element_by_id("getcode_num")
left = code_image.location['x']
top = code_image.location['y']
right = code_image.size['width'] + left
bottom = code_image.size['height'] + top
im = Image.open(file_path)
img = im.crop((left, top, right, bottom))
img.save(file_path)
# pytesseract 可以识别比较规则的验证码

# image = Image.open(file_path)
# text = pytesseract.image_to_string(image)

r = ShowapiRequest("http://route.showapi.com/184-4", "110187", "31fead27b6414c27b467e278ec3a62ed" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", file_path)
res = r.post()
text = res.json()['showapi_res_body']['Result']

driver.find_element_by_id("register_email").send_keys(user_email)
driver.find_element_by_id("register_nickname").send_keys(user_name)
driver.find_element_by_id("register_password").send_keys("123456liqing")
driver.find_element_by_id("captcha_code").send_keys(text)
driver.find_element_by_id("register-btn").click()
# driver.close()