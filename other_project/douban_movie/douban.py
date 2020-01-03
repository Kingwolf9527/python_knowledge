# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/19 16:17

'''
    ::将目标网站上的页面抓取下来
    ::将抓取下来的数据根据一定的规则进行提取
'''

import requests
from lxml import html

#爬取珠海地区正在上映的所有电影
url = 'https://movie.douban.com/cinema/nowplaying/zhuhai/'

headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer' : 'https://movie.douban.com/'

}

res = requests.get(url,headers=headers)
test = res.text

html_douban = html.etree.HTML(test)

ul = html_douban.xpath('//ul[@class="lists"]')[0]      #这里返回两个elemnet,[<Element ul at 0x1f8a7ed0988>, <Element ul at 0x1f8a7ed0b08>],因为正在上映和即将上映的ul属性一样，我们需要的是正在上映
lis = ul.xpath('./li')
#创建电影的实例，空列表
movies = []
for li in lis:
    # print(html.etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = li.xpath('@data-title')[0]
    score = li.xpath('@data-score')[0]
    release = li.xpath('@data-release')[0]
    duration = li.xpath('@data-duration')[0]
    region = li.xpath('@data-region')[0]
    director = li.xpath('@data-director')[0]
    actors = li.xpath('@data-actors')[0]
    votecount = li.xpath('@data-votecount')[0]
    thumbnail = li.xpath('.//img/@src')[0]
    movie = {

        'title' : title,
        'score': score,
        'release': release,
        'duration': duration,
        'region': region,
        'director': director,
        'actors': actors,
        'votecount': votecount,
        'thumbnail' : thumbnail

    }

    movies.append(movie)

print(movies)
