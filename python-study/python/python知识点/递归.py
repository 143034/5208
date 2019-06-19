'''
递归:
    概念:一个调用自身的函数
    方式:
        1.写出临界条件
        2.找这一次和上一次的关系
        3.假设当前函数已经能用,调用自身计算上一次的结果,在求出本次的结果
'''
'''
def fun():
    fun()
'''
#输入一个数求1+..n的值
def sum(n):
    result = 0
    for i in range(1,n + 1):
        result += i
    return result
re = sum(10)
print(re)
#递归方法
def sum1(n):
    if n == 1:
        return 1
    else:
        return n + sum1(n-1)
re = sum1(10)
print(re)
        
