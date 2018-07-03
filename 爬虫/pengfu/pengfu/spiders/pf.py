# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pengfu.items import PengfuItem

class PfSpider(CrawlSpider):
    name = 'pf'
    allowed_domains = ['pengfu.com']
    start_urls = ['https://www.pengfu.com/xiaohua_1.html']

    PfListRult = LinkExtractor(allow=r'pengfu.com/xiaohua_1.html')
    PfDetaRult = LinkExtractor(allow=r'pengfu.com/xiaohua_\d+.html')

    Rults = (
    Rule(PfListRult, follow=True),
    Rule(PfDetaRult, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        item = PengfuItem()

        # # 头像
        # head_portrait = scrapy.Field()
        # # 作者
        # author = scrapy.Field()
        # # 标题
        # title = scrapy.Field()
        # # 文章
        # article = scrapy.Field()

        item['head_portrait'] = response.xpath('.//div[class="@w645 fl"]//a[@class="mem-header"]/img/@src/text').extract()
        item['author'] = response.xpath('.//div[class="@w645 fl"]//p/a/text()').extract()
        item['title'] = response.xpath('.//div[class="@w645 fl"]/h1/a/text()').extract()
        item['article']  =response.xpath('.//div[4]/text()').extract()
        yield item