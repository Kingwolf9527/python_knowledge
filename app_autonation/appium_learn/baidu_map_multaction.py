# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/31 9:20

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
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
desired_capability['appPackage'] = 'com.baidu.BaiduMap'
#设置超时时间
# desired_capability['newCommandTimeout'] = '3000'
# 需要调用的app的launcher-activity
desired_capability['appActivity'] = 'com.baidu.baidumaps.WelcomeScreen'
# 保持回话,这个参数比较重要，决定是否重置会话
desired_capability['noReset'] = 'false'
# 安装app
desired_capability['app'] = r'D:\appium_apk_test\baiduditu.apk'

# 建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capability)
driver.implicitly_wait(8)


#点击"同意"按钮
driver.find_element_by_id('com.baidu.BaiduMap:id/ok_btn').click()
time.sleep(5)

#处理系统弹窗权限，全部允许
try:
    eles = driver.find_elements_by_id('android:id/button1')
    #采用死循环，全部系统弹窗都点击允许
    while True:
        for ele in eles:
            if ele.text == u'允许':
                driver.find_element_by_android_uiautomator('new UiSelector().text("允许")').click()
            elif ele.text == u'确定':
                driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
            elif ele.text == u'始终允许':
                driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
except:
    pass

#点击"进入地图"
driver.find_element_by_id('com.baidu.BaiduMap:id/btn_enter_map').click()
driver.implicitly_wait(3)

#处理弹窗
try:
    driver.find_element_by_id('com.baidu.BaiduMap:id/guide_close')
except:
    pass
else:
    driver.find_element_by_id('com.baidu.BaiduMap:id/guide_close').click()

#获取页面的宽高
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']

#地图的缩放操作
def pinch():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    pinch_action = MultiAction(driver)

    #缩放处理
    action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8,y=y*0.8).wait(1000).move_to(x=x*0.6,y=y*0.6).wait(1000).release()

    print('start pinch.....')

    #MultiAction把缩放处理追加进去,并且统一执行
    pinch_action.add(action1,action2)
    pinch_action.perform()

#地图的放大操作
def zoom():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    #缩放处理
    action1.press(x=x*0.4,y=y*0.4).wait(1000).move_to(x=x*0.2,y=y*0.2).wait(1000).release()
    action2.press(x=x*0.6,y=y*0.6).wait(1000).move_to(x=x*0.8,y=y*0.8).wait(1000).release()

    print('start zoom....')

    #MultiAction把放大处理追加进去,并且统一执行
    zoom_action.add(action1,action2)
    zoom_action.perform()

if __name__ == '__main__':
    for i in range(3):
        pinch()

    for i in range(3):
        zoom()

