# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/2/21 5:38

import os

def get_loc_info():
    loc_info = {}
    file_path = os.path.dirname(__file__)
    path = file_path + '/config/loc_info.txt'
    with open(path,'r',encoding='utf-8') as f:
        for data in f:
            data = data.strip()
            result = data.split('=')
            #数据存储格式为字典，用嵌套列表的字典更新
            loc_info.update(dict([result]))
    return loc_info

if __name__ == '__main__':
    info = get_loc_info()
    for key in info:
        print(key,info[key])