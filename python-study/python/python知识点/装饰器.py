'''
装饰器:
    概念:是一个闭包，把一个函数当做参数返回一个替代版的函数,本质上就是一个返回函数的函数.
'''
'''
#例一
def fun1():
    print('i am a good man')
def outer(fun):#函数体做参数
    def inner():
        print('*******')
        fun()
    return inner
fun1 = outer(fun1)
fun1()
'''
'''
#例二
def outer(fun):
    def inner(age):
        if age < 0:
            age = 0
        fun(age)
    return inner
@outer#使用@符号将装饰器应用到函数
def say(age):
    print('sunk is %d years old!' %(age))
#say = outer(say)
say(-10)
'''
'''
通用装饰器:
函数的参数理论上没有限制,但在实际应用中最好不要超过6到7个
'''
'''
#例三
def outer(fun):
    def inner(*args, **kwargs):
        print('*************')
        fun(*args, **kwargs)
    return inner
@outer
def say(name,age):
    print('my name is %s, i am %d years old' %(name,age))
say('luo',22)
'''
