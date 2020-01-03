# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Jianshu.items import JianshuItem


class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):

        #文章的标题
        title = response.xpath('//h1[@class="title"]/text()').get()

        #文章作者
        author = response.xpath('//div[@class="info"]/span[@class="name"]/a/text()').get()

        #头像
        avatar = response.xpath('//div[@class="author"]/a[@class="avatar"]/img/@src').get()

        #发布时间
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get()
        pub_time = pub_time.replace(u'*','')

        #文章所有内容，包括样式
        content = response.xpath('//div[@class="show-content"]').get()   #因为需求是要把内容中的所有东西都复制过去，包括样式

        #文章的url
        origin_url = response.url

        #文章的id,是在url里面的/p/后面的那些12位数字和字母组成的
        # 两种例子：https://www.jianshu.com/p/3f43f7b9f17f
        #以及;https://www.jianshu.com/p/416cc1671773?utm_campaign=maleskine&utm_content=note&utm_medium=pc_all_hots&utm_source=recommendation
        first_url = response.url
        second_url = first_url.split('?')[0]
        article_id = second_url.split('/')[-1]

        # 文章字数
        word_count = response.xpath('//span[@class="wordage"]/text()').get()
        word_count = word_count.replace(u'字数 ','')

        # 文章阅读数
        read_count = response.xpath('//span[@class="views-count"]/text()').get()
        # read_count = read_count.replace(u'阅读 ', '')

        # 文章的评论数
        comment_count = response.xpath('//span[@class="comments-count"]/text()').get()
        # comment_count = comment_count.replace(u'评论 ', '')

        # 文章喜欢数
        like_count = response.xpath('//span[@class="likes-count"]/text()').get()
        # like_count = like_count.replace(u'喜欢 ', '')

        # 文章所属的专题
        subjects = response.xpath('//div[@class="include-collection"]/a/div/text()').getall()
        subjects = ','.join(subjects)

        #设置一个字典存储数据
        item = JianshuItem()
        item['title'] = title
        item['author'] = author
        item['avatar'] = avatar
        item['pub_time'] = pub_time
        item['content'] = content
        item['origin_url'] = origin_url
        item['article_id'] = article_id
        item['word_count'] = word_count
        item['read_count'] = read_count
        item['comment_count'] = comment_count
        item['like_count'] = like_count
        item['subjects'] = subjects

        yield item




