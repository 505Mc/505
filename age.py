print("欢迎来到年龄计算器！")
age = 0

# 这是防护代码，输入字母/符号都不会崩溃
try:
    add = int(input("年龄增长："))
    final_age = age + add
    print("你的最终年龄：", final_age)
    
    if final_age >= 18:
        print("你成年了")
    else:
        print("你未成年")

except ValueError:
    print("输入有误！请输入数字")
