from sys import getrefcount
import redis
# a = [1,2,3]
#
# print(getrefcount(a))
# del a
#
# b = 'achen'
# print(getrefcount(b))
# c = b
# print(getrefcount(c))
# print(getrefcount(b))
# del c
# print(getrefcount(b))

#
# x = [1,2,3]
# print(getrefcount(x))
# y = [4,5,6]
# print(getrefcount(y))
# print("@@@@@@@@@@@@@@@@")
#
# x.append(y)
# print(getrefcount(x))
# print(getrefcount(y))
# print("##################")
# y.append(x)
# print(getrefcount(x))
# print(getrefcount(y))
# print("$$$$$$$$$$$$$$$$$$$$")
# del x
# # print(getrefcount(x))
# print(getrefcount(y))

a = 12
print(getrefcount(a))
a = 11

print(getrefcount(a))
b = a
print(getrefcount(a))