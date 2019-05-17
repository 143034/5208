from student import Student
stu = Student('tom',18,1000,110)
print(stu.name,stu.age,stu.stuId)
stu.eat()
print(stu.getMoney())

#person私有属性money没有继承但可以通过setMoney和getMoney()
