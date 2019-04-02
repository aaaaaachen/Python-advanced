#
# L = (x for x in range(10))
# print(L,type(L))
#
#
# for l in L:
#     print(l)


def fun():
    yield 1
    yield 2
    yield 3
    return 'aaa'

# print(type(fun()))
# print(next(fun()))
f = fun()
while True:
    try:
        print(next(f))
    except Exception as e:
        print(e)
        break