# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/30 19:57

import requests
from lxml import html
import os
import re
from urllib import request


def parse_page(url):

    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    response = requests.get(url,headers=headers)
    text =response.text

    html_ibaotu = html.etree.HTML(text)

    video_lists = html_ibaotu.xpath('//div[@class="main-body"]')
    for video_list in video_lists:

        video_srcs = video_list.xpath('.//div[@class="video-play"]/video/@src')
        video_alts = video_list.xpath('.//div[@class="show-image"]/img/@alt')
        for video_src ,video_alt in zip(video_srcs,video_alts):

            video_src = 'https:' + video_src
            filename = video_alt + '.mp4'
            #下载video
            request.urlretrieve(video_src,'video/'+ filename)
            print(filename + '  下载完成了！')



def main():

    for x in range(1,11):
        url = 'https://ibaotu.com/shipin/7-0-0-0-0-%d.html' %x
        parse_page(url)



if __name__ == '__main__':
    main()
