# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/16 23:08

from scrapy import cmdline

cmdline.execute('scrapy crawl qsbk_spider'.split())     #需要分割成列表才能正常执行