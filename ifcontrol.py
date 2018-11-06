x = int(input("请输入一个正数："))
if x < 0:
    x = 0
    print("负数变成0")
elif x == 0:
    print("0")
elif x == 1:
    print("1")
else:
    print("其它")
