# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bdproject.items import BdprojectItem,LXprojectItem

class BdSpider(CrawlSpider):
    name = 'bd'
    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all']
    # redis_key = ':bd:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'https.*?t-all_s-all_a-all_l-all'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https.*?lvyou.baidu.com/zhongguo'),callback='parse_detail', follow=True),
        Rule(LinkExtractor(allow=r'https.*?lvyou.baidu.com/zhongguo/luxian'),callback='parse_lx', follow=True)
    )

    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        print(response.status)
        print(response.url)
        pass
    def parse_detail(self,response):
        # print(response.status)
        item = BdprojectItem()

        item['title'] = response.xpath('.//div[@class="dest-name "]/span[@class="main-name clearfix"]/a/text()').extract_first('')
        item['grade'] = response.xpath('.//div[@class="main-score"]/text()').extract_first('')
        item['comment'] = response.xpath('.//div[@class="main-score"]/a[@class="remark-count"]/text()').extract_first('')
        item['intro'] = response.xpath('.//p[@class="main-desc-p"]/text()').extract_first('')
        item['route'] = scrapy.Field('.//div[@class="title-ul"]/a[@herf]')

        # print(response.status)
        # print(response.url)

        yield  item

    def parse_lx(self,response):
        item = LXprojectItem()
        item['title'] = response.xpath('.//div[@class="path-info-container"]//div[@class="plan-title-box"]/a/text()').extract_first('')
        item['way1'] = response.xpath('.//div[@class="path-info-container"]//div[@class="day-dest"][1]/span/text()').extract_first('')
        item['way2'] = response.xpath('.//div[@class="path-info-container"]//div[@class="day-dest"][2]/span/text()').extract_first('')

        # print(response.status)
        # print(response.url)

        yield item



