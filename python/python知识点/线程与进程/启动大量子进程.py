from multiprocessing import Process ,Pool
import os ,time , random
def run(name):
    print('子进程%d开始---%s'%(name,os.getpid()))
    start = int(time.time())
    time.sleep(random.randint(5,10))
    end = int(time.time())
    print('子进程%d结束---%s'%(name,os.getpid()))
    print('%d耗时%d'%(name,(end-start)))

if __name__=='__main__':
    print('父进程开始')
    #创建多个进程pool进程池
    #表示可以同时执行的进程数量，默认cpu核心数
    pp = Pool(4)
    for i in range(5):
        #创建进程放入进程池同意管理
        pp.apply_async(run,args=(i,))
    #比需先调用close,之后不能再添加进程
    #等待所有子进程结束在调用父进程
    pp.close()
    pp.join()





    print('父进程结束')
