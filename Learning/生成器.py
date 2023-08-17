# 生成器
# Python中一边循环一边计算的机制，称为生成器generator

# 把一个列表生成式的[]改成(),就创建了一个generator
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L)
print(g)

# 打印generator的元素，需要通过next()函数获取generator的下一个返回值
print(next(g))

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到没有元素

# 使用for循环，generator是可迭代对象
g = (x * x for x in range(10))
for n in g:
    print(n)

# 著名的斐波那契数列(Fibonacci)，除第一个和第二个数外，任意一个数都可由前两个数相加得到
# 斐波那契数列用列表生成式写不出来，但是，用函数把它打印出来很容易：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
# 上面的函数可以输出斐波那契数列的前N个数
print(fib(6))

# 把fib函数变成generator函数，只需要把print(b)改为yield b就可以了：
def fib(max):
    n, a, b  = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 这是定义generator的另一种方法，如果一个函数包含yield关键字，那么这个函数就不再是一个
# 普通函数，而是一个generator函数，返回的是一个generator
f = fib(6)
print(f)

# 练习，杨辉三角，把每一行看做一个list，写一个generator，不断输出下一行的list
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)
