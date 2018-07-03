from urllib.request import Request,urlopen
import urllib.parse as parse

url='http://www.baidu.com'
response = urlopen(url)
# print(response.read().decode('utf-8'))
# print(response.code)
print(response.getheader('Bdqid'))
