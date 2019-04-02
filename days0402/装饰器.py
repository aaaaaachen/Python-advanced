
def check(sg):
    def ck():
        user = input("用户名：")
        if user == 'achen':
            sg()
        else:
            print("没有权限")
    return ck


@check
def selectgood():
    print("查询商品")

@check
def insertgood():
    print("插入商品")

selectgood()
insertgood()