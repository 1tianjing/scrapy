# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

class jobboleArticleImagePipleline(ImagesPipeline):
    # IMAGE =

    def get_media_requests(self, item, info):
        #根据图片链接构造一个requests,给调度器,放在任务队列里
        image_url = item['coverImage']
        yield  scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        #图片任务下载完成之后会执行这个方法
        # imagepaths = [x for ok, x in results if ok]
        #
        # if imagepaths:
        #     image_path = imagepaths[0]['path']
        #     item['coverImageLocalpath'] = image_path

        for ok,value in results:
            if ok:
                image_path = value['path']
                item['coverImageLocalpath'] = image_path
                return item





class JobboleprojectPipeline(object):
    def process_item(self, item, spider):
        return item




# class JobboleprojectPipeline(object):
#
#     # def __init__(self):
#     #     self.client = pymysql.Connect('localhost','root','bc123','jobbole',3306,charset='utf8')
#     #     self.cursor = self.client.cursor()
#
#     def open_spider(self,spider):
#         #在这也可以写数据库信息
#         #spider文件开始执行就会执行这个方
#         print('open_spider')
#
#     # def process_item(self, item, spider):
#
#         # insert_sql = """
#         #    INSERT INTO article(coverImage,title,publishTime,content,tags,url) VALUES(%s,%s,%s,%s,%s,%s)
#         # """
#         # self.cursor.execute(insert_sql,(item['coverImage'],item['title'],
#         #                                 item['publishTime'],item['content'],
#         #                                 item['tags'],item['url'])
#         #                     )
#         # self.client.commit()
#
#         # return item
#
#
#     def close_spider(self,spider):
#         # 爬虫任务全部执行完毕，就会执行这个方法
#         self.cursor.close()
#         self.client.close()


# class JobboleprojectFilePipeline(object):
#
#     def __init__(self):
#         self.client = pymysql.Connect('localhost', 'root', 'ljh123456', 'jobbole', 3306, charset='utf8')
#         self.cursor = self.client.cursor()
#
#     def open_spider(self, spider):
#         # 在这也可以写数据库信息
#         # spider文件开始执行就会执行这个方法
#         print('open_spider')
#
#     def process_item(self, item, spider):
#         insert_sql = """
#            INSERT INTO article(coverImage,title,publishTime,content,tags,url) VALUES(%s,%s,%s,%s,%s,%s)
#         """
#         self.cursor.execute(insert_sql, (item['coverImage'], item['title'],
#                                          item['publishTime'], item['content'],
#                                          item['tags'], item['url'])
#                             )
#         self.client.commit()
#
#         return item
#
#     def close_spider(self, spider):
#         # 爬虫任务全部执行完毕，就会执行这个方法
#         self.cursor.close()
#         self.client.close()

