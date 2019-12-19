# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# 导入依赖
from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiuAndroid(object):
    driver = WebDriver

    @classmethod
    def setup_class(cls):
        print("setup class 在当前类下的所有用例执行之前只执行一次")
        cls.driver = cls.restart_app()
        # print(cls.driver.contexts)
        WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='交易']")))
        cls.driver.find_element_by_xpath("//*[@text='交易']").click()

    def setup_method(self):
        print("setup method 在每个测试用例执行之前执行一次")
        # 获取启动的appium的driver实例，用于后续每个case的driver
        self.driver = TestXueqiuAndroid.driver

        self.driver.find_element_by_xpath("//*[@text='交易']").click()

    def test_webview_simulator_native(self):
        self.driver.find_element_by_xpath("//*[@text='A股开户']").click()
        self.driver.find_element_by_xpath("//*[@text='立即开户']")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='立即开户']")))

    def test_webview_simulator_css(self):
        print(self.driver.contexts)
        print(self.driver.current_context)
        self.driver.switch_to.context('WEBVIEW_com.xueqiu.android')
        print(self.driver.current_context)

    def test_webview_simulator_fund(self):
        self.driver.find_element_by_xpath("//*[@text='基金开户']").click()

    def teardown_method(self):
        print("teardown method")
        # 不加也没关系，如果不quit，启动appium会自动quit之前的session
        self.driver.back()
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
