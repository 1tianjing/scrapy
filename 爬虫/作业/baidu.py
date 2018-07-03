import urllib.request
from urllib import parse
import ssl
def tiebaSpider(url,beginPage,endPage,key1,key2):
    """
    作用：负责处理url，分配每个url去发送请求
    url：需要处理的第一个url
    beginPage: 爬虫执行的起始页面
    endPage: 爬虫执行的截止页面
    """
    for page in range(beginPage,endPage+1):
        pn=(page-1)*10
        filename='第'+str(page)+"页.txt"
        #组合为完整的url，并且pn值每次增加50
        fullurl=url+key1+"&pn="+str(pn)+key2
        #调用loadPage()发送请求获取HTML页面
        html = loadPage(fullurl,filename)
        #将获取到的HTML页面写入本地
        writeFile(html,filename)
def loadPage(url,filename):
    '''
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        filename: 文件名
    '''

    print("正在下载"+filename)
    requestContent = ssl._create_unverified_context()
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    request=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(request,context=requestContent)
    return response.read()
    #最后如果我们希望将爬取到了每页的信息存储在本地磁盘上，我们可以简单写一个存储文件的接口
def writeFile(html,filename):
    """
        作用：保存服务器响应文件到本地磁盘文件里
        html: 服务器响应文件
        filename: 本地磁盘文件名
    """

    print("正在存储"+filename)
    with open(filename,'wb') as f:
        f.write(html)
    print("-"*20)

if __name__=="__main__":
    kw=input("请输入需要爬取的贴吧:")
    #输入其实也和终止页，str转成int类型
    beginPage=int(input("请输入起始页："))
    endPage=int(input("请输入终止页:"))
    url="http://www.baidu.com/s?"
    key1=parse.urlencode({'wb':kw})
    key2=parse.urlencode({'op':kw})
    tiebaSpider(url,beginPage,endPage,key1,key2)



