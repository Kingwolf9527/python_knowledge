# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/27 18:02

import requests
from lxml import html
import re
import os
from urllib import request


url = 'http://p.weather.com.cn/2018/12/3034732.shtml#p=1'

#获取当前目录路径
img_path_dir = os.path.join(os.path.dirname(__file__),'weather_img')
if  not os.path.exists(img_path_dir):
    os.mkdir(img_path_dir)

response = requests.get(url)
text = response.content.decode('utf-8')

html_pic = html.etree.HTML(text)

#获取所有缩列图的src
img_urls = html_pic.xpath('//div[@class="carousel carousel-navigation"]//li/img/@src')
for img_url in img_urls:
    #获取原图的url
    img_url = re.sub(r'_s','',img_url)
    #获取图片名称
    img_name = img_url.split('/')[-1]
    #拼接文件夹和文件
    img_path = os.path.join(img_path_dir, img_name)
    #下载图片
    request.urlretrieve(img_url,img_path)
