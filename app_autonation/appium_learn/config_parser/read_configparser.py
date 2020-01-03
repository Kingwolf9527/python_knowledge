# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/3 18:42

import configparser
import os

class Config_paser(object):

    def __init__(self):

        path = os.path.dirname(__file__)
        #配置文件的路径
        file_path = os.path.join(path,'android_9_config.ini')
        #读取配置文件
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path)


    def get_selectoin(self,selection_name,key_parm):
        """
        :param selection_name:
        :param key_parm:
        :return:
        """
        value = self.cf.get(selection_name,key_parm)
        return value


if __name__ == '__main__':
    con = Config_paser()
    device_name = con.get_selectoin('capability','deviceName')
    print(device_name,type(device_name))




