import os,time
from multiprocessing import Process

def process1():
    while True:
        print("进程1 pid%d"%os.getpid())
        time.sleep(1)


def process2():
    while True:
        print("进程2 pid%d"%os.getpid())
        time.sleep(1)

def main():
    p1 = Process(target=process1,name="aaa")
    print(p1.name)
    p1.start()
    # p1.join()
    p1.terminate()

    p2 = Process(target=process2,name="bbb")
    print(p2.name)
    p2.start()
    print(p1.is_alive())


if __name__ == '__main__':

    main()