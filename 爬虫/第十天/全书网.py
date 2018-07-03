from concurrent.futures import ThreadPoolExecutor
import re
import requests
import os

#设置线程池
pagePool = ThreadPoolExecutor(5)
textPool = ThreadPoolExecutor(5)
finishPool = ThreadPoolExecutor(5)


def search(url, tp):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',

    }
    #发起请求
    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'  #解码
    if tp == 1:
        a = r'更多</a></em><a\shref="(.*?)"\sclass="readTo">马上阅读</a></span></li'
        ret = re.compile(a, re.S)
        ret = re.findall(ret, response.text)
        return ret
    elif tp == 2:
        text = response.text
        title = r'<DIV class=dirtitone><H2>(.*?)</H2></div>'
        title = re.compile(title, re.S)
        title = re.findall(title, text)
        os.mkdir(title[0])
        print(title[0],'创建成功')
        b = r'<DIV\sclass="clearfix dirconone">(.*?)</DIV> '
        b = re.compile(b, re.S)
        b = re.findall(b, text)
        a = r'<li><a\shref="(.*?)"\stitle="(.*?)">.*?</a></li>'
        ret = re.compile(a, re.S)
        ret = re.findall(ret, b[0])
        return ret,title
    elif tp == 3:
        book = response.text
        a = r'<div\sclass="mainContenr".*?><script\stype="text/javascript">.*?;</script>(.*?)<script\stype="text/javascript">.*?</script></div>'
        a = re.compile(a, re.S)
        a = re.findall(a, book)
        return a


def textDone(future):
    texts,title = future.result()
    for text in texts:
        book = search(text[0], 3)
        book = str(book[0]).replace('&nbsp;','').replace('<br />','').replace(r'\n','')
        name = '%s/%s.txt'%(title[0],text[1])
        print(name)
        with open(name, 'w') as f:
            f.write(book)


def bookDone(future):
    books = future.result()
    for book in books:
        a = r'.*?_(\d*?).html'
        ret = re.compile(a, re.S)
        ret = re.findall(ret, book)
        url = 'http://www.quanshuwang.com/book/%s/%s' % (ret[0][:3], ret[0])
        handler = textPool.submit(search, url, 2)
        handler.add_done_callback(textDone)
    textPool.shutdown()


def main():
    urls = [
        'http://www.quanshuwang.com/list/1_1.html'
    ]
    for url in urls:
        handler = pagePool.submit(search, url, 1)
        handler.add_done_callback(bookDone)

    pagePool.shutdown()


if __name__ == '__main__':
    main()
