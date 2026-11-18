height = float(input("请输入您的身高（米）："))
weight = float(input("请输入您的体重（千克）："))

bmi = weight / (height * height)
print("您的BMI指数为：", bmi )

if bmi < 18.5:
    print("您的体重过轻～")
elif bmi < 24.9:
    print("正常范围，注意保持！")
elif bmi < 29.9:
    print("您的体重过重～")
else:
    print("肥胖，请注意健康！")
