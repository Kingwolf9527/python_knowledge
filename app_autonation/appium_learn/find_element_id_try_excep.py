# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/20 23:53

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

#配置capability信息
desired_capability = {}
#操作系统
desired_capability['platformName'] = 'Android'
#操作系统的版本
desired_capability['platformVersion'] = '9'
#设备名称
desired_capability['deviceName'] = 'kingwolf'
#设备的udid(通过adb devices获取的)
desired_capability['udid'] = 'eac4b4a4'
#需要调用的app包名
desired_capability['appPackage'] = 'com.tal.kaoyan'
#需要调用的app的launcher-activity
desired_capability['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

#保持回话,这个参数比较重要，决定是否重置会话
desired_capability['noReset'] = 'true'

#安装app
desired_capability['app'] = r'D:\appium_apk_test\kaoyanbang.apk'

#建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capability)

driver.implicitly_wait(5)

#判断首次安装和非首次，非首次是没有引导页的，就不存在相应的引导页面的按钮
def check_skipbtn():
    print('check skipbtn')
    try:
        #'跳过'按钮的定位
        skip_btn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no shipbtn')
    else:
        skip_btn.click()

check_skipbtn()

