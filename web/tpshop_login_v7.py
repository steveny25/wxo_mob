import unittest
import time
from web.utils import DriverUtil, get_tips_message
from web.login_page import LoginProxy
from parameterized import parameterized
from web.read_json import read_login_data
import logging

# import json
logging.basicConfig(level=logging.DEBUG, filename='./debug.log')


def build_login_data():
    # with open('./login_data.json', encoding='utf-8') as f:
    #     data = json.load(f)
    #     # 声明空列表
    #     # data_list = []
    #     data_list = list()  # python规范以对象形式创建空列表
    #
    #     # print(data.values())
    #     for i in data.values():
    #         data_list.append((i.get('username'),
    #                           i.get('password'),
    #                           i.get('code'),
    #                           i.get('is_success'),
    #                           i.get('expect')))
    #
    #     # print(data_list)
    #     return data_list

    data = read_login_data()
    return data


class TestTPShopLogin(unittest.TestCase):
    """登录测试类"""

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()  # 获取浏览器对象
        cls.login_proxy = LoginProxy()  # 登录页面业务执行对象

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        cls.driver.quit()
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setUp(self) -> None:
        self.driver.get('http://192.168.20.59')  # 打开首页
        self.driver.find_element_by_link_text('登录').click()  # 点击登录链接

    def tearDown(self) -> None:
        pass
        # time.sleep(3)
        # self.driver.quit()

    @parameterized.expand(build_login_data())
    def test_login_func(self, username, password, code, is_success, expect):
        """登录测试方法"""
        self.login_proxy.login(username, password, code)

        print('username={}, password={}, code={}, expect={}').format(
            username, password, code, expect)

        logging.info()

        # 条件判断是正向还是反向
        if is_success:
            # 正向用例
            time.sleep(2)
            # 获取页面标题
            title = self.driver.title
            # 设置断言判断结果
            self.assertIn(expect, title)
        else:
            # 反向用例断言
            # 获取错误提示信息
            msg = get_tips_message()
            # 设置断言判断结果
            self.assertIn(expect, msg)

    # def test_account_does_not_exist(self):
    #     """账号不存在"""
    #     self.login_proxy.login('13811110000', '123456', '8888')
    #
    #     msg = self.driver.find_element_by_class_name('layui-layer-content').text
    #     print('msg=', msg)
    #
    #     # 设置断言判断结果
    #     self.assertIn('账号不存在', msg)
    #
    # def test_wrong_password(self):
    #     """密码错误"""
    #     self.login_proxy.login('13612345678', '111111', '8888')
    #
    #     msg = self.driver.find_element_by_class_name('layui-layer-content').text
    #     print('msg=', msg)
    #
    #     # 设置断言判断结果
    #     self.assertIn('密码错误', msg)


if __name__ == '__main__':
    unittest.main()
