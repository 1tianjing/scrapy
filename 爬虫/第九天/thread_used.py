import threading
import time

def download(url):
    print(url)
    time.sleep(1)
    print(threading.current_thread().name)
    


def main():
    starttime = time.time()
    task_list = ['url1','url2','url3','url4']
    # for url in task_list:
    #     download(url)
    # list存放你当前创建的线程对象
    thread_list = []
    for url in task_list:
        # 创建一个子线程              设置执行函数
        thread = threading.Thread(target=download,name="线程"+url,args=[url,])
        # 设置为True 表示为后台进程
        # thread.setDaemon(True)
        #为FALSE  表示为前台
        thread.setDaemon(False)
        #启动线程
        thread.start()
        thread_list.append(thread)
        thread.join()
    
    #子线程调用join()，表示告诉主线程，必须等我执行完毕  你才能结束
    for thread in thread_list:
        thread.join()

    endtime = time.time()
    print('耗时'+str(endtime-starttime))
    print(threading.current_thread().name)

if __name__ =='__main__':
    main()