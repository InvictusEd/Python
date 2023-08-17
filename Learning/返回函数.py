# 返回函数
def createSum(*n):
    def sum():
        ax = 0
        for i in n:
            ax = ax + i
        return ax
    return sum

f = createSum(1, 2, 3)
print(f())
