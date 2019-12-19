'''test_login.py
'''

import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from getsmscode import getCodeFromSms
from elementexit import findelement
@allure.feature("登陆功能")
class Test_XueqiuLogin(object):
    # 启动app并进入登录页面
    def setup_method(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["automationName"] = "uiautomator2"
        # caps["noReset"] = "true"
        caps["autoGrantPermissions"] = True
        caps["unicodeKeyboard"] = True
        caps["resetKeyboard"] = True
        caps["newCommandTimeout"] = 60
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        time.sleep(5)
        self.driver.find_element_by_id("user_profile_icon").click()
        self.driver.find_element_by_id("tv_login").click()

    @allure.story("微信登陆")
    def test_login_Weixin(self):
        self.driver.find_element_by_id("rl_login_by_wx").click()

        # 微信已登录
        if findelement(self.driver,By.XPATH,"//*[@text='确认登录']"):
            self.driver.find_element_by_xpath("//*[@text='确认登录']").click()
        if findelement(self.driver,By.ID,"screen_name"):
            username = self.driver.find_element_by_id("screen_name")
            usernametext = username.get_attribute("text")
            print(usernametext)
            assert usernametext == "qd_tudou"

        # 微信未登录
        if findelement(self.driver,By.XPATH,"//*[@text='请填写微信号/QQ号/邮箱']"):
            self.driver.find_element_by_xpath("//*[@text='请填写微信号/QQ号/邮箱']").send_keys("12345678")
            self.driver.find_element_by_xpath("//*[@text='请填写密码']").send_keys("12345678")
            self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/ch6' and @text='登录']").click()
            wrong = self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/cvo' and @text='帐号或密码错误，请重新填写。']")
            assert wrong.is_displayed()


    @allure.story("手机验证码登陆")
    def test_login_Phone(self):

        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        self.driver.find_element_by_id("register_phone_number").send_keys("13061406764")
        self.driver.find_element_by_id("register_code_text").click()
        smscode = getCodeFromSms()
        # wait = WebDriverWait
        if smscode:
            # smscode = int(smscode)
            print(smscode)
            self.driver.find_element_by_xpath("//*[@text='请输入四位验证码']").send_keys(smscode)
            self.driver.find_element_by_id("button_next").click()
        else:
            print("未接收到验证码")
        if findelement(self.driver,By.XPATH,"//*[@resource-id='com.xueqiu.android:id/md_title' and @text='语音验证']"):
            self.driver.find_element_by_xpath("//*[@resource-id='md_buttonDefaultNegative' and @text='取消']").click()

        # 后面进行图片验证，不知道如何操作

    @allure.story("密码登陆")
    def test_login_password(self):
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        self.driver.find_element_by_id("tv_login_with_account").click()
        self.driver.find_element_by_id("login_account").send_keys("13061406764")
        self.driver.find_element_by_id("login_password").send_keys("")
        self.driver.find_element_by_id("button_next").click()
    @allure.story("密码登陆：用户名错误")
    def test_login_wrong_usrname(self):
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        self.driver.find_element_by_id("tv_login_with_account").click()
        self.driver.find_element_by_id("login_account").send_keys("12345678901")
        self.driver.find_element_by_id("login_password").send_keys("12345678901")
        self.driver.find_element_by_id("button_next").click()
        wrong = self.driver.find_element_by_xpath("//*[@text='用户名或密码错误']")
        assert wrong.is_displayed()
    @allure.story("密码登陆: 密码错误")
    def test_login_wrong_password(self):
        self.driver.find_element_by_id("tv_login_by_phone_or_others").click()
        self.driver.find_element_by_id("tv_login_with_account").click()
        self.driver.find_element_by_id("login_account").send_keys("13061406764")
        self.driver.find_element_by_id("login_password").send_keys("12345678901")
        self.driver.find_element_by_id("button_next").click()
        wrong = self.driver.find_element_by_xpath("//*[@text='用户名或密码错误']")
        assert wrong.is_displayed()

    # 退出登录
    def teardown_method(self):
        print("teardown_method")
        self.driver.quit()

if __name__ == "__main__":
    pytest.main(["-s","test_login.py","--alluredir","./report/test_login"])
