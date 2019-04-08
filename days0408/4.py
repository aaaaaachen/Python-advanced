import os,time
from multiprocessing import Process


def process1(pam1,**kwargs):
    print("进程1:",pam1,kwargs)
    pam1.append(2)
    print(pam1,"####")

def process2():
    print("进程2")


def main():
    list1 = [1]

    p1 = Process(target=process1,args=(list1,),kwargs={"name":"achen"})

    p1.start()
    print(list1)


if __name__ == '__main__':
    main()