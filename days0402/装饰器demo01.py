import time

def checktime(fun):
    print("ww")
    def check(*args,**kwargs):
        start_time = time.time()
        fun(*args,**kwargs)
        end_time = time.time()
        print('运行时间：',end_time-start_time)
    return check

@checktime
def add(a,b):
    print("a={} + b={}".format(a,b))
    time.sleep(1)
    sum=a+b
    print(sum)

add(1,2)
