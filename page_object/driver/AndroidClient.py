from appium import webdriver
from selenium.webdriver.android.webdriver import WebDriver


class AndroidClient(object):
    driver = WebDriver

    @classmethod
    def installApp(cls) -> WebDriver:
        caps = {}
        caps['platformName'] = "android"
        caps['deviceName'] = "hogwarts"
        caps['appPackage'] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermission"] = "true"

        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

        return cls.driver

    @classmethod
    def restartApp(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissin"] = "true"
        caps["noReset"] = "true"
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

        return cls.driver
