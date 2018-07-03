#糗事百科

import threading
import queue
import json
import requests
from lxml import etree
import ssl

# https://www.qiushibaike.com/8hr/page/2/
class ThreadCrawl(threading.Thread):
    def __init__(self,threadname,pagequeue,dataqueue):
        # 继承父类方法
        super(ThreadCrawl, self).__init__()
        #线程名称
        self.threadname = threadname
        #下载队列任务
        self.pagequeue = pagequeue
        #存放结果的队列  一开始为空
        self.dataqueue = dataqueue

        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        #print(self, threaname)

    # 重写父类的方法  目的是为了发起请求 拿到响应结果
    def run(self):
        print('爬取'+threading.current_thread().name)
        while not self.pagequeue.empty():
            print('开启'+self.threadname)
            #从任务列表里面拿代码
            page = self.pagequeue.get()
            #拼接完整的url
            fullurl = 'https://www.qiushibaike.com/8hr/page/'+ str(page)+'/'
            #发起请求，获取响应结果
            response = requests.get(fullurl,headers=self.header)
            #打印结果状态码
            # print(response.status_code)
            if response.status_code == 200:
                #将获取的结果存放在dataqueue中，让后面的解析线程解析
                self.dataqueue.put(response.text)
            #print(self.dataqueue,type(self.dataqueue))
            #print('run起来')


class ThreadParse(threading.Thread):
    def __init__(self,threadname,dataqueue,lock):
        super(ThreadParse,self).__init__()
        #threadname线程名称
        self.threadname = threadname
        #解析任务队列
        self.dataqueue = dataqueue
        #线程锁
        self.lock = lock

    def run(self):
        print('解析'+threading.current_thread().name)
        #解析获取的数据
        #判断如果队列里面有值，则继续执行，从队列中获取页码源码进行解析
        while not self.dataqueue.empty():
            html = self.dataqueue.get()
            print('获取到了')
            self.parse(html)

    def parse(self,html):
        #解析数据
        parse_data = etree.HTML(html)
        #获取段子列表
        contentList = parse_data.xpath('//div[@id="content-left"]/div')
        for sub_div in contentList:
            #取段子的发布者名称
            title = sub_div.xpath('.//h2/text()')[0]
            #取段子的内容
            content = sub_div.xpath('.//div[@class="content"]/span/text()')[0]
            dict = {
                'title':title,
                'content':content,
            }
            # print(dict)
            # print(t2)
            #加锁（是为了保证同一个资源，某一时刻只被一个线程执行）
            self.lock.acquire()
            #使用json.dumps将python对象转换成一个json字符串
            with open('duanzi.json','a') as f:
                #ensure_ascii默认是ture,是ascii编码，这里我们需要设置False
                f.write(json.dumps(dict,ensure_ascii=False)+'\n')
            #解锁（解锁后其他线程才能够使用）
            self.lock.release()



# 主线程
def mian():
    # 创建一个任务队列
    pagequeue = queue.Queue(30)
    #创建一个数据队列,将获取的请求结果，放在这个队列中
    dataqueue = queue.Queue()
    for i in range(1, 14):
        # 往任务队列中存要请求的页码
        pagequeue.put(i)
    

    # 创建线程来获取网页的内容
    # 首先创建爬取任务线程名称
    crawlnanes = ['一号', '二号', '三号']
    #来创建一个列表，存放所有的爬取线程
    threadcreaws = []
    for threadname in crawlnanes:
        #创建线程
        thread = ThreadCrawl(threadname,pagequeue,dataqueue)
        #启动线程
        thread.start()
        threadcreaws.append(thread)

        # thread.join()

    for thread in threadcreaws:
        thread.join()
    #创建一个锁，为了同一个资源,某一时刻只被一个线程执行
    lock = threading.Lock()
    #创建解析的线程名称
    parseThreadname = ['a','b','c']
    #创建list  存放所有的解析线程
    threadParse = []
    for threadname in parseThreadname:
        parsethread = ThreadParse(threadname,dataqueue,lock)
        parsethread.start()
        threadParse.append(parsethread)

    for thread in threadParse:
        thread.join()

    #打印主线程
    print(threading.current_thread().name)

if __name__ == '__main__':
    mian()
    #入口函数调用main方法
