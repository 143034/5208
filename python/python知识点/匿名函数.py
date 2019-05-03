'''
可迭代对象:能直接用于for循环的对象(interable)
可以用isinstance()判断一个对象是否为可迭代对象
导入:
    from collections import Iterable
'''
#from collections import  Iterable
#迭代器:
l = (x for x in range(10))
print(next(l))
print(next(l))
print(next(l))

'''
def func1(*args, **kwargs)可以传任意类型参数
**kwargs使用列表类型传参
lambda 创建匿名函数
    特点:
        1.lambda只是一个表达式,函数体比def简单
        2.主体是一个表达式而不是代码块,只能在表达式中分装简单的逻辑
        3.有自己的命名空间且不能访问自有参数列表参数之外的或全局命名空间的参数
        4.虽然lanbda是一个表达式且看起来只能写一行.与c与c++内敛函数不同
    格式:
        lanbda 参数1,参数2,...... , 参数n:表达式
    
'''
sum = lambda num1, num2:num1+num2
print(sum(1,2))
