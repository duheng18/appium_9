# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# 导入依赖
from appium import webdriver

# 配置
caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

# 初始化driver
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# 追加一句隐式等待 隔半秒就去check一下是否有下面的元素，定位到后（10内找到不会一直等到10s）直接下一步。
driver.implicitly_wait(10)

# 写case
el1 = driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_with_account")
el3.click()

# 断言

# 退出
driver.quit()
