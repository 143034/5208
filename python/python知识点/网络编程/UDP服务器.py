import socket

udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


udpServer.bind(('192.168.2.193',8901))


while True:
    data, addr = udpServer.recvfrom(1024)
    print('客户端说',data.decode('utf-8'))
    info = input('请输入数据：')
    infos = udpServer.sendto(info.encode('utf-8'),addr)