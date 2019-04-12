from socket import *
import threading

def tlisten(s):
    while True:
        client,raddr = s.accept()
        print(client, raddr)
        nickname = client.recv(1024).decode('gbk')
        users[str(nickname)] = client
        print(users)
        # print(client,raddr)
        # userdict[str(raddr[1])] = client
        # print(raddr,'当前用户量：',len(userdict))
        # tr = threading.Thread(target=trece,args=(client,))
        # tr.start()

        # userlist = [str(raddr[1]),client]
        print(raddr, '当前用户量：', len(users))
        tr = threading.Thread(target=trece, args=(client,nickname))
        tr.start()

def trece(client,nickname):
    while True:
        try:
            result = client.recv(1024).decode('gbk')
            if len(result) > 0:
                to = result.split(':')[0]
                message = result.split(':')[1]

                print(to)
                print(message)
                print(type(to))


                # print(userdict)


                # if to in userdict.keys():
                #     print("aaaaaaaaaaaaaaaaaaaa")
                #     userdict[to].send(message.encode('utf8'))
                # if to.upper() == 'ALL':
                #     for k in userdict.keys():
                #         print(client.getpeername()[1],'-------',k)
                #         if k != client.getpeername()[1]:
                #             userdict[k].send(message.encode('gbk'))
                if to in users.keys():
                    users[to].send(message.encode('gbk'))
                    users[to].send(nickname.encode('gbk'))
            # else:
            #     userdict.pop(client.getpeername()[1])
            #     print('断开连接,在线人数为：',len(userdict))
            #     break
        except Exception as e:
            print(client.getpeername()[1],'断开连接')
            break

def single():
    pass

if __name__ == '__main__':
    # userdict = {}
    users = {}
    userlist = []
    ADDR = ('192.168.12.172',60000)
    server = socket(AF_INET,SOCK_STREAM)
    server.bind(ADDR)
    server.listen()

    tl = threading.Thread(target=tlisten,args=(server,))
    tl.start()