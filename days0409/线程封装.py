import threading
import time


def thread1(self):
    print("dont run")

class MyThread(threading.Thread):
    def run(self):
        print("runnnnn")



def main():
    # t1 = MyThread()
    t1 =MyThread(target=thread1)
    t1.start()

if __name__ == '__main__':
    main()