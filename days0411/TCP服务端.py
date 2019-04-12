# -*- coding: utf-8 -*-
from socket import *
import threading




def rece(client,BUFFERSIZE):
    while True:
        info = client.recv(BUFFERSIZE)
        # print(info)
        print("收到：",info)

        # inputstr = input("请输入：").encode('utf8')
        # client.send(inputstr)


#
def send(client):
    while True:
        inputstr = input("请输入：")
        if inputstr == 'exit':
            socketserver.close()
        else:
            client.send(inputstr.encode('gbk'))



if __name__ == '__main__':
    BUFFERSIZE = 1024
    SOCKETADDR = ('192.168.12.172',60000)
    # 构造socket对象
    socketserver = socket(AF_INET,SOCK_STREAM)
    # 绑定地址
    socketserver.bind(SOCKETADDR)
    # 开始监听
    socketserver.listen()
    # 接受连接 accept 为阻塞方法
    # client,clientaddr = socketserver.accept()
    # print(client.clientaddr)
    client,raddr = socketserver.accept()
    print(client,raddr)
    t1 = threading.Thread(target=rece,args=(client,BUFFERSIZE))
    t1.start()

    t2 = threading.Thread(target=send,args=(client,))
    t2.start()
    t1.join()
    t2.join()

    client.close()
