# 函数的参数
# def power(x):
#     return x * x


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 默认参数可以简化函数的调用。设置默认参数时，要注意：
# 必选参数在前，默认参数在后
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
# 使用默认参数最大的好处是能降低调用函数的难度


print(power(5, 2))
print(power(5, 3))
print(power(5))


# 举个例子
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)


enroll('Sarah', 'F')


# 当要传入年龄、城市等信息时
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print("city:", city)


# 这样大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：
enroll('Sarah', 'F')
# 只有与默认参数不符的学生才需要提供额外的信息:
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


# 默认参数是可变参数，每次调用都会继承上一次
# def add_end(L=[]):
#     L.append('END')
#     return L


# 修改一下，改为不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


# 如果可以设计一个不变对象，那就尽量设计成不变对象


# 可变参数
# 由于参数个数不确定，我们首先想到可以把a, b, c作为一个list或tuple传进来
# 计算a^2+b^2+c^2
def calc(number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


# 在调用时需要先组装出一个list或tuple:
# 如果利用可变参数，调用函数的方式可以简化成这样：
print(calc([1, 2, 3]))
print(calc([1, 3, 5, 7]))


# 所以，我们把函数的参数改为可变参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 定义可变参数和定义一个list或tuple相比，仅仅加了一个*号，函数内部参数numbers接收到的是一个tuple
# 函数代码完全不变，但是，调用函数时，可以传入任意个参数，包括0个参数
print(calc(1, 2))
print(calc())
# 如果有一个list或者tuple，要调用可变参数
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
# 这种写法当然可以，但是太繁琐，所以我们可以在list或tuple前面加一个*号变成可变参数传进去
nums = [1, 2, 3]
print(calc(*nums))


# 相当有用

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 函数person除了必选参数外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
person('Michael', 30)
# 也可以传入任意个数的关键字参数
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
# 关键字参数可以扩展函数功能，比如在person里，我们保证能接收到name和age两个参数
# 但是，如果调用者愿意提供更多的参数，我们也能收到
# 和可变参数类似，也可以先组装出一个dict,然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
# 当然上面复杂的调用可以简化
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# kw将获得一个dict，注意kw获得的是一份拷贝，对kw的改动不会影响函数外的extra

# 命名关键字参数
# 以person()，希望检查是否有city和job参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
# 如果要限制关键字参数名字，可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的为命名关键字参数
person('Jack', 24, city='Beijing', job='Engineer')
# 命名关键字参数必须传入参数名，没有名字会报错
# 还可以缺省
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
# 由于city具有默认值，调用时，可以不传入city参数
person('Jack', 24, job='Engineer')

# 参数组合
# 必选参数、默认参数、可变参数、关键字参数、命名关键字参数5种
# 参数定义顺序必须是：必选、默认、可变、命名关键字、关键字
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
# 通过tuple和dict也可以调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# 所以对于任意函数，都可以通过类似func(*args, **kw)的形式去调用它，无论它的参数是如何定义的
# 虽然组合多达5种参数，但不要同时使用太多组合，否则函数接口的可理解性很差

# 练习
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
def mul(*x):
    sum = 1
    for i in x:
        sum = i * sum
    return sum
print(mul(5, 6))
