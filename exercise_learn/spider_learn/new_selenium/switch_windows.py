# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/5 22:33

"""
    虽然在窗口中切到了新的页面，但是driver还是没有切换
    如果想要在代码中切换到新的页面，并且做一下爬虫
    那么应该使用driver.switch_to_window来切换到指定的窗口
    从driver.window_handles中取出具体第几个窗口
    driver.window_handles是一个列表，里面装的全是窗口句柄
    它会按照打开页面的顺序来存储窗口的句柄

"""

from selenium import webdriver
import time

#本地定义一个profile文件夹，再通过ChromeOptions定义，再使用add_argument方法，指定'user-data-dir'的路径为我们创建的profile文件夹路径，最后再Chrome方法里面调用chrome_options就可以了
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=F:\profile")

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.baidu.com')

#获得当前窗口的句柄
first_handle = driver.current_window_handle
print(first_handle)

#进去百度页面后，此时，再打开另外一个窗口，进入freebuf页面，利用JS的语法window.open('+url')
driver.execute_script("window.open('https://www.freebuf.com')")

#获取所有窗口的句柄
handles = driver.window_handles
print(handles)
# print(driver.current_url)        #发现当前驱动的url还是第一个窗口的百度   https://www.baidu.com/

# #因此，需要切换句柄到新窗口的页面，才能把驱动也同时切换到新窗口，最终才能在新窗口用驱动来定位相关操作，使用方法是：
# driver.switch_to_window(driver.window_handles[1])
# print(driver.current_window_handle)
# print(driver.current_url)

#循环判断窗口是否为当前窗口
for handle in handles:
    if handle != first_handle:
        #需要切换句柄到新窗口的页面，才能把驱动也同时切换到新窗口，最终才能在新窗口用驱动来定位相关操作
        driver.switch_to_window(handle)
        print('欢迎来到安全交流基地freefbuf')
        time.sleep(3)
        testname = driver.find_element_by_xpath('//li[@class="icon-contribute"]//span').text
        if testname == '投稿':
            print('安全渗透，未来光明')
        time.sleep(3)
        driver.close()

#返回原先到的窗口
driver.switch_to_window(first_handle)
driver.find_element_by_id('kw').send_keys('安全渗透')
time.sleep(3)
driver.quit()






