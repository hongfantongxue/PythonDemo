# 1.程序中定义
age = 18
name = "tom"

# 2.动态输入
x = eval(input("输入一个数:"))
print(x)

# 输出
# 1.格式化输出方法format
# 基本格式: "字符{0}字符{1}",format(v0,v1)
PI = 3.1415
E = 2.71828
print("PI = {0},E = {1}".format(PI, E))

# 2.浮点型简化输出
# 2.1.留两位小数
print("{0:.2f}".format(PI))
# 2.2.按百分位输出
print("{0:.1%}".format(0.8786))
# 2.3.科学计数法输出
print("{0:.2e}".format(0.8786))
# 2.4.整数的进制转换输出
# 十进制整数转二进制,unicode码,十进制,八进制,十六进制输出
print("二进制{0:b}, unicode码{0:c},十进制{0:d},八进制{0:o}, 十六进制{0:x}".format(450))
