# 云南行政区域划分

# 原始的yn.txt中的“兰坪白族普米族自治县”和yunnan.txt中的“兰坪普米族白族自治县”名称不一致，导致输出的数据有误
# yunnan.txt中的镇和街道可能数据有误，和全省行政区划设置情况统计表对应不上
d1 = {}
with open('yn.txt', mode='r', encoding='utf-8') as f1:
    for line in f1:
        city, *county = line.strip().split()
        d1.update({city: county})
dijishi = zizhizhou = 0
yn = set(d1)
for i in yn:
    if i.endswith("市"):
        dijishi += 1
    elif i.endswith("自治州"):
        zizhizhou += 1
print("云南省有", dijishi, "个地级市", "和", zizhizhou, "个自治州\n", sep="")

xian = zizhixian = xianjishi = qu = 0
ynxian = ynzizhixian = ynxianjishi = ynqu = 0
for i, j in d1.items():
    for k in j:
        if k.endswith("县") and not k.endswith("自治县"):
            xian += 1
            ynxian += 1
        elif k.endswith("自治县"):
            zizhixian += 1
            ynzizhixian += 1
        elif k.endswith("市"):
            xianjishi += 1
            ynxianjishi += 1
        elif k.endswith("区"):
            qu += 1
            ynqu += 1
    print(f"{i}有{xian}个县，{zizhixian}个自治县,{xianjishi}个县级市，{qu}个区")
    xian = zizhixian = xianjishi = qu = 0
print("\n")

d2 = {}
with open('yunnan.txt', mode='r', encoding='utf-8') as f2:
    for line in f2:
        xian, *xiang = line.strip().split()
        d2.update({xian: xiang})
# pprint.pprint(d2)
xiang = minzuxiang = zhen = jiedao = 0

for i, j in d2.items():
    for k in j:
        if k.endswith("乡") and not k.endswith("族乡"):
            xiang += 1
        elif k.endswith("族乡"):
            minzuxiang += 1
        elif k.endswith("镇"):
            zhen += 1
        elif k.endswith("街道"):
            jiedao += 1
    print(f"{i}有{xiang}个乡，{minzuxiang}个民族乡,{zhen}个镇，{jiedao}个街道")
    xiang = minzuxiang = zhen = jiedao = 0
print("\n")

dizhouxiang = dizhouminzuxiang = dizhouzhen = dizhoujiedao = 0
ynxiang = ynminzuxiang = ynzhen = ynjiedao = 0
for i, j in d1.items():
    for n, m in d2.items():
        if n in j:
            for k in m:
                if k.endswith("乡") and not k.endswith("族乡"):
                    dizhouxiang += 1
                    ynxiang += 1
                if k.endswith("族乡"):
                    dizhouminzuxiang += 1
                    ynminzuxiang += 1
                if k.endswith("镇"):
                    dizhouzhen += 1
                    ynzhen += 1
                if k.endswith("街道"):
                    dizhoujiedao += 1
                    ynjiedao += 1
    print(f"{i}有{dizhouxiang}个乡，{dizhouminzuxiang}个民族乡，{dizhouzhen}个镇，{dizhoujiedao}个街道")
    dizhouxiang = dizhouminzuxiang = dizhouzhen = dizhoujiedao = 0
print("\n")
print("云南共有", ynxian, "个县，", ynzizhixian, "个自治县，", ynxianjishi, "个县级市，", ynqu, "个区", sep="")
print("云南共有", ynxiang, "个乡，", ynminzuxiang, "个民族乡，", ynzhen, "个镇，", ynjiedao, "个街道", sep="")
