# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2019/7/18 2:54

import yaml
import os

yaml_config_path = os.path.join(os.path.dirname(__file__),'test1.yaml')

with open(yaml_config_path,'r',encoding='utf-8') as f:
    real_data = yaml.load(f,Loader=yaml.FullLoader)
    print(real_data)