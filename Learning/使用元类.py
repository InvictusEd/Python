# 使用元类
# 先定义函数
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

# 需要3个参数,class名称，继承父类集合，class的方法名称于函数绑定

h = Hello()
h.hello()
