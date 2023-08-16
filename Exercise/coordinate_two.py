# 阿拉伯数字转中文计数

from functools import reduce
from operator import add
from string import digits

Chinesedigits = "零一二三四五六七八九"
place = " 十百千万十百千亿十百千兆十百千"
mapping = dict(zip(digits, Chinesedigits))
number = 23385


def func10(number):
    flag1 = list(reversed(str(number)))
    flag2 = []
    for i in flag1:
        flag2.append(mapping[i])
    flag3 = list(zip(flag2, place))
    flag4 = []
    for i, j in flag3:
        flag4.append(i + j)
    result = list(reversed(flag4))
    return str(reduce(add, result)).strip()


print(func10(number))

# 数字转字符串然后取反赋值给a
# a = list(reversed(str(number)))
# b = []
# d = []
# print(a)
# for i in a:
# b为字典对应大写中文数字
#    b.append(mapping[i])
# print(b)
# c = list(zip(b, place))
# print(c)
# for i, j in c:
#    d.append(i + j)
# print(d)
# e = list(reversed(d))
# print(e)
# f = reduce(add, e)
# print(f)
