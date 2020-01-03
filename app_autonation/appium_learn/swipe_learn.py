# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/31 6:24

from appium_learn.capability_simple import driver
import time


#获取页面的宽高
def get_size():

    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

size = get_size()
print(size)

#向左滑动，Y轴不变，X轴由大到小
def swipe_left():
    left_size = get_size()
    #设置起始的X轴和Y轴,left_size返回的是一个元祖，第一个参数是X轴的，第二个参数是Y轴的
    x1 = int(left_size[0]*0.9)
    y1 = int(left_size[1]*0.5)
    x2 = int(left_size[0]*0.2)
    #调用滑动方法
    driver.swipe(x1,y1,x2,y1,1000)

#向左滑动三次
for i in range(2):
    swipe_left()
    time.sleep(0.5)

#最后点击立即体验按钮，进入登录页面
driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()