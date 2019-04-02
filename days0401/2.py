class Stu():
    """
    stu类

    """
    room = 'py1901'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def getdoc(cls):
        return cls.__doc__

    @staticmethod
    def getroom():
        return Stu.room

    def getname(self):
        return self.name

s1 = Stu('achen',20)
print(s1.getroom())
print(Stu.getroom())

print(s1.getdoc())
print(Stu.getdoc())

print(s1.getname())
print(Stu.getname())

"""
    区别：实例方法用来操作实例属性
         也能操作类属性
         类属性只能操作类
         
         实例方法

        定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
    
        调用：只能由实例对象调用。
        
        
        类方法

        定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
    
        调用：实例对象和类对象都可以调用。
        
        
        静态方法

        定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
    
        调用：实例对象和类对象都可以调用。
"""
