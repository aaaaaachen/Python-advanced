

class Stu():
    room = 'py1901'

    def __init__(self,name,score):
        self.name = name
        self.score = score

a1 = Stu('ww',30)
a2 = Stu('cc',87)

# print(a1.score)
# print(a1.room)
# print(Stu.room)
# print(id(a1),id(a2)) # 内存地址不同
# print(id(Stu.room),id(a1.room),id(a2.room)) # 内存地址相同


class Tea():
    '''
    teacher 类
    '''
    room = 'py1901'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    @classmethod
    def getdoc(cls):
        print(cls.__doc__)

    @staticmethod
    def getroom():
        print(Tea.room)

    @property
    def getage(self):
        return self.age

    @getage.setter
    def setage(self,age):
        self.age = age




t1 = Tea('zzy',39)
#

t1.getage
t1.setage = 30
print(t1.getage)

# Tea.getdoc()
# Tea.getroom()
#
# t1.getroom()
# print(t1.getname())

'''
区别：
'''