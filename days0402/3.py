
# 定义检测用户的装饰器
def checkuser(fun):
    def check():
        print("判断是否为用户")
        if input("用户名：") == 'achen':
            print('账户正确')
            fun()
        else:
            print("账号错误，无权操作")

    return check

@checkuser
def selectgood():
    print("查看商品")

a = selectgood()