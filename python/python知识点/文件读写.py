'''
文件读写:
    打开文件:
        open(path, flag[,encoding][,errors])
        path为路径
        flag为打开方式(r,rb,r+,w,wb,w+,a,a+)
        r:以只读方式打开文件
        rb:以二进制文件打开文件,只读文件,文件的描述放在文件的开头
        r+:打开一个读写文件
        w:打开一个文件用于读写,如果文件已经存在会覆盖,不存在则创建新文件
        wb:打开一个文件写入二进制
        w+:打开一个文件用于读写
        a:打开一个文件用于追加，如果文件存在,文件描述符会放到文件末尾
        a+:
        encodeing:编码格式
        errors:错误处理
    读文件:
        1.
            f.read()
        2.
            f.read(10)#读几个字符
        3.
            f.readline(n)读取整行,n代表指定字符数
        4.
            f.readlines()读取所有行并返回列表
    修改文件描述符位置:
        f.seek(n)
    关闭文件:
        f.close()
    简便方法:不管文件打开成功或是失败文件最后都会关闭
    with open(path, 'r') as f:
        print(f.read())
'''
try:
    f1 = open(path, 'r')
    print(f1.read())
finally:
    if f1:
        f1.close()
