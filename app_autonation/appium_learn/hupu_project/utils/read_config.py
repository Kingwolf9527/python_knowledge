# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/6/5 20:18

import configparser
import os

class Read_config(object):

    def __init__(self,file):
        path = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(path,'config',file)
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path,encoding='utf-8')

    def get_selection(self,selection_name,parms):
        """
        :param selection_name:
        :param parms:
        :return:
        """
        value = self.cf.get(selection_name,parms)
        return value

if __name__ == '__main__':
    r = Read_config(file='hupu_app_config.ini')
    activity = r.get_selection('capability_app','appActivity')
    print(activity)