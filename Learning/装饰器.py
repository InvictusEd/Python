# 装饰器
def now():
    print('2022-12-28')

f = now
f()

# 函数对象有一个__name__属性，可以拿到函数名字
print(now.__name__)
print(f.__name__)

# 代码运行期间动态增加功能的方式，称之为“装饰器”(Decorator)
# 本质上，decorator就是一个返回函数的高阶函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# log是一个decorator，接受一个函数作为参数，并返回一个函数
# 借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2022-12-28')
# 调用now()函数，不仅会运行now()本身，还会在运行now()前打印一行日志
now()
