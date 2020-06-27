"""
    author: shanghongfan
    Date: 2020/6/26 17:52
    Description: 处理随机问题的标准库
 """
"""
    1.随机种子, seed(种子),相同的随机种子会产生相同的随机数, 如果不设置随机种子,以系统当前时间为默认值
    2.产生随机整数
        randint(a,b), 产生[a,b]之间的随机整数        
        randrange(a), 产生[0,a)之间的随机整数 
        randrange(a,b,step), 产生[a,b)之间的随机整数,以step为步长
    3.产生浮点数
        random(),产生[0.0,1.0)之间的随机浮点数
        uniform(a,b), 产生[a,b]之间的浮点数
    4.序列用函数
        choice(seq), 从序列类型中随机返回一个元素
        choices(seq,weights=None,k), 对序列类型进行k次重复采样,可设置权重
        shuffle(seq), 将序列中的元素随机排列, 返回打乱中后的序列
        sample(pop, k), 从pop类型中随机选取k个元素, 以列表类型返回
    5.概率分布
        gauss(mean, std) 生产一个符合高斯分布的随机数
        
"""
from random import *
seed(10)
print(random())

print(randrange(10))
print(randrange(1, 10, 2))

print(choice(["java", "C#", "python"]))
print(choice(("java", "C#", "python")))
print(choice("abcd"))

print(choices(["java", "C#", "python"], [3, 3, 4], k=10))

numbers = ["1", "2", "3", "4"]
shuffle(numbers)
print(numbers)

print(sample(numbers, k=3))

print(gauss(0, 1))

# 多取几个数, 生成高斯分布直方图
import matplotlib.pyplot as plt
res =[gauss(0, 1) for i in range(100000)]
plt.hist(res, bins=10000)
plt.show()

# 生成四位由数字和字母构成的验证码
import random
import string

print(string.digits)
print(string.ascii_letters)
str = string.digits + string.ascii_letters
i = 0
while i <= 100:
    v = random.sample(str, k=4)
    print(v)
    print(''.join(v))
    i+=1