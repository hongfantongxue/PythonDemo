"""
    求绝对值：abs()
    幂次方：pow(x,n) x的n次方
    pow(x, y, z) x的y次方再模运算z
    四舍五入：round(a, 2)
    整数商和模运算：divmod（13, 5） 输出结果：（2, 3）
    最大值与最小值：max(),min()
    求和函数：sum()
"""
"""
    借助python科学计算库math/scipy/numpy
"""
import math
# 指数运算 e = 2.71828183 的一次方
print(math.exp(1))
# 对数运算
print(math.log2(2))
# 开平方运算, 根号下4
print(math.sqrt(4))

import numpy as np
a = [1, 2, 3, 4, 5]
# 求平均值
print(np.mean(a))
# 求中位数
print(np.median(a))
# 求标准差
print(np.std(a))