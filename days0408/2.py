import os
from multiprocessing import Process

def process1():
    print("进程1的pid%d 进程1的ppid%d"%(os.getpid(), os.getppid()))

def process2():
    print("进程2的pid%d 进程2的ppid%d"%(os.getpid(), os.getppid()))


def main():
    p1 = Process(target=process1)
    p1.start()

    p2 = Process(target=process2)
    p2.start()



if __name__ == "__main__":
    main()