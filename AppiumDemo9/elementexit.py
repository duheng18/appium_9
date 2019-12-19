from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def findelement(driver:WebDriver,by:By,value:str):
    try:
        driver.find_element(by=by,value=value)
        return True
    except NoSuchElementException:
        return False

