from concurrent.futures import ThreadPoolExecutor
import requests
import threading
import os
from lxml import etree
import re
from urllib.request import urlopen
# https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=1
# https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=2
# https://www.jianshu.com/c/7b2be866f564?utm_medium=index-collections&utm_source=desktop
def get_data(url):
    print('开始下载'+url)
    print(threading.current_thread().name)
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    response = requests.get(url,headers=header) 
    if response.status_code == 200:
        return response.text
        # print(response.text)
def done(future):
    text = future.result()
    html = etree.HTML(text)
    li = html.xpath('//li[@class="have-img"]')
    # print(li)
    #https://www.jianshu.com/p/de0074bf6e4c
    url_list = []
    for i in li:
        title_url = i.xpath('.//div[@class="content"]/a[@class="title"]/@href')[0]
        title = i.xpath('.//div[@class="content"]/a[@class="title"]/text()')[0]
        # print(title_url,title)
        urls = 'https://www.jianshu.com/' + title_url
        url_list.append(urls)
        if not os.path.exists(title):
            #如果不存在，则创建文件夹
            os.mkdir(title)
    # print(url_list)
    all_pool(url_list)

def all_pool(url_list):
    chapterpool = ThreadPoolExecutor(3)
    for url in url_list:
       a = chapterpool.submit(all_url,url)
       a.add_done_callback(all_list)
    chapterpool.shutdown(True)

def all_url(url):
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url,headers=header) 
    if response.status_code == 200:
        return response.text

def all_list(future):
    text = future.result()
    html = etree.HTML(text)
    article = html.xpath('//div[@class="article"]')
    img_list = []
    for itm in article:
        title = itm.xpath('.//h1/text()')[0]
        name = itm.xpath('.//span[@class="name"]/a/text()')[0]
        time = itm.xpath('.//span[@class="publish-time"]/text()')[0]
        content = itm.xpath('.//div[@class="show-content-free"]/p/text()')
        img = itm.xpath('.//div[@class="image-view"]/img/@data-original-src')
        filename = title + '/' + title + '.txt'
        img1 = []
        for i in img:
            imgs = 'https:' + i
            img1.append(imgs)
        if len(content) !=0:
            dict = name + '\n' + time + '\n' + content[0]
            with open(filename,'w') as f:
                f.write(dict)
        elif len(content) == 0:
            dict =name + '\n' + time
            with open(filename,'w') as f:
                f.write(dict)
        imglist = []
        imglist.append(title)
        imglist.append(img1)
        img_list.append(imglist)
        # print(img1)
        
    all_img(img_list)
def all_img(img_list):
    for item in img_list:
        # print(item)
        a = 1
        for i in item[1]:
            # print(i)
            response = urlopen(i)
            # print(response.read())
            filename = item[0] + '/' + item[0]+ str(a) + '.jpg'
            with open(filename,'wb') as f:
                f.write(response.read())
            a = a+1

def main():
    pool = ThreadPoolExecutor(2)
    for i in range(1,2):
        url = 'https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=' + str(i)
        a = pool.submit(get_data,url)
        a.add_done_callback(done)
    pool.shutdown(True)


if __name__ == '__main__':
    main()