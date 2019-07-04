import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定ip和端口

server.bind(('192.168.2.193',8081))
#监听
server.listen(5)

print('victory')

#等待连接
clientSocket, clientAddress = server.accept()

print('%s ------ %s 成功' %(str(clientSocket),clientAddress))
while True:
    data = clientSocket.recv(1024)
    print('收到数据' + data.decode('utf-8'))
    clientSocket.send('good......'.encode("utf-8"))
