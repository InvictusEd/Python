import math


# 自定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
# 在缩进块中编写函数体，函数的返回值用return语句返回

# 我们自定义一个求绝对值的my_abs函数为例
# isinstance是错误异常处理
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-4))


# 定义空函数
def nop():
    pass


# pass的其他用法
age = 18
if age >= 18:
    pass


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 同时获得返回值（假象）
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# 实际上返回值是一个tuple
r = move(100, 100, 60, math.pi / 6)
print(r)


# 小结：定义函数时，需要确定函数名和参数个数，如有必要需要进行数据类型检查
# 函数体内用return随时返回函数结果
# 函数执行完毕也没有return时，自动return None
# 函数可以返回多个值，但其实就是一个tuple

# 练习：定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("bad operand type")
    flag = b ** 2 - 4 * a * c
    if flag > 0:
        x1 = (-b + math.sqrt(flag)) / (2 * a)
        x2 = (-b - math.sqrt(flag)) / (2 * a)
    elif flag == 0:
        x1 = x2 = (-b + flag) / (2 * a)
    elif flag < 0:
        return None
    return x1, x2


print(quadratic(1, 3, -4))
# a, b, c = 1, 2, 3
# print('%d,%d,%d' % (a, b, c))
# print("{0}{1}{2}".format(a, b, c))
# print(f"{a}{b}{c}")
