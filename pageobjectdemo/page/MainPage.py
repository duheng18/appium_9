from python.Appium.pageobjectdemo.driver.AndroidClient import AndroidClient
from python.Appium.pageobjectdemo.page.StockPage import StockPage


class MainPage(object):
    def __init__(self):
        AndroidClient.restartApp()

    def gotoHangqing(self):
        AndroidClient.driver.find_element_by_xpath('//*[@text="行情"]')
        AndroidClient.driver.find_element_by_xpath('//*[@text="行情"]').click()
        return StockPage()
