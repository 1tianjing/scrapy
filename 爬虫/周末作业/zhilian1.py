import requests
from lxml import etree
def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    response = requests.get('https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E6%8A%80%E6%9C%AF&sm=0&p=1',headers=headers)
    html = etree.HTML(response.text)
    list = html.xpath('.//*[@id="newlist_list_content_table"]//table')
    for i in list:
        link = i.xpath('.//div/a[1]/@href')
        print(link)








if __name__ == '__main__':
    main()