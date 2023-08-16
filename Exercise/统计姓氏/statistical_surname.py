"""
统计出现频率最高的前三的姓氏及次数
"""
import os
from collections import Counter

# os.chdir(os.path.expanduser("~/Desktop"))
name = []
with open("cs20.csv") as file:
    file.readline()
    for line in file:
        name.append(line.strip().split(",")[1][0])
print(Counter(name).most_common(3))
# d={}
# for i in name:
#     d.setdefault(i, 0)
#     d[i]+=1
# print(sorted(d.items(), key=lambda x:x[1], reverse=True))
