"""
    author: shanghongfan
    Date: 2020/6/25 14:15
    Description: 
 """
# set 集合 一系列互不相等的集合,无序的
student_set = {"张三", "李四", "王五", "张三"}
print(student_set)

# 集合运算
student_class1 = {"张三", "李四", "王五"}
student_class2 = {"李四", "王五", "赵六"}

# 交集运算
print(student_class1 & student_class2)
# 并集运算
print(student_class1 | student_class2)
# 差集运算
print(student_class1 - student_class2)
# 非共同元素
print(student_class1 ^ student_class2)

# 增加元素, 集合.add(元素)
student_set.add("赵六")
# 移除元素, 集合.remove(元素)
student_set.remove("赵六")
# 集合长度
print(len(student_set))
# 集合遍历
for i in student_set:
    print(i)
