# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import sys
sys.path.append('..')
from page.register_page import RegisterPage


class RegisterHandle:
    def __init__(self, driver):
        self.register_p = RegisterPage(driver)
        pass

    # 输入邮箱
    def send_user_email(self, email):
        self.register_p.get_email_element().send_keys(email)
        pass

    # 输入用户名
    def send_user_name(self, name):
        self.register_p.get_name_element().send_keys(name)

    # 输入密码
    def send_user_password(self, password):
        self.register_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self, code):
        self.register_p.get_code_element().send_keys(code)

    # 获取文字信息
    def get_user_text(self, info, user_info):
        if info == 'register_email_error':
            text = self.register_p.get_email_error_element().get_attribute("value")
        elif info == 'register_name_error':
            text = self.register_p.get_name_error_element().get_attribute("value")
        elif info == 'register_password_error':
            text = self.register_p.get_password_error_element().get_attribute("value")
        elif info == 'rcode_text_error':
            text = self.register_p.get_code_error_element().get_attribute("value")
        else:
            text = None
        if text == user_info:
            return True
        else:
            return False

    # 点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

