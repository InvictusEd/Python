gender = input("请输入您的性别(男/女)：")
weight = eval(input("请输入您的体重（kg）："))
height = eval(input("请输入您的身高(m)："))
waist = eval(input("请输入您的腰围(cm)："))

BMI = weight/height ** 2

print("您的BMI值 = ", '%.1f' % BMI)
print("您的体重分类为：")
if BMI >= 28.0:
    print("肥胖")
elif 24.0 <= BMI < 28.0:
    print("超重")
elif 18.5 <= BMI < 24.0:
    print("体重正常")
elif BMI < 18.5:
    print("体重过低")

print("您的中心型肥胖分类为：")
if gender == "男":
    if 85 <= waist < 90:
        print("中心型肥胖前期")
    elif waist >= 90:
        print("中心型肥胖")
    else:
        print("无中心型肥胖症状")
if gender == "女":
    if 80 <= waist < 85:
        print("中心型肥胖前期")
    elif waist >= 85:
        print("中心型肥胖")
    else:
        print("无中心型肥胖症状")
