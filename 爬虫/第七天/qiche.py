import requests
from bs4 import BeautifulSoup
import re
import csv
import json

#发起一个请求
header = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36'

}
url = 'https://www.autohome.com.cn/all/1/'
response = requests.get(url,headers=header)
# print(response.status_code)  #打印响应状态  看是否成功
# print(response.text)

#构建一个bs对象
soup_html = BeautifulSoup(response.text,features='html.parser')
# print(soup_html.prettify())  #以规范的html文输出

article_list = soup_html.select('.article li')
# print(article_list) 

objids = []
article_dict_list = []
for item in article_list:
    # print(item)
    # print(type(item))
    if len(item.select('a')) != 0:
        title = item.select('h3')[0].get_text()
        #获取属性的两种方式
        href = item.select('a')[0].attrs['href']
        # href1 = item.select('a')[0].get('href')
        image_url = item.select('.article-pic img')[0].attrs['src'] 
        publish_time = item.select('.fn-left')[0].get_text()
        content = item.select('p')[0].get_text()
        visit_num = item.select('.fn-right em')[0].get_text()
        comment_num = item.select('.fn-right em')[1].get_text()
        #分析页面之后我们发现要从文章详情的url中获取文章的id
        #//www.autohome.com.cn/news/201806/918204.html#pvareaid=

        #//www.autohome.com.cn/news/201806/918204-5.html#pvareaid=102624

        #//www.autohome.com.cn/drives/201806/918204-5.html#pvareaid=102624

        #//www.autohome.com.cn/advice/201806/918123.html#pvareaid=102624

        #//www.autohome.com.cn/culture/201806/918288.html#pvareaid=102624

        #//www.autohome.com.cn/drive/201806/916111-5.html#pvareaid=102624

        #//www.autohome.com.cn/drive/201806/915188-6.html#pvareaid=102624

        #//www.autohome.com.cn/tech/201806/917978.html#pvareaid=102624

        # a = re.compile(r'.*?cn.*?/\d*/(.*?)[-,.].*?html')
        a = re.compile('.*?cn.*?/\d*?/(.*?)[-,.].*?html')
        # a = re.compile(r'//www.autohome.com.cn/\w*?/\d*?/(\d*?)\W*\s*.html#pvareaid=\d*?',re.S)
        # objid = re.findall(a,href)[0][:6]
        objid = re.findall(a,href)[0]
        objids.append(objid)
        dict = {
            'title':title,
            'href':href,
            'image_url':image_url,
            'publish_time':publish_time,
            'content':content,
            'visit_num':visit_num,
            'comment_num':comment_num,
            'objid':objid,
        }
        article_dict_list.append(dict)
        # print(title,href,image_url,publish_time,content,visit_num,comment_num)
        # print(href)
print(len(objids))
# print(objids)

objids_str = '.'.join(objids)
# print(type(objids_str))
# print(objids_str)
url = 'https://reply.autohome.com.cn/api/getData_ReplyCounts.ashx'
params = {
    'appid':'1',
    'dateType':'jsonp',
    'objids':objids_str,
}
com_response = requests.get(url,params=params,headers=header)
# print(com_response.text)
# print(com_response.status_code)
com_data = com_response.text.replace('(','').replace(')','').replace("'",'"')
# print(com_data)
com_list = json.loads(com_data)['commentlist']
# print(type(com_list))
# print(len(com_list))

# print(article_dict_list[0])
with open('qichezhijia.csv','a') as csvfile:
    filedNames = ('title','href','image_url','publish_time','content','visit_num','comment_num','objid')
    writer = csv.DictWriter(csvfile, fieldnames=filedNames)
    writer.writeheader()
    for i in range(0,len(com_list)):
        print(i)
        com_dict = com_list[i]
        article_item = article_dict_list[i] 
        article_item['comment_num'] = com_dict['replycountall']
        # print(article_item)
        writer.writerow(article_item)



# print(response.json())







#获取评论列表数据
#目标url为：
#https://reply.autohome.com.cn/api/getData_ReplyCounts.ashx?
# appid=1&dateType=jsonp&
# objids=918391.918393.917966.918351.918385.918383.918348.918371.918379.918369.918374.918370.918360.918357.918359.918347.912740.918337.918350.918349.918341.918338.918343.918345.918342.918340.917871.918339.918333.918244.918334.918336.918105.917978.916111.915188.918335.918332.918288.918312.918325.918327.918330.918311.918320.918316.918318.918317.918256.918310.918313.918308.918307.918304.918305.918299.918283.918284.918204.918300&callback=jQuery172043917176046810547_1528424385514&_=1528424388486    
