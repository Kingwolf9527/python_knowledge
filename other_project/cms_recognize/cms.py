# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/16 5:38

import requests
import json

class Get_cms(object):

    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Referer': 'http://whatweb.bugscaner.com/look/',
            'Host' : 'whatweb.bugscaner.com'
        }
        self.url = 'http://whatweb.bugscaner.com/what/'

        self.post_data = {
            'url' : input('请输入需要检测的网站url：')
            # 'url' : 'http://www.hbsc.cn'
        }

    def get_cms(self):


        response = requests.post(self.url,data=self.post_data,headers=self.headers)

        #转化为字典处理
        text = response.json()
        # text = json.loads(response.text)

        """
            脚本语言,服务类型,前端语言都需要增加判断，因为有可能网站识别出来的内容没有这些字段,通过判断相关key值是否在字典对象的所有key值里面
        
        """
        if 'CMS' in text.keys():
            # 识别出来的CMS类型
            cms = text['CMS']
        else:
            cms = '无法识别'
        if 'Programming Languages' in text.keys():
            # 脚本语言
            Languages = text['Programming Languages'][0]
        else:
            Languages = '无法识别'

        if 'Web Servers' in text.keys():
            #服务类型
            Web_Servers = text['Web Servers'][0]
        else:
            Web_Servers = '无法识别'

        if 'JavaScript Frameworks' in text.keys():
            #前端语言
            JavaScript_Frameworks = text['JavaScript Frameworks'][0]
        else:
            JavaScript_Frameworks = '无法识别'

        CMS_details = {

            'cms' : cms,
            'language' : Languages,
            'server' : Web_Servers,
            'javascript_frameworks' : JavaScript_Frameworks

        }

        print(CMS_details)


if __name__ == '__main__':

    CMS = Get_cms()
    CMS.get_cms()