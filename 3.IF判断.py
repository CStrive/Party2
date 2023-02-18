age = 15
if age > 18:
    print("可以结婚了!")
else:
    print("不能结婚")
print("程序完毕")

price = int(input("请输入你的报价:"))
if price >= 1000 and price <= 50000:
    print("您的报价可以！")
elif price > 50000:
    print("直接爆款")
else:
    print("算了吧")
print("程序结束!")

a2 = int(input("确认你的年龄为18？"))
if a2 >= 18:
    print("可以继续观看!")
    if(int(input("再次确认你的年龄到了18？")) >= 18):
        print("请继续")
    else:
        print("分级观看")
else:
    print("已报警")