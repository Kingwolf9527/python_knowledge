# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/4/3 3:34

import yaml_usage

slogan=['welcome','to','51zxw']
website={'url':'www.51zxw.net'}

#将python数据类型转化为yaml数据类型
data_list = yaml_usage.dump(slogan)
print(data_list)
#结果是：[welcome, to, 51zxw]

data_dict = yaml_usage.dump(website)
print(data_dict)
#结果是：{url: www.51zxw.net}
