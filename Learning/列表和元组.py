# 列表：list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))

# 索引访问list中每一个元素
print(classmates[0])
print(classmates[1])
print(classmates[2])

# 确保索引不越界，最后一个元素的索引是-1
print(classmates[-1])
# 倒数第2，第3，4会越界
print(classmates[-2], classmates[-3])

# list是一个可变的有序表，可往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 把元素插入到指定位置
classmates.insert(1, 'Jack')
print(classmates)

# 删除list末尾的元素，用pop()方法: 出最后一个元素
classmates.pop()
print(classmates)
classmates.pop(1)  # 指定元素
print(classmates)

# 把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

# list的元素类型可以不同
L = ['Apple', 123, True]
print(L)

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s)
# 将其拆开理解
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s)

# 空list
L = []
print(len(L))

# 另一种有序列表元组:tuple，一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
# tuple的意义：因为tuple不可变，所以代码更安全，如果可能，能用tuple代替list就尽量用tuple
# tuple的陷阱：当定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)
# 空tuple
t = ()
print(t)
# 1个元素的tuple
t = (1)  # ()被python认为是数学公式中的小括号，产生了歧义,所以这里实际上是t = 1
print(t)
t = (1,)  # 用,来消除歧义
print(t)

# "可变的"tuple  tuple指向不变，但指向的list是可变的
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# 练习：用索引取出下面list的指定元素
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple
print(L[0][0])
# 打印Python
print(L[1][1])
# 打印Lisa
print(L[2][2])
# 小结：list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们
