import threading
import time

class MyThread(threading.Thread):
    def run(self):
        while True:
            time.sleep(1)
            print("hi")

def main():
    t = MyThread()
    t.start()


if __name__ == '__main__':
    main()