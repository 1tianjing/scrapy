# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#


SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

#用的是scrapy-redis自带的去重组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#调度器组件
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#保存暂时的开启的状态   为True表示会保存相关记录,下次请求会接着上一次
SCHEDULER_PERSIST = True
#以下三个表示队列请求
#第一个是scrapy-redis默认的队列(有优先级)  一般使用默认的
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#使用的是队列,先进先出FIFO
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#是一个栈结构,先进后出FIFO
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

#设置数据管道文件scrapy-redis.piplines.RedsPipeline是必须要打开的
#才能够将数据存储到redis数据库中
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# log日志等级
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
#下载延时
DOWNLOAD_DELAY = 1


#设置你要存储的redis数据库的主机的IP地址
REDIS_HOST = '192.168.43.112'
# 设置你要存储的redis数据库的端口号
REDIS_PORT = '6379'