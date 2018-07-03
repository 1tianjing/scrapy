# -*- coding: utf-8 -*-
import scrapy


class Tencent1Spider(scrapy.Spider):
    name = 'tencent1'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/']

    def parse(self, response):
        pass
