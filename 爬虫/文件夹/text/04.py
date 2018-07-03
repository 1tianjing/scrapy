def noreturn():
    print('noreturn函数不写return语句')

def justreturn():
    print('justreturn函数只写return,不返回具体内容')
    return

def returnval():
    x=10
    y=10
    z=x+y
    print('returnval函数写return语句，并返回求和的结果')
    return z


print('函数noreturn调用结果是：',noreturn())
print('函数justreturn调用结果是：',justreturn())
print('函数returnval调用结果是：',returnval())

