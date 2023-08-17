# 继承和多态
class Animal:
    def run(self):
        print('Animal is running...')

# 狗类
class Dog(Animal):
    # 对子类增加方法
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')

# 猫类
class Cat(Animal):
    def run(self):
        print('Cat is running...')

# 子类自动有父类方法
dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

# 子类会覆盖父类方法
# 多态，调用方只管调用，不管细节
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())

# Python不需要传入Animal类型，只需要保证对象有一个run()方法
