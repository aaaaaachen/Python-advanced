import copy

a = [1,2,3,[4,5,[6,7]]]
b = copy.copy(a)
c = copy.deepcopy(a)
b[0] = 1.2
b[3].insert(1,4.5)
print(b[3])
b[3][3].insert(1,6.7)
c[1] = 'w'
a[2] = 'e'

print(b)
print(a)
print(c)
print(id(a),id(b),id(c))
for x,y,z in zip(a,b,c):
    print(id(x),id(y),id(z))