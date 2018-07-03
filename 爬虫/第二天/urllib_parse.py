#urllib_parse:解析url,拼接，编码

import urllib.parse
url = 'https://www.so.com/s?ie=utf-8&src=dlm&shb=1&hsid=74ccbb4e94968c72&ls=n191cf9929f&q=%E7%BE%8E%E5%A5%B3'
result = urllib.parse.urlparse(url)  #urlparse:拆分一个url链接  分解出各个部分
print(result)
# schema：协议
# netloc:域名
# paht:路径
# params:参数
# query:查询条件 一般用于get请求
# fragment:锚点

# unlunparse 拼接
urls = ('https','www.so.com','/s','','ie=utf-8&src=dlm&shb=1&hsid=74ccbb4e94968c72&ls=n191cf9929f&q=%E7%BE%8E%E5%A5%B3','')
fullurl = urllib.parse.urlunparse(urls)
print(fullurl)

# unlencode：一般用于将字典序列化为url编码的格式
dict={
    'name':'a',
    'password':'l123',
}
data = urllib.parse.urlencode(dict).encode('UTF-8')
data = bytes(urllib.parse.urlencode(dict),encoding='UTF-8')
print(data)
# parse_qs:将url编码的格式反序列化为字典
result = urllib.parse.parse_qs(data)
print(result)

for k,v in result.items():
    print(k.decode('(UTF-8)'))
    print(v[0].decode('UTF-8'))
#urljoin:url的拼接
base_url = 'http://maoyan.com/cinemas'
son_url = '/cinema/15331?poi=95489636'
fullurl = urllib.parse.urljoin(base_url,son_url)
#http://maoyan.com/cinema/15331?poi=95489636的拼接结果
print(fullurl)