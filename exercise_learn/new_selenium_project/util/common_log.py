# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/12/6 3:01

import logging
import os
import time


class Common_Logs(object):

    def __init__(self,logger):

        """
        1.获取logger对象
        2.创建handle，包括控制台handle以及保存文件handle
        3.为logger对象添加handle
        4.设置日记输出格式
        5.为handle设置格式
        :param logger: 区分不同模块的logger对象
        """

        #获取logger对象
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)


        #创建handle，包括控制台handle以及保存文件handle
        self.console_handle = logging.StreamHandler()
        self.console_handle.setLevel(logging.INFO)

        #设置file_handle的文件命名格式
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'logs')
        log_prefix = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time())) + '.log'
        log_name = os.path.join(log_dir,log_prefix)
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)

        #为logger对象添加handle
        self.logger.addHandler(self.console_handle)
        self.logger.addHandler(self.file_handle)

        #设置日记输出格式
        format_stype = '%(asctime)s --- %(filename)s --- %(funcName)s ---  %(lineno)d --- %(levelname)s --- %(message)s'
        formatter = logging.Formatter(format_stype)

        #为handle设置格式
        self.console_handle.setFormatter(formatter)
        self.file_handle.setFormatter(formatter)

    def get_logger(self):

        """
        获取logger对象
        :return:
        """

        return self.logger


    def close_log(self):

        """
        关闭handle以及logger对象，减少内存io，提升性能
        :return:
        """

        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()



if __name__ == '__main__':

    test_log = Common_Logs()
    test = test_log.get_logger()

    test.info('next test')

    test_log.close_log()



