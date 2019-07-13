'''
多任务
multiprocessing 库

跨平台版本的多进程模块，提供了process类代表一个进程对象
'''
from multiprocessing import Process
from time import sleep
import os
#子进程代码
def run(str):
    while True:
        #获取进程id号
        #获取当前进程的父进程id号
        print('5208 is %s---%s----%s'%(str, os.getpid(), os.getppid()))
        sleep(1)

if __name__ == '__main__':
    print('主进程启动    %s'%(os.getpid()))
    #创建子进程
    #target说明进程执行的任务
    #给子进程传参
    p = Process(target=run,args=('nice',))
    #启动进程
    p.start()
    while True:
        print('5108')
        sleep(1)
