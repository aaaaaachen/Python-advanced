import json

class Goods():
    # name = None
    # price = None
    def __init__(self,name,price):
        self.name = name
        self.price = price


#
# name = input("商品名：")
# price = input("价格：")
# g1 = Goods(name,price)
#
# print(g1.name,g1.price)
# dict = {"name":g1.name,"price":g1.price}
#
#
with open("data.txt","w") as file:
    info = json.dumps(dict,ensure_ascii=False)
    print(dict,type(dict))
    print(info,type(info))
    file.write(info)


with open("data.txt","r") as file:
    res = file.read()
    result = json.loads(res)
    print(res)
    print(result)
    # json.loads()


# g1 = Goods('watch',100)
# print(g1.name)

# name = input("请输入商品名：")
# price = input("请输入价格：")
# Goods = type("Goods",(),{"name":name,"price":price})
# print(Goods.__dict__)
# g1 = type('g1',(Goods,),{'name':name,'price':price})
# print(g1.__dict__)

# g1 = Goods()
# print()

# dict = {"name":g1.}




