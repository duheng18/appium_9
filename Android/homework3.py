# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python


from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "Test"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"
caps["unicodeKeyboard"] = "true"
caps["resetKeyboard"] = "true"
# caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
driver.hide_keyboard()

# 点击搜索框，输入alibaba,选择第一个搜索结果，并判断是否已经加入自选
search = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
search.click()
search_input_text = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
search_input_text.send_keys("alibaba")
# 点击alibaba
ali = driver.find_element_by_id("com.xueqiu.android:id/listview").find_element_by_class_name(
    "android.widget.RelativeLayout").click()
searchresults = driver.find_element_by_id("com.xueqiu.android:id/ll_stock_item_container").find_elements_by_class_name(
    "android.widget.RelativeLayout")[0]
print(searchresults)
if searchresults.find_element_by_id("com.xueqiu.android:id/follow_btn").text == '加自选':
    searchresults.find_element_by_id("com.xueqiu.android:id/follow_btn").click()
    driver.find_element_by_id("com.xueqiu.android:id/md_buttonDefaultNegative").click()
else:
    print('已添加')

# 返回并进入自选股，获取自选股列表，并判断阿里巴巴是否添加成功
cancel = driver.find_element_by_id("com.xueqiu.android:id/action_close")
cancel.click()
selectedstocks = \
    driver.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.RelativeLayout")[1]
selectedstocks.click()

stocks = driver.find_elements_by_id("com.xueqiu.android:id/portfolio_stockName")
stocklist = []
for stock in stocks:
    stockname = stock.get_attribute("text")
    stocklist.append(stockname)
print(stocklist)
assert '阿里巴巴' in stocklist
