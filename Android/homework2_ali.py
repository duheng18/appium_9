# __author:lenovo
# date:2019/5/8

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import os

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
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el4.send_keys("alibaba")

# 在搜索框中输入“alibaba”
el5 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el5.send_keys("alibaba")

# 点击alibaba
ali = driver.find_element_by_id("com.xueqiu.android:id/listview").find_element_by_class_name(
    "android.widget.RelativeLayout").click()
value1 = driver.find_element_by_id("com.xueqiu.android:id/follow_btn").text
print(value1)
# value2 = driver.find_element_by_id("com.xueqiu.android:id/followed_btn").text
# print(value2)
# if value1 == '已添加':
#     print("已勾选")
#     value1 = driver.find_element_by_id("com.xueqiu.android:id/follow_btn").click()
#
# elif value2 == '加自选':
#     print("未勾选")
#     el9 = driver.find_element_by_id("com.xueqiu.android:id/follow_btn").click()
#     el10 = driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultNegative").click()
#     # el9 = driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultPositive").click()
# else:
#     print("you are wrong")
#     driver.quit()
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)