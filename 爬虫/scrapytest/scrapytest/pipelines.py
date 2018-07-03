# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
# 管道文件:处理,清洗数据
# 数据保存,持久化
class ScrapytestPipeline(object):

    def __init__(self):
        # 连接数据库
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.tengxun # db = client['tengxun']
        self.jobs = self.db.jobs
        # self.file = open('job.json','a+')

    def open_spider(self,spider):
        print('spider启动')
        pass


    def process_item(self, item, spider):
        #先把数据转化成字典类型,再往mongo里插入数据

        self.jobs.insert(dict(item))
        # print(item)
        print(type(item))
        return item


    def close_spider(self,spider):
        self.client.close()
        print('spider执行结束')
        pass
