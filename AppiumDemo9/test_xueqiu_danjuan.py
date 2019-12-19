from appium import webdriver
import pytest
import time
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestXueqiuAndroid(object):
    driver = WebDriver

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

        # 初始化driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 追加一句隐式等待 隔半秒就去check一下是否有下面的元素，定位到后（10内找到不会一直等到10s）直接下一步。
        driver.implicitly_wait(15)
        return driver

    @classmethod
    def restart_app(cls) -> webdriver:
        # 配置
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["chromedriverExecutableDir"] = "/Users/duheng/Downloads/2.43"
        # 为了更快的驱动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps["noReset"] = "true"

        # 初始化driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 追加一句隐式等待 隔半秒就去check一下是否有下面的元素，定位到后（10内找到不会一直等到10s）直接下一步。
        driver.implicitly_wait(15)
        return driver

    def setup_class(cls):
        cls.driver = cls.restart_app()
        WebDriverWait(cls.driver, 20, 1).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='交易']")))

    def setup_method(self):
        self.driver = TestXueqiuAndroid.driver
        self.driver.find_element_by_xpath("//*[@text='交易']").click()


    def test_danjuan(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='基金开户']")))
        self.driver.find_element_by_xpath("//*[@text='基金开户']").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((MobileBy.ID, "btn_login")))
        self.driver.find_element_by_id("btn_login").click()
        time.sleep(3)
        print(self.driver.contexts)
        print(self.driver.current_context)
        # 切换context
        self.driver.switch_to.context('WEBVIEW_com.xueqiu.android')
        print(self.driver.current_context)
        time.sleep(3)

        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(5)
        self.driver.find_element_by_id('telno').send_keys('18810075728')
        time.sleep(5)
        self.driver.find_element_by_id('code').send_keys('123456')
        time.sleep(5)
        self.driver.find_element_by_id('next').click()

        # print()
        # time.sleep(3)

    def method_teardown(self):
        self.driver.back()
        self.driver.back()
