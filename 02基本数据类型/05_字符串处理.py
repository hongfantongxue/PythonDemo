"""
    author: shanghongfan
    Date: 2020/6/25 09:15
    Description:
 """
# 字符串分割, split(分割字符)
str = "java,c,c#,php,html,python,java"
str_list = str.split(",")
print(str)
print(str_list)
# 字符串聚合, "聚合字符".join(可迭代数据类型:如字符串/列表)
s = "1234567"
s_join = ",".join(s)
print(s)
print(s_join)

# 删除字符串两端指定字符, 字符串.strip("指定删除的字符")

# 字符串替换, 字符串.replace("被替换","替换成")

# 字符串统计, 字符串.count("待统计字符串")
print("java:", str.count("java"))

# 字符串大小写
# 字符串.upper(), 字母全部大写
# 字符串.lower(), 字母全部小写
# 字符串.title(),首字母大写

