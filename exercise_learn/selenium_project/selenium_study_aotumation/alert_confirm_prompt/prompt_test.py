# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/19 4:06

from selenium import webdriver
import time
import os

"""
    
    处理prompt对话框

"""
#案例1

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=F:\profile')
chromedriver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'chromedriver.exe')
driver = webdriver.Chrome(chrome_options=options,executable_path=chromedriver_path)

driver.get(r'F:\GitExtensions_python\project_spider\exercise_learn\selenium\selenium_study_aotumation\alert_confirm_prompt\alert_confirm_prompt_test1.html')
driver.implicitly_wait(10)
# 获取prompt对话框的按钮，点击按钮，弹出prompt对话框
driver.find_element_by_id('prompt').click()
time.sleep(1)

# 获取prompt对话框
prompt = driver.switch_to.alert

# 获取对话框内容
text = prompt.text
print(text)

# 在弹框内输入信息
prompt.send_keys('狼胸最牛逼！')
# 点击“确认”按钮，提交输入的内容
prompt.accept()

time.sleep(2)
driver.quit()
