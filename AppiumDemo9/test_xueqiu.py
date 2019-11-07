# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# 导入依赖
from appium import webdriver
import pytest
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction
import time


class TestXueqiuAndroid(object):
    driver = WebDriver

    @classmethod
    def setup_class(cls):
        print("setup class 在当前类下的所有用例执行之前只执行一次")
        cls.install_app()

    def setup_method(self):
        print("setup method 在每个测试用例执行之前执行一次")
        # 获取启动的appium的driver实例，用于后续每个case的driver
        self.driver = self.restart_app()

    def test_login(self):
        # 写case
        el1 = self.driver.find_element_by_id("user_profile_icon")
        el1.click()
        el2 = self.driver.find_element_by_id("iv_login_phone")
        el2.click()
        el3 = self.driver.find_element_by_id("tv_login_with_account")
        el3.click()

    def test_found(self):
        # 写case
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']").click()

    def test_swipe(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        for i in range(5):
            self.driver.swipe(1000, 1000, 200, 200)
            time.sleep(2)

    def test_action(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=1000, y=1000).move_to(x=200, y=200).release().perform()
            print(i)
            time.sleep(2)

    def test_action_percent(self):
        rect = self.driver.get_window_rect()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']")
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=rect['width'] * 0.8, y=rect['height'] * 0.8).move_to(x=rect['width'] * 0.2, y=rect[
                                                                                                             'height'] * 0.2).release().perform()
            print(i)
            time.sleep(2)
            self.driver.get_screenshot_as_file(str(i) + '.png')

    def test_window_size(self):
        print(self.driver.get_window_rect())

    def teardown_method(self):
        print("teardown method")
        # 不加也没关系，如果不quit，启动appium会自动quit之前的session
        self.driver.quit()

    @classmethod
    def install_app(cls) -> webdriver:
        # 配置
        caps = {}
        # 如果有必须要进行第一次安装
        # caps["app"] = "/Users/duheng/Downloads/xueqiu_wxdialog.apk"
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 解决第一次启动的问题
        caps["autoGrantPermissions"] = "true"
        # caps["noReset"]="true"

        # 初始化driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 追加一句隐式等待 隔半秒就去check一下是否有下面的元素，定位到后（10内找到不会一直等到10s）直接下一步。
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def restart_app(cls) -> webdriver:
        # 配置
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 为了更快的驱动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps["noReset"] = "true"

        # 初始化driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 追加一句隐式等待 隔半秒就去check一下是否有下面的元素，定位到后（10内找到不会一直等到10s）直接下一步。
        driver.implicitly_wait(10)
        return driver
