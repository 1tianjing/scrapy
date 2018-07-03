
# -*- coding: utf-8 -*-
import scrapy
from ecy.items import EcyItem

class EcyspiderSpider(scrapy.Spider):
    name = 'ecyspider'
    allowed_domains = ['bcy.net']
    start_urls = ['https://bcy.net/illust']

    def parse(self, response):
        # https://bcy.net/circle/timeline/showtag?since=25101.527&grid_type=flow&sort=hot&tag_id=5798
        picids = response.xpath('.').re(r'<li class="js-smallCards _box" data-since="(.*?)">')[0]
        print(picids)
        for i in range(1,5):
            url = 'https://bcy.net/circle/timeline/showtag?since=%s&grid_type=flow&sort=hot&tag_id=5798'%(float(picids)-0.03*i)
            yield scrapy.Request(url, callback=self.picParse)


    def picParse(self,response):
        names = response.xpath('.').re(r'<span\sclass="fz12\slh18\susername\scut\sdib\svam">(.*?)</span>')
        comments = response.xpath('.').re(r'<span\sclass="like">(.*?)</span>')
        picUrls = response.xpath('.').re(r'<img\s*?class="cardImage"\s*?src="(.*?)">\s*?</a>')
        for i in range(0,len(names)):
            item = EcyItem()
            item['name'] = names[i]
            item['comment'] = comments[i]
            item['picUrl'] = picUrls[i]
            yield item
        # print(picUrl)