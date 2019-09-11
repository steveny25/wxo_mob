from app.page.page_address import PageAddress
from app.page.page_login import PageLogin
from app.page.page_order import PageOrder
from app.tool.get_driver import GetDriver


class PageIn:

    def __init__(self):
        self.driver = GetDriver.get_driver()

    # 获取PageLoin对象
    def page_get_pagelogin(self):
        return PageLogin(self.driver)

    # 获取PageOrder对象
    def page_get_pageorder(self):
        return PageOrder(self.driver)

    # 获取PageAddress对象
    def page_get_pageaddress(self):
        return PageAddress(self.driver)