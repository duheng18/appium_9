# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "demo.txt"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_open")
el1.click()
el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el2.click()
el3 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el4.click()
el5 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el5.send_keys("pdd")

# driver.quit()