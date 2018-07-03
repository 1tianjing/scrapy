#pip install requests
#http://docs.python-requests.org/
import requests

#使用requests发get起一个请求
# response = requests.get('http://docs.python-requests.org/')
#发起一个带参数get的请求
#https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E7%88%AC%E8%99%AB&rsv_
dict = {
    'wd':'爬虫',
}
# response = requests.get('https://www.baidu.com/s',params=dict,proxies=proxy)
# print(response.url)

#发起一个请求默认是会验证SSL证书，这里verify设置为False意思就是关闭（忽略验证）
# response = requests.get('https://www.12306.com',verify = False)

#设置代理
proxy = {
    'https':'https://125.120.10.240:6666',
}
response = requests.get('https://www.baidu.com',params=dict,proxies=proxy)

# #响应的状态码
print(response.status_code)
# #响应结果
# print(response.text)
# #字节类型  b'xxxxx'
# print(response.content)
# #查看当前请求的网址
# print(response.url)
# #获取响应的头
# print(response.headers)

#可以直接读取cookie
cookie = response.cookies
# print(cookie)

cookie_str=''

for i in cookie:
    print(i.name,i.value)
    cookie_str = cookie_str+i.name+'='+i.value+';'
print(cookie_str[:-1])


