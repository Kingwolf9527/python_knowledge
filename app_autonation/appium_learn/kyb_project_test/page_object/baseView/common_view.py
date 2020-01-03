# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/5 6:39

from appium_learn.kyb_project_test.page_object.baseView.base_view import BaseView
from appium_learn.kyb_project_test.utils.common_logs import Common_log
from appium_learn.kyb_project_test.utils.driver import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import csv

logger = Common_log(logger='commom_view').get_logger()

class Common_view(BaseView):

    skipbtn = (By.ID,'com.tal.kaoyan:id/tv_skip')

    def check_skipbtn(self):
        """
        检测是否存在跳过按钮
        :return:
        """
        logger.info('=================check skip_btn========================')
        try:
            # '跳过'按钮的定位
            skip_btn = self.driver.find_element(*self.skipbtn)
        except NoSuchElementException:
            logger.error('====================no shipbtn======================')
        else:
            skip_btn.click()
            logger.info('=====================pass the skip-page==================')

    def get_screensize(self):
        """
        获取屏幕尺寸
        :return:
        """
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']

        return x,y

    def swipe_left(self):
        """
        左滑操作
        :return:
        """
        logger.info('====================swipe left============================')
        left = self.get_screensize()
        x1 = int(left[0]*0.9)
        y1 = int(left[1]*0.5)
        x2 = int(left[0]*0.2)
        self.swipe(x1,y1,x2,y1,duration=1000)

    def swipe_up(self):
        """
        上滑操作
        :return:
        """
        logger.info('====================swipe up============================')
        up = self.get_screensize()
        x1 = int(up[0]*0.5)
        y1 = int(up[1]*0.9)
        y2 = int(up[1]*0.2)
        self.swipe(x1,y1,x1,y2,duration=500)

    def strftime(self):
        """
        格式化时间
        :return:
        """
        self.time_strf = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

        return self.time_strf

    def get_screenshot_image(self,moudle_file):
        """
        截图
        :param moudle:
        :return:
        """
        image_fun = self.strftime()
        image_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/screenshots_images/'
        #判断保存截图的文件夹是否存在
        isexists = os.path.exists(image_dir)
        if not isexists:
            try:
                os.makedirs(image_dir)
            except FileExistsError:
                logger.info('============================NO file========================')
        image_name = os.path.join(image_dir,'%s_%s.png' %(moudle_file,image_fun))

        logger.info('=============================get %s screenshots===============================' %moudle_file)
        self.driver.get_screenshot_as_file(image_name)


