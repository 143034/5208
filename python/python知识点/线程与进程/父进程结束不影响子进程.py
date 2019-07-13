from multiprocessing import Process
from time import sleep
import os
#子进程代码
def run(str):
        print('启动子进程')
        sleep(3)
        print('子进程结束')

if __name__ == '__main__':
    print('主进程启动')
    p = Process(target=run,args=('nice',))
    p.start()
    #让父进程等待子进程结束，再执行父进程
    p.join()
    print('主进程结束')
'''
父进程结束不影响子进程
让父进程等待子进程结束，再执行父进程
'''