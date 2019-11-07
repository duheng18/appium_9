'''
# 作业三：
# 完成雪球登录场景的测试
# 要去带有setup_class setup_method体系
# 微信 验证码 密码 错误的用户名 错误的密码 至少编写5条用例
'''
import appium
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class TestWeixinLogin(object):
    driver = WebDriver

    @classmethod
    def install_app(cls):
        # 配置
        caps = {}
        # 如果有必须要进行第一次安装
        # caps["app"] = "/Users/duheng/Downloads/xueqiu_wxdialog.apk"
        caps["platformName"] = "android"
        caps["deviceName"] = "demo.txt"
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
    def restart_app(cls):
        desired_caps = {
            "platformName": "android",
            "deviceName": "demo.txt",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        return driver

    @classmethod
    def setup_class(cls):
        cls.driver = cls.install_app()
        ele1 = cls.driver.find_element_by_id('user_profile_container')
        ele1.click()

    def setup_method(self):
        self.driver = TestWeixinLogin.restart_app()
        ele2 = self.driver.find_element_by_id('login_more')
        ele2.click()

    def test_login_user(self):
        ele3 = self.driver.find_element_by_id('login_account')
        ele3.send_keys('111111')
        els4 = self.driver.find_element_by_id('login_password')
        els4.send_keys('123456')
        ele5 = self.driver.find_element_by_id('button_next')
        ele5.click()
        ele6 = self.driver.find_element_by_id('md_buttonDefaultPositive')
        ele6.click()

    def teardown_method(self):
        self.driver.back()
