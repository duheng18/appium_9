import pytest

from python.Appium.page_object_homework.page.MainPage import MainPage


class TestStockIndex(object):
    def test_StockIndex(self):
        main = MainPage()
        assert main.gotoSelected().getShenzhenStockIndex("深证成指") > 8000
