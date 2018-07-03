
# 清洗数据
from bs4 import BeautifulSoup

html = """ 
<hl>
<head><title>The Dormouse's story</title></head> 
<body> 
<p class="title" name="dromouse"><b>The Dormouse's story</b></p> 
<p class="story">Once upon a time there were three little sisters; and their names were <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>, <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.</p> 
<p class="story">...</p> 
"""
soup = BeautifulSoup(html,'lxml')
# prettify()帮助我们格式化的输出转换的html
# print(soup.prettify)
# print(soup.p)
# print(soup.head)
# print(soup.p.attrs)  #获取标签所有的属性

# 假删属性
# del soup.p['class']
# print(soup.p)

#findall()
result = soup.find_all('p')
# print(result)
for i in result: 
    print(i)
    print(i.attres)
    print(i.name)
    # print(i.string）
    print(i.get_text())


