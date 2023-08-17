# 偏函数
import functools

int2 = functools.partial(int, base=2)
print(int2('1000000'))
# functools.partial的作用就是把一个函数的某些参数固定住

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
