# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/21 17:00

import os

def get_user_info():
    user_info = []
    file_path = os.path.dirname(__file__)
    path = file_path + '/config/account_info.txt'
    with open(path,'r',encoding='utf-8') as f:
        for data in f:
            user_dict = {}
            data = data.strip()
            result = data.split(',')
            for da in result:
                da = da.strip()
                account_data = da.split('=')
                #数据存储格式为字典，用嵌套列表的字典更新
                user_dict.update(dict([account_data]))
            user_info.append(user_dict)
    return user_info

if __name__ == '__main__':
    tt = get_user_info()
    for t in tt:
        print(t)
    print(tt)