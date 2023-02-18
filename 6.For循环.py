name = "JETBRAINSBB PY"
count = 0;
for x in name:
    if 'B' == x:
        count+=1
    print(x)
print("B有%d个"%count)

for i in range(0,10):
    print(i)

print("for循环版本的乘法表")

for k in range(1,10):
    for j in range(1,k + 1):
        print(f"{j} * {k} = {j * k}\t",end='')
    print()