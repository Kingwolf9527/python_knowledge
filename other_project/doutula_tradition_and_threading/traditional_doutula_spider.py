# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/29 23:36

import requests
from lxml import html
import re
import os
from urllib import request


def parse_page(url):

    headers = {

        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host' : 'www.doutula.com'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html_doutu = html.etree.HTML(text)
    imgs = html_doutu.xpath('//div[@class="col-sm-9"]//img[@class!="gif"]')           #img[@class!="gif"]这里的图片是占位符，不是我们需要的
    for img in imgs:
        #表情对应的url
        img_urls = img.get('data-original')

        #表情的名称
        img_alts = img.get('alt')
        #还要用正则处理一下文件名，因为在Windows下，文件名是有规定的，有不是符合是不允许的
        img_alts = re.sub(r'[\?？\.。！!，]','',img_alts)
        #取表情文件的后缀名,用os.path.splitext()方法来分割字符串
        suffix = os.path.splitext(img_urls)[1]

        #下载下来的表情名称
        filename = img_alts + suffix
        #把表情下载下来，用到urllib的urlretrieve
        request.urlretrieve(img_urls,'images/'+ filename)

def main():
    #处理分页问题
    for x in range(1,11):
        url = 'http://www.doutula.com/article/list/?page=%d' %x
        #把目标url传进来
        parse_page(url)


if __name__ == '__main__':
    main()