# 装饰器案例
def isCheck(func):
    def wrapper(name, passwd):
        if name == "xaiohua" and passwd == "123":
            print("login success")
            return func(name, passwd)
        else:
            print("login failed")

    return wrapper


@isCheck
def login(name, passwd):
    print("sucess")


login("xaiohua", "123")

# #闭包案例
# def outer():
#     name = "XAIOHUA"
#     newName = name.lower()
#     def inner(num):
#         print("inner",num)
#         return newName + str(num)
#     return inner

# a= outer()
# b = a(1212)
# print(b)
