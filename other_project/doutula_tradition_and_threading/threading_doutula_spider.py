# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/11/30 8:07

'''
    queue:安全队列是不用考虑锁的问题的

'''

import requests
from lxml import html
import re
import os
from urllib import request
import threading
from queue import Queue


#先创建生产者类
class Procuder(threading.Thread):

    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host': 'www.doutula.com'
    }

    #需要把队列传进来，所以需要重写init函数(*args:任意位置参数，**kwargs：任意关键字参数，当不确定要哪些参数的时候，把这两个参数写进去，表示任意的参数)
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        #重写方法之前，需要调用父类的Thread方法，传给init函数
        super(Procuder, self).__init__(*args,**kwargs)    #传给父类
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        #这里需要用到死循环，因为需要保证线程执行完后，不断的去page_queue队列中拿url出来解析
        while True:
            #当线程中，已经没有数据了，就应该退出循环
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            #把每一页的url传进去解析
            self.parse_page(url)

    def parse_page(self,url):

        response = requests.get(url, headers=self.headers)
        text = response.text
        html_doutu = html.etree.HTML(text)
        imgs = html_doutu.xpath('//div[@class="col-sm-9"]//img[@class!="gif"]')  # img[@class!="gif"]这里的图片是占位符，不是我们需要的
        for img in imgs:
            # 表情对应的url
            img_urls = img.get('data-original')

            # 表情的名称
            img_alts = img.get('alt')
            # 还要用正则处理一下文件名，因为在Windows下，文件名是有规定的，有不是符合是不允许的
            img_alts = re.sub(r'[\?？\.。！!，*]', '', img_alts)
            # 取表情文件的后缀名,用os.path.splitext()方法来分割字符串
            suffix = os.path.splitext(img_urls)[1]
            # 下载下来的表情名称
            filename = img_alts + suffix

            #把文件名和表情的url传给img_queue队列中
            self.img_queue.put((img_urls,filename))


class Consumer(threading.Thread):

    #需要把队列传进来，所以需要重写init函数(*args:任意位置参数，**kwargs：任意关键字参数，当不确定要哪些参数的时候，把这两个参数写进去，表示任意的参数)
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        #重写方法之前，需要调用父类的Thread方法，传给init函数
        super(Consumer, self).__init__(*args,**kwargs)    #传给父类
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            #当图片队列中已经没有数据以及每一页的url队列也没有数据了，就应该退出线程
            if self.img_queue.empty() and self.page_queue.empty():
                break
            #解包操作，img_queue队列中的img_urls和filename会一一对应
            img_urls,filename = self.img_queue.get()
            # 把表情下载下来，用到urllib的urlretrieve
            request.urlretrieve(img_urls, 'images/' + filename)
            print(filename,'   下载完成了！！！')

def main():

    #创建两个队列：每一页的url队列以及图片的url队列
    page_queue = Queue(200)
    img_queue = Queue(5000)
    #处理分页问题
    for x in range(1,101):
        url = 'http://www.doutula.com/article/list/?page=%d' %x
        #把目标url加到每一页的url队列中
        page_queue.put(url)

    #创建线程和启动线程
    for x in range(5):
        t = Procuder(page_queue,img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()


if __name__ == '__main__':
    main()