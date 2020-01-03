# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/15 1:56

'''

    通过JavaScript设置浏览器窗口的滚动条的位置.用window.scrollTo(100,450)，100代表左间距，450代表上间距，然后用execute_script()函数执行

'''

'''
    元素等待：重点是显氏等待

'''

'''
    窗口的截图功能

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

#设置窗口的大小
# driver.maximize_window()
driver.set_window_size(700,700)

#搜索框以及内容(通过设置显氏等待和休眠时间两种方式)
# element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'kw')))
# element.send_keys('selenium2')
#
# element2 = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
# element2.click()
driver.find_element_by_id('kw').send_keys('selenium2')
time.sleep(2)
driver.find_element_by_id('su').click()
time.sleep(2)


#通过JavaScript设置浏览器窗口的滚动条的位置
js ="window.scrollTo(100,450);"
driver.execute_script(js)
time.sleep(5)

#窗口截图
driver.get_screenshot_as_file(r'F:\baidu.jpg')

driver.quit()
