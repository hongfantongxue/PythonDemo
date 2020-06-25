"""
    author: shanghongfan
    Date: 2020/6/25 14:30
    Description: 
 """
# 单分支
age = 8
if age > 7:
    print("age大于7")

# 二分支
if age > 7:
    print("age大于7")
else:
    print("age不大于7")
# 多分支
money = 100000
if money < 100:
    print("小于100")
elif money < 1000:
    print("小于1000")
elif money < 10000:
    print("小于10000")
else:
    print("土豪")

# if嵌套语句
age = eval(input("请输入年龄:"))
if age > 18:
    """
        bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
        bool 是 int 的子类
        bool(0) ==>False
        bool(1)==>True
    """
    is_pubic_place = bool(eval(input("请输入是否为公共场合:1表示公共场合,0表示非公共场合")))
    if not is_pubic_place:
        print("可以吸烟")
    else:
        print("公共场合禁止吸烟")
else:
    print("小于18禁止吸烟")
