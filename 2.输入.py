print("欢迎使用中国农业银行自助ATM")
account = int(input("请输入你的账号："))
print("您的账号是：%s"%account)
result = account > 1;
print(f"您的账号比1大？{result},类型为：{type(result)}")
