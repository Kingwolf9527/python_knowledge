# -*- coding: utf-8 -*-

"""
    redis的相关配置修改：
    1.确保request存储在啊Redis中
    SCHEDULER = "scrapy_redis.scheduler.Scheduler"

    2.确保所有爬虫共享相同的去重指纹
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDopeFilter"

    3.设置Redis的item pipeline
    ITEM_PIPELINES = {"scrapy_redis.pipelines.RedisPipeline" : 300 }

    4.在Redis中保持scrapy-Redis用到的队列，不会清楚Redis中的队列，从而可以实现暂停和恢复的功能
    SCHEDULER_PERSIST = True

    5.设置Redis连接信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


"""

BOT_NAME = 'FangTianXia'

SPIDER_MODULES = ['FangTianXia.spiders']
NEWSPIDER_MODULE = 'FangTianXia.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'FangTianXia (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'FangTianXia.middlewares.FangtianxiaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'FangTianXia.middlewares.User_agentMiddlewares': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     # 'FangTianXia.pipelines.HousePipeline': 300,      #这个pipeline是用json方式存储数据的
#     'FangTianXia.pipelines.House_mysqlPipeline': 300,        #这个pipeline是用mysql存储数据的
# }                                                         #采用下面的Redis的pipeline

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# redis的相关配置修改：
# 1.确保request存储在啊Redis中
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 2.确保所有爬虫共享相同的去重指纹
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 3.设置Redis的itempipeline
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300,
}

# 4.在Redis中保持scrapy - Redis用到的队列，不会清楚Redis中的队列，从而可以实现暂停和恢复的功能
SCHEDULER_PERSIST = True

# 5.设置Redis连接信息
REDIS_HOST = "192.168.3.9"
REDIS_PORT = 6379
