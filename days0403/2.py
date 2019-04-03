

def renameattrs(classname,parentclass,attrs):
    newattrs ={}
    print(classname)
    classname = "new"+classname
    print(classname)
    for k,v in attrs.items():
       if not k.startswith("__"):
            # print(k)
            k = k+"attr"
            newattrs[k] = v

    for k,v in newattrs.items():
        print(k,v)
    return type(classname,parentclass,newattrs)

class Goods(metaclass=renameattrs):
    id = None
    name = None


g1 = Goods()

print(g1.__dir__())
print(g1.__class__)


