




def renameattribute(classname,parentclass,attrs):
    newattrs = {}

    'heee'.lower()
    classname.lower()[0]
    # print(classname.lower()[0],type(classname))

    for k,v in attrs.items():
        if not k.startswith("__"):
             # print(k)
             k = classname.lower()[0]+"_"+k
             # print(k)
             newattrs[k] = v

    for k,v in newattrs.items():
        print(k,v)

    return type(classname,parentclass,attrs)

class Student(metaclass=renameattribute):
    id = None
    name = None


s = Student()
print(s.__dict__)
print(Student.__dict__)