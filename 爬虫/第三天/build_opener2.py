import urllib.request as request
import http
import ssl
import requests

#requests.get()

#自定义opener
#之前使用的是urlopen()

context = ssl._create_unverified_context()
#构建一个HTTPSHandler  处理器对象，支持处理HTTP请求
https_handler = request.HTTPSHandler(context=context,debuglevel=1)
opener = request.build_opener(https_handler)
#构建一个HTTPSHandler  处理器对象，之处处理HTTPS请求
#https_handler = request.HTTPHandler()
#调用urllib.request.Request方法，创建支持处理HTTP请求的opener对象
#opener = request.build_opener(http_handler)
req_header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}
url = "http://www.baidu.com"
req = request.Request(url)
response = opener.open(url)
print(response.code)