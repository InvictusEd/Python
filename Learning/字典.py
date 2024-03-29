# 使用dict和set
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也成为map
# 使用键-值(key-value)存储，具有极快的查找速度

# 根据同学的名字查找对应的成绩，用list实现
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
# 给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩,list越长，耗时约长

# 如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表多大，查找速度都不会变慢。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 67
print(d['Adam'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

# 如果key不存在，dict就会报错
# 要避免key不存在的错误，有两种办法
# 一是通过in判断key是否存在：
print('Thomas' in d)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas', -1))
# 返回None时Python的交互环境不显示结果

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)
# dict内部存放的顺序和key放入的顺序是没有关系的
# dict特点：查找和插入的速度极快，不会随着key的增加而变慢
# 需要占用大量的内存，内存浪费多

# list与之相反
# list特点，查找和插入时间随着元素的增加而增加；
# 占用空间小，浪费内存很少
# 所以dict是用空间来换取时间的一种方法

# dict无处不在，正确使用dict非常重要，牢记dict的key必须是不可变对象
# 因为dict根据key来计算value的存储位置，如果每次计算相同的key得出结果不同，那dict内部完全混乱了。
# 这个通过key计算位置的算法称为哈希算法(Hash)
# 要保证hash的正确性，作为key的对象就不能变。因此在Python中，字符串、整数等都是不可变的，因此，可以放心的作为key。
# 而list是可变的，就不能作为key

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 要创建一个set，需要提供一个list作为输入集合
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)
# 注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1, 2, 3这3个元素，
# 显示的顺序也不表示set是有序的
s = set([1, 1, 2, 2, 3, 3])
print(s)  # 重复的元素在set中自动被过滤

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样
# 所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”

# str是不变对象，而list是可变对象，对list进行操作是会变化的
a = ['c', 'b', 'a']
a.sort()
print(a)
# 对str进行操作
a = 'abc'
a.replace('a', 'A')
print(a)  # 结果仍然是abc
# 将代码改成这样
a = 'abc'
b = a.replace('a', 'A')
print(b)
# 所以对于不变对象，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远不可变

# 小结：使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串
# tuple虽然是不可变对象，试试(1, 2, 3)和(1, [2, 3])放入dict或set中
a = {(1, 2, 3): (1, [2, 3])}
print(a[(1, 2, 3)])  # tuple可以作为dict的value
# a = {(1, [2, 3]): 9}
# print(a[(1, [2, 3])])   # tuple中不包含list子集时可以作为key
s = set((1, 2, 3))
print(s)
s = set((1, [2, 3]))    # idea编译器不会报错，但IDLE会报错
print(s)    # 所以带list子集的tuple也不能作为set的key

