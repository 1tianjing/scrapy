# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#继承CrawlSpider,CrawlSpider又继承自Spider
class CrawljobboleSpider(CrawlSpider):
    name = 'crawlJobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']


    # allow：满足括号中“正则表达式”的值会被提取，如果为空，则全部匹配。
    # deny：与这个正则表达式(或正则表达式列表)不匹配的URL一定不提取。
    # restroct_xpaths 如果指定了xpath路径,那么allow只能在制定了xpath路径下取匹配
    # restrict_css同上


    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
