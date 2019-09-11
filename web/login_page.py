# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author   : Daexiong
# @Time     : 2019-08-15 10:47
# @File     : login_page.py
# @Software : PyCharm

"""
登录页面
"""
from selenium.webdriver.common.by import By
from web.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    """登录页面-对象库层(封装元素定位方法)"""

    def __init__(self):
        # self.driver = DriverUtil.get_driver()  # 获取浏览器对象

        super().__init__()  # 获取父类浏览器对象

        self.username = (By.ID, 'username')  # 用户名
        self.password = (By.ID, 'password')  # 密码
        self.verify_code = (By.ID, 'verify_code')  # 验证码
        self.login_btn = (By.NAME, 'sbtbutton')  # 按钮

    def find_username(self):
        return self.find_element_func(self.username)

    def find_password(self):
        return self.find_element_func(self.password)

    def find_verify_code(self):
        return self.find_element_func(self.verify_code)

    def find_login_btn(self):
        return self.find_element_func(self.login_btn)


class LoginHandler(BaseHandle):
    """登录页面-操作层(封装元素操作方法)"""

    def __init__(self):
        self.login_page = LoginPage()  # 元素定位对象

    def input_username(self, username):
        """用户名输入方法"""
        self.input_text(self.login_page.find_username(), username)

    def input_password(self, pwd):
        self.input_text(self.login_page.find_password(), pwd)

    def input_verify_code(self, code):
        self.input_text(self.login_page.find_verify_code(), code)

    def click_login_btn(self):
        # self.login_page.find_login_btn().click
        self.click_element(self.login_page.find_login_btn())


class LoginProxy(object):  # 一般业务层用proxy
    """登录页面-业务层(封装测试业务方法)"""

    def __init__(self):
        self.login_handle = LoginHandler()  # 操作对象

    def login(self, username, pwd, code):
        """登录方法"""
        self.login_handle.input_username(username)  # 输入用户名
        self.login_handle.input_password(pwd)  # 输入密码
        self.login_handle.input_verify_code(code)  # 输入验证码
        self.login_handle.click_login_btn()  # 点击登录
