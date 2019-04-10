import threading, time

from threading import Thread


def prt(num):
    while True:
        print("@@@@",threading.current_thread().name,num)
        time.sleep(1)


def main():
    for i in range(5):
        t1 = Thread(target=prt,name='MyThread',args=(i,))
        t1.start()


if __name__ == '__main__':
    print(threading.enumerate())
    main()