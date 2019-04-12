from socket import *
import threading


def rece(sc,BUFFERSIZE):
    while True:
        try:
            info = sc.recv(BUFFERSIZE)
            if len(info)>0:
                print(info.decode('gbk'))
            else:
                sc.close()
        except Exception as e:
            print(e)
            break


def send(sc):
    while True:
        try:
            if sc._closed:
                break
            else:
                inputstr = input("输入：")
                if sc._closed:
                    break
                else:
                    sc.send(inputstr.encode('gbk'))
        except:
            break


if __name__ == '__main__':
    try:
        BUFFERSIZE = 1024
        ADDR = ('192.168.12.172',60000)
        socketclient = socket(AF_INET,SOCK_STREAM)
        socketclient.connect(ADDR)


        t1 = threading.Thread(target=rece,args=(socketclient,BUFFERSIZE))
        t1.start()

        t2 = threading.Thread(target=send, args=(socketclient,))
        t2.start()

        t1.join()
        t2.join()
    except Exception as e:
        print(e)
        print('断开连接')
    # socketclient.close()
