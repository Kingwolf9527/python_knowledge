# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/3/1 2:39

import logging
import os
import time


"""
自定义日记文件

1.创建logger
2.创建handler,可以有多个handler
3.定义formatter,给handler添加formatter
4.给logger添加handler

"""

class LogDetail(object):

    #定义logger对象的名称
    def get_logger(self):
        return self.logger

    #初始化加载，传递logger对象
    def __init__(self,logger):

        #1.创建logger对象
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        #2.创建一个handler，用于写入日记文件
        file_time = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
        log_path = os.path.dirname(os.path.dirname(__file__)) + '/log/'
        #判断日记目录是否存在，不存在就重新创建
        dir_exists = os.path.exists(log_path)
        if not  dir_exists:
            try:
                os.makedirs(log_path)   #注意这里是创建多层目录
            except FileNotFoundError as e:
                print('not file')
        #完整的log名称
        log_name = log_path + file_time + '.log'

        #创建日记文件,
        file_handler = logging.FileHandler(log_name,encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        #3.创建一个handler，用于输入控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        #4.定义log输出格式
        log_type = '%(asctime)s -- %(name)s  --%(filename)s -- %(levelname)s -- %(message)s'
        formatter = logging.Formatter(log_type)
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        #5.给logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)