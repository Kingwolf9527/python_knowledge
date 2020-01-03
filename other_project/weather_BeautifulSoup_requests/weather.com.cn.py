# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/23 3:14

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

#定义一个全局变量，存储爬取到的数据
All_data = []

def parse_weather(url):

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    text = res.content.decode('utf-8')

    #创建soup对象
    #如果遇到特殊情况，比如：某些网页的HTML代码不规范，有不闭合的标签，BeautifulSoup的解析器最好用html5lib，它的容错性最好
    # soup = BeautifulSoup(text,'lxml')
    soup = BeautifulSoup(text,'html5lib')
    #抓取当天的天气预报
    today_weather = soup.find('div',attrs={'class':'conMidtab'})
    # 把所有的省份找出来
    tables = today_weather.find_all('table')
    for table in tables:
        #找出每一个省份的城市
        trs = table.find_all('tr')[2:]     #因为前两个tr标签是表头，没有我们需要的数据，所有需要去掉
        for index,tr in enumerate(trs):
            #找出每个城市的详情
            tds = tr.find_all('td')
            #这里会存在一个问题，每个省份，第一个城市的td标签，存的是省份的名称，第二个td标签才是城市名称，但是第二个城市起，都是第一个td标签存城市名称，因此这里要根据下标来判断
            if index == 0:
                city_td = tds[1]
            else:
                city_td = tds[0]
            #找出每一个城市名称
            city = list(city_td.stripped_strings)[0]
            temperature_td = tds[-2]
            #找出每个城市的最低温度
            min_temperature = list(temperature_td.stripped_strings)[0]
            #最后保存每个城市的最低气温以及对应的城市，因为后续要对最低气温做可视化分析，所以要把最低气温转为整形，否则无法正确排序
            All_data.append({'city':city,'min_temperature':int(min_temperature)})
            # print({'city':city,'min_temperature':min_temperature})


def main():

    #把所有地区的url放进列表中，最好遍历一下就可以了
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
        ]
    for url in urls:
        #再把url传给执行函数执行
        parse_weather(url)

        #分析数据
        #根据最低气温排序(sort默认排序是升序),这里用匿名函数处理
        #这个x代表的是列表All_data列表中的每一个元素，而这每一个元素都是一个字典，而这字典中的min_temperature就是我们需要进行排序的数据
        All_data.sort(key=lambda x:x['min_temperature'])

        #这里的需求是取最低气温，前10位的城市
        data = All_data[0:10]
        #取出所有的城市和最低气温
        cities = list(map(lambda x:x['city'],data))
        min_temperatures = list(map(lambda x:x['min_temperature'],data))

        #创建bar柱状型对象
        bar = Bar('中国天气最低气温排行榜','By kingwolf')
        # 主要方法，用于添加图表的数据和设置各种配置项:第一个参数是name，放在图形的右上角展示，第二个参数是X轴参数，显示的是列表或者元祖，第三个参数是Y轴参数，显示的是列表或者元祖
        bar.add('test',cities,min_temperatures)
        bar.render('weather.html')


if __name__ == '__main__':
    main()