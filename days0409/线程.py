from threading import Thread
import time


def prt():
    print("#####")
    time.sleep(1)

def timecount(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(end - start)
    return fun

@timecount
def main():
    for r in range(5):


        prt()


@timecount
def thresdmain():
    list = []
    for r in range(5):

        t1 = Thread(target=prt)
        t1.start()
        list.append(t1)

    for i in list:
        i.join()




if __name__ == '__main__':
    main()
    # thresdmain()