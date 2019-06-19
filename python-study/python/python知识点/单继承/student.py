from person import Person
class Student(Person):
    def __init__(self, name, age, money, stuId):
        #调用父类中的__init__Person属性
        super(Student, self).__init__(name, age, money)
        #独有属性
        self.stuId = stuId
