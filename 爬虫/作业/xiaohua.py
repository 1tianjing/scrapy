# import urllib.request,urllib.parse
from urllib.request import Request,urlopen
import re
# 构造请求
# req = urllib.request.Request(url,headers=headers)
# response = urllib.request.urlopen(req)

# req = Request(url,headers=headers)
# response = urlopen(req)

def get_data(url,startpage,endpage):
    for i in range(startpage,endpage+1):
        # print(i)
        fullurl = url + 'list%s.html'%i
        # 构建完整的url
        # print(fullurl)
        # 调用方法发起请求
        send_requset(fullurl)

def send_requset(fullurl):
    # print(fullurl)

    req = Request(fullurl)
    # 直接使用urlopen打开网址不是说这个方法不可以使用，而是当我们需要添加headers或
    # 则是其他参数的时候，有些参数这个方法没有，所有我们需要使用Resquest请求
    response = urlopen(req)
    html = response.read().decode('gbk')
    # print(response.read().decode('gbk'))
    compile1 = re.compile('<li.*?_Blank.*?<img.*?src="(.*?)".*?<p>(.*?)</p>',re.S)
    # result_image = re.findall(compile1,html)
    # print(result_image)
    compile2 = re.compile('<img.*?class="lazy".*?data-original="(.*?)".*?<p>(.*?)</p>',re.S)
    result2_image = re.findall(compile1,html) + re.findall(compile2,html)
    print(result2_image)
    for info in result2_image:
        download_image(info[1].replace(' ','').replace('<b>','').replace('</b>',''),info[0])
        infotext = ':'.join(info).replace(' ','').replace('<b>','').replace('</b>','')
        print(infotext)
        with open('xiaohua.txt','a') as f:                               
            f.write(infotext+'\n')

def download_image(filename,image_url):
    respnse = urlopen(image_url)
    filename = filename + image_url[-4:]
    with open('xiaohua/'+filename,'wb') as f:
        f.write(respnse.read())

def main():
    startpage = input('请输入开始的页码(从1开始):')
    endpage = input('请输入结束页码：')
    print(startpage,endpage)
    url = 'http://www.yggk.net/xiaohua/xiaohua/'
    get_data(url,int(startpage),int(endpage))

if __name__ == '__main__':
    main()