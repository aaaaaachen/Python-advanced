import os
from multiprocessing import Process


def process1():
    print("程序~1______run")

class MyProcess(Process):
    def __init__(self,target):
        Process.__init__(self,target=target)

    def run(self):
        print("程序执行")

def main():
    # p1 = MyProcess(target=process1)
    # p1.start()
    p = MyProcess(target=process1)
    p.start()


if __name__ == '__main__':
    main()



