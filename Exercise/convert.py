# 阿拉伯数字转中文计数

dict1 = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七', 8: '八', 9: '九', 0: '零'}
dict2 = {1: '', 2: '十', 3: '百', 4: '千', 5: '万', 6: '十', 7: '百', 8: '千', 9: '亿', 10: '十', 11: '百', 12: '千'}
number = ''
flag1 = False
flag2 = False
count = 0
num = input("请输入要转换的数字:")
if num == '0':
    print('零')
else:
    list1 = num.split('.')
    list2 = list(str(list1[:1])[2:-2])
    for i in reversed(list2):
        count += 1
        if int(i) == 0:
            if flag1:
                if count != 5:
                    continue
                else:
                    number = dict2[count] + number
            else:
                if not flag2:
                    number = dict2[count] + number
                else:
                    number = '零' + number
            flag1 = True
        else:
            flag1 = False
            flag2 = True
            number = dict1[int(i)] + dict2[count] + number
    print(number)
