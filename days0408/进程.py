import os ,time
from multiprocessing import Process

def p1process():
    while True:
        print("进程P1执行了%d"%os.getpid())
        time.sleep(1)

def p2process():
    while True:

        print("进程P2执行了%d"%os.getpid())
        time.sleep(1)

def main():
    p1 = Process(target=p1process)
    p1.start()
    # p1.join()
    p1.terminate()



    p2 = Process(target=p2process)
    p2.start()
    # p2.join()


    while True:
        time.sleep(4)
        print(p1.is_alive())

if __name__ == "__main__":
    main()

    # while True:
    #     time.sleep(3)
    #     print("@@@@@@@@@@@")
