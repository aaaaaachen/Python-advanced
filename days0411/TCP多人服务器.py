from socket import *
import threading

def tlisten(sc):
    while True:
        client,clientaddr = sc.accept()

        userdict[str(clientaddr[1])] = client
        print('已连接', clientaddr[1],len(userdict))


        tr = threading.Thread(target=trece, args=(client,))
        tr.start()


def trece(sc):
    while True:
        reslut = sc.recv(BUFFERSIZE)
        if len(reslut)>0:
            to = reslut.decode('gbk').split(":")[0]
            message = reslut.decode('gbk').split(":")[1]
            print(to,message)
            print(sc.getpeername())
            if to in userdict:
                userdict[to].send(message.encode('utf8'))
            else:
                print('对方已离线'.encode('gbk'))

        else:
            userdict.pop(str(sc.getpeername()[1]))
            print('断开连接','在线人数：',len(userdict))
            break

if __name__ == '__main__':
    userdict = {}
    BUFFERSIZE = 1024
    ADDR = ('192.168.12.172',60000)
    server = socket(AF_INET,SOCK_STREAM)
    server.bind(ADDR)
    server.listen()

    tl = threading.Thread(target=tlisten,args=(server,))
    tl.start()

