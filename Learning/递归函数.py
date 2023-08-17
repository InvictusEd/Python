# 递归函数
# 一个函数在内部调用自身本身，这个函数就是递归函数

#举个例子
# 计算阶乘 n! = 1 * 2 * 3 ... * n
# 用函数fact(n)表示，可以看出：fact(n)可以表示为n * fact(n-1)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(1))
print(fact(5))
# 递归函数定义简单，逻辑清晰，但要注意防止栈溢出
# fact(1000)
# 解决栈溢出用尾递归优化
# 尾递归：在函数返回时候，调用自身本身，并且，return语句不能包含表达式
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


fact_iter(5, 1)

# 练习：汉诺塔问题
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)
move(3, 'A', 'B', 'C')
