# 序列化
import pickle

# 写入
d = dict(name='Bob', age=20, score=88)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 读出
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
