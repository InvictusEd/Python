# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素
print(L[0], L[1], L[2])
# 用循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
# 对于这种指定索引范围的操作，Python提供了切片操作符
print(L[0:3])
# 如果第一个索引是0，还可以省略
print(L[:3])
# 支持倒数切片
print(L[-2:])
print(L[-2:-1])
# 记住倒数第一个元素索引是-1

# 我们创建一个0-99的数列：
L = list(range(100))
print(L)
# 获取前十个数
print(L[:10])
# 后十个数
print(L[-10:])
# 前11-20个数
print(L[10:20])
# 前10个数，每两个取一个
print(L[:10:2])
# 所有数，每5个取一个
print(L[::5])
# 什么都不写，原样复制
print(L[:])

# tuple切片
print((0, 1, 2, 3, 4, 5)[:3])

# 字符串切片
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

# 练习：利用切片操作实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    if len(s) == 0:
        return s
    else:
        while len(s) > 0 and (s[0] == ' ' or s[0] == '\t'):
            s = s[1:]
        while len(s) > 0 and (s[-1] == ' ' or s[-1] == '\t'):
            s = s[:-1]
    return s
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')