# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author   : Daexiong
# @Time     : 2019-08-13 18:35
# @File     : utils.py
# @Software : PyCharm

"""
公共方法类
"""
from selenium import webdriver
import time


def get_tips_message():  # 封装方法 与使用 分离; 观察,缺啥,给啥.
    """获取提示框信息"""
    # 6. 获取错误提示信息
    # msg = self.dr.find_element_by_class_name('layui-layer-content').text
    msg = DriverUtil.get_driver().find_element_by_class_name(
        'layui-layer-content').text
    print(f'msg={msg}')
    return msg  # 返回提供给调用的位置


class DriverUtil(object):
    """浏览器驱动工具类"""

    _dr = None  # 设置浏览器对象初始化状态 ( 前面加下划线 保护变量)

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        # 为了防止反复创建浏览器对象,需要对浏览器对象是否存在进行判断
        if cls._dr is None:
            cls._dr = webdriver.Chrome()
            # cls._dr.get("http://www.baidu.com")
            cls._dr.get("http://192.168.20.59/")
            # Windows maximize and implicit waiting.
            cls._dr.maximize_window()
            cls._dr.implicitly_wait(10)

        return cls._dr

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        # 需要判断浏览器对象存在,才能执行退出操作,否则会报错.
        # if self._dr is not None:
        if cls._dr:
            cls._dr.quit()
            cls._dr = None  # 此处 确保浏览器对象从内存中移除掉.


if __name__ == '__main__':
    # 获取浏览器对象
    DriverUtil.get_driver()
    # 退出浏览器
    time.sleep(3)
    DriverUtil().quit_driver()
