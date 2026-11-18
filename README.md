# My-Python-Learning-Journey

## 项目简介

本仓库用于存放《Python 语言》课程的练习程序与学习记录。目前包含两个小程序：

1. **BMI 计算器**：根据用户输入的身高和体重计算 BMI 指数，并判断体重状况（过轻 / 正常 / 过重 / 肥胖），帮助用户快速了解自己的身体质量指数。
2. **保险柜密码程序**：模拟密码验证场景，用户输入正确密码后"打开保险柜"，输入 q 可退出程序。

## 文件说明

| 文件名 | 用途 |
|---|---|
| `bmi_calculator.py` | BMI 计算器：输入身高体重，计算 BMI 并判断体重状况 |
| `safe_password.py` | 保险柜密码程序：while 循环验证密码，支持退出 |
| `README.md` | 项目说明文档 |

## 代码说明

### bmi_calculator.py

- 使用 `input()` 接收用户输入，并用 `float()` 将输入转换为浮点数；
- 核心公式：`bmi = weight / (height * height)`；
- 使用 `if...elif...else` 多分支结构，根据 BMI 数值区间输出不同的体重评价。

```python
height = float(input("请输入您的身高（米）："))
weight = float(input("请输入您的体重（千克）："))
bmi = weight / (height * height)

```

### safe_password.py

- 使用 `while True` 构建无限循环，持续接收密码输入；
- 使用 `break` 语句在密码正确或输入 q 时退出循环；
- 使用 `if...elif...else` 区分三种情况：退出、密码正确、密码错误。

```python
while True:
    user_input = input("请输入6位密码（输入q退出）：")
    if user_input == "q":
        break
    elif user_input == password:
        print("密码正确，打开保险柜！")
        break
```

## 学习心得与规划

通过浏览 GitHub 上其他 Python 项目，我发现优秀的项目都有结构清晰的 README 文档：用简洁的语言说明项目是做什么的、文件如何组织、核心代码怎么工作。这让我意识到，代码不仅要能运行，还要让别人看得懂、愿意用。本次编写 README 的过程，也让我第一次系统使用了 Markdown 的标题、列表、表格和代码块语法，体会到内容与排版分离的便利。

我计划以后每学完一课，就把课堂练习整理成规范的小程序提交到这个仓库，并为每个程序写好说明；期末时这个仓库将成为我完整的 Python 学习档案，也可以作为个人作品展示。
