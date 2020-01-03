# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/11/20 4:48

import configparser
import os
from util.common_log import Common_Logs

#实例化logger
log_name = Common_Logs(logger='common_config')
logger = log_name.get_logger()

class Read_Config(object):

    def __init__(self,filename=None):

        self.cf = configparser.ConfigParser()

        if filename == None:
            filename_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'config')
            filename = os.path.join(filename_dir,"register_element.ini")

        else:
            filename = filename

        self.cf.read(filename,encoding='utf-8')

    def get_value(self,selection,key):
        """
        读取相应的selection配置文件
        :param selection:   配置文件的selection
        :param value:       对应selection的key值
        :return:
        """
        result = self.cf.get(selection,key)
        return result


if __name__ == '__main__':

    test = Read_Config().get_value(selection='RegisterElement',key='user_nickname')
    print(test)