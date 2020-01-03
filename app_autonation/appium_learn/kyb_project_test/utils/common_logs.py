# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/5 6:10

import os
import logging
import time

class Common_log(object):


    #初始化加载，传递logger对象
    def __init__(self,logger):
        #1.创建logger对象
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        #2.创建handler，写入日记文件
        time_format = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
        log_path = os.path.dirname(os.path.dirname(__file__)) + '/app_logs/'
        #判断日记文件所在的文件夹是否存在
        isexists_dir = os.path.exists(log_path)
        if not isexists_dir:
            try:
                os.makedirs(log_path)
            except FileExistsError as e:
                print('No file')

        #定义日记文件的名称
        log_name = log_path + time_format + '.log'

        #创建handler的磁盘文件存储日记
        file_handler = logging.FileHandler(log_name,encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        #创建控制台handler，把log打印到控制台上，方便调试
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        #3.格式化日记的输出内容
        format_type = '%(asctime)s --- %(filename)s --- %(name)s --- %(levelname)s --- %(message)s ---'
        formatter = logging.Formatter(format_type)

        #为所有的handler格式化日记输出内容
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        #4.为logger对象添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    # 定义log对象的名称
    def get_logger(self):
        return self.logger




