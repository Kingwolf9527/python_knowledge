# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/30 22:24

import requests
from lxml import html
from urllib import request
import threading
from queue import Queue


#创建生产者(获取每一页的url队列类)
class Procuder(threading.Thread):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    def __init__(self,page_queue,video_queue,*args,**kwargs):
        # 重写方法之前，需要调用父类的Thread方法，传给init函数
        super(Procuder, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.video_queue = video_queue

    def run(self):
        # 这里需要用到死循环，因为需要保证线程执行完后，不断的去page_queue队列中拿url出来解析
        while True:
            # 当线程中，已经没有数据了，就应该退出循环
            if self.page_queue.empty():
                break
            #通过队列获取每一页的url
            url = self.page_queue.get()
            # 把每一页的url传进去解析
            self.parse_page(url)

    def parse_page(self,url):

        response = requests.get(url,headers=self.headers)
        text =response.text

        html_ibaotu = html.etree.HTML(text)

        video_lists = html_ibaotu.xpath('//div[@class="main-body"]')
        for video_list in video_lists:
            video_srcs = video_list.xpath('.//div[@class="video-play"]/video/@src')
            video_alts = video_list.xpath('.//div[@class="show-image"]/img/@alt')
            for video_src ,video_alt in zip(video_srcs,video_alts):

                video_src = 'https:' + video_src
                filename = video_alt + '.mp4'

                #把video的url和文件名传给video下载的队列中
                self.video_queue.put((video_src,filename))


#创建消费者(下载每页的video的队列类)
class Consumer(threading.Thread):

    def __init__(self,page_queue,video_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.video_queue = video_queue

    def run(self):
        while True:
            # 当video队列中已经没有数据以及每一页的url队列也没有数据了，就应该退出线程
            if self.video_queue.empty() and self.page_queue.empty():
                break
            # 解包操作(zip)，video_queue队列中的video_src和filename会一一对应
            video_src,filename = self.video_queue.get()
            # 把video下载下来，用到urllib的urlretrieve
            request.urlretrieve(video_src,'video/' + filename)
            print(filename,'  已经下载完成！')

def main():

    #创建队列，每一页的队列以及video的队列
    page_queue = Queue(100)
    video_queue = Queue(2000)

    # 处理分页问题
    for x in range(1,11):
        url = 'https://ibaotu.com/shipin/7-0-0-0-0-%d.html' % x
        # 把目标url加到每一页的url队列中
        page_queue.put(url)

    #创建线程和启动线程
    for x in range(5):
        t = Procuder(page_queue,video_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue,video_queue)
        t.start()



if __name__ == '__main__':
    main()
