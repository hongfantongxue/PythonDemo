"""
    author: shanghongfan
    Date: 2020/6/26 17:53
    Description: 迭代器
 """
"""
    1.排列组合迭代器
        1.1.笛卡尔积:product
        1.2.排列:permutations
        1.3.组合:combinations
        1.4.元素可重复组合:combinations_with_replacement
    2.拉链
        2.1.短拉链:zip
        2.2.长拉链:zip_longest
    3.无穷迭代器
        3.1.计数:count(start=0, step=1), 从start开始返回均匀间隔的值, step指定间隔
        3.2.循环:cycle(iterable),创建一个迭代器,返回iterable中所有元素, 无线重复
        3.3.重复:repeat(object, [times]), 不断重复object,times重复次数, times可省略
    4.其他迭代器
        4.1.锁链:chain()
        4.2.枚举:enumerate()
        4.3.分组:groupby()
    
"""
import itertools

"""
    笛卡尔积:
            ('A', '0')
            ('A', '1')
            ('B', '0')
            ('B', '1')
            ('C', '0')
            ('C', '1')
"""
for i in itertools.product("ABC", "01"):
    print(i)
# 取三个数,进行排列
for i in itertools.product("ABC", repeat=3):
    print(i)

for i in itertools.permutations("ABC", 3):
    print(i)

for i in itertools.combinations("ABC", 2):
    print(i)

for i in itertools.combinations_with_replacement("ABC", 2):
    print(i)

for i in zip("ABC", "123"):
    print(i)
"""
    长拉链:
    ('A', '1')
    ('B', '2')
    ('C', '3')
    ('?', '4')
    ('?', '5')
"""
for i in itertools.zip_longest("ABC", "12345", fillvalue="?"):
    print(i)
