# list = [i for i in range(10)]
#
# for l in list:
#     print(l)

# list1 = (i for i in range(10))

# for 循环遍历
# for l in list1:
#     print(l)

# next
# while True:
#     try:
#         print(list1.__next__())
#     except StopIteration as e:
#         print("越界")
#         print(e)
#         break


def field(num):
    a,b = 0,1
    yield a
    yield b

    n = 0
    while n<num:
        a,b = b,a+b
        yield b
        n = n+1

f = field(10)
for i in f:
    print(i)


def fun():

    yield 1
    yield 2
    yield 3
    return 'aaa'


a = fun()
while True:
    try:
        print(next(a))
    except StopIteration as e:
        print(e)
        break
