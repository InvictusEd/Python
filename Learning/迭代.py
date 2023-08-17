from collections.abc import Iterable
# 迭代
# 用for循环遍历list或tuple
# 只要是可迭代对象都可以迭代
# 比如dict就可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
# 默认迭代的是key，如果要迭代value
for value in d.values():
    print(value)
# 同时迭代key和value
for k, v in d.items():
    print(k, v)

# 字符串也可以迭代

# 判断可迭代对象：collections.abc模块的Iterable类型判断
print(isinstance('abc', Iterable))

# 实现下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 练习，使用迭代查找一个list中最小和最大值，并返回一个tuple:
def findMinAndMax(L):
    if L == []:
        return (None, None)
    min = L[0]
    max = L[0]
    for i in L:
        if i < min:
            min = i
        elif i > max:
            max = i
    value = (min, max)
    return(value)

print(findMinAndMax([1,4,9]))
