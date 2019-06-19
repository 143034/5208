'''
import pickle 数据持久型模块
    mylist = [1,2,3,4,5,6]
    path = r''
    f = open(path,'wb')
    pickle.dump(mylist, f)
    f.close()
    #读取
    f1 = open(path,'rb')
    tem = pickle.load(f1)
    print(tem)
    f1.close()
os
    包含了普通的操作系统的功能
    模块导入:
        import os
'''
import os
print(os.name)#获取操作系统类型  nt-windows posix-linux Mac-OS X
print(os.uname_result)#打印详细信息
print(os.environ)#获取操作系统中的环境变量
print(os.environ.get('ALLUSERSPROFILE'))#获取指定环境变量
print(os.curdir)#获取当前目录
print(os.getcwd())#获取当前工作目录
#print(os.listdir(path))以列表返回指定目录下所有的文件
#os.mkdir('文件')#在当前目录下创建目录
#os.rmdir('文件')#在当前目录下删除目录
#print(os.stat('文件'))#获取文件属性
#os.rename('old','new')#修改名字
#os.remove('文件')#删除文件
#os.system('notepad')运行shell命令
#print(os.path.('./'))#查看绝对路径
#os.path.getsize()#查看文件大小
#print(os.path.dirname())#文件的目录
#print(os.path.basename())#文件的目录
'''
'''


