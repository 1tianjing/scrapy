# urllib使用代理
# 服务器把我们 的IP封掉：因为请求的次数国语频繁，超过服务器的
import urllib.request

#构建一个代理的ProxyHandler对象
handler = urllib.request.ProxyHandler({'协议':'端口号'})
# 需要用户名和密码的代理（需要验证）
# urllib.request.ProxyHandler({'协议':'用户名':密码@ip+端口号})
# 创建一个opener对象
opener = urllib.request.build_opener(handler)

# 使用opener.open方法去发起请求
response = opener.open('http://www.baidu.com')
# 查看响应的结果
print(response.code) 