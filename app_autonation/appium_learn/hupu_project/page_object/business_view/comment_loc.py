# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/6/5 22:58

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from hupu_project.page_object.base_view.common_view import Comment_view
from hupu_project.utils.driver import Driver
from selenium.common.exceptions import NoSuchElementException
import time
import pysnooper

class Comment_loc(Comment_view):

    #初始化，相关权限的处理
    permission_loc = (By.ID, 'android:id/button1')
    uiautomator_loc1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("允许")')
    uiautomator_loc2 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确定")')
    uiautomator_loc3 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("始终允许")')

    #版本更新提示处理(点击"忽略")
    ignore_loc = (By.ID,'com.hupu.games:id/lef_btn')

    #社区元素
    bbs = (By.ID,'com.hupu.games:id/btn_bbs')

    #话题元素
    topic = (By.ID,'com.hupu.games:id/txt_name')

    #话题名字(list定位)
    topic_name = (By.ID,'com.hupu.games:id/tv_topic_name')

    #最新回复的元素(list定位，取值第一个)
    recent_comment = (By.ID,'com.hupu.games:id/txt_name')


    #帖子的标题(list定位)
    title = (By.ID,'com.hupu.games:id/tv_title')


    def permission(self):
        """
        初始化权限，默认全部允许
        """
        try:
            eles = self.driver.find_elements(*self.permission_loc)
            while True:
                for ele in eles:
                    if ele.text == u'允许':
                        self.driver.find_element(*self.uiautomator_loc1).click()
                    elif ele.text == u'确定':
                        self.driver.find_element(*self.uiautomator_loc2).click()
                    elif ele.text == u'始终允许':
                        self.driver.find_element(*self.uiautomator_loc3).click()
        except:
            pass

    def update(self):
        """
        判断是否有升级弹窗，点击取消
        :return:
        """
        # 判断是否存在版本更新，点击"忽略"
        try:
            ignore_ele = self.driver.find_element(*self.ignore_loc)
            time.sleep(1)
            ignore_ele.click()
            print('ignore update version')
        except:
            pass

    def click_bbs(self):
        """
        选择"社区"
        :return:
        """
        #先执行权限判断
        self.permission()

        time.sleep(5)

        #判断是否存在版本更新，点击"忽略"
        self.update()

        time.sleep(3)

        #点击社区
        try:
            ele = self.driver.find_element(*self.bbs)
        except NoSuchElementException:
            pass
        else:
            time.sleep(2)
            ele.click()
            print('进入社区')
            return True

    def click_topic(self):
        """
        选择"话题"
        :return:
        """
        if self.click_bbs():
            try:
                eles = self.driver.find_elements(*self.topic)
            except NoSuchElementException:
                pass
            else:
                time.sleep(2)
                eles[1].click()
                print('进入话题')
                return True

    def click_topic_name(self):
        """
        选择"步行街主干道"
        :return:
        """
        if self.click_topic():
            try:
                eles = self.driver.find_elements(*self.topic_name)
            except NoSuchElementException:
                pass
            else:
                time.sleep(2)
                eles[0].click()
                print('进入步行街主干道')
                return True

    def click_recent_comment(self):
        """
        进入最新回复页面,取值第一个
        :return:
        """
        if self.click_topic_name():
            try:
                eles = self.driver.find_elements(*self.recent_comment)
            except NoSuchElementException:
                pass
            else:
                time.sleep(2)
                eles[0].click()
                print('进入"最新回复"页面')
                return True



    @pysnooper.snoop(output='../../app_log/snoop_test1.log',prefix='--*--')
    def click_topic_title(self):
        """
        浏览所有帖子
        :return:
        """
        if self.click_recent_comment():
            try:
                self.driver.implicitly_wait(10)
                eles = self.driver.find_elements(*self.title)
                print(len(eles))
                print(eles)
                time.sleep(2)
                for i in range(len(eles)):
                    eles[i].click()
                    time.sleep(2)
                    #上滑操作，页面滚动到底部rrrr
                    self.swipr_up(duration=10000)
                    #返回上一层
                    self.driver.back()

            except NoSuchElementException as e:
                print('Error is : %s' %e)
                print('没有找到帖子')



if __name__ == '__main__':

    driver = Driver().read_caps()
    c_loc = Comment_loc(driver)
    c_loc.click_topic_title()
