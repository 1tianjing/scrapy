import urllib.request
from urllib import parse
import ssl
#以豆瓣的电影搜索借口为例，构造get请求
def getajax():
    url = 'https://movie.douban.com/j/search_subjects?'
    # https://movie.douban.com/j/search_subjects?page_limit=20&page_start=40&sort=recommend&tag=%E9%9F%A9%E5%89%A7&type=tv
    # 变动的参数
    data = {
        'page_limit':'20', #页面限制
        'page_start':'40',  #页面开始
        'sort':'recommend',  #推荐分类
        'tag':'韩剧',  #标签
        'type':'tv',  #类型
    }
    #转换成url编码格式（字符串，这里不是post请求不用转换成字节，直接拼接在地址上）
    data = parse.urlencode(data)
    url = url+data
    print('urlencode转换后：'+data,'完整的get请求地址为：'+url)
    requestContext = ssl._create_unverified_context()
    #Requeset对象作为urlopen()方法的参数，发送给服务器并接受响应
    response = urllib.request.urlopen(url,context=requestContext)
    #打印结果可以知道获取的结果为一个json串
    result = response.read()
    print(type(response))
    print(result)
    print(response.url)
    print(type(dict))
    print(dict)

if __name__ == '__main__':
    getajax()
    
