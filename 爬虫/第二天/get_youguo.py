from urllib.request import Request,urlopen
import urllib.parse as parse
import re
import ssl

url = 'https://www.ugirls.com/'
context = ssl._create_unverified_context()
response = urlopen(url,context=context)          
resultcontent = response.read().decode('utf-8')
# 构建一个正则对象
#
pattern1 = re.compile('<img.*?model_img\slazy.*?data-original="(.*?)".*?alt=.*?>',re.S)
# pattern = re.compile('<img.*?magazine_img.*?src="(.*?)".*?data-original.*?>',re.S)
# result = re.findall(pattern,resultcontent)
# print(result)
result = re.findall(pattern1,resultcontent)
print(result)  
for i in result:
    response = urlopen(i,context=context)  #打开每一个链接
    a = response.read()                    #读取信息
    filename = i[-10:]                     #文件名字=后十位
    with open('pic/'+filename,'wb') as f:  #打开pic
        f.write(a)                         #写入a

