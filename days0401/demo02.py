import types

class Stu():
    room = 'py1901'
    __slots__ = ('name','age',)
    # def __init__(self,name,age,score):
    #     self.name = name
    #     self.age = age
    #     self.score =score

# s1 = Stu('achen',22,33)
s1 = Stu()
s1.name = 'achen'
# s1.age = 20
# s1.score = 40
