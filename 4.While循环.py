import random

i = 0
while i <= 100:
    print("JETBRAINS")
    i += 1
print("循环结束")
print("计算1累加到100的和")
num = 1
sum = 0
while num<=100:
    sum+=num
    num += 1
print("结果为：%d"%sum)

print("----------------------------")
print('猜数字')
r1 = random.randint(1, 50)
flag = True
while flag:
    r2 = int(input("请输入你的猜出的数字："))
    if r2 > r1:
        print("猜中了")
        flag = False
    else:
        print("猜错了，小了")
        continue
print('游戏结束')
