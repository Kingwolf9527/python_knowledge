# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/6/5 21:49

import time
import os
from hupu_project.page_object.base_view.baseview import Baseview
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Comment_view(Baseview):


    def get_size(self):
        """
        获取屏幕尺寸
        :return:
        """
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']

        return x,y

    def swipe_left(self,duration):
        """
        左滑操作
        :return:
        """
        left = self.get_size()
        x1 = int(left[0]*0.9)
        y1 = int(left[1]*0.5)
        x2 = int(left[0]*0.2)
        self.swipe(x1,y1,x2,y1,duration)

    def swipr_up(self,duration):
        """
        上滑操作
        :return:
        """
        up = self.get_size()
        x1 = int(up[0]*0.5)
        y1 = int(up[1]*0.9)
        y2 = int(up[1]*0.2)
        self.swipe(x1,y1,x1,y2,duration)

    def strftime(self):
        """
        格式化时间
        :return:
        """
        self.strf_time = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))

        return self.strf_time

    def screenshot_image(self,moudle_name):
        """
        截图函数
        :param moudle:
        :return:
        """
        image_strf = self.strftime()
        dir_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/screenshot/'
        #判断保存截图的文件夹是否存在
        isexists = os.path.exists(dir_path)
        if not isexists:
            try:
                os.makedirs(isexists)
            except FileExistsError as e:
                print(e)
        #截图文件的命名
        image_name = os.path.join(dir_path,'%s_%s.png' % (moudle_name,image_strf))

        #保存截图
        self.driver.get_screenshot_as_file(image_name)