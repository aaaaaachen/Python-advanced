from socket import *
import threading
COUNT = 0
def trece(client):
    while True:
        res = client.recv(1024)
        if len(res)>0:
            print(res)
        else:
            client.close()

if __name__ == '__main__':
    try:
        ADDR = ('192.168.12.172',60000)
        client = socket(AF_INET,SOCK_STREAM)
        client.connect(ADDR)


        # client.close()

    except Exception as e:
        print(e)
    while True:
        tr = threading.Thread(target=trece, args=(client,))
        try:
            if not client._closed:
                tr = threading.Thread(target=trece, args=(client,))
                inputstr = input('请输入消息：')
                client.send(inputstr.encode('gbk'))
            else:
                client.close()
                break
        except Exception as e:
            print('连接中断')
            client.close()
            break
