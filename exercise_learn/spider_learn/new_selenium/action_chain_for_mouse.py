# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/4 2:32

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time



driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

#定位到百度输入框的位置以及按钮的位置
input_tag = driver.find_element_by_id('kw')
sumit_but = driver.find_element_by_id('su')

#这里采用分步氏的方法

#定义行为链action_chains
action_chains = ActionChains(driver)

#移动元素
action_chains.move_to_element(input_tag)

#发送某个键到指定元素
action_chains.send_keys_to_element(input_tag,'python')

#再移动到按钮
action_chains.move_to_element(sumit_but)

#点击按钮
action_chains.click()

#最后全部执行perform()(ActionChains都会按照顺序执行所有的操作)
action_chains.perform()


#链式的方法(ActionChains都会按照顺序执行所有的操作)

ActionChains(driver).move_to_element(input_tag).send_keys_to_element(input_tag,'python').move_to_element(sumit_but).click().perform()
