
import requests
import re
import json
# 获取首页分类菜单

# 'http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery21109555013915685151_152844997983
# 3&pids=109499%2C109520%2C109731%2C109753%2C110549%2C109779%2C110548%2C110547%2C109757%2C109793%2C109795%2C110563%2C110546%2C110544&_=1528449979837'
# 从连接中找分类id 分类的名称
response  =requests.get('http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery2110055639624415818045_1528697742318&pids=110119&_=1528697742319')
# print(response.text)
pattern = re.compile("jQuery.*?\((.*?)\)")   
json_data = re.findall(pattern,response.text)[0]
# print(json_data)#转化成json串
data = json.loads(json_data) #转化成python对象
# print(type(data))  #返回的是一个字典
big_ategory = data['data']['110119']['list']  #取字典的键
print(big_ategory)
# print(len(big_ategory))

pids = []
for item in big_ategory:
    print(item)  #在列表循环
    pids.append(item['categoryPid'])  #循环的取categoryPid
# print(pids)
pids = ','.join(pids)  #用逗号拼接起来
print(pids)

#获取全部分类
url = 'http://mce.mogucdn.com/jsonp/multiget/3'
parmas = {
    'callback':'jQuery21109165411369411709_1528699316717',
    'pids':pids,
    '_':'1528699316718'
}
response = requests.get(url,parmas) #发起请求
print(response.text)

category_pattern = re.compile('http.*?/(\d+).*?acm',re.S)
category_list = []
user_categorys = []

all_json = re.findall(pattern,response.text)[0]
# print(all_json)

all_data = json.loads(all_json)
# print(all_data)

all_dict = all_data['data']
for k,v in all_dict.items():
    # print(k,v)
    for sub_dict in v['list']:
        title = sub_dict['title']
        id = re.findall(category_pattern,sub_dict['link'])
        print(id)
        dict = {
            title:id[0]
        }
        user_categorys.append(dict)
        category_list.append(dict)
print("尊敬的用户你可以从以下的列表中筛选商品"+'\n'+str(user_categorys))
# print(category_list)
kw = input("情书你选择的商品分类：")
startpage = int(input("请输入起始页"))
endpage = int(input("请输入结束页"))






