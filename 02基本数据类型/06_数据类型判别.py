"""
    author: ShangHongfan
    Date: 2020/6/25 10:15
    Description:
 """
# 1.数据类型判别,type(变量)
age = 20
name = "张三"
print(type(age))
print(type(name))
# 2.检查字符串是否只有数字组成
print("20".isdigit())
# 3.检查字符串是否只有数字和字母组成
print("abc123".isalnum())

# 4.类型转换
# 4.1.数字类型转字符串
print("My age is " + str(age))
