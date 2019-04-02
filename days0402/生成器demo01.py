def fun(times):
    a,b = 0,1
    yield a
    yield b

    n=0
    while n<times:
        c=0
        c =a
        a = b
        b = c+b

        yield b
        n+=1

f = fun(10)
# for i in f:
#     print(i)

s = 'acnsns'
for i in s:
    print(i)

print(f)
while True:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print(e.value)
        break