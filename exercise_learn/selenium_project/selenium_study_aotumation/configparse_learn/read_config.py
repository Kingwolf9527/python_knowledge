# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/27 19:37

import configparser
import os


class Read_config(object):

    def __init__(self,filepath=None):
        if filepath:
            config_path = filepath
        else:
            # 配置文件的路径
            path = os.path.dirname(__file__)
            config_path = os.path.join(path,'config_local.ini')
        # 读取配置文件
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_db(self,parm):
        value = self.cf.get('db',parm)
        return value

if __name__ == '__main__':
    read_config = Read_config()
    port = read_config.get_db('db_port')
    print(port,type(port))

