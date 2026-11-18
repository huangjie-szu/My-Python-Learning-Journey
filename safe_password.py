password = "338822"
while True:
    user_input = input("请输入6位密码（输入q退出）：")
    if user_input == "q":
        print("已退出程序。")
        break
    elif user_input == password:
        print("密码正确。")
        break
    else:
        print("您输入的密码不正确，请重新输入。")
