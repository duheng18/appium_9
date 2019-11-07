
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
        cls.driver = cls.install_app()
        el1 = cls.driver.find_element_by_id("user_profile_icon")
        el1.click()

    def setup_method(self):
        print("setup method 在每个测试用例执行之前执行一次")
        # 获取启动的appium的driver实例，用于后续每个case的driver
        self.driver = TestXueqiuAndroid.driver
        el2 = self.driver.find_element_by_id("iv_login_phone")
        el2.click()

    def test_login_password(self):
        self.driver.find_element_by_id('sina_login').click()
        self.driver.back()
        time.sleep(5)

    def test_login_phone(self):
        el3 = self.driver.find_element_by_id("tv_login_with_account")
        el3.click()


    def teardown_method(self):
        print("teardown method")
        # 不加也没关系，如果不quit，启动appium会自动quit之前的session
        self.driver.back()

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
