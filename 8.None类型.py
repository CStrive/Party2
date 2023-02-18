def say():
    print("hello")
def say2():
    return None
c = say()
# None
print(c)
# <class 'NoneType'>
print(type(c))

# global 全局变量声明
def show():
    global tf
    tf = "BUS"
show()
print(tf)