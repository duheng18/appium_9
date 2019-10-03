from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "9"
caps["deviceName"] = "862501c7"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps['autoGrantPermission'] = 'True'
caps['noReset'] = 'True'
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

# 找到基金一栏
ele1 = driver.find_element_by_xpath("//*[contains(@class,'HorizontalScrollView')]//*[@text='基金']")
ele_list = driver.find_elements_by_xpath("//*[contains(@class,'HorizontalScrollView')]//*[@text='基金']/../../*")
ele1.click()
w_size = driver.get_window_size()

# 确定'基金'后有多少个tab
last_p = ""
tap_list=[]
while True:
    ele_text = []
    for ele in ele_list:
        try:
            text_tmp = ele.find_element_by_xpath("//*[@text!='']").text
            ele_text.append(text_tmp)
        except:
            pass

    if len(tap_list) and tap_list[-1] == ele_text[-1]:
        break
    for tex in ele_text:
        if tex not in tap_list:
                tap_list.append(tex)

    ele_lo = ele_list[-1].location
    driver.swipe(ele_lo['x'],ele_lo['y'],1,ele_lo['y'])
    ele_list = driver.find_elements_by_xpath("//*[contains(@class,'HorizontalScrollView')]//*[@text='%s']/../../*" % text_tmp)


# 从右向左滑动切换tab
for i in range(len(tap_list[tap_list.index('基金'):])):
    # 由下往上滑动
    for i in range(5):
        driver.swipe(w_size['width']*0.5,w_size['width']*0.7,w_size['width']*0.5,w_size['width']*0.2)
        time.sleep(1)
    driver.swipe(w_size['width']*0.8,w_size['width']*0.5,w_size['width']*0.2,w_size['width']*0.5)

driver.quit()