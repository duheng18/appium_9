# __author:lenovo
# date:2019/5/8

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
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el4.send_keys("alibaba")

# 取消tip弹窗
driver.implicitly_wait(5)

# 在搜索框中输入“alibaba”
el5 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el5.send_keys("alibaba")
driver.implicitly_wait(5)

# 点击alibaba
ali = driver.find_element_by_id("com.xueqiu.android:id/listview").find_element_by_class_name(
    "android.widget.RelativeLayout").click()


# 下次再说
def say_nex_time():
    el8 = driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultNegative").click()


# 立刻评价
def immediate_evaluation():
    el9 = driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultPositive").click()


def check_click():
    if say_nex_time():
        # 点击雪球app评价的“下次再说”按钮
        print("下次再说")
    elif immediate_evaluation():
        print("立刻评价")
    else:
        print("exit")



def has_checked():
    check_enabled()
    # 点击第一条搜索结果右边的“+”，进行自选股的添加
    # 退出
    driver.quit()

# 确认是否是选中状态
def check_enabled():
    if driver.find_element_by_accessibility_id("com.xueqiu.android:id/followed_btn").is_enabled() == "true":
        print("已勾选")
    else:
        has_checked()
        print("未勾选")
        el7 = driver.find_element_by_id("com.xueqiu.android:id/follow_btn").click()
        check_click()
