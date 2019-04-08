# from multiprocessing import Process
#
# def run():
#     print("run")
# def main():
#     p = Process()
#     p.run = run
#     p.start()
#     p.join()
#     print("finish")
#
# if __name__ == "__main__":
#     main()



from multiprocessing import Process
import os
class MyProcess(Process):
    def __init__(self):
    # init parent class
        Process.__init__(self)
    def run(self):
        print("pid %d" % os.getpid())



def main():
    p = MyProcess()
    p.start()
    p.join()
    print("finish")

if __name__ == "__main__":
    main()
