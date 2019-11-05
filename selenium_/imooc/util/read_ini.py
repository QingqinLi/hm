# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import configparser
from common.settings import item_path


# 操作配置文件
class ReadIni:
    def __init__(self, file_name=None, node=None):
        # cf = configparser.ConfigParser()
        # cf.read("/Users/qing.li/PycharmProjects/hm/selenium_/imooc/common/LocalElement.ini")
        # user_mail = cf.get("RegisterElements", "register_email")
        # print(user_mail)
        if not file_name:
            file_name = '/Users/qing.li/PycharmProjects/hm/selenium_/imooc/common/LocalElement.ini'
        if node:
            self.node = node
        else:
            self.node = 'RegisterElements'

        self.cf = self.load_ini(file_name)

    # 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取value值
    def get_value(self, key):
        return self.cf.get(self.node, key)



ini = ReadIni()
print(ini.get_value("register_email"))