# 定制类
class Student(object):
    def __init__(self, name):
        self.name = name

    # 打印的好看,str返回用户看到
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # 调试用repr
    def __repr__(self):
        return 'Student object (name: %s)' % self.name

    # getattr方法，动态返回一个属性
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
            # 返回函数也是可以的，但是调用方式要变为s.age()
            # return lambda: 25

    # __call__()方法，可以直接对实例进行调用
    def __call__(self):
        print('My name is %s.' % self.name)

# iter方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    # 要取出像list那样的元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

if __name__ == '__main__':
    s = Student('Michael')
    print(s)
    # iter,next
    for n in Fib():
        print(n)
    f = Fib()
    # getitem
    print(f[0])
    print(f[2])

    # 但是list有个神奇的切片方法：
    print(list(range(100))[5:10])
    # 对于Fib报错,我们要在getitem做判断
    print(f[0:5])
    # call方法调用
    s()
    # 通过callable()函数，我们可以判断一个对象是否是“可调用”对象
    print(callable('str'))
    print(callable(Student))
