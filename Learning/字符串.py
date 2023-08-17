print('I\'m \"OK\"!')
print('''line1
line2
line3''')
print(10/3)
# 地板除
print(10//3)
print(10%3)

# 字符串
# !/usr/bin/env python3  这一行注释为了告诉Linux/OS X系统，这是一个Python可执行程序,Windos系统会忽略这个注释
# -*- coding: utf-8 -*- 这一行注释为了告诉Python解释器，按照UTF-8编码读取源代码，否则中文输出可能会乱码
# 且确保文编编辑器正在使用UTF-8 without BOM编码
print('包含中文的str')
print(ord('A'))  # 获取字符的整数表示
print(chr(66))  # 把编码转换成对应字符

len('ABC')  # 计算包含的字符

# 格式化字符串
print('Hello %s' % 'World')
print('I have %d$' % 10000)
print('You have %.2f$' % 3.1415)
print('Age:%s. Gender:%s' % (25, True)) # %s是万能的
print('rate:%d%%' % 7)

# 格式化字符串format()方法
print('{0}成绩提升了{1}%'.format('小明', 17))
print('{0}成绩提升了{1:.1f}%'.format('小明', 17.256))

# 格式化字符串f-string
r = 2.5
s = 3.14*r**2
print(f'The area of a circle with radius {r} is {s:.2f}')

# 练习
s1 = 72
s2 = 85
r = (85-72)/72*100
print(f"小明成绩提升了{r:.1f}%")
print("小明成绩提升了{0:.1f}%".format(r))
print("小明成绩提升了%.1f%%" % r)