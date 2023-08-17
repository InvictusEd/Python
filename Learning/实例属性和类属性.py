# 实例属性和类属性
class Student:
    name = 'Student'

    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90
print(s.name)
print(Student.name)
del s.name
print(s.name)

# 实例属性优先级比类属性高
