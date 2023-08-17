# 使用__slots__
class Student:
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

# 注意，__slots__仅在当前实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样子类实例允许定义的属性就是自身加上父类的__slots__

