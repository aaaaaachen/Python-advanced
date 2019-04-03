


def getinfo():
    print(Goods.name)
    print(Goods.id)

def getname():
    print(Food.name)

Goods = type("Good",(),{"id":None,"name":None,"getinfo":getinfo})

Food = type("Food",(Goods,),{"getinfo":getinfo,"getname":getname,"type":type})

g1 = Goods
f1 = Food

g1.getinfo()
f1.getinfo()