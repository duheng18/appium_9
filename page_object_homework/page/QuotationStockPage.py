from python.Appium.page_object_homework.driver.AndroidClient import AndroidClient


class QuotationStockPage(object):
    def getShenzhenStockIndex(self, name) -> float:
        price = AndroidClient.driver.find_element_by_xpath(
            "//*[contains(@resource-id,'index_name') and @text='" + name + "']/..//*[contains(@resource-id,'index_price')]").text

        return float(price)
