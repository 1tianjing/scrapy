import urllib.request
import http.cookiejar

#创建一个cookiesjar 对象  用来存储cookie
cookie = http.cookiejar.CookieJar()
#构建一个处理cookies的处理器  handler
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
#构建opener
opener = urllib.request.build_opener(cookie_handler)
#使用open方法向服务器发起一个请求  获取响应
response = opener.open('http://www.baidu.com')
#获取响应的状态
print(response.code)
#获取cookie
print(cookie)
#
