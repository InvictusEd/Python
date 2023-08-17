from functools import reduce
# map/reduce
# map接受两个参数，一个是函数，一个是Iterable

# 把f(x)=x2 作用在一个list，可用map()实现
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# 把list所有数字转为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数
# reduce把结果继续和序列的下一个元素做累积计算，其效果是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 比如对一个序列求和，可以用reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))

# 换成整数13579
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def fn(x, y):
    return x * 10 + y
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(char2num, '13579')))

# 整理成一个str2int的函数就是
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

# 还可以用lambda函数进一步简化：
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# 练习，利用map()函数，把用户输入的不规范英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x, y: x * y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    idx = s.index('.')
    L1 = s[0:idx]
    #return L1
    L2 = s[(idx + 1):]
    f1 = reduce(lambda x, y: float(x) * 10 + float(y), L1)
    #return f1
    f2 = reduce(lambda x, y: float(x) * 10 + float(y), L2)
    return f1 + f2 / 10**len(L2)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
