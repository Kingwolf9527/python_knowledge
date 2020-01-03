# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/20 3:19

from lxml import html
import requests

Base_domain = 'https://hr.tencent.com/'

Headers = {

    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Host' : 'hr.tencent.com'

}

#获取所需要的职位的目标链接url的函数，以及拼接好完整的url，把它放在执行函数那里，分页处理
def get_position_url(url):

    res = requests.get(url,headers=Headers)
    text = res.text
    #获取element对象
    html_tencent = html.etree.HTML(text)
    tablelist = html_tencent.xpath('//table[@class="tablelist"]')[0]
    position_urls = tablelist.xpath('.//tr[@class="even"]//a/@href | .//tr[@class="odd"]//a/@href')
    position_urls = map(lambda url:Base_domain+url,position_urls)
    return position_urls

#解析职位详情页面的函数
def parse_detail(url):

    #实例一个职位的对象
    job = {}
    res = requests.get(url,headers=Headers)
    text = res.content.decode('utf-8')
    html_position = html.etree.HTML(text)
    #职位详情页面
    detail_list = html_position.xpath('//table[@class="tablelist textl"]')[0]
    position_name = detail_list.xpath('.//td[@id="sharetitle"]/text()')[0]
    job['position_name'] = position_name
    #地点，类别，人数
    place_type_num = detail_list.xpath('.//tr[@class="c bottomline"]/td/text()')
    #工作地点
    workplace = place_type_num[0]
    job['place'] = workplace
    #职位类别
    category = place_type_num[1]
    job['type'] = category
    #招聘人数
    nums = place_type_num[2]
    job['num'] = nums
    #工作职责和工作要求
    duty_requires = html_position.xpath('//tr[@class="c"]/td/ul')
    #工作职责
    duty = duty_requires[0].xpath('.//text()')
    job['duty'] = duty
    #工作要求
    require = duty_requires[1].xpath('.//text()')
    job['require'] = require

    return job

#处理分页的url情况，执行目标链接的url，并且跳转到职位详情页面的函数
def spider():
    base_url = 'https://hr.tencent.com/position.php?keywords=Python&lid=0&tid=87&start={}#a'
    #创建一个工作职位的列表，来存储字典
    jobs = []
    # 第一个for循环，是用来控制总共有几页
    for x in range(0,51):
        x = x * 10
        url = base_url.format(x)
        #调用获取目标链接的url函数，获取目标链接的url
        position_urls = get_position_url(url)
        # 第二个for循环，是用来遍历一页当中所有职位的详情url
        for position_url in position_urls:
            # 把url放到解析函数中解析职位详情页面
            job = parse_detail(position_url)
            jobs.append(job)
            print(jobs)
        #     break                   #这两个break是调试用的，只是输出第一页第一个url的链接使用
        # break


if __name__ == '__main__':
    spider()