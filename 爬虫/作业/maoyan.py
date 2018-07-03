from urllib.request import Request,urlopen
from urllib import parse
import ssl
import re
def tiebaSpider(url,beginPage,endPage):
    b=[]
    for page in range(beginPage,endPage + 1):  #循环
        pn = (page-1)*12
        fullurl=url+'offset='+str(pn) #路径加页数  构成一个新的路径
        #print(fullurl)
        response=urlopen(fullurl)  #打开fullurl  获取信息
        resultcontent=response.read().decode('utf-8')  #读取信息  再转义
        #匹配正则
        pattern=re.compile('<div.*?cinema-info.*? href="(.*?)".*?>(.*?)</a>.*?cinema-address">(.*?)</p>',re.S)
        #寻找读取到的信息
        result=re.findall(pattern,resultcontent)
        for i in result:
            b.append(i) #将获取到的信息追加到b
    with open('filename.txt','a') as f:  #打开文件
        f.write(str(b))  #将b写入到文件中
        print('完成')
def main():
    beginPage=int(input("请输入起始页："))
    endPage=int(input("请输入终止页"))
    url = 'http://maoyan.com/cinemas?'
    tiebaSpider(url,beginPage,endPage)

if __name__ =='__main__':
    main()
#自己调用自己

        