from pyquery import PyQuery
import lxml
import requests

url = 'http://blog.jobbole.com/all-posts/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
response = requests.get(url,headers=headers)
# print(response.status_code)
with open('bole.html','w') as f:
    f.write(response.text)


pq_html = PyQuery(response.text)
# pq_html = PyQuery(filename='bole.html')

pq_html = PyQuery(url)
# print(pq_html.html())
# print(type(pq_html))

result_articles = pq_html('.post.floated-thumb')
# print(result_articles.items())

for sub_div in result_articles.items():
    print('————————我是分割线—————————')
    # print(sub_div)
    title = sub_div(".archive-title").text()
    link = sub_div(".archive-title").attr('href')

    print(title,link)
    # print(sub_div.children()) #获取子元素/
    # print(sub_div.hasClass('da'))

