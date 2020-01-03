# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/26 3:07

import requests
from lxml import html
import time

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Origin': 'https://sou.zhaopin.com',
    'Referer': 'https://sou.zhaopin.com/?jl=489&kw=%E5%AE%89%E5%85%A8%E6%B8%97%E9%80%8F&kt=3',
    'Host' : 'fe-api.zhaopin.com',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language' : 'zh-CN,zh;q=0.9',
    'Cookie' : 'adfbid2=0; sts_deviceid=1674c41fb77d3-01a8eb93f0aa9b-8383268-1049088-1674c41fb7911a; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; __xsptplus30=30.2.1543218954.1543218954.1%231%7CbaiduPC%7CCPC%7Cpp%7C8804373%7Cpp%23%23HmJdQlEyYT0BpEDc0EgJEKps7cfsOyof%23; _jzqa=1.3011842312371671600.1543172656.1543172656.1543218954.2; _jzqy=1.1543172656.1543218954.1.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98.-; urlfrom2=121123457; adfcid2=sg_pz_000033; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221674c421605148-0bb93a69e6757f-8383268-1049088-1674c4216071fd%22%2C%22%24device_id%22%3A%221674c421605148-0bb93a69e6757f-8383268-1049088-1674c4216071fd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22sogoupcpz%22%2C%22%24latest_utm_medium%22%3A%22CPT%22%2C%22%24latest_utm_campaign%22%3A%22pp%22%2C%22%24latest_utm_content%22%3A%22qg%22%2C%22%24latest_utm_term%22%3A%22title%22%7D%7D; ZP_OLD_FLAG=false; urlfrom=121123457; adfcid=sg_pz_000033; adfbid=0; jobRiskWarning=true; sts_sg=1; sts_sid=167835e843851-0e76ed09723504-6313363-1049088-167835e84391ad; sts_chnlsid=121123457; dywea=95841923.3649160384435661000.1543172651.1544040444.1544097269.4; dywec=95841923; dywez=95841923.1544097269.4.7.dywecsr=sogoupcpz|dyweccn=pp|dywecmd=CPT|dywectr=title|dywecct=qg; __utma=269921210.414906929.1543172652.1544040444.1544097269.7; __utmc=269921210; __utmz=269921210.1544097269.7.7.utmcsr=sogoupcpz|utmccn=pp|utmcmd=CPT|utmctr=title|utmcct=qg; __utmt=1; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1543218953,1543218961,1544040444,1544097269; zp_src_url=https%3A%2F%2Fwww.zhaopin.com%2F%3Futm_source%3Dsogoupcpz%26utm_medium%3DCPT%26utm_term%3Dtitle%26utm_content%3Dqg%26utm_campaign%3Dpp%26sid%3D121123457%26site%3Dsg_pz_000033; dyweb=95841923.8.10.1544097269; __utmb=269921210.8.10.1544097269; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1544097312; GUID=d55f00ca390f478fba1282dd86b1cdd4; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%229eb73bc1-aef5-4da5-ab26-7a418bb987d5-sou%22%2C%22funczone%22:%22smart_matching%22}}; sts_evtseq=30'
}

def get_url_page(url):
    # 处理分页的内容
    base_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%AE%89%E5%85%A8%E6%B8%97%E9%80%8F&kt=3&_v=0.58688805&x-zp-page-request-id=3ddaf47a67264c8e8ba39f9aa393c4da-1544097318276-10264'
    for x in range(0, 5):
        x = x * 60
        url = base_url.format(x)

    #先处理一页的内容
    res = requests.get(url,headers=Headers)
    print(res.content.decode('utf-8'))
    print(res.json())
    #json方法，如果返回来的是json数据，那这个方法会自动loads成字典
    text = res.json()
    position_descs = text['data']['results']
    for position_desc in position_descs:
        #职位number以及职位的详情页面url
        position_number = position_desc['number']
        position_url = 'https://jobs.zhaopin.com/%s.htm' % position_number
        parse_url(position_url)

def parse_url(url):

    res = requests.get(url,headers=Headers)
    content = res.text
    html_position = html.etree.HTML(content)
    #定位到职位详情
    details = html_position.xpath('//div[@class="main"]')
    for detail in details:
        #职位名称
        position_name = detail.xpath('.//div[@class="new-info"]//h1/text()')
        #薪水
        position_salary = detail.xpath('.//div[@class="new-info"]//div[@class="l info-money"]/strong/text()')
        #公司名称
        company_name = detail.xpath('.//div[@class="company l"]/a/text()')
        #所在地区，学历要求，工作年限，招聘人数
        introduces_spans = detail.xpath('.//div[@class="info-three l"]/span')

        # 所在地区
        area_spans = introduces_spans[0]
        area = area_spans.xpath('.//text()')[0]

        # 工作年限
        work_year_spans = introduces_spans[1]
        work_year = work_year_spans.xpath('.//text()')[0]

        # 学历要求
        education_spans = introduces_spans[2]
        education = education_spans.xpath('.//text()')[0]

        # 招聘人数
        recruitment_num_spans = introduces_spans[3]
        recruitment_num = recruitment_num_spans.xpath('.//text()')[0]

        #职位优势
        position_advantage = detail.xpath('//div[@class="pos-info-tit"]/div/span')

        #职位描述，包括岗位职责和任职要求
        position_descs = detail.xpath('//div[@class="pos-ul"]')



def main():

    #处理分页的内容
    base_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E5%AE%89%E5%85%A8%E6%B8%97%E9%80%8F&kt=3&_v=0.58688805&x-zp-page-request-id=3ddaf47a67264c8e8ba39f9aa393c4da-1544097318276-10264'
    for x in range(0,5):
        x = x * 60
        url = base_url.format(x)
        get_url_page(url)
        # break

if __name__ == '__main__':
    main()