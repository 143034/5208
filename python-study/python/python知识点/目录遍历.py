'''
遍历目录:

path = r"C:\Users\Administrator\Desktop\文件工作区"
import os

def getalldir(path, sp=''):
    filelist = os.listdir(path)
    sp += '   '
    for filename in filelist:
        fileabs = os.path.join(path,filename)
        if os.path.isdir(fileabs):
            print(sp + '目录', filename)
            getalldir(fileabs , sp)
        else:
            print(sp + '普通文件', filename)
#getalldir(path)
'''
import os
path = r"C:\Users\Administrator\Desktop\文件工作区"
def getalldir(path):
    stack = []
    stack.append(path)
    while len(stack) != 0:
        dirpath = stack.pop()
        filelist = os.listdir(dirpath)
        for filename in filelist:
            fileabs = os.path.join(dirpath, filename)
            
            if os.path.isdir(fileabs):
                print('目录', filename)
                stack.append(fileabs)
            else:
                print('普通文件' ,filename)
getalldir(path)
