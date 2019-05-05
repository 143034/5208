'''
偏函数
    import functools
    print(int('1010',base = 2))
作用域:
    变量可以使用的范围
    程序的变量并不是在所有位置都能使用
    局部作用域
    函数作用域
    全局作用域
    內建作用域
异常处理:
    1.当程序遇到错误时不结束，而是越过错误继续向下执行
    try ... except ... else语句
    格式:
        try:
            语句t
        except 错误码 as e:
            语句1
            。。。
        except 错误码 as e:
            语句n
        else:
            语句e
    作用:用来检测try语句中的错误,让except语句捕获错误信息并处理.
        1.如果try语句执行出现错误,会匹配第一个错误码,如果匹配到就执行对应的语句.
        2.如果try语句执行错误,没有匹配到异常,错误将会被提交到上一层的try语句,或到程序的最上层，
        3.如果try语句执行没有错误,不会匹配异常,会执行else内容.
    使用except带有多种异常:
        try:
            pass
        except(多个错误码):
            print('相应错误')
    2.语句t无论是否有错误都将执行语句e
    try ... except ... finally语句
    格式:
        try:
            语句t
        except 错误码 as e:
            语句1
            。。。
        except 错误码 as e:
            语句n
        finally:
            语句e
    语句t无论是否有错误都将执行语句e
    
'''
'''
import functools
print(int('1010',base = 2))
#把一个参数固定住,形成一个新函数
int3 = functools.partial(int,base = 2)
print(int3('11010'))
'''
'''
try:
    print(3/0)
#except ZeroDivisionError as e:
except:
    print('除数为0')
else:
    print('*****')
'''
'''
预言:
    def func(num , div):
        assert(div != 0),
        return num/div
    print(func(10,0))
'''
def func(num , div):
    assert(div != 0),'div不能为0'
    return num/div
print(func(10,0))
