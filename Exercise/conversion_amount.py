"""
数字金额转换中文金额案例
六十万零四千 604000
六十八万 680000
七万八千 78000
一百万零四百 1000400
"""
dict1 = {1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍',6: '陆', 7: '柒', 8: '捌', 9: '玖', 0: '零'}
dict2 = {1: '元', 2: '拾', 3: '佰', 4: '仟', 5: '万',6: '拾', 7: '佰', 8: '仟', 9: '亿', 10: '拾',11: '佰', 12: '仟', 13: '角', 14: '分', 15: '整'}
money = '' # 整个输出的过程就是个字符串拼接的过程
flag = False # 十百千的零不用管,flag用来处理0
flag2 = False # 判断是否需要填加大写零
isint = False # 是否是整数
count = 0 # 适用于整数
count2 = 12 # 适用于小数
num = input("小盆友,请输入要转换的数字金额:")
if num == '0':
    print('0元整')
else:
    aa = num.split('.') # split分出来的是列表,aa就变成了有两个元素的列表
    bb = list(str(aa[:1])[2:-2]) # bb存储的数字金额的整数部分,列表转成字符再转列表
    cc = list(str(aa[1:])[2:-2]) # cc存储的是数字金额的小数部分
    if len(cc) <= 0: # 判断输入的数字金额是否是整数或是小数,定下标签
        isint = True # 的确是整数
    else:
        isint = False # 有小数部分

    for i in reversed(bb): # reversed函数返回一个翻转的迭代器 123456-->54321从个位开始处理
        count += 1 # count用来选择后面具体是哪一个对应的称呼
        if int(i) == 0: # 如果当前碰到的数字是0
            if flag == True:
                if count != 5: # 万以下的直接念 不涉及念零的问题，比如说4000四千，和0没关
                    continue # 跳过当前一层循环 来到下一个for循环
                else: # 超过了万,就得把万加进去
                    money = dict2[count] + money #把万加进去
            else: # flag = False的情况,已经超出了万数
                if flag2 == False: # 如果数字不需要读零，直接加入
                    money = dict2[count] + money
                else: # 数字不是结尾是零就得念出来
                    money = '零' + money
            flag = True # 把0处理掉之后置flag为True，第一个0不用管，所以最开始没啥事
        else: # i不是零的情况
            flag = False # 把flag回置成False
            flag2 = True # 以防下一次碰到零，下一次碰到0的时候，就得考虑读零的事情了
            money = dict1[int(i)] + dict2[count] + money
    for i in cc: # 处理小数部分,在dict2的后半段,所以定义count2来找后面的分,角
        count2 += 1
        money = money + dict1[int(i)] + dict2[count2]
    if isint == True: # 整数金额数加个整
        money += '整'

    print(money)
