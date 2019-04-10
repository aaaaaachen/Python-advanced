from multiprocessing import Process,Pool,Queue,Manager
import time

def read(q):
    while True:
        print("queue size is %d" % q.qsize())
        i = q.get()
        print("get %d "% i)


def write(q):
    for i in range(5):
        q.put(i)
        print("put %d" % i)
        print("queue size is %d"% q.qsize())
        time.sleep(0.2)


def main():
    q = Manager().Queue(5)
    q.put(-2)
    q.put(-1)
    pool = Pool(5)
    pool.apply_async(write,(q,))
    pool.apply_async(read,(q,))
    pool.close()
    pool.join()
    print("finish")

if __name__ == '__main__':
    main()