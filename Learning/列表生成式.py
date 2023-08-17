# 列表生成式

# 要生成list
print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
# 但是太繁琐,列表生成式可以用一行语句生成
[x * x for x in range(1, 11)]

# 列表生成式要把生成的元素放到前面，后面跟for循环。
# for循环后面还可以加上if判断，这样就能筛选出偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])

# 使用两层循环生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# 运用列表生成式，写出非常简洁的代码

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

# 列表生成式也可以使用两个变量来生成list
print([k + '=' + v for k, v in d.items()])

# 把一个list中的所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# if else
# 在列表生成式中，for前面的if else 是表达式，而for后面的if是过滤条件，不能带else
print([x if x % 2 == 0 else -x for x in range(1, 11)])

# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]
print(L2)
