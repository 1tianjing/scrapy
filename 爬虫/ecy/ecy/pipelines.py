# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
import json
import pymongo
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


class EcyImagesPipline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
    def get_media_requests(self, item, info):
        '''根据图片链接构造请求'''
        imageUrl = item['picUrl'][0:-4]
        print(imageUrl)
        yield scrapy.Request(imageUrl)

    def item_completed(self, results, item, info):
        '''图片下载完成后执行这个方法'''
        dir_path = os.path.abspath(os.path.dirname(__file__))
        IMAGES_STORE = os.path.join(dir_path, 'images')
        # print(IMAGES_STORE + '/' + results[0][1]['path'])
        #
        # print('SSSSSSSSSSSSSSSSSSSSSSSS',IMAGES_STORE)
        try:
            os.rename(IMAGES_STORE + '/' + results[0][1]['path'], IMAGES_STORE + '/' + item['name'] + '.jpg')
        finally:
            localpath = IMAGES_STORE + '/' + item['name'] +  '.jpg'
            item['localLink'] = localpath
            return item





class EcyPipeline(object):
    # def __init__(self):
    #     self.filename = open('ecy.json', 'a+')
    #
    # def open_spider(self, spider):
    #     print('spider启动')
    #
    #
    # def process_item(self, item, spider):
    #
    #     json_str = json.dumps(dict(item), ensure_ascii=False) + '\n'
    #     print('dddddddddddddddddddddddddddddd', json_str)
    #
    #     self.filename.write(json_str)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.filename.close()
    #     print('spider关闭')

    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.ecy  # db = client['tencent']
        self.ecy = self.db.ecy  # jobs = db['jobss']

    def open_spider(self,spider):
        print('spider启动')

    def close_spider(self,spider):
        self.client.close()
        print('spider关闭')

    def process_item(self, item, spider):
        self.ecy.insert(dict(item))
        return item





