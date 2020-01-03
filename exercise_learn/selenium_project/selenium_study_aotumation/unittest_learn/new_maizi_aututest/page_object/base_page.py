# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/3 5:38


"""
    1.二次封装类，封装了 selenium 的一些常用方法。
    2.主要用于给页面类进行使用
"""

import time
import os
from new_maizi_aututest.utils.log import LogDetail
from selenium.common.exceptions import NoSuchElementException


# 引用自定义日志类
logger = LogDetail(logger='base_page').get_logger()

class BasePage(object):

    #初始化driver对象
    def __init__(self,driver):
        self.driver = driver

    #浏览器退出的方法
    def quit_browser(self):
        logger.info('Quit browser Now')
        self.driver.quit()

    #浏览器前进的方法
    def forword_browser(self):
        self.driver.forword()
        logger.info('Click forward on current page.')

    # 浏览器后退方法/返回的方法
    def back_browser(self):
        self.driver.back()
        logger.info('Click back on current page.')

    # 关闭当前浏览器窗口
    def close_browser(self):
        try:
            self.driver.close()
            logger.info('Close and quit the browser')
        except NoSuchElementException as e:
            logger.error('Failed to quit the browser with %s' %e)

    # 保存图片，截图
    def screenshot_imgs(self):
        # 1.创建保存截图文件目录
        path = os.path.dirname(os.path.dirname(__file__))
        img_path = path + '/screenshot_img/'
        # 2.判断文件夹是否存在，不存在则创建
        isEsists = os.path.exists(img_path)
        if not isEsists:
            try:
                os.makedirs(img_path)
            except FileExistsError as e:
                logger.error("Failed new bulid folder %s" %e)
        # 3.创建图片
        img_time = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))

        # 定义图片文件格式
        screenshot_img_name = img_path + img_time + '.png'
        try:
            self.driver.get_screenshot_as_file(screenshot_img_name)
            logger.info("Had take screenshot and save to folder : /screenshot_img")
        except NameError as e:
            logger.error('Failed to take screenshot! %s' %e)


    # find_element_**  元素定位方法  selector:元素位置

    def find_element(self,selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        # 创建一个空的元素对象
        element = ''
        if '=>' not in  selector:
            return self.driver.find_element_by_id(selector)
        #元素名称
        selector_name = selector.split('=>')[0]
        #元素属性值
        selector_value = selector.split('=>')[1]

        # 通过下面方法查到元素对象本身
        #id定位
        if selector_name == 'i' or selector_name == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element  %s:successful"
                            "by %s via value:%s" % (element.text, selector_name, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.screenshot_imgs()

        #name定位
        elif selector_name == 'n' or selector_name == 'name':
            try:
                element = self.driver.find_element_by_name(selector_value)
                logger.info("Had find the element  %s:successful"
                            "by %s via value:%s" % (element.text, selector_name, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.screenshot_imgs()

        #class_name定位
        elif selector_name == 'c' or selector_name == 'class_name':
            try:
                element = self.driver.find_element_by_class_name(selector_value)
                logger.info("Had find the element  %s:successful"
                            "by %s via value:%s" % (element.text, selector_name, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.screenshot_imgs()

        #tag_name定位
        elif selector_name == 't' or selector_name == 'tag_name':
            try:
                element = self.driver.find_element_by_tag_name(selector_value)
                logger.info("Had find the element  %s:successful"
                            "by %s via value:%s" % (element.text, selector_name, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.screenshot_imgs()

        #link_text定位
        elif selector_name == 't' or selector_name == 'link_text':
            try:
                element = self.driver.find_element_by_link_text(selector_value)
                logger.info("Had find the element  %s:successful"
                            "by %s via value:%s" % (element.text, selector_name, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.screenshot_imgs()

        #partial_link_text定位
        elif selector_name == 'p' or selector_name == 'partial_link_text':
            try:
                element = self.driver.find_element_by_partial_link_text(selector_value)
                logger.info("Had find the element  %s:successful"
                            "by %s via value:%s" % (element.text, selector_name, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.screenshot_imgs()

        #css定位
        elif selector_name == 'c' or selector_name == 'css_selector':
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                logger.info("Had find the element  %s:successful"
                            "by %s via value:%s" % (element.text, selector_name, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.screenshot_imgs()

        #xpath定位
        elif selector_name == 'x' or selector_name == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element  %s:successful"
                            "by %s via value:%s" % (element.text, selector_name, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.screenshot_imgs()
        else:
            logger.error("Please enter a valid type of targeting elements.")
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    #文本输入框
    def send_keys(self,selector,text):
        # 1.获取元素对象
        loc = self.find_element(selector)  # 调用元素定位，获取对象
        # 2.文本框操作
        try:
            loc.clear()
            loc.send_keys(text)
            logger.info('Had type  %s in inputBox' %text)
        except NameError as e:
            logger.error('Failed to type in input box')
            self.screenshot_imgs()

    # Text clear 文本框清空 selector:元素位置
    def clear(self,selector):
        loc = self.find_element(selector)
        try:
            loc.clear()
            logger.info("Clear text in input box before type")
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.screenshot_imgs()

    # Text click 点击事件 selector:元素位置
    def click(self, selector: object) -> object:
        loc = self.find_element(selector)
        try:
            loc.click()
            logger.info("The emement was click")  # 并不是每个元素都存在 text 属性
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.screenshot_imgs()

    # get_url_title 获取网页标题
    def get_title(self):
        title = self.driver.title
        logger.info("Current page title is %s" % title)
        return  title

    #执行js
    def script(self,src):
        self.driver.execute_script(src)

