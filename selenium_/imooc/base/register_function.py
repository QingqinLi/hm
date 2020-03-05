# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import sys
sys.path.append('..')
sys.path.append('.')
from selenium import webdriver
import time
import random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
from base.find_element import FindElement


class RegisterFunction:

    def __init__(self, driver, file_path):
        self.driver = driver
        self.file_path = file_path

    def get_picture(self, file_path):
        self.driver.save_screenshot(file_path)
        find_element = FindElement(self.driver)
        code_image = find_element.get_element("code_image")
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

    def clear_element(self):
        self.driver.refresh()
