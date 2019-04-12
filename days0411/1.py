from socket import *
import threading


# def send(sc):
#     inputstr = input('请输入')
#     sc.send()


if __name__ == '__main__':
    ADDR = ('192.168.12.172',60000)
    server = socket(AF_INET,SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    client,raddr = server.accept()
    print(raddr)
    # t1 = threading.Thread(target=send,args=(client,))
    # t1.start()

    while True:
        result = client.recv(1024)
        print(result.decode('gbk'))
        inputstr = input('请输入：')
        client.send(inputstr.encode('gbk'))