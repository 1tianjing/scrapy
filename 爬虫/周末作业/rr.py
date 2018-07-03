import requests
#创建session对象，可以保存Cookie值
ssion = requests.session()
#处理headerds
header = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36'

}
#需要登陆的用户名和密码
data={'email':'15110500442 ','password':'sjl111111'}
#发送附带用户名和密码的请求，并且获取登陆后的Cookie值，保存在ssion里
ssion.post('http://www.renren.com/PLogin.do',data=data)
#ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = ssion.get('http://www.renren.com/966301461/profile')
#打印响应内容
print(response.text)