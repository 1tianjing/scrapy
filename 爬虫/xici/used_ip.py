# -*— coding：UTF-8 -*-
import urllib.request
import RandomIPhandler
import ssl
import logging
handler = RandomIPhandler.RandomIPhandler()
ip = handler.get_random_ip()
print(ip)
proxy = ip[3]+'://'+ip[1]+":"+ip[2]
print(proxy)
proxy_handler = urllib.request.ProxyHandler({ip[3]:proxy}) 
context = ssl._create_unverified_context()
opener = urllib.request.build_opener(proxy_handler,urllib.request.HTTPSHandler(context=context,debuglevel=1))
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}
req = urllib.request.Request('https://www.jianshu.com/p/a5cb4070e733',headers=headers)
response = opener.open(req)
# print(response.code)
# print(response.msg)
with open('baidu.html','w') as f:
    f.write(response.read().decode('utf-8'))

