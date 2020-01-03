# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/3 3:02

import yaml_usage

with open('userinfo.yaml_usage','r') as f:
    data = yaml_usage.load(f)
    print(data)

    #打印男主的姓名，年龄和信息
    name_host = data['name']
    print(name_host)
    age_host = data['age']
    print(age_host)

    #读取配偶的姓名，年龄
    name_hostess = data['spouse']['name']
    print(name_hostess)
    age_hostess = data['spouse']['age']
    print(age_hostess)

    #分别读取两个孩子的姓名，年龄
    name_old_brother = data['children'][0]['name']
    print(name_old_brother)
    age_old_brother = data['children'][0]['age']
    print(age_old_brother)

    name_young_brother = data['children'][1]['name']
    print(name_young_brother)
    age_young_brother = data['children'][1]['age']
    print(age_young_brother)

    #注意：此处只是变量类型的数据变更，不会真正修改到yaml配置表中的数据
    data['name'] = 'kingwolf'
    print(data['name'])