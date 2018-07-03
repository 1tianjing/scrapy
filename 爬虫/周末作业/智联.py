from concurrent.futures import ThreadPoolExecutor
import threading
import requests
from lxml import etree
import os


def basic_page_git(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    request_page = requests.get(link,headers=headers)
    #print('线程', threading.current_thread().name, '正在运行')
    #print('请求状态码:',request_page.status_code)
    return request_page

def analysis_page(future):
    page = future.result()
    html = etree.HTML(page.text)
    stay_analysis_page = html.xpath('//*[@id="newlist_list_content_table"]//table')
    for i in stay_analysis_page:
        link = i.xpath('.//div/a[1]/@href')
        if len(link) != 0:
            #print('线程', threading.current_thread().name, '正在运行')
            request_son_webpage_thread_pool(link)


def request_son_webpage_thread_pool(link):
    pool = ThreadPoolExecutor(5)
    for i in link:
        a = pool.submit(request_son_webpage, i)
        a.add_done_callback(analysis_son_webpage)
    pool.shutdown()

def request_son_webpage(i):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    request_son_page = requests.get(i, headers=headers)
    #print('线程', threading.current_thread().name, '正在运行')
    # print('请求状态码:',request_page.status_code)
    return request_son_page

def analysis_son_webpage(future):
    page = future.result()
    html = etree.HTML(page.text)
    e = html.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()')#标题
    n = html.xpath('/html/body/div[6]/div[1]/ul/text()')
    q = html.xpath('/html/body/div[6]/div[1]/ul/li/span/text()')#基本详情标题
    w = html.xpath('/html/body/div[6]/div[1]/ul/li/strong/text()')#基本详情内容
    a = html.xpath('//*[@id="span4freshdate"]/text()')#发布日期
    v = html.xpath('/html/body/div[6]/div[1]/ul/li[8]/strong/a/text()')#工作性质
    c = html.xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]/text()')#职务描述标题
    b = html.xpath('/html/body/div[6]/div[1]/div[1]/div/div[1]//text()')#职务描述详情
    p = html.xpath('/html/body/div[6]/div[2]/div[1]/p/a/@href')[0]


    request_company = requests.get(str(p))
    company = etree.HTML(request_company.text)
    company_q = company.xpath('/html/body/div[2]/div[1]//text()')
    company_w = company.xpath('/html/body/div[2]/div[1]/div[2]//text()')


    #print(w)
    if not os.path.exists('F:/Users/lenovo/request/第二周作业/'+e[0]):
        os.mkdir('F:/Users/lenovo/request/第二周作业/'+e[0])
    with open(e[0]+'/'+ c[0] + '.txt','a') as f:
        for i in q:
            f.write(i)

        f.write('\n')
        for i in w:
            name = i.replace("\xa0", "")
            f.write(name)
        f.write(a[0])
        f.write(v[0])
        f.write('\n')
        for i in b:
            name = i.replace("\n","").replace("\xa0", "")
            f.write(name+'\n')
        for i in company_q:
            name = i.replace("\r\n", "")
            f.write(name+'\n')





def establish_thread_pool(url):
    pool = ThreadPoolExecutor(5)
    for i in range(1, 2):
        link = url + str(i)
        a = pool.submit(basic_page_git,link)
        a.add_done_callback(analysis_page)
    pool.shutdown()
