import threading,time
from socket import *

def send():
    while True:
        info = input("speak:").encode("utf8")
        socketclient.sendto(info,ADDR)

def rece():
    time.sleep(5)
    while True:
        receivedata,addr = socketclient.recvfrom(BUFFERSIZE)
        if receivedata:
            print("收到请回复",receivedata.decode(encoding="utf-8"),"-------------",addr)


if __name__ == '__main__':
    BUFFERSIZE = 1024
    ADDR = ('127.0.0.1', 60000)
    socketclient = socket(AF_INET,SOCK_DGRAM)


    t1 = threading.Thread(target=send)
    t2 = threading.Thread(target=rece)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
