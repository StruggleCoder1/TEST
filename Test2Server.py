import socket
import sys

socketserver=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
# 绑定主机和地址
socketserver.bind((host, port))
# 监听5个数量
socketserver.listen(5)
while True:
    # 被动接受TCP客户端连接,(阻塞式)等待连接的到来
    clientsocket,addr= socketserver.accept()
    print("连接地址: %s" % str(addr))
    msg = '第一个网络程序！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    msg1 = clientsocket.recv(1024)
    print(msg1)
    clientsocket.close()
    print(socketserver.gettimeout())