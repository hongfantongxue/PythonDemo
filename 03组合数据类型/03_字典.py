"""
    author: shanghongfan
    Date: 2020/6/25 13:29
    Description: 
 """
# dict 字典 {key1: value1, key2, value2, ...}
student = {202001: "张三", 202002: "李四", 202003: "王五"}
print(student[202002])

# 字典的长度, 键值对的个数
print(len(student))
# 字典的索引
print(student[202002])
# 增加键值对 变量名[新建] = 新值
student[202004] = "赵六"
print(student)
# 删除键值对
del student[202004]
print(student)
# 删除键值对, 变量名.pop(待删除的键)
value = student.pop(202002)
print(value)
print(student)
# 随机删除一个键值对, 并以元组返回删除键值对
key, value = student.popitem()
print(key, value)
print(student)

# 修改键值对
student[202001] = "小明"
print(student)

# 字典.get(key, default) 从字典中获取键key对应的值,如果没有这个键,则返回default
str = "牛奶奶找刘奶奶买牛奶"
d = {}
for i in str:
    d[i] = d.get(i, 0)+1
print(d)

# 字典.keys() 字典.values()方法
print(list(student.keys()))
print(list(student.values()))

# 字典的遍历, 字典.items()
for k, v in student.items():
    print(k, v)