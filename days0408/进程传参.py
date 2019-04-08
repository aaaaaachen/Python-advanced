import os ,time
from multiprocessing import Process

def p1process(*args,**kwargs):
    print(args[0],kwargs)

class MyProcess(Process):
    def __init__(self,target):
        Process.__init__(self,target=target)

    def run(self):
        print("执行了")

def main():
    # p = Process(target=p1process,args=("ww",20))
    # p1 = MyProcess(target=p1process)
    # p1.start()
    list = [1]
    p = Process(target=p1process,args=list,kwargs={"name":"achen"})
    p.start()




if __name__ == "__main__":
    main()