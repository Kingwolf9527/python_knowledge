# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/30 23:32

import os
import yaml_usage

def get_account():

    #获取配置文件的路径
    current_path = os.path.dirname(__file__)

    # 获取yaml文件路径
    yaml_path = os.path.join(current_path,'account.yaml_usage')

    #读取配置信息
    with open(yaml_path,'r',encoding='utf-8') as f:
        account_config = f.read()    # 读出来是字符串
        dict_account = yaml_usage.load(account_config)  # 用load方法转字典
        useraccount = dict_account['account']
        userpassword = dict_account['password']
        return useraccount,userpassword
