# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 目标文件，在这里定义目标数据，用来存储，
# 可以理解为一个model
class JobboleprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 用css来提取数据
    # 封面
    coverImage = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 标签
    tags = scrapy.Field()
    # 文章的详情链接
    url = scrapy.Field()
    #图片的本机路径
    coverImageLocalpath = scrapy.Field()

