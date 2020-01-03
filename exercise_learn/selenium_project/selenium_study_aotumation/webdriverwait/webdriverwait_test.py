# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/19 2:25

from selenium import webdriver
import time

#引进WebDriverWait类和expected_conditions类
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=F:\profile')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.baidu.com')
element_id = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.ID, 'kw')))

element_id.send_keys('python selenium')
time.sleep(2)
driver.close()