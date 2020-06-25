# 整数
# 默认十进制 二进制0b、八进制0o、十六进制0x
# 16 = 0b10000 = 0o20 = 0x10
i = 16
# 转二进制
a = bin(i)
# 转八进制
b = oct(i)
# 转十六进制
c = hex(i)
print(a, b, c)

# 二进制转十进制
d = int(a, 2)
# 八进制转十进制
e = int(b, 8)
# 十六进制转十进制
f = int(c, 16)
print(d, e, f)

# 四舍五入 round(a, 1) 1表示小数点后保留的位数
