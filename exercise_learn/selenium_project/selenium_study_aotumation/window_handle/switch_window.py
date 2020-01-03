# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/18 23:38

from selenium import webdriver
import time
import os


"""
    case:多窗口切换---在百度学术首页，点击注册按钮，进入注册页面，然后返回学术搜索页面，输入关键词搜索

"""

#设置好user-date-dir的路径
options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=F:\profile')

#设置驱动对象
chromedriver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'chromedriver.exe')
driver = webdriver.Chrome(chrome_options=options,executable_path=chromedriver_path)

#百度学术首页
driver.get('http://xueshu.baidu.com/')
#先获取首页的句柄
current_handle = driver.current_window_handle
print(current_handle)

time.sleep(3)

#点击注册，进入注册页面
driver.find_element_by_link_text('注册').click()

#获取所有窗口的句柄
handles = driver.window_handles
print(handles)

#判断当前页面的句柄是否等于首页的句柄，如果不是就切换驱动和窗口到新页面，就是注册页面
for handle in handles:
    if handle != current_handle:
        driver.switch_to.window(handle)
        time.sleep(2)
        #判断是否真正进入注册页面
        keyword = driver.find_element_by_xpath('//div[@id="login_link"]/span').text
        if keyword == '我已注册，现在就':
            print('欢迎进入百度学术注册页面！')
        time.sleep(1.5)

for handle in handles:
    if handle == current_handle:
        #切换回首页，搜索关键字
        driver.switch_to.window(current_handle)
        print('欢迎回到学术首页！')
        #定位输入框和点击按钮
        driver.find_element_by_id('kw').send_keys('渗透测试')
        driver.find_element_by_id('su').click()
        time.sleep(1.5)

        #搜索后面的页面url是：http://xueshu.baidu.com/s?wd=%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95&rsv_bp=0&tn=SE_baiduxueshu_c1gjeupa&rsv_spt=3&ie=utf-8&f=8&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D
        search_url = 'http://xueshu.baidu.com/s?wd=%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95&rsv_bp=0&tn=SE_baiduxueshu_c1gjeupa&rsv_spt=3&ie=utf-8&f=8&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D'
        if driver.current_url == search_url:
            print('搜索结果页面完成！')

driver.quit()

# 结果是：
# CDwindow-4CB752150657F04F79F3C7DFCFDD60B6
# ['CDwindow-4CB752150657F04F79F3C7DFCFDD60B6', 'CDwindow-2285B07E9BF5F9F82E55840961273895']
# 欢迎进入百度学术注册页面！
# 搜索结果页面完成！