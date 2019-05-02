import math
import random
'''a,b = 1,2
print(a,b)
print(6>9)
#判断两个数的大小
a=10
b=100
c = (a>b)-(a<b)
print((a>b)-(a<b),c)
print(max(a,b))
print(min(a,b))
#pow用来取次方
print(pow(b,a))
print(pow(2,3))
#round用来4舍5入
print(round(3.1415))
print(round(3.1415,3))
'''
'''
math库的使用
ceil 向上取整
floor 向下取整
modf返回整数和小数部分
sqrt开方
'''
print(math.ceil(18.1))
print(math.floor(18.1))
print(math.modf(11.2))
print(math.sqrt(16))
'''
random模块使用
[]列表类型
range(5):[0,1,2,3,4]
print(random.choice("range"))作用:
['r','a','n','g','e']
choice操作传列表
产生1-100随机数:range(100)+1
选取按照左闭右开的方式
randrange()前两位通range使用相同，后一位代表间隔
random.random():产生随机小数
shuffle随机打乱列表
uniform随机生成实数范围在()中
'''
print(random.choice([1,2,3,4,5,6]))
print(random.choice(range(5)))
print(random.choice("range"))
print(random.randrange(0,100,2))
print(random.random())
list = [1,2,3,4,5]
random.shuffle(list)
print(list)
print(random.uniform(3,4))
