# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/7/31 19:20

import os
import time
from selenium import webdriver



# 设置user-data-dir路径
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=F:\profile')
chromedriver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chromedriver.exe')
driver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver_path)

driver.get('https://www.12306.cn/index/')
driver.implicitly_wait(25)

#出发地和目的地
driver.find_element_by_id('fromStationText').clear()
driver.implicitly_wait(5)
driver.find_element_by_id('fromStationText').send_keys('上海')
driver.implicitly_wait(5)
driver.find_element_by_xpath('//div[@class="citylineover"]/span[1]').click()
time.sleep(5)

driver.find_element_by_id('toStationText').clear()
driver.implicitly_wait(5)
driver.find_element_by_id('toStationText').send_keys('深圳')
driver.implicitly_wait(5)
driver.find_element_by_xpath('//div[@class="citylineover"]/span[1]').click()
time.sleep(5)

#去掉readonly属性
js_readonly = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js_readonly)

#第一种方法输入日期
# driver.find_element_by_id('train_date').clear()
# driver.find_element_by_id('train_date').send_keys('2019-08-01')

#第二种，通过js的value赋值
date_js = 'document.getElementById("train_date").value="2019-08-01";'
driver.execute_script(date_js)
#点击其他地方，去掉下拉框
driver.find_element_by_id('search-input').click()
driver.implicitly_wait(5)

# #选择学生票
driver.find_element_by_id('isStudentDan').click()
driver.implicitly_wait(5)

#查询按钮
driver.find_element_by_id('search_one').click()

driver.implicitly_wait(20)
#确认查询是否正常
try:
    page_text = driver.find_element_by_xpath('//div[@class="quick-gif"]/a')
    driver.implicitly_wait(5)
    print(page_text.text)
    if page_text.text == '订票帮手':
        print('查询正常！')
    else:
        print('查询有误')
except Exception as e:
    print(e)
    print('No found element')
    driver.quit()