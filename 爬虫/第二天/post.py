from urllib.request import Request,urlopen
import re
import urllib.parse as parse
import ssl

url='https://www.so.com/s?ie=utf-8&src=dlm&shb=1&hsid=74ccbb4e94968c72&ls=n191cf9929f&q=%E7%BE%8E%E5%A5%B3'
# response=urlopen(url)
# resultcontext = response.read().decode('utf-8')
# print(resultcontent)
# pattern = re.compile('',re.S)
# result = re.findall(pattern,resultcontext)
# print(result)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}
req = Request(url,headers=headers) #请求
response = urlopen(req)            #打开req  获取
print(response.read().decode())    #读取 转译

#构造一个post请求
data = {
    'q':'美女',
    'ie':'utf-8',
}
data = parse.urlencode(data).encode('utf-8')  
context = ssl._create_unverified_context() 
req = Request('https://httpbin.org/post',data=data,headers=headers,method='POST')
response = urlopen(req,context=context)
print(response.read().decode('utf-8'))