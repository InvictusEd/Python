"""
限制人数抽签
exe文件是直接可运行程序
"""
import os
import random

# 读取文件中的学生名单
with open('st.txt', 'r', encoding='utf-8') as f:
    students = f.readlines()

# 去除每个学生名字末尾的换行符
students = [s.strip() for s in students]

# 抽取6个名字
selected = random.sample(students, 6)

# 输出抽取结果
print("抽取的6名学生是：")
for name in selected:
    print(name)

os.system("pause")
