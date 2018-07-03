import requests
import re
from lxml import etree
import os

def main():

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    url = 'https://www.jianshu.com/c/7b2be866f564?utm_medium=index-collections&utm_source=desktop'
    response = requests.get(url,headers=headers)
    # print(response.text)
    html = etree.HTML(response.text)
    url_list = []

    list = html.xpath('.//li[@class="have-img"]')
    
    for i in list:
        title = i.xpath('.//div[@class="content"]/a[@class="title"]/text()')[0]
        writer = i.xpath('.//a[@class="nickname"]/text()')[0]
        link = i.xpath('.//div[@class="content"]/a[@class="title"]/@href')[0]
        fullurl = 'https://www.jianshu.com/' + link
        print(title,writer,fullurl)
        url_list.append(fullurl)
        if not os.path.exists(title):
            os.mkdir(title)

if __name__ == '__main__':
    main()