'''
UDP:





TCP是建立可靠连接，并且通信双方都可以交流，使用UDP时不需建立连接，知道对方ip和端口号就可以通信，
但不确定到达

UDP虽然不可靠，但和TCP相比速度较快，对于要求不高的数据可以适应UDP
'''
import socket
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.connect(('192.168.2.193', 2425))
udp.send('sunck is a good man'.encode('utf-8'))
