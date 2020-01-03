# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/21 1:18

from appium_learn.capability_simple import driver,NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

'''

    1.常规定位
    2.uiautomator定位
        a.resourceId定位
        b.text定位
        c.className定位
        d.用法：new UiSelector().resourceId()/text()/className()

'''

#正常的登录页面(首次登录的场景)
def login():
    # account element:常规定位
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    # driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('kingwolfbook14')

    #uiautomator定位
    #new UiSelector().resourceId()定位
    # driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('kingwolfbook14')
    #new UiSelector().text()定位
    # driver.find_element_by_android_uiautomator('new UiSelector().text("请输入用户名")').send_keys('kingwolfbook14')
    #new UiSelector().className()定位
    driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.EditText")').send_keys('kingwolfbook14')

    # password element
    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('922521dfxs')
    # login_button element
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

#非首次登录的用户场景
try:
    driver.find_element_by_id('com.tal.kaoyan:id/mainacvitity_button_myself')
    # WebDriverWait(driver,10).until(lambda x:x.find_element_by_id('com.tal.kaoyan:id/mainacvitity_button_myself'))
except NoSuchElementException:
    login()
else:
    driver.find_element_by_id('com.tal.kaoyan:id/mainacvitity_button_myself').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
    login()
