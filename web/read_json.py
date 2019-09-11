# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author   : Daexiong
# @Time     : 2019-08-16 16:14
# @File     : read_json.py
# @Software : PyCharm

import json


def read_login_data():
    with open('./login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        # 声明空列表
        # data_list = []
        data_list = list()  # python规范以对象形式创建空列表

        # print(data.values())
        for i in data.values():
            data_list.append((i.get('username'),
                              i.get('password'),
                              i.get('code'),
                              i.get('is_success'),
                              i.get('expect')))

        print(data_list)
        return data_list
