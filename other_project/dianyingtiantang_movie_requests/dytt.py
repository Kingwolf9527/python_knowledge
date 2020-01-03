# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/19 19:00

import requests
from lxml import html

Base_domain = 'https://www.dytt8.net'
Headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Upgrade-Insecure-Requests': '1'
}

def get_detail_urls(url):

    res = requests.get(url, headers=Headers)
    text = res.text

    html_dytt = html.etree.HTML(text)

    # 获取电影详情的url(这里是一页的电影详情url)
    detail_urls = html_dytt.xpath('//table[@class="tbspan"]//a/@href')
    # for detail_url in detail_urls:
    #     # 再结合前面的Base_domain，重新组装完整的url
    #     print(Base_domain + detail_url)

    #用map()函数来映射，结果lambda匿名函数
    detail_urls = map(lambda url:Base_domain+url,detail_urls)
    return detail_urls
    #把这个列表detail_urls中的每一个元素都去执行前面的那个函数base_domain+url
    #map(fun,*iterable )--第一个参数是函数，第二个参数一个列表或者元祖(一个或多个序列)

    # #上面的匿名函数等同于：
    # def square(x):  # 计算平方数
    #     return x ** 2
    # map(square, [1, 2, 3, 4, 5])  # 计算列表各个元素的平方
    # [1, 4, 9, 16, 25]
    #lambda匿名函数：
    # map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
    # [1, 4, 9, 16, 25]


def parse_detail(url):

    #实例一个对象字典
    movie = {}
    res = requests.get(url,headers=Headers)
    text = res.content.decode('gbk')
    html_dytt = html.etree.HTML(text)
    title = html_dytt.xpath('//h1/font[@color="#07519a"]/text()')[0]
    movie['title'] = title
    #整个电影详情都在整个zoom里面
    zoom = html_dytt.xpath('//div[@id="Zoom"]')[0]
    imgs = zoom.xpath('.//img/@src')          #定位到的有二张图片，一张是海报，一张是电影截图
    poster = imgs[0]
    screenshot = imgs[1]
    movie['poster'] = poster
    movie['screenshot'] =screenshot

    def parse_info(info,rule):
        return info.replace(rule,'').strip()

    #其他详情信息都在同一个页面里，都是text()定位到
    infos = zoom.xpath('.//text()')
    # for info in infos:
    #在同时需要index和value值的时候可以使用 enumerate。下列分别将字符串，数组，列表与字典遍历序列中的元素以及它们的下标，把下标以及下标对应的值
    for index,info in enumerate(infos):
        # print(info)
        # print(index)
        # print('=='*30)
        #判断一下开头的字符串
        if info.startswith('◎片　　名'):
            #因为infos中打印出来的字符串很乱，需要处理一下没有的字符串，替换成空格,而且最后处理一下左右的空格(这里定义一个函数统一处理)
            # info = info.replace('◎片　　名','').strip()
            info = parse_info(info,'◎片　　名')
            movie['name'] = info
            # print(movie)
        elif info.startswith('◎年　　代'):
            # info = info.replace('◎年　　代','').strip()
            info = parse_info(info,'◎年　　代')
            movie['year'] = info
        elif info.startswith('◎产　　地'):
            # info = info.replace('◎产　　地','').strip()
            info = parse_info(info,'◎产　　地')
            movie['country'] = info
        elif info.startswith('◎类　　别'):
            # info = info.replace('◎类　　别','').strip()
            info = parse_info(info,'◎类　　别')
            movie['type'] = info
        elif info.startswith('◎语　　言'):
            # info = info.replace('◎语　　言','').strip()
            info = parse_info(info,'◎语　　言')
            movie['language'] =info
        elif info.startswith('◎字　　幕'):
            # info = info.replace('◎字　　幕','').strip()
            info = parse_info(info,'◎字　　幕')
            movie['subtitle'] = info
        elif info.startswith('◎上映日期'):
            # info = info.replace('◎上映日期','').strip()
            info = parse_info(info,'◎上映日期')
            movie['release date'] = info
        elif info.startswith('◎IMDb评分'):
            # info = info.replace('◎IMDb评分','').strip()
            info = parse_info(info,'◎IMDb评分')
            movie['imdb_score'] = info
        elif info.startswith('◎豆瓣评分'):
            # info = info.replace('◎豆瓣评分','').strip()
            info = parse_info(info,'◎豆瓣评分')
            movie['douban_score'] = info
        elif info.startswith('◎视频尺寸'):
            # info = info.replace('◎视频尺寸','').strip()
            info = parse_info(info,'◎视频尺寸')
            movie['size'] = info
        elif info.startswith('◎片　　长'):
            # info = info.replace('◎片　　长').strip()
            info = parse_info(info,'◎片　　长')
            movie['mins'] = info
        elif info.startswith('◎导　　演'):
            # info = info.replace('◎导　　演','').strip()
            info = parse_info(info,'◎导　　演')
            movie['director'] = info
        elif info.startswith('◎编　　剧'):
            # info = info.replace('◎编　　剧','').strip()
            info = parse_info(info,'◎编　　剧')
            movie['scriptwriter'] = info
        elif info.startswith('◎主　　演'):
            # info = info.replace('◎主　　演','').strip()
            info = parse_info(info,'◎主　　演')
            #把所有演员都放进列表中
            actors = [info]          #因为后面获取的演员都是从第二个下标开始的，第一个演员在info里面，也要加进去，后面的append会在后面插入
            #因此这里是从当前的index出发，继续通过index去遍历所有演员，而不是通过info去遍历，而且info已经包含第一个演员的信息了，所以，遍历的index从index+1起
            for y in range(index+1,len(infos)):
                actor = infos[y].strip()             #处理一下前后的空格
                # print(actor)
                #当遇到简介的时候，意味着所有演员都被提取完毕(简介的开头是：◎)
                if actor.startswith('◎'):
                    break
                actors.append(actor)
            # print(actors)
            movie['actors'] = info
