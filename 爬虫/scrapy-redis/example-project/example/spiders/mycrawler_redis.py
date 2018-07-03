from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider
from example.items import ExampleItem


class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'

    # rules = (
    #     # follow all links
    #     Rule(LinkExtractor(), callback='parse_page', follow=True),
    # )

    rules = [
        # Rule(LinkExtractor(allow=('start=\d+',),allow_domains=('hr.tencent.com')),follow=True),
        Rule(LinkExtractor(allow=(r'position_detail.php',), allow_domains=('hr.tencent.com')),
             callback='parse_page', follow=True)
    ]

    #根据给的任务，动态去获取域
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MyCrawler, self).__init__(*args, **kwargs)


    #获取到数据之后的一个解析
    def parse_page(self, response):
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