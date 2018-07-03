# -*- coding: utf-8 -*-
# Spider（爬虫）：它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，
# 并将需要跟进的URL提交给引擎，再次进入Scheduler(调度器)
import scrapy
from scrapytest.items import ScrapytestItem
from urllib.parse import urljoin  #拼接网址

class TengxunSpider(scrapy.Spider):
    # 爬虫的名称  作用:启动爬虫的时候会根据名称找对应的爬虫文件
    name = 'tengxun'
    # 允许爬取的域,可以是多个  爬取的链接必须能在这个域下面  可以是多个域
    allowed_domains = ['hr.tencent.com']
    # 起始的url,可以是多个
    start_urls = ['https://hr.tencent.com/position.php']

    # 解析数据  response返回的请求访问返回的结果
    def parse(self, response):
        print(response.status)

        # print(response.body)

        #目标数据:职位名称,工作地点,职位类别,工作职责,工作要求
        job_even = response.xpath('.//tr[@class="even"]/td[@class="l square"]/a/@href').extract()
        job_odd = response.xpath('.//tr[@class="odd"]/td[@class="l square"]/a/@href').extract()
        jobs = job_even+job_odd  #总的职位的链接
        for nodeurl in jobs:
            fullurl = urljoin('https://hr.tencent.com/position.php',nodeurl)
            print(fullurl)
            # yield意思是:实现异步,每当遇到yield就会暂停一下,然后先返回yield后面的值,下次再执行时,会从上次执行中断的地方开始
            yield scrapy.Request(fullurl,callback=self.parseJobDetail)


    def parseJobDetail(self,response):
        print(response.status)
        item = ScrapytestItem()
        item['jobName'] = response.xpath('.//td[@id="sharetitle"]/text()').extract()[0]
        item['workLocation'] = response.xpath('.//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        item['jobType'] = response.xpath('.//tr[@class="c bottomline"]/td[2]/text()').extract()[0]
        item['jobDesc'] = response.xpath('.//table[@class="tablelist textl"]/tr[3]//li/text()').extract()
        item['jobInfo']  = response.xpath('.//table[@class="tablelist textl"]/tr[4]//li/text()').extract()
        # print(jobName,workLocation,jobType,jobDesc,jobInfo)

        yield item