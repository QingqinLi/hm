# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import sys
sys.path.append('..')

from util.ShowapiRequest import ShowapiRequest
import time
from PIL import Image
from base.find_element import FindElement


class GetCode:

    def __init__(self, driver, file_path):
        self.file_path = file_path
        self.driver = driver
        self.find_e = FindElement(self.driver)

    # 获取截图
    def get_picture(self):
        print("file_path", self.file_path)
        self.driver.save_screenshot(self.file_path)
        code_image = self.find_e.get_element("code_image")
        # code_image = self.get_user_element("code_image")
        left = code_image.location['x']
        top = code_image.location['y']
        right = code_image.size['width'] + left
        bottom = code_image.size['height'] + top
        im = Image.open(self.file_path)
        img = im.crop((left, top, right, bottom))
        img.save(self.file_path)
        time.sleep(2)
        return self.file_path

    # 获取验证码图片
    def get_code_picture(self):
        file_path = self.get_picture()
        r = ShowapiRequest("http://route.showapi.com/184-4", "110187", "31fead27b6414c27b467e278ec3a62ed")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_path)
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        time.sleep(2)
        return text