import pytest

from python.Appium.page_object.page.MainPage import MainPage


class TestSelected(object):
    def test_price(self):
        main = MainPage()
        # assert main.gotoSelected().getPriceByName("科大讯飞") == 28.83
        assert main.gotoSelected().getPriceByName("贵州茅台") == 1233.75

    def test_add_stock(self):
        pass
