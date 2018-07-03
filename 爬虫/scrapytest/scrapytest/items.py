# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 设置要保存的字段信息
class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称, 工作地点, 职位类别, 工作职责, 工作要求
    jobName = scrapy.Field()
    workLocation = scrapy.Field()
    jobType = scrapy.Field()
    jobDesc = scrapy.Field()
    jobInfo = scrapy.Field()
    pass
