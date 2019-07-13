'''
单任务现象
不会执行到run方法
'''
from time import sleep

def run():
    while True:
        print('5208')
        sleep(1.2)

if __name__ == '__main__':
    while True:
        print('5108')
        sleep(1)
run()
