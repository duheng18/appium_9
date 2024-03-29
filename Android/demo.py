# test_android_contacts.py

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '9'


class TestWebViewAndroid():
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            'appPackage': 'com.example.zip.android.contactmanager',
            'appActivity': '.ContactManager',
            'platformName': 'Android Emulator',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': 'Nexus_6P_API_28',
            'app': PATH('ContactManager.apk')
        }
        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value

    def test_add_contacts(self, driver):
        el = driver.find_element_by_accessibility_id("Add Contact")
        el.click()

        textfields = driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("Appium User")
        textfields[2].send_keys("someone@appium.io")

        assert 'Appium User' == textfields[0].text
        assert 'someone@appium.io' == textfields[2].text

        driver.find_element_by_accessibility_id("Save").click()

        # for some reason "save" breaks things
        # alert = driver.switch_to.alert

        # no way to handle alerts in Android
        driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        driver.press_keycode(3)


if __name__ == '__main__':
    pytest.main()
