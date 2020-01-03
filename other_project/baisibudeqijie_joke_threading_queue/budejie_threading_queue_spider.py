# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/1 0:53

import requests
from lxml import html
from queue import Queue
import threading
import re
import csv

class Procuder(threading.Thread):

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    def __init__(self,page_queue,duanzi_queue,*args,**kwargs):
        super(Procuder, self).__init__(*args,**kwargs)
        self.base_domain = 'http://www.budejie.com'
        self.page_queue = page_queue
        self.duanzi_queue = duanzi_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            # 通过队列获取每一页的url
            url = self.page_queue.get()
            # 把每一页的url传进去解析
            response = requests.get(url,headers=self.headers)
            text = response.text
            html_budejie = html.etree.HTML(text)
            desc_lists = html_budejie.xpath('//div[@class="j-r-list-c-desc"]')
            for desc_list in desc_lists:
                #content内容
                jokes = desc_list.xpath('.//text()')
                #转为字符串处理
                joke = '\n'.join(jokes).strip()
                #链接,这里获取的url是不完整的，需要拼接url
                link = self.base_domain + desc_list.xpath('.//a/@href')[0]
                #把joke和link传到duanzi的队列中
                self.duanzi_queue.put((joke,link))
            #通过打印每一页的数据，可以清晰查看，页数是url的最后一个数字
            print('='*50+'第%s页下载完成了！' % url.split('/')[-1]+'='*50)
                # #作者
                # author_lists = desc_list.xpath('.//div[@class="j-list-user"]//a[@class="u-user-name"]/text()')
                # #内容
                # content_lists = desc_list.xpath('.//div[@class="j-r-list-c-desc"]/a/text()')
                # #点赞
                # icon_up_lists = desc_list.xpath('.//li[@class="j-r-list-tool-l-up"]//span/text()')
                # #不喜欢
                # icon_down_lists = desc_list.xpath('.//div[@class="j-r-list-tool-l "]/ul/li[@class="j-r-list-tool-l-down "]/span/text()')
                # #分享
                # share_lists = desc_list.xpath('.//div[@class="j-r-list-tool-ct-share-c"]/span/text()')
                # share = ''.join(share_lists)
                # share = re.sub(r'分享','',share).strip()
                # share_lists = share.split('  ')
                # print(share_lists)
                #
                # for author_list,content_list,icon_up_list,icon_down_list,share_list in zip(author_lists,content_lists,icon_up_lists,icon_down_lists,share_lists):
                #     self.duanzi_queue.put((author_list,content_list,icon_up_list,icon_down_list,share_list))


class Consumer(threading.Thread):

    def __init__(self,duanzi_queue,writer,global_lock,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.duanzi_queue = duanzi_queue
        #加了全局锁和文件操作
        self.writer = writer
        self.global_lock = global_lock

    def run(self):
        # duanzis = []

        while True:
            try:
                joke,link = self.duanzi_queue.get(timeout=40)
                #因为在Windows上，IO操作的多线程需要加锁
                self.global_lock.acquire()
                #写入文件
                self.writer.writerow((joke,link))
                #解锁
                self.global_lock.release()
                print('保存一条')
            except:
                break
        #     if self.duanzi_queue.empty() and self.page_queue.empty():
        #         break
        #     author_list, content_list, icon_up_list, icon_down_list, share_list = self.duanzi_queue.get()
        #     duanzi = {
        #
        #         'author_list' : author_list,
        #         'content_list' : content_list,
        #         'icon_up_list' : icon_up_list,
        #         'icon_down_list' : icon_down_list,
        #         'share_list' : share_list
        #
        #     }
        #
        #     duanzis.append(duanzi)
        # print(duanzis)



def main():

    #创建队列
    page_queue = Queue(100)
    duanzi_queue = Queue(2000)

    #全局锁
    global_lock = threading.Lock()
    #写入文件
    fp = open('dudejie.csv','a',newline='',encoding='utf-8')
    #csv的写操作
    writer = csv.writer(fp)
    # 把表头的数据写进去
    writer.writerow(('content','link'))

    #分页处理
    for x in range(1,11):
        url = 'http://www.budejie.com/text/%d' %x
        #把每一页的url传给page_queue队列
        page_queue.put(url)

    for x in range(5):
        t = Procuder(page_queue,duanzi_queue)
        t.start()

    for x in range(5):
        t = Consumer(duanzi_queue,writer,global_lock)
        t.start()



if __name__ == '__main__':
    main()