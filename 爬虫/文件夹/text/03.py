num = 100
print('函数调用前num 的值为:',num)

def func():
    global num
    num=200
    num+=100
    print('函数体中num的值是:',num)

func()
print('函数调用后num的值为',num)

