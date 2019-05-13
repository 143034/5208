'''
面向对象:
    创建类：(首字母大写,其他遵循驼峰原则)
        class 类名(父类列表):
            属性
            行为
    实例化对象:
        对象名 = 类名(参数列表)
        没有参数小括号也不能省略
    访问对象的属性与方法:
        访问属性:
            对象名.属性名
            赋值: 对象名.属性名 = 新值
        访问方法:
            对象名.方法名(参数列表)
    构造函数:(对象的初始状态)
        __init__()在使用类创建对象的时候自动调用
        如果不显示的写出构造函数,默认添加一个空的构造函数
        
'''
#object基类,所有类的父类,没有合适的父类就用object
class Person(object):
    #定义属性
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __del__(self):
        print('这是析构函数')
    #name = ''
    #age = 0
    #heigh = 0
    #weight = 0
    #定义方法
    #注意:方法的参数必须以self当第一个参数
    #代表类的实例
    def run(self):
        print('run')
    def eat(self,food):
        print('eat ' + food)
    def say(self):
        print('Hello, my name is %s,i am %d years old' %(self.name,self.age))
        print(self.__class__)
    def open(self):
        print('打开门')
    def close(self):
        print('关闭门')
#实例化对象:创建两个完全不同的对象
#per = Person('hanmeimei', 20, 170, 55)
#print(per.name,per.age)
#访问属性
'''
per.name = 'tom'
per.age = '18'
per.height = '160'
per.weight = '80'
print(per.name,per.age,per.height,per.weight)
'''
#访问方法
#per.eat('apple')
#per.open()
#per.close()
'''
self:
    代表类的实例,而非类
    那个对象调用方法,那么该方法的self就代表那个对象
    self.__class__ 代表类名
    self不是关键字,换成其他也是可以的
'''
#per = Person('hanmeimei', 20, 170, 55)
#per.say()
#per1 = Person('hanme', 21, 171, 56)
#per1.say()
'''
析构函数:
    __del__() 释放对象时自动调用
'''
per = Person('hanmeimei', 20, 170, 55)
#释放对象:(对象释放后就不能再执行了)
#del per
per.say()
#while 1:
#    pass
'''
def func():#在函数里定义的对象会在函数结束时自动释放
    per2 = Person('a',1,1,1)
func()
while 1:
    pass
'''
