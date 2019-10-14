import time

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueqiuAndroid(object):
    dirver = WebDriver

    @classmethod
    def setup_class(cls):
        print("setup class!")
        cls.driver = cls.init_appium()

    def setup_method(self):
        print("setup method!")
        TestXueqiuAndroid.driver = self.restart_appium()
        self.driver = TestXueqiuAndroid.driver

    def test_login(self):
        # 写case
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login_with_account")
        el3.click()

    def test_jijin(self):
        # 写case
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'indicator')]//*[@text='基金']").click()

    def teardown_method(self):
        self.driver.quit()

    def test_swipe(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'indicator')]//*[@text='基金']")
        for i in range(5):
            self.driver.swipe(1000, 1000, 200, 200)
            time.sleep(2)

    def test_action(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'indicator')]//*[@text='基金']")
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=1000, y=1000).move_to(x=200, y=200).release().perform()
            time.sleep(2)

    def test_action_per(self):
        size = self.driver.get_window_rect()
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'indicator')]//*[@text='基金']")
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=size['width'] * 0.8, y=size['height'] * 0.8).move_to(x=size['width'] * 0.2, y=size[
                                                                                                             'height'] * 0.2).release().perform()
            time.sleep(2)

    def test_get_window_size(self):
        print(self.driver.get_window_rect())
        print(self.driver.get_window_size())

    @classmethod
    def init_appium(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(15)
        return driver

    @classmethod
    def restart_appium(cls) -> WebDriver:
        caps = {}
        # caps["app"]=''
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["autoGrantPermissions"] = "true"
        caps["noReset"] = True

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(15)
        return driver
