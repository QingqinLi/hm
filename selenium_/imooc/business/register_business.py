# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import sys
sys.path.append('..')
from handle.register_handle import RegisterHandle


class RegisterBusiness:

    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def register(self, email, name, password, code):
        # 通用的代码，封装起来
        self.register_h.send_user_email(email)
        # 验证邮箱，其他的内容不需要输入，失去焦点的时候就已经提示了
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()

    # 执行操作
    def login_email_error(self, email, name, password, code):
        self.register(email, name, password, code)
        if self.register_h.get_user_text("register_email_error", "请输入有效的电子邮件地址"):
            return True
        else:
            return False

    def login_name_error(self, email, name, password, code):
        self.register(email, name, password, code)
        if self.register_h.get_user_text("register_name_error", "字符长度必须大于等于4，一个中文字算2个字符"):
            return True
        else:
            return False

    def login_password_error(self, email, name, password, code):
        self.register(email, name, password, code)
        if self.register_h.get_user_text("register_password_error", "最少需要输入 5 个字符"):
            return True
        else:
            return False

    def login_code_error(self, email, name, password, code):
        self.register(email, name, password, code)
        if self.register_h.get_user_text("code_text_error", "验证码错误"):
            return True
        else:
            return False

    def register_success(self, email, name, password, code):
        self.register(email, name, password, code)
        if self.register_h.get_register_btn():
            return False
        else:
            return True
