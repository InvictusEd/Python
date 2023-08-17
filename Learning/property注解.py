# property
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


if __name__ == '__main__':
    s = Student()
    s.score = 60
    print(s.score)
    s.age = 6


# @property可以让调用者写出简短的代码，同时保证对参数进行必要的检查

