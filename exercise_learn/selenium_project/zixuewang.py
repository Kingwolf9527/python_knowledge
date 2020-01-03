# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/1 21:21

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

url = 'http://www.51zxw.net/login?redirect_url=http%3A%2F%2Fwww.51zxw.net%2F'

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=F:\profile')
driver = webdriver.Chrome(chrome_options=options)

driver.get(url)
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//div[@class="inputRow"]/input[@id="remberLogin"]')))

driver.find_element_by_name('loginStr').send_keys('kingwolf狼胸')
time.sleep(1)

driver.find_element_by_name('pwd').send_keys('922521dfxs')
time.sleep(1)

driver.find_element_by_xpath('//button[@class="btn radius size-L btn-danger"]').click()
time.sleep(0.5)

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//span[@id="news_login"]/div/a/font')))

if driver.current_url == 'http://www.51zxw.net/':
    print('登录成功！')