# 查看函数帮助
help(abs)
# abs()函数
print(abs(-20))
# TypeError报错，函数参数类型和参数数量
# max函数
print(max(2, 3, 1, -5))
# 数据类型转换
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(bool(1))
print(bool(''))
# 把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-1))

# 练习，用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
