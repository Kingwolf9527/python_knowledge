# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/30 4:58

from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver


# 配置capability信息
desired_capability = {}
# 操作系统
desired_capability['platformName'] = 'Android'
# 操作系统的版本
desired_capability['platformVersion'] = '7.1.1'
# 设备名称
desired_capability['deviceName'] = 'kingwolf'
# 设备的udid(通过adb devices获取的)
desired_capability['udid'] = '127.0.0.1:62025'
# 需要调用的app包名
desired_capability['appPackage'] = 'com.wondershare.drfone'
#设置超时时间
desired_capability['newCommandTimeout'] = '3000'
# 需要调用的app的launcher-activity
desired_capability['appActivity'] = 'com.wondershare.drfone.ui.activity.WelcomeActivity'


# 保持回话,这个参数比较重要，决定是否重置会话
desired_capability['noReset'] = 'true'

# 安装app
desired_capability['app'] = r'D:\appium_apk_test\dr.fone3.2.0.apk'

#指定Chromedriver路径
# desired_capability['chromedriverExecutable'] = r'C:\Users\KingWolf\AppData\Roaming\npm\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win\chromedriver.exe'

# 建立连接
driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_capability)
driver.implicitly_wait(8)

#定位backup元素
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

#显式等待，因为scan过程需要一定的时间,直到下一页的按钮出现
WebDriverWait(driver,12).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

driver.implicitly_wait(10)
#跳转到webview的页面也需要等待一下,直到wenview出现
# WebDriverWait(driver,10).until(lambda x:x.find_element_by_class_name('android.webkit.WebView'))

#吧contexts打印出来
contexts = driver.contexts
print(contexts)

#切换context到h5上
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')

#在web页面进行selenium元素定位
#发送邮箱
driver.find_element_by_id('email').send_keys('lccr777@163.com')
#点击按钮
driver.find_element_by_class_name('btn_send active').click()
print('send email success！')

