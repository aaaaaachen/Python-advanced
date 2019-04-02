import types
class AI():
    def __init__(self):
        pass

def move(self):
    print("move")

a1 = AI()
a1.move = types.MethodType(move,a1)
# a1.move()
print(a1.move())
del a1.move
a1.move()


@classmethod
def attack(cls):
    print('attack')

@staticmethod
def dead():
    print("dead")

a1 = AI()
AI.attack = attack
AI.dead = dead

AI.dead()
AI.attack()

a2 = AI()
a2.dead()
a2.attack()

AI().attack()
