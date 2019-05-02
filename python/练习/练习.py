import math
print("水仙花")
while(1):
    a = int(input("请输入一个三位数："))
    if (a//100)**3 + ((a//10)%10)**3 + (a%10)**3==a:
            print("yes")
            break
    else:
        print("no")
print("回文数")
while(1):
    b = int(input("请输入一个五位数:"))
    if (b//10000) == (b%10):
        if((b//1000)%10) == ((b%100)//10):
            print("yes")
            break
        else:
            print("no")
    else:
        print("no")
print("大小判断")
c = int(input("请输入第一个值:"))
d = int(input("请输入第二个值:"))
e = (c>d)-(d>c)
#print(e)
if e==1:
    print("这两个数第一个大",c)
else:
    print("这两个数第二个大",d)
#print(max(c,d))
f = int(input("请输入第三个值:"))
print("这三个数中最大的值是:",max(c,d,f))

