# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/19 3:59

from selenium import webdriver
import time
import os

"""
    
    处理confirm对话框

"""
options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=F:\profile')
chromedriver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'chromedriver.exe')
driver = webdriver.Chrome(chrome_options=options,executable_path=chromedriver_path)

driver.get(r'F:\GitExtensions_python\project_spider\exercise_learn\selenium\selenium_study_aotumation\alert_confirm_prompt\alert_confirm_prompt_test1.html')
driver.implicitly_wait(10)

# 获取confirm对话框的按钮，点击按钮，弹出confirm对话框
driver.find_element_by_id('confirm').click()
time.sleep(2)

# 获取confirm对话框
confirm = driver.switch_to.alert

# 获取对话框的内容
text = confirm.text
print(text)

# 点击“确认”按钮
confirm.accept()

# ## 点击“取消”按钮
# confirm.dismiss()

time.sleep(2)
driver.quit()