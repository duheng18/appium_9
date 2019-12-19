from python.Appium.pageobjectdemo.page.MainPage import MainPage
import pytest


class TestStockIndex(object):
    def testPrice(self):
        main = MainPage()
        assert main.gotoHangqing().getPrice('上证指数') > 2800
