'''
进入雪球首页，进入基金的新闻页（不是第一个基金按钮），对他以及它右侧的每个新闻栏目，执行上滑5次，进入下个栏目用从右边到左边滑动
滑动使用相对坐标，而不是绝对坐标
'''

import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.touch_action import TouchAction
import time


class TestXueqiu(object):
    driver = WebDriver

    @classmethod
    def setup_class(cls):
        print("setup class 在当前类下的所有用例执行之前只执行一次")
        # cls.install_app()

    def setup_method(self):
        print("setup method 在每个测试用例执行之前执行一次")
        # 获取启动的appium的driver实例，用于后续每个case的driver
        self.driver = self.restart_app()

    def test_move(self):
        rect = self.driver.get_window_rect()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']").click()
        time.sleep(3)
        action = TouchAction(self.driver)
        for i in range(8):
            for j in range(5):
                # 上下滑动
                action.press(x=rect['width']*0.5, y=rect['height']*0.5).move_to(x=rect['width'] *0.2, y=rect[
                                                                                                           'height']*0.2).release().perform()
                print(i)
                time.sleep(2)
            # 左右滑动
            action.press(x=rect['width']*0.2, y=rect['height']*0.2).move_to(x=rect['width']*0.5,
                                                                            y=['height']*0.2).release().perform()
            time.sleep(3)

    @classmethod
    def install_app(cls):
        caps = {}
        caps['app'] = ''
        caps['platformName'] = 'android'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['automationName'] = 'UiAutomator2'
        caps["deviceName"] = "piex"
        caps['autoGrantPermissions'] = 'true'

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def restart_app(cls):
        caps = {}
        caps['platformName'] = 'android'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['automationName'] = 'UiAutomator2'
        caps["deviceName"] = "piex"
        caps['noReset'] = 'true'

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver
