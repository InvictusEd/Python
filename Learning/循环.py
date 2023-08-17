# 循环
# Python的循环有两种，一种是for...in循环，
# 依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
# 所以for x in... 循环就是把每个元素带入变量x，然后执行缩进块的语句

# 再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# 如果要计算1-100的整数之和，从1写到100，Python提供了一个range()函数，可以生成一个整数序列
# 再通过list()函数可以转换为list
# 比如range(5)生成的序列是从0开始小于5的整数:
print(list(range(5)))
# 生成0-100的整数序列
print(list(range(101)))
# 计算如下
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环
# 计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 练习，用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print("Hello,", x)

# break语句，提前退出循环
# 循环打印1-100的数字
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
# 如果要提前结束循环，可以用break语句:
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break;
    print(n)
    n = n + 1
print('END')

# continue语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    print(n)
# 上面的程序可以打印出1-10，但是如果只想打印奇数，可以用continue语句跳过某些循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n为偶数，执行continue语句
        continue
    print(n)

# 小结：break和continue通常配合if语句使用，不要滥用break和continue，容易造成代码逻辑分叉过多，容易出错。
# 大多数循环并不需要用到break和continue语句，上述例子都可以通过改写循环条件或者修改循环逻辑值，去掉break和continue语句。
# ctrl+c 可以推出死循环程序
