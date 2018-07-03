from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def index(request):
    return HttpResponse(request.path)

def detail(request,num):
    return HttpResponse(num)

def detail2(request,num1,num2,num3):
    return HttpResponse('%s-%s-%s'%(num1,num2,num3))

#展示接收的页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')

#接收一键一值的情况
def getTest2(request):
    #根据链接接收值
    a1 = request.GET.get('a')
    b1 = request.GET.get('b')
    c1 = request.GET.get('c')

    #构造上下文
    context = {'a':a1,'b':b1,'c':c1}
    #调用模板进行渲染
    return render(request,'booktest/getTest2.html',context)

#接收一间多值的情况
def getTest3(request):
    return render(request,'booktest/getTest3.html')