from urllib.request import Request,urlopen
import urllib.parse as parse
import re
import ssl
url='http://www.yggk.net/xiaohua/xiaohua/list1.html'


# print(response.code)
context = ssl._create_unverified_context()
response = urlopen(url,context=context)
resultcontent = response.read().decode('gbk')

# pattern=re.compile('<a.*?target="_Blank">.*?<img.*?src="(.*?)".*?>',re.S)
# result=re.findall(pattern,html)
# print(result)

pattern1=re.compile('<img.*?class="lazy".*?data-original="(.*?)".*?>',re.S)
result1=re.findall(pattern1,resultcontent) 
print(result1)

for i in result1:
    respone = urlopen(i,context=context)
    a = respone.read()
    filename=i[-10:]
    with open('pic/'+filename,'wb') as f :
        f.write(a)