# ◎主　　演　波伊德·霍布鲁克 Boyd Holbrook    第一个
# 　　　　　　崔凡特·罗兹 Trevante Rhodes
# 　　　　　　雅各布·特伦布莱 Jacob Tremblay
# 　　　　　　科甘-迈克尔·凯 Keegan-Michael Key
# 　　　　　　奥立薇娅·玛恩 Olivia Munn
# 　　　　　　斯特林·K·布朗 Sterling K. Brown
# 　　　　　　托马斯·简 Thomas Jane
# 　　　　　　阿尔菲·艾伦 Alfie Allen
# 　　　　　　杰克·布塞 Jake Busey
# 　　　　　　伊冯娜·斯特拉霍夫斯基 Yvonne Strahovski
            # #因为主演有多个，但是是通过<br />一行一行的显示的，如果这样直接打印出来，那么久只能打印一个主演，例如：波伊德·霍布鲁克 Boyd Holbrook，要想解决这种问题，只能在当前节点下，再次遍历infos列表,但是我们要知道当前处于哪个列表，就需要for循环的另外一个用法enumerate(),把index和info都输出
        #简介跟主演也是同样处理的
        elif info.startswith('◎简　　介'):
            # info = info.replace('◎简　　介','').strip()
            info = parse_info(info,'◎简　　介')
            for y in range(index+1,len(infos)):
                descripe = infos[y].strip()
                if descripe.startswith('【下载地址】'):
                    break
                # print(descripe)
                movie['descripe'] = info
                # print(info)
        #获取下载地址，不用在for循环里面了
    download_url = html_dytt.xpath('//td[@bgcolor="#fdfddf"]/a/@href')[0]
    # print(download_url)
    movie['download_url'] = download_url
    # print(download_url)
    return movie


def spider():
    #通过分页寻找到页码和url的规律，因此，采用url格式化的方式处理url
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    #第一个for循环，是用来控制总共有几页
    for x in range(1,184):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        #第二个for循环，是用来遍历一页当中所有电影的详情url
        for detail_url in detail_urls:
            movie = parse_detail(detail_url)
            movies.append(movie)
            # print(movies)
        print(movies)
        #     break                            #这两个break是为了调试，只打印第一页的内容，退出当前循环
        # break


if __name__ == '__main__':
    spider()