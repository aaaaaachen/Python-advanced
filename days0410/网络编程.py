import socket, threading,time
from socket import *
from threading import Thread

# DATA_SIZE = 1024
# #
# socketclient = socket(AF_INET,SOCK_DGRAM)
# #
# #
# addr = ('127.0.0.1',60000)
#
# res = input("speak:")
#
# socketclient.sendto(res.encode("utf8"),addr)
#
# while True:
#     receivedata,saddr = socketclient.recvfrom(DATA_SIZE)
#     print(receivedata,saddr)
#


def send_message():
    while True:
        res = input("speak:")
        socketclient.sendto(res.encode("utf8"),addr)
        time.sleep(1)


def rece_message(*args):
    time.sleep(6)
    while True:
        receivedata, saddr = socketclient.recvfrom(args[0])
        print("receive:",receivedata.decode("utf8"),saddr)

if __name__ == '__main__':
    DATA_SIZE = 1024
    socketclient = socket(AF_INET, SOCK_DGRAM)
    addr = ('192.168.12.172', 60000)

    t1 = Thread(target=send_message)
    t1.start()
    t2 = Thread(target=rece_message,args=(DATA_SIZE,))
    t2.start()
    t2.join()
    t1.join()




