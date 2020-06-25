"""
    用 ""或者 ''表示
"""
# 双中有单
print("i'm 18 years old")
# 单中有双
print('"python" is good')
# 转义字符 \
# \ 还可以用于程序换行继续输入
s = "py\
thon"
print(s)

"""
    字符串性质
"""
str = "hello world"
# 索引
print(str[2])

# 字符串切片获取多个字符 0表示起始位置,3表示终止位置,1表示连续间隔
# [] 前闭后开
print(str[0:3:1])
print(str[0:3])
"""
    字符串拼接 +
    字符串成倍复制: 字符串 * n
"""


# 1.判断子字符串是否在原字符串中 in
str = "hello python"
print("llo" in str)
# 2.遍历字符串
for s in str:
    print(s)
# 字符串长度len()
print(len(str))

# 字符编码
# 将中文字库, 英文字母, 数字,特殊字符等转换成计算机可识别的二进制数
# 每个单一字符对应一个唯一的互不重复的二进制编码
# python中使用的是unicode编码
# 将字符转换为unicode编码, ord(字符)
print(ord("1"))
print(ord("a"))
print(ord("*"))
print(ord("中"))
print(ord("上"))

# 将unicode编码转换为字符, chr(编码)
print(chr(20013))




















