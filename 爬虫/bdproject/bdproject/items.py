# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BdprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #评分
    grade = scrapy.Field()
    #评论
    comment = scrapy.Field()
    #简介
    intro  = scrapy.Field()
    #更多行程
    route = scrapy.Field()


class LXprojectItem(scrapy.Item):
    #标题
    title = scrapy.Field()
    #路线1
    way1 = scrapy.Field()
    #路线2
    way2 = scrapy.Field()
