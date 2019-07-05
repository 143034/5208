'''
客户端:创建tcp连接时主动发起连接的叫客户端

服务端:接受客户端的连接

'''
#网络编程包
import socket
#创建socket,
'''
参数一:指定协议AF_INET（AF_INET6）
参数二:执行使用面向流的tcp协议

'''

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接参数为元组
#第一个元素为要连接的服务器的ip
#第二个为端口号
sk.connect(('www.baidu.com',80))
sk.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
#等待接收数据
data = []
while True:
    #每次接受1k数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break
dataStr = str(b''.join(data).decode('utf-8'))
#断开连接
sk.close()
print(dataStr)
