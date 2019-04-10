from multiprocessing import Process,Queue
import time,os



def pwrite(taskqueue):
    print(taskqueue.qsize())
    for i in range(10):
        taskqueue.put(i)



def pread(taskqueue):

    while True:
        print("size----------->",taskqueue.qsize())
        r = taskqueue.get()
        print("get %d"%r)
        print("size----------->", taskqueue.qsize())

    taskqueue.get()


def main():
    queue = Queue(10)
    write = Process(target=pwrite,args=(queue,))
    write.start()
    write.join()

    read = Process(target=pread,args=(queue,))
    read.start()

if __name__ == '__main__':
    main()