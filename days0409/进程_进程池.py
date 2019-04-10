from multiprocessing import Pool
import os,time


def process(i):
    # while True:
        time.sleep(1)
        # print("pid%d  ppid%d i=%d "%(os.getpid(), os.getppid(),i))
        print(i)
    # print("pid%d  ppid%d  i=%d" % (os.getpid(), os.getppid(), i))
def main():
    print(os.getpid())

    pool = Pool(4)
    # pool.apply_async(process)
    # pool.apply_async(process)
    # pool.apply_async(process)
    # pool.apply_async(process)

    # pool.apply(process)
    # pool.close()
    # pool.join()
    # pool.apply(process)
    # pool.apply(process)
    # pool.apply(process)


    for i in range(20):
        pool.apply(process,args=(i,))
        print("你好")

    # start = time.time()
    # for i in range(20):
    #     pool.apply_async(process,(i,))
    # end = time.time()
    # time.sleep(1)
    # print(end-start)
    pool.close()
    time.sleep(2)
    # pool.terminate()
    pool.join()

    print("finish")


if __name__ == '__main__':
   main()

#
# from multiprocessing import Pool
# import os
# import time
# def fun(name, age, **kwargs):
#     print("QQQQQ")
#     while True:
#         time.sleep(1)
#         print("pid %d" % os.getpid())
#         print(name, age, kwargs)
# time.sleep(1)
# pool = Pool(5)
# for i in range(20):
#     pool.apply_async(fun, ("zzy", 20), {"isalive": False})
#     print("###########")
# pool.close()
# # pool.join()
# print("finish")
