import copy
a = [1,2,3,[4,5]]

# b = a
#
# print(a,b)
#
# # a.insert(1,"#")
# #
# # print(a,b)
#
# a[3].insert(1,"@")
# # print(a,b)
#
# c = copy.copy(a)
#
# # print(id(a),id(c))
# print(a, c)
# a.insert(1,"#")
# # a[3].insert(1,"&")
# print(a,c)
# for x,y in zip(a,c):
#     print(id(x),id(y))


d = copy.deepcopy(a)

print(a,d)
# print(id(a),id(d))
a[3].insert(1,"*")
# a.insert(2,"#")
print(a,d)
for x,y in zip(a,d):
    print(id(x),id(y))



