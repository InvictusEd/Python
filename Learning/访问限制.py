# 访问限制
# 让内部属性不被外部访问
class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

# 如果要获取，要增加方法

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

# 如果要修改，增加方法，好处是可以做检查

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，
# 并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
# 不是private变量，所以，不能用__name__、__score__这样的变量名。

# 现在已经无法从外部访问__name和__score了
bart = Student('Bart Simpson', 59)
