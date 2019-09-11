"""
    编写：
        0. 模块名：page_页面/模块
        1. 类名将模块名以大驼峰形式抄进来，有下划线去掉下划线；
        2. 方法：将操作步骤，每一步单独封装成一个方法
        3. 根据需求组合业务方法；
"""
from app import page
from app.base.base import Base


class PageLogin(Base):

    # 输入用户名
    def page_input_username(self, username):
        # 调用 输入方法
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login(self):
        self.base_click(page.login_btn)

    # 组合业务方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login()
