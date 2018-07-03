from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from example.items import ExampleItem

#这里的代码跟scrapy中的crawlspider是一样的
#但是我们使用了scrapy-redis框架并且在settings.py文件中配置了
#scrapy-redis的相关组件之后（去重、调度器等）他就可以将相关信息放在redis数据库中
class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    rules = [
        # Rule(LinkExtractor(allow=('start=\d+',),allow_domains=('hr.tencent.com')),follow=True),
        Rule(LinkExtractor(allow=(r'position_detail.php',),allow_domains=('hr.tencent.com')),callback='parseJobDetail',follow=True)
    ]

    def parseJobDetail(self, response):
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



