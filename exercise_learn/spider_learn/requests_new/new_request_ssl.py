# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/19 2:43

import requests

# 证书验证(前提条件是：该网站的协议是https，而且不信任网站证书才行)

# 不加verify=False这个关键字参数的话会出现验证错误问题，因为这个网站的协议不被信任
response = requests.get('https://www.12306.cn', verify=False)
print(response.text)