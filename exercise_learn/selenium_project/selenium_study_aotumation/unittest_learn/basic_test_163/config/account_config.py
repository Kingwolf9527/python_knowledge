# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/1/30 23:32

import os
import yaml_usage

def get_account_info():

    #获取配置文件的路径
    current_path = os.path.dirname(__file__)

    # 获取yaml文件路径
    yaml_path = os.path.join(current_path,'account.yaml_usage').replace('\\','/')

    accounts = []
    passwprds = []

    #读取配置信息
    with open(yaml_path,'r',encoding='utf-8') as f:
        account_config = f.read()
        dict_accounts = yaml_usage.load(account_config)
        for dict_account in dict_accounts:
            useraccount = dict_account['account']
            userpassword = dict_account['password']
            accounts.append(useraccount)
            passwprds.append(userpassword)
            print(accounts)
            print(passwprds)
        return accounts,passwprds

if __name__ == '__main__':
    get_account_info()