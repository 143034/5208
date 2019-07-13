'''
全局变量再多个进程中不能共享
'''
from multiprocessing import Process
from time import sleep

num  =100


def run():
    print('子进程开始')
    global num
    num += 1
    print(num)

    print('子进程结束')


if __name__ == '__main__':
    print('父进程开始')
    p = Process(target=run)
    p.start()
    p.join()
    #再子进程中修改全局变量对父进程中的全局变量没有影响
    print('父进程结束--%d'%(num))