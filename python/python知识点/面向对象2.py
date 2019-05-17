'''
__repr__()与__str__()
    重写:(将函数重新定义写一遍)
    __repr__():给机器用的,在解释器里面直接敲对象名回车的方法
    __str__():在print时自动调用,是给用户用,是一个描述对象的方法
    在没有str时只有repr时,有str = repr
    优点:
        打印对象的多属性
'''
class Person(object):
    #定义属性
    def __init__(self,name,age,height,weight, money):
        self.name = name
        self.age = age#私有属性
        self.height = height
        self.weight = weight
        self.__money = money#私有属性
    def __str__(self):
        return '%s-%d-%d-%d' %(self.name, self.age, self.height, self.weight)
    def run(self):
        print(self.__money)
    def setmoney(self, money):
        if money < 0:
            money = 0
        self.__money = money
    def getmoney(self):
        return self.__money
        
per = Person('hanmeimei', 20, 170, 55, 10000)
#per.__money = 21
#print(per.__money)
per.run()
'''
访问限制:
    如果让内部的属性不能再外部直接访问,在内部可以使用,但在外部可以用_Person__money访问
    在属性前加__那么这个属性就变成了私有属性
    通过自定义的方法实现对私有属性的赋值与取值
    __xxx__特殊变量,值可以直接访问的都当私有的使用
    _xxx 变量在外部也是可以直接访问的都当私有的使用
'''
per.setmoney(10)
print(per.getmoney())
#per.__money()#不能直接访问
per._Person__money = 1
#_Person__money可以访问
print(per.getmoney())

