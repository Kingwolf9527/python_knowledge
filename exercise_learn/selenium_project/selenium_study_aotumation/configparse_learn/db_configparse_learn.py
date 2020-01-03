# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/27 19:23

import configparser
import os

#配置文件的路径
path = os.path.dirname(__file__)
config_path = os.path.join(path,'config_local.ini')

#读取配置文件
cf = configparser.ConfigParser()
cf.read(config_path)

#读取配置文件中，所有的selections，列表形式，也就是所有的配置，例如：数据库，邮箱等等
select = cf.sections()

#获取某个section名为db所对应的所有键
options = cf.options('db')

## 获取section名为db所对应的全部键值对
item = cf.items('db')

#获取[db]中db_name对应的值
name = cf.get('db','db_name')
print(name)

