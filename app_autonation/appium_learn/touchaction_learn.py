# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/31 7:20

"""
    不是用selenium的touch_actions.TouchActions，是用appium的touch_action.TouchAction
    两者的差别很大

"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
# from selenium.webdriver.common.touch_actions import TouchActions
from appium.webdriver.common.touch_action import TouchAction
import time

# 配置capability信息
desired_capability = {}
# 操作系统
desired_capability['platformName'] = 'Android'
# 操作系统的版本
desired_capability['platformVersion'] = '9'
# 设备名称
desired_capability['deviceName'] = 'kingwolf'
# 设备的udid(通过adb devices获取的)
desired_capability['udid'] = 'eac4b4a4'
# 需要调用的app包名
desired_capability['appPackage'] = 'com.mymoney'
#设置超时时间
desired_capability['newCommandTimeout'] = '3000'
# 需要调用的app的launcher-activity
desired_capability['appActivity'] = 'com.mymoney.biz.splash.SplashScreenActivity'
# 保持回话,这个参数比较重要，决定是否重置会话
desired_capability['noReset'] = 'false'
# 安装app
desired_capability['app'] = r'D:\appium_apk_test\Mymoney.apk'

# 建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capability)
driver.implicitly_wait(8)

#定义滑动方法
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

#向左滑动
def swipe_left():
    left_swipe = get_size()
    x1 = int(left_swipe[0]*0.9)
    y1 = int(left_swipe[1]*0.5)
    x2 = int(left_swipe[0]*0.2)
    driver.swipe(x1,y1,x2,y1,1000)

#向上滑动
def swipe_up():
    left_swipe = get_size()
    x1 = int(left_swipe[0]*0.5)
    y1 = int(left_swipe[1]*0.9)
    y2 = int(left_swipe[1]*0.2)
    driver.swipe(x1,y1,x1,y2,1000)

#判断，引导页面的是否存在下一页的按钮，在做滑动操作
WebDriverWait(driver,8).until(lambda x:x.find_element_by_id('com.mymoney:id/next_btn'))
#向左滑动两次
for i in range(2):
    swipe_left()
    time.sleep(0.5)

#点击"开始随手记"，进入页面
driver.find_element_by_id('com.mymoney:id/begin_btn').click()
driver.implicitly_wait(2)

#点击“设置”，进入页面
driver.find_element_by_id('com.mymoney:id/nav_btn_forth').click()
#判断页面是否加载成功，在执行滑动操作
WebDriverWait(driver,8).until(lambda x:x.find_element_by_id('com.mymoney:id/cell_generic_text_cell_cl'))

#向上滑动，找到"高级"设置，点击，进入页面,用uiautomator方法定位元素
swipe_up()
driver.implicitly_wait(1)
driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()
driver.implicitly_wait(1)

#点击"密码保护"，进入页面
driver.find_element_by_android_uiautomator('new UiSelector().text("密码保护")').click()
driver.implicitly_wait(1)

#点击"手势密码"，进入页面
driver.find_element_by_id('com.mymoney:id/ll_gesture_psd').click()
driver.implicitly_wait(1)

#设置手势密码,需要滑动操作两次
for i in range(2):
    TouchAction(driver).press(x=265,y=555).wait(2000)\
    .move_to(x=555,y=575).wait(1000)\
    .move_to(x=825,y=835).wait(1000)\
    .move_to(x=832,y=1116).wait(1000)\
    .release().perform()
