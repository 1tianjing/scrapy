from scrapy_redis.spiders import RedisSpider
from example.items import ExampleItem

class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'
    redis_key = 'myspider:start_urls'
    # 这种也是可以设置域的，但是太固定
    # allowed_domains = ['']

    #这个方法的目的是什么：根据你给定的url，动态的获取URL中的域
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        print(response.status)
        item = ExampleItem()
        # 目标数据：职位名称、工作地点、职位类别、工作职责、工作要求
        item['jobName'] = response.xpath('//td[@id="sharetitle"]/text()').extract()[0]
        item['workLocation'] = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        item['jobType'] = response.xpath('//tr[@class="c bottomline"]/td[2]/text()').extract()[0]
        item['jobDesc'] = response.xpath('//table[@class="tablelist textl"]/tr[3]//li/text()').extract()
        item['jobInfo'] = response.xpath('//table[@class="tablelist textl"]/tr[4]//li/text()').extract()
        # print(jobName,workLocation,jobType,jobDesc,jobInfo)
        yield item
