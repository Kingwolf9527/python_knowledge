# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/20 23:53

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


# 配置capability信息
desired_capability = {}
# 操作系统
desired_capability['platformName'] = 'Android'
# 操作系统的版本
desired_capability['platformVersion'] = '5.1.1'
# 设备名称
desired_capability['deviceName'] = '127.0.0.1:62001'
# 设备的udid(通过adb devices获取的)
# desired_capability['udid'] = 'eac4b4a4'
# 需要调用的app包名
desired_capability['appPackage'] = 'com.tal.kaoyan'
#设置超时时间
desired_capability['newCommandTimeout'] = '4000'
# 需要调用的app的launcher-activity
desired_capability['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

#设置uiautomator2来处理toast消息
desired_capability['automationName'] = 'uiautomator2'

# 保持回话,这个参数比较重要，决定是否重置会话
desired_capability['noReset'] = 'true'

# #相关键盘操作，包含输入有中文字符
desired_capability['unicodeKeyboard'] = 'true'
desired_capability['resetKeyboard'] = 'true'

# 安装app
desired_capability['app'] = r'D:\appium_apk_test\kaoyanbang.apk'

# 建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capability)
driver.implicitly_wait(8)

#判断首次安装和非首次，非首次是没有引导页的，就不存在相应的引导页面的按钮

def check_skipbtn():
    print('check skipbtn')
    try:
        # '跳过'按钮的定位
        skip_btn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no shipbtn')
    else:
        skip_btn.click()
        print('pass the skip-page')

#后面的滑动操作，需要注释掉这里
check_skipbtn()
