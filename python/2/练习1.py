#1000以内的水仙花数
n = 100
list = []
while n<1000:
    if(n//100)**3 + ((n//10)%10)**3 + (n%10)**3 == n:
        list.append(n)
    n += 1
print('1000以内的水仙花数有:',list)
#五位数回文数的个数
n = 10000
i = 0
while n<100000:
    if (n//10000) == (n%10) and ((n//1000)%10) == ((n%100)//10):
            i += 1
    n +=1
print('五位回文数的个数为:', i)
#判断质数

num = int(input('请输入一个数'))
i= 2
if num==2:
        print('yes')
while i < num:
    if (num/i)%i == 0:
        print('no')
        break
    else:
        i += 1
        if i == num-1:
            print('yes')
    

'''
#分解质因数
num = int(input('请输入一个数'))
i= 2
while i < num:
    if (num/i)%i == 0:
        b = int(num/i)
        print(i ,b)
    else:
        i += 1
        if i ==num - 1:
            print('这个数是质数')
            '''
      
            

