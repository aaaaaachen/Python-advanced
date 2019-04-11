import time
from threading import Thread

from socket import *

# def send():
#     while True:
#         res = input("speak:").encode("utf8")
#         serversocket.sendto(res,ADDR)

def rece():
    time.sleep(5)
    while True:
        receivedata, saddr = serversocket.recvfrom(1024)
        print(receivedata.decode("utf-8"), saddr)
        if receivedata:
            res = input("收到请回答：").encode("utf8")
            serversocket.sendto(res,saddr)


if __name__ == '__main__':
    serversocket = socket(AF_INET, SOCK_DGRAM)
    # ADDR = ('127.0.0.1', 60000)
    ADDR = ("192.168.12.172",60000)
    serversocket.bind(ADDR)


    # t1 = Thread(target=send)
    t2 = Thread(target=rece)

    # t1.start()
    t2.start()
    # t1.join()
    t2.join()

