# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/6 3:19

from selenium import webdriver
import time

#本地定义一个profile文件夹，再通过ChromeOptions定义，再使用add_argument方法，指定'user-data-dir'的路径为我们创建的profile文件夹路径，最后再Chrome方法里面调用chrome_options就可以了

#设置代理ip，就是再使用add_argument方法，添加一个代理ip，指定'--proxy-server=完整的代理ip'
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=F:\profile")

options.add_argument('--proxy-server=http://59.57.151.126:31689')

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://httpbin.org/ip')