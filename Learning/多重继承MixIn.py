# 多重继承MixIn
class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, RunnableMixIn):
    pass
