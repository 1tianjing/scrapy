# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from datetime import datetime

class ExamplePipeline(object):
    def process_item(self, item, spider):
        #是一个时间搓
        # item["crawled"] = datetime.utcnow()
        #爬虫的名称
        # item["spider"] = spider.name
        print('经过了pipeline')
        return item
