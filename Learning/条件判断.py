# 条件判断
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
# 加上elif
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

再议input
birth = input('birth:')  # 输入报错，因为input()返回的数据类型是str，str不能直接和整数比较
if birth < 2000:
    print('00前')
else:
    print('00后')

s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 练习
height = 1.75
weight = 80.5
bmi = 80.5 / 1.75**2
print(f'BMI:{bmi:.2f}')
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi <= 25:
    print('正常')
elif 25 <= bmi <= 28:
    print('过重')
elif 28 <= bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')
