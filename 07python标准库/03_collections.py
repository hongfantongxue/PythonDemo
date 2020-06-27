"""
    author: shanghongfan
    Date: 2020/6/26 17:53
    Description: 容器数据类型
 """
"""
    1.具名元组
        typename: 元组名字, field_names:域名
        collections.namedtuple(typename, field_names)  
    2.计数统计,是一个字典类型
        Counter()
        频率统计
            Counter(colors).most_common(3)
    3.双向队列, deque
           
"""
import collections

point = collections.namedtuple("Point", ["x", "y"])
p = point(x=1, y=2)
print(p)
print(p.x, p.y)
from collections import Counter, deque

# 计数统计, 结果:Counter({'1': 1, '2': 1, '3': 1})
print(Counter("123"))

colors = ["red", "blue", "red", "green", "blue", "blue"]
# 取出3个频率最高的元素和计数
Counter(colors).most_common(3)

# 将每一个元素展开, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print(list(Counter("1234567890").elements()))
# 双向队列
d = deque("abc")
# 增加
d.append("d")
# 左端增加
d.appendleft("d")
# 删除
d.pop("c")
# 左端删除
d.popleft("a")
