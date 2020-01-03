# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/24 22:03

from appium_learn.capability_simple import driver,NoSuchElementException
import random
from selenium.webdriver.support.wait import WebDriverWait
import os

#register_button
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
driver.implicitly_wait(8)

#select imgage
# images = driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.tal.kaoyan:id/iv_picture")')
images = driver.find_elements_by_id('com.tal.kaoyan:id/iv_picture')
images[1].click()
driver.implicitly_wait(2)

#click finish
driver.find_element_by_id('com.tal.kaoyan:id/picture_tv_ok').click()

#varity finish
driver.find_element_by_id('com.tal.kaoyan:id/menu_crop').click()

#account-info
username = 'kingwolf' + str(random.randint(1000,9000))
print('username is : %s' %username)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)

#password-info
password = 'abc' + str(random.randint(2000,8000))
print('password is : %s' %password)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)

#email-info
email = 'king' + str(random.randint(100,900)) + '@163.com'
print('email is : %s' %email)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)

#register-button
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
driver.implicitly_wait(5)

#select target major
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
majors = driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')
#select economics
majors[1].click()

#major details
details = driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')
#select statistics
details[2].click()

#select managemenet statistics
select_majors = driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')
select_majors[2].click()

#select target school
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_school').click()
driver.implicitly_wait(5)

#add shcool:弹出框处理，跟其他的定位不一样
os.system('adb shell input tap 190 1810')
# WebDriverWait(driver,10,0.1).until(lambda x:x.find_element_by_id('com.tal.kaoyan:id/home_add_school_addimg'))
# driver.find_element_by_id('com.tal.kaoyan:id/home_add_school_addimg').click()

# main_ele = driver.find_element_by_id('com.tal.kaoyan:id/activity_myinfo_school_draggridview')
# main_ele.find_element_by_class_name('android.widget.ImageView').click()


#select province
provinces = driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')
#select beijing
provinces[0].click()

#select schools
schools = driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')
#select BIT
schools[5].click()
driver.implicitly_wait(3)

# #varity select
# driver.find_element_by_id('com.tal.kaoyan:id/activity_myinfo_addschool_commit').click()
# driver.find_element_by_xpath('//android.widget.TextView[@text="确定"]').click()
os.system('adb shell input tap 994 1564')
driver.implicitly_wait(2)

#login button
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()

