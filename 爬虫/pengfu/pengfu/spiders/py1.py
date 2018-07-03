# -*- coding: utf-8 -*-
import scrapy


class Py1Spider(scrapy.Spider):
    name = 'py1'
    allowed_domains = ['pengfu.com']
    start_urls = ['http://pengfu.com/']

    def parse(self, response):
        pass
