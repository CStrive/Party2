from _decimal import Decimal

str1 = "jetbrains"
print("长度为：", len(str1))

# count = 0
# for i in str1:
#     count+=1
# print("长度为：",count)

# 函数的定义
def strlen(data):
    count = 0
    for i in data:
        count+= 1
    return count

print(f"JAVA 字符长度为：{strlen('JAVA')}")
print(f"JS 字符长度为：{strlen('JS')}")

def sayhi():
    print('你好！')

sayhi()

def add(x,y):
    print(f"{x} + {y} = {(x + y)}")

add(4, 6)
add(11,5)
add(0.1,0.2)
add(4,2.5)
add(43,.5)
add(1.1,2.2)
print(str(0.1+0.2))