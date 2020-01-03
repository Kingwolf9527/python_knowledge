# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/20 5:09

import time
import os
from selenium.common.exceptions import NoSuchElementException
from util.read_config import Read_Config
from util.common_log import Common_Logs

#实例化logger
log_name = Common_Logs(logger='base_view')
logger = log_name.get_logger()


class Elemnet(object):

    def __init__(self,driver):

        self.driver = driver
        self.rc = Read_Config()


    def ele_processing(self,selection,key):

        """
        读取配置信息
        :param selection:     配置文件所需要读取的selection
        :param key:           对应selection的key值
        :return:
        """
        result =  self.rc.get_value(selection,key)
        #定位方式
        by = result.split('>>>')[0]
        #定位的值
        value = result.split('>>>')[1]
        try:
            #声明ele全局变量
            global ele

            if by == 'id':
                try:
                    ele = self.driver.find_element_by_id(value)
                    logger.info('------ the element is: %s    ------' %ele)
                except NoSuchElementException as e:
                    logger.info("NoSuchElementException:%s" % e)
            elif by == 'name':
                try:
                    ele = self.driver.find_element_by_name(value)
                    logger.info('------ the element is: %s    ------' %ele)
                except NoSuchElementException as e:
                    logger.info("NoSuchElementException:%s" % e)
            elif by == 'tag_name':
                try:
                    ele = self.driver.find_element_by_tag_name(value)
                    logger.info('------ the element is: %s    ------' %ele)
                except NoSuchElementException as e:
                    logger.info("NoSuchElementException:%s" % e)
            elif by == 'class_name':
                try:
                    ele = self.driver.find_element_by_class_name(value)
                    logger.info('------ the element is: %s    ------' %ele)
                except NoSuchElementException as e:
                    logger.info("NoSuchElementException:%s" % e)
            elif by == 'link_text':
                try:
                    ele = self.driver.find_element_by_link_text(value)
                    logger.info('------ the element is: %s    ------' %ele)
                except NoSuchElementException as e:
                    logger.info("NoSuchElementException:%s" % e)
            elif by == 'partial_link_text':
                try:
                    ele = self.driver.find_element_by_partial_link_text(value)
                    logger.info('------ the element is: %s    ------' %ele)
                except NoSuchElementException as e:
                    logger.info("NoSuchElementException:%s" % e)
            else:
                try:
                    ele = self.driver.find_element_by_xpath(value)
                    logger.info('------ the element is: %s    ------' %ele)
                except NoSuchElementException as e:
                    logger.info("NoSuchElementException:%s" % e)


        except  NoSuchElementException:
            logger.info('Please enter a valid type of targeting elements.')
            raise NameError("Please enter a valid type of targeting elements.")

        return ele

    def element_send_keys(self,selection,key,value,clear_first=True):

        """
        发送数据
        :param selection:      配置文件所需要读取的selection
        :param key:            对应selection的key值
        :param value:          发送的值
        :param clear_first:    默认是先清除信息，再输入
        :return:
        """
        loc = self.ele_processing(selection,key)
        try:
            #发送数据
            if clear_first:
                #先清除信息，防止出错
                loc.clear()
            loc.send_keys(value)
        except AttributeError:
            logger.error('------  页面未找到:    %s  元素      ------' %loc)


    def clicl_element(self,selection,key):

        """
        点击按钮
        :param selection:
        :param key:
        :return:
        """
        loc = self.ele_processing(selection,key)
        try:
            #点击按钮
            loc.click()
        except AttributeError:
            logger.error('------  页面未找到:    %s  元素      ------' %loc)

    def switch_iframe(self,selection,key):

        """
        切换iframe表单（一般站点的iframe的id或者name都是动态变化的，最好采用xpath定位到iframe的层次）
        :param selection:
        :param key:
        :return:
        """
        loc = self.ele_processing(selection,key)
        try:
            #切换iframe表单
            self.driver.switch_to.frame(loc)
        except AttributeError:
            logger.error('------  页面未找到:    %s  元素      ------' %loc)

        finally:
            #退出iframe表单，回到top层(看情况是否做这一步)
            self.driver.switch_to.default_content()

    def execute_js(self,selection,key):

        """
        执行js脚本
        :param selection:
        :param key:
        :return:
        """
        js_loc = self.rc.get_value(selection,key)
        try:
            #执行js脚本
            self.driver.execute_script(js_loc)
        except AttributeError:
            logger.error('------  页面未找到:    %s  元素      ------' %js_loc)

    def get_current_url(self):

        """
        获取当前页面的url
        :return:
        """

        return self.driver.current_url


    def get_title(self):

        """
        获取当前页面的标题
        :return:
        """

        return self.driver.title

    def get_screenshot_image(self, moudle_file):

        """
        截图方法
        :param moudle_file: 用来表示哪个出现问题的
        :return:
        """
        #设置图片命名格式
        name_format = time.strftime('%Y:%m:%d %H_%M_%S',time.localtime(time.time()))
        image_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/images/'
        #判断截图文件夹是否存在
        isexists = os.path.exists(image_dir)
        if not isexists:
            try:
                os.makedirs(image_dir)
            except FileExistsError:
                logger.info('------  No file   ------')

        #拼接截图文件名
        image_name = os.path.join(image_dir,'%s___%s.png' %(moudle_file,name_format))

        logger.info('=============================get %s screenshots===============================' %moudle_file)
        #调用截图函数
        self.driver.get_screenshot_as_file(image_name)
