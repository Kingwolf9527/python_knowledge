# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/9/15 3:23
'''
    通过JavaScript调用html5的使用

'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://videojs.com/')

#定位视频文件
video = driver.find_element_by_xpath('//*[@id="preview-player_html5_api"]')

#返回播放文件的地址
url = driver.execute_script("return arguments[0].currentSrc;",video)
print(url)

#播放视频
print("start")
driver.execute_script("return arguments[0].play()",video)

#播放15秒
time.sleep(15)

#暂停视频
print("stop")
driver.execute_script("arguments[0].pause()",video)

