# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/19 3:38

"""
    处理alert弹窗

"""

from selenium import webdriver
import time
import os

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=F:\profile')
chromedriver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'chromedriver.exe')
driver = webdriver.Chrome(chrome_options=options,executable_path=chromedriver_path)

driver.get(r'F:\GitExtensions_python\project_spider\exercise_learn\selenium\selenium_study_aotumation\alert_confirm_prompt\alert_confirm_prompt_test1.html')
driver.implicitly_wait(10)

# 获取alert对话框的按钮，点击按钮，弹出alert对话框
driver.find_element_by_id('alert').click()
time.sleep(1)

# 获取alert对话框
alert = driver.switch_to.alert

# 获取对话框内容
text = alert.text
print(text)
time.sleep(2)

# alert对话框属于警告对话框，我们这里只能接受弹窗
alert.accept()
time.sleep(2)
driver.quit()