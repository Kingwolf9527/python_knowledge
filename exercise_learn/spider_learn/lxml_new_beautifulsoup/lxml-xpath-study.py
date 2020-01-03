# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/19 14:52

'''
    ::获取所有tr标签
    ::获取第二个tr标签
    ::获取所有class属性等于even的tr标签
    ::获取所有a标签的href属性
    ::获取所有职位信息(纯文本)

'''

from lxml import html

parser = html.etree.HTMLParser(encoding='utf-8')
html_job = html.etree.parse('tencent_job.html',parser=parser)

# #1.获取所有tr标签
# trs = html_job.xpath('//tr')
# for tr in trs:
#     print(html.etree.tostring(tr,encoding='utf-8').decode('utf-8'))


# #2.获取第二个tr标签
# tr = html_job.xpath('//tr[2]')[0]
# print(html.etree.tostring(tr,encoding='utf-8').decode('utf-8'))

#
# #3.获取所有class属性等于even的tr标签
# trs = html_job.xpath('//tr[@class="even"]')
# for tr in trs:
#     print(html.etree.tostring(tr,encoding='utf-8').decode('utf-8'))


##4.获取所有a标签的href属性
# trs = html_job.xpath('//a/@href')
# for tr in trs:
#     print('https://hr.tencent.com/' + tr)


#5.获取所有职位信息(纯文本)
trs = html_job.xpath('//tr[position()>1]')        #因为第一个tr是表头信息，没有用的，有用的数据在第二个tr标签开始

# 实例化一个职位的列表
positions = []

for tr in trs:

    #在某个标签下，再执行xpath函数，获取这个标签下的子孙元素，那么应该在//之前加上一个点，代表是在当前元素下获取的
    href = tr.xpath('.//a/@href')[0]          #因为xpath返回的是一个列表
    fullurl = "https://hr.tencent.com/" + href
    # title = tr.xpath('.//a/text()')[0]
    title = tr.xpath('./td[1]//text()')[0]
    categroy = tr.xpath('./td[2]/text()')
    nums = tr.xpath('./td[3]/text()')
    address = tr.xpath('./td[4]/text()')
    pubtime = tr.xpath('./td[5]/text()')
    # print(fullurl)
    # print(title)
    # print(categroy)
    # print(nums)
    # print(address)
    # print(pubtime)
    # break

    #最后通过字典，把数据组装成一个列表
    position = {

        'url' : fullurl,
        'title' : title,
        'categroy' : categroy,
        'nums' : nums,
        'address' : address,
        'pubtime' : pubtime

    }

    positions.append(position)

print(positions)