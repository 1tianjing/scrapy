from bs4 import BeautifulSoup
import requests
from lxml import etree
import csv

url = 'https://hr.tencent.com/position.php?&start=0#a'
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
}

response = requests.get(url,headers=header)
# print(response.status_code)

with open('qche.html','w') as f:
    f.write(response.text)
html = response.text
# xhtml = etree.HTML(response.text)
soup = BeautifulSoup(open('qche.html'),'lxml')
# print(soup.prettify())
# print(type(soup))
# result = soup.find_all('tr')
result1 = soup.find_all(class_='even')
result2 = soup.find_all(class_='odd')
result = result1+result2

for tr in result:
    # print(tr)
    title = tr.select('td a')[0].get_text()
    job_type = tr.select('td')[1]  #获取所有的td标签
    need_pople = tr.select('td')[2].get_text
    adress = tr.select('td')[3].get_text
    publish = tr.select('td')[4].get_text
    
    print(title,job_type,need_pople,adress,publish)
    

    # dict = {
    #     'title':title,
    #     'job_type':job_type,
    #     'need_pople':need_pople,
    #     'adress':adress,
    #     'publish':publish,
    # }
    # with open('zhiwei.scv','a') as csvfile:
    #     # 创建一个csv的文件操作句柄
    #     fieldnames = ['title','job_type','need_pople','adress','publish'] 
    #     write = csv.DictWriter(csvfile,fieldnames=fieldnames)
    #     write.writerow(csvfile)