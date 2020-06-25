"""
    author: shanghongfan
    Date: 2020/6/25 13:24
    Description: 
 """
# tuple 元组,元素不支持修改
num_tuple = (1, 2, 3, 4, 5)

numbers = [202001, 202002, 202003]
name = ["张三", "李四", "王五"]
print(list(zip(numbers, name)))

for number, name in zip(numbers, name):
    print(number, name)