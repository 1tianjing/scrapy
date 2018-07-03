#Xpath选择器
import requests
from lxml import etree
import re
# 注意，此处缺少一个 </li> 闭合标签
text = '''
<div>
    <ul>
         <li class="item-0">
             <a href="link1.html">first item</a>
         </li>
         <li class="item-1" id='item-1'>
             <a href="link2.html">second item</a>
        </li>
        <li class="item-inactive">
        </li>
        <li class="item-1">
             <a href="link4.html">fourth item</a>
        </li>
        <li class="item-0">
            <a href="link5.html">fifth item</a>
        </li>
    </ul>
</div>
'''

# 生成了一个Element对象，也就是一个HTML文档类型，
# 这里会帮我们自动补全不完整的HTML字符串
html = etree.HTML(text)
html_str = etree.tostring(html).decode('UTF-8')
# print(html_str)
#打印补全后的结果为，这里会将对应的标签给我们补全
# <html><body><div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1" id="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>

#     </ul>
# </div>
# </body></html>
# 如果要读取本地的html那可以使用下面的方法
# etree.parse('html文件名')

#常用的几个xpath语法
# / 从根节点开始找   //li
# // 从html文本中查找目标节点，不考虑位置
# @+属性名称 表示选取属性。
# text()匹配文本
# //div/ul/li[position()<3]  表示选取最前面的两个属于 div/ul 元素的子元素的 li 元素。
# li[@class="item-1"] 表示选择取class为item-1的li标签
# li[@id="item-1"] 表示选择取class为item-1的li标签

# result = html.xpath('//li[@class="item-1"]/a/text()')
# result = html.xpath('//li[position()<3]/a/text()')
result = html.xpath('/html/body/div/ul/li[1]/a/@href')[0]
result = html.xpath('//li[1]/a/@href')[0]
result = html.xpath('//li[@id="123"]/a/@href')

result = html.xpath('//li')
# for item in result:
#     htmlstr = etree.tostring(item).decode('UTF-8')
#     # print('++++++++++')
#     # print(htmlstr.decode('UTF-8'))
#     re_rule = re.compile('<a.*?href="(.*?)">',re.S)
#     result = re.findall(re_rule,htmlstr)
#     # print(result)
#     # a = item.xpath('./a/text()')
#     if len(result) == 0:
#         result = ['未知']
#     print(result[0])
    
# print(result)
# if result:
#     a = result[0]

# print(result)

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
url = 'http://blog.jobbole.com/all-posts/'
response = requests.get(url,headers=header)
# print(response.status_code)
# print(response.text)
# with open('data.html','w') as f:
#     f.write(response.text)
page_html = etree.HTML(response.text)
article_list = page_html.xpath('//div[@class="post floated-thumb"]')
print(article_list)
for item in article_list:
    title = item.xpath('.//a[@class="archive-title"]/text()')
    link = item.xpath('.//a[@class="archive-title"]/@href')
    if len(title) == 0:
        title = ['你大爷']
    

    print(title[0])
    print(link[0])



