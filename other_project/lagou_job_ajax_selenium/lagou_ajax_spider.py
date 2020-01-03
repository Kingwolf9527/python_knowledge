# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/6 20:06

import requests
import time
from lxml import html
import re

Headers = {
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'Host': 'www.lagou.com',
      'Origin': 'https://www.lagou.com',
      'Referer': 'https://www.lagou.com/jobs/list_%E5%AE%89%E5%85%A8%E6%B8%97%E9%80%8F?px=default&city=%E5%85%A8%E5%9B%BD',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36',
      'X-Anit-Forge-Code': '0',
      'X-Anit-Forge-Token': 'None',
      'X-Requested-With': 'XMLHttpRequest',
      'Cookie' : 'user_trace_token=20180703143820-743b275e-29f2-401a-802b-c2de2d9563f6; _ga=GA1.2.1365295142.1530599901; LGUID=20180703144054-08bd9a5a-7e8c-11e8-98e2-5254005c3644; JSESSIONID=ABAAABAAAGGABCB7A11DAA9354CB37BF24B93979558084B; _gid=GA1.2.2083809331.1544099169; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542541478,1544099170; _gat=1; LGSID=20181206223957-cd657df3-f964-11e8-8ce6-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%25B5%258B%25E8%25AF%2595%3F%26px%3Ddefault%26city%3D%25E7%258F%25A0%25E6%25B5%25B7; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E5%25AE%2589%25E5%2585%25A8%25E6%25B8%2597%25E9%2580%258F%3Fcity%3D%25E7%258F%25A0%25E6%25B5%25B7%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; X_HTTP_TOKEN=6cc54d2fc9f0c588acf8b6b21649c7b2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216783f63c83208-09fc7a14e8e4b1-6313363-1049088-16783f63c851fd%22%2C%22%24device_id%22%3A%2216783f63c83208-09fc7a14e8e4b1-6313363-1049088-16783f63c851fd%22%7D; sajssdk_2015_cross_new_user=1; SEARCH_ID=4219af716e8046b29005bdc6fed1d714; LGRID=20181206224028-e0180c7f-f964-11e8-8d29-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1544107229'
}

def request_url_page():

    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'

    data = {
        'first' : 'false',
        'pn' : '1',
        'kd' : '安全渗透'
    }

    #分页处理,url都是一样的，不同的分页，区别在pn的页码不同
    for x in range(1,31):
        data['pn'] = x
        response = requests.post(url,data=data,headers=Headers)
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionId = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' %positionId
            parse_potion_detail(position_url)
            break
        break



def parse_potion_detail(url):

    response = requests.get(url,headers=Headers)
    text = response.text
    html_position = html.etree.HTML(text)

    #职位名称
    position_name = html_position.xpath('//div[@class="job-name"]/span/text()')[0]

    #工作经验，薪水，学历要求，工作地点详情
    descs = html_position.xpath('//dd[@class="job_request"]//span')

    #薪水
    salary_spans = descs[0]
    salary = salary_spans.xpath('.//text()')[0]

    #工作地点
    city_spans = descs[1]
    city = city_spans.xpath('.//text()')[0]
    # 使用正则处理一下不需要的符合和空格
    city = re.sub(r'[\s/]','',city).strip()

    #工作经验
    work_year_spans = descs[2]
    work_year = work_year_spans.xpath('.//text()')[0]
    work_year = re.sub(r'[\s/]','',work_year).strip()

    #学历要求
    education_spans = descs[3]
    education = education_spans.xpath('.//text()')[0]
    education = re.sub(r'[\s/]', '', education).strip()

    #职位诱惑
    position_advantage = html_position.xpath('//dd[@class="job-advantage"]/p/text()')[0]

    #职位描述
    position_desc = html_position.xpath('//dd[@class="job_bt"]//p/text()')
    #转为字符串的形式(''.join(列表))
    position_desc = ''.join(position_desc).strip()

def main():
    request_url_page()

if __name__ == '__main__':
    main()