# Python内建的filter()函数用于过滤序列
# filter()也接收一个函数和一个序列，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素

# 例如，在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# filter()这个高阶函数用于筛选
# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

# 用filter求素数，埃氏筛法
# 生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
# 生成器
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 这个生成器先返回第一个素数2，然后，利用filter()不断产生筛选后的新的序列。
# 由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    num = str(n)
    while len(num) >0:
        if len(num) == 1:
            return True
        if num[0] == num[-1]:
            num = num[1:len(num)-1]
            continue
        else:
            return False
    return True

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')