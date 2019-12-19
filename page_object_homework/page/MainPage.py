from python.Appium.page_object_homework.driver.AndroidClient import AndroidClient
from python.Appium.page_object_homework.page.QuotationStockPage import QuotationStockPage


class MainPage(object):
    # 调用appium启动app
    def __init__(self):
        AndroidClient.restartApp()

    # 进入自选页
    def gotoSelected(self):
        # 调用全局的drvier对象调用webdriver api操纵app
        AndroidClient.driver.find_element_by_xpath("//*[@text='行情']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='行情']").click()

        return QuotationStockPage()
