import time,threading
from socket import *

def rece():
    time.sleep(10)
    while True:
        receivedata,addr = socketserver.recvfrom(BUFFERSIZE)
        print(receivedata.decode('utf8'),addr)
        if receivedata:
            info = input("收到请回复:")
            socketserver.sendto(info.encode('utf8'),addr)


if __name__ == '__main__':
    ADDR = ('127.0.0.1',60000)
    BUFFERSIZE = 1024
    socketserver = socket(AF_INET,SOCK_DGRAM)
    socketserver.bind(ADDR)
    t1 = threading.Thread(target=rece)
    t1.start()
    t1.join()