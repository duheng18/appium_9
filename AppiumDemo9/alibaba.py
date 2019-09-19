# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

driver.implicitly_wait(10)
el1 = driver.find_element_by_id("com.xueqiu.android:id/quick_action").find_element_by_class_name(
    'android.widget.ImageView')
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/item_add_stock")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("alibaba")
el4 = driver.find_element_by_id("com.xueqiu.android:id/listview").find_element_by_class_name(
    "android.widget.RelativeLayout")
el4.click()
el5 = driver.find_element_by_id("com.xueqiu.android:id/ll_stock_item_container").find_element_by_id("com.xueqiu.android:id/add_attention")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultNegative")
el6.click()

driver.quit()
