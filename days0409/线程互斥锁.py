import threading, time
from threading import Thread,Lock
import threading

num = 0

def thread1():
    global num
    for r in range(1000000):
        # mutex.acquire()
        # num+=1
        # mutex.release()

        num+=1

# def thread2():
#     global num
#     for r in range(1000000):
#         mutex.acquire()
#         num += 1
#         mutex.release()

def main():
    t1 = Thread(target=thread1)
    t1.start()
    # time.sleep(1)
    t2 = Thread(target=thread1)
    t2.start()
    time.sleep(1)
    t1.join()
    t2.join()


if __name__ == '__main__':
    mutex = threading.Lock()

    print(num)
    main()
    print(num)