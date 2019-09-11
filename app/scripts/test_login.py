from app.page.page_in import PageIn
import pytest

from app.tool.get_driver import GetDriver
from app.tool.read_txt import read_txt
from app.tool.read_yaml import read_yaml


def get_data():
    # arrs = []
    # for data in read_txt("login.txt"):
    #     arrs.append(tuple((data.strip().split(","))))
    # return arrs[1::]

    arrs = []
    for data in read_yaml("login.yaml").values():
        arrs.append((data.get("username"), data.get("password")))

    return arrs


class TestLogin:
    # 初始化
    def setup_class(self):
        # 实例化获取PageLogin
        self.login = PageIn().page_get_pagelogin()

    # 结束
    def teardown_class(self):
        # 关闭driver驱动对象
        # 坑 2 只能调用 关闭driver
        GetDriver.quit_driver()
        # 错误写法，没有置空操作
        # self.login.driver.quit()

    # 登录测试方法
    @pytest.mark.parametrize("username, pwd", get_data())
    def test_login(self, username, pwd):
        # 调用业务方法
        self.login.page_login(username, pwd)

# pytest.main("-s Atest_login.py")