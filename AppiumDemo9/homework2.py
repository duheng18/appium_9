# coding: utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

caps = {
  "platformName": "android",
  "deviceName": "FFK0217921009464",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "autoGrantPermissions": "true",
  "unicodeKeyboard": "true",
  "resetKeyboard": "true"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

# 获取屏幕的大小和坐标
window_size = driver.get_window_size()


def move_to_up_once(touch_action):
    # 上滑一次
    touch_action.press(x=window_size['width'] * 0.99, y=window_size['height'] * 0.9).wait(1000).move_to(x=window_size['width'] * 0.99, y=window_size['height'] * 0.3).release().perform()


def move_to_up(touch_action, times):
    for i in range(times):
        print("第%s次从下往上滑" % str(i+1))
        move_to_up_once(touch_action)
        sleep(2)


def move_to_left_once(touch_action):
    # 向左滑行一次
    touch_action.press(x=window_size['width'] - 1, y=window_size['height'] * 0.5).move_to(x=1, y=window_size['height'] * 0.5).release().perform()
    sleep(2)


# 点击基金 -- title
driver.find_element_by_xpath("//*[contains(@resource-id,'indicator')]//*[@text='基金']").click()
sleep(4)

# 基金右边的新闻栏目个数
count_title = 8

action = TouchAction(driver)

for i in range(count_title):
    # 先向上滑5次
    print("第%s个新闻栏目" % str(i+1))
    move_to_up(action, 5)
    # 向左滑行
    if i < 7:
        move_to_left_once(action)