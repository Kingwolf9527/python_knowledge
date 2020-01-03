# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/4 3:20

#隐性等待
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(20) # 隐性等待，最长等30秒
# driver.get('https://www.baidu.com')
# time.sleep(3)
# driver.quit()


#显性等待（WebDriverWait）
import time
from selenium import webdriver

#引进WebDriverWait类和expected_conditions(它的意思是：预期条件)类
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

try:
    element_id = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.ID, 'kw')))
    element_id.send_keys('python selenium')

    time.sleep(2)

finally:
    driver.close()
