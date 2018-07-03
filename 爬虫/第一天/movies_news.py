import urllib.request as request
import urllib.parse as parse
#import ssl
#目标网址

url = "http://www.1905.com/"
#构造请求，发起请求，获取响应
response = request.urlopen(url)
#获取内容，用decode解码 赋值给resultcontent
resultcontent = response.read().decode('utf8')
#直接打印结果
print(response.read().decode('utf-8'))
#写入本地文件
f = open('movie.html','w')
#往文件里写入东西
f.write(resultcontent)


# with open('movie.html','w') as f:
#     f.write(resultcontent)