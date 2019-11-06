# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import sys
sys.path.append('..')
from base.find_element import FindElement

class RegisterPage:

    def __init__(self, driver):
        self.fd = FindElement(driver)

    def get_email_element(self):
        return self.fd.get_element("register_email")

    def get_name_element(self):
        return self.fd.get_element("register_name")

    def get_password_element(self):
        return self.fd.get_element("register_password")

    def get_code_element(self):
        return self.fd.get_element("register_captcha")

    def get_button_element(self):
        return self.fd.get_element("register_btn")

    def get_email_error_element(self):
        return self.fd.get_element("register_email_error")

    def get_name_error_element(self):
        return self.fd.get_element("register_name_error")

    def get_password_error_element(self):
        return self.fd.get_element("register_password_error")

    def get_code_error_element(self):
        return self.fd.get_element("register_code_error")
