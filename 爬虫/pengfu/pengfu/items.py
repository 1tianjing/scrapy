# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PengfuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #头像
    head_portrait = scrapy.Field()
    #作者
    author = scrapy.Field()
    #标题
    title = scrapy.Field()
    #文章
    article = scrapy.Field()
