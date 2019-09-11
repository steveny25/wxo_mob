from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        return (WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
                .until(lambda x: x.find_element(*loc)))

    # 输入 方法
    def base_input(self, loc, value):
        # 获取
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 点击 方法
    def base_click(self, loc):
        self.base_find(loc).click()
