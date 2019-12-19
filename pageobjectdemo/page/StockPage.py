from python.Appium.pageobjectdemo.driver.AndroidClient import AndroidClient


class StockPage(object):
    def getPrice(self, name) -> float:
        price = AndroidClient.driver.find_element_by_xpath(
            "//*[contains(@resource-id,'index_name') and @text='" + name + "']/..//*[contains(@resource-id,'index_price')]").text
        return float(price)
