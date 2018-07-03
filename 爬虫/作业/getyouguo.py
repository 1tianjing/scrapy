from urllib.request import Request,urlopen
from urllib import parse
import ssl
import re
def tiebaSpider(url, beginPage, endPage):
    b = []
    for page in range(beginPage, endPage + 1):
        #url+页数 构成一个完整的路径
        fullurl = url + str(page) + '.html'
        # print(fullurl)
        #获取网址
        reqponse = urlopen(fullurl)
        #读取页面 转义
        resultcontent = reqponse.read().decode('utf-8')
        pattern = re.compile('<img.*?magazine_img.*?data-original="(.*?)".*?alt.*?>',re.S)
        result = re.findall(pattern,resultcontent)
        for i in result:  #循环遍历
            b.append(i)  #追加到b里面
    # print(b)
    writes(b)  #将b传到函数writes中
    
    #<img class="magazine_img lazy" 
    # src="https://img.ugirls.tv/uploads/magazine/cover/2014/10/29/a785b00a3a8c6e0b3ae4a2ba2b85b0b8_cover_web_l.jpg" 
    # data-original="https://img.ugirls.tv/uploads/magazine/cover/2014/10/29/a785b00a3a8c6e0b3ae4a2ba2b85b0b8_cover_web_l.jpg" 
    # alt="[E050]尤果网Miko梦露" width="" height="" style="display: block;">
def writes(b):
    a = 1
    for i in b:
        print("正在保存")
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }  #浏览器访问地址
        #忽略https访问请求
        requestContent = ssl._create_unverified_context()
        # 网址  地址   = request
        request = Request(i, headers=headers)
        #获取  可以忽略https的访问协议  打开网址获取信息赋值给response
        response = urlopen(request,context=requestContent)
        #读取获取的信息
        image = response.read()
        # 将字符串赋值到filename(文件)
        filename = str(a) + '.jpg'
        # 打开filename  别名 f  wb:以二进制的形式打开一个文件 如果存在就覆盖  不存在就新建
        with open(filename, "wb") as f:
            #将获取到的信息写入f
            f.write(image)
            print("已成功下载"+filename)
        a = a + 1  #每循环一次就加1

def main():
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))
    url = 'https://www.ugirls.com/Index/Search/Magazine-57-'
    tiebaSpider(url,beginPage,endPage)  #传参数

if __name__ == '__main__':
    main()
#自己调用自己