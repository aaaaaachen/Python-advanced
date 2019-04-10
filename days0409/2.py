import time
from threading import Thread
from multiprocessing import Queue,Process


def read(taskqueue):
    # while True:
    #     print("size----------->", taskqueue.qsize())
    #     r = taskqueue.get()
    #     print("get %d" % r)
    #     print("size----------->", taskqueue.qsize())

    while True:
        print("size----------->", taskqueue.qsize())
        r = taskqueue.get()
        print("get %d" % r)
        print("size----------->", taskqueue.qsize())



def write(taskqueue):
    for i in range(10):
        print("put---------->",taskqueue.qsize())
        taskqueue.put_nowait(i)
        print("put---------->", taskqueue.qsize())



def main():
    queue = Queue(10)

    pread = Process(target=read,args=(queue,))
    pwrite = Process(target=write,args=(queue,))

    pread.start()
    pwrite.start()

    # pwrite.join()



if __name__ == '__main__':
    main()