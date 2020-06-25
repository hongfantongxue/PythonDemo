"""
    author: shanghongfan
    Date: 2020/6/25 12:20
    Description: 列表
                字符串转列表,元组转列表,集合转列表,列表拼接,增加元素,
                删除元素,查找元素,修改元素,列表复制,列表排序
 """
num_list = [1, 2, 3, 4, 5]
print(num_list[1])

# 1.字符串转列表,结果:['人', '工', '智', '能', '是', '未', '来', '趋', '势']
print(list("人工智能是未来趋势"))
# 2.元组转列表,结果:[1, 2, 3, 4, 5]
print(list((1, 2, 3, 4, 5)))
# 3.集合转列表,结果:['李四', '张三', '王五']
print(list({"张三", "李四", "王五", "张三"}))
# 特殊列表:range()
# range(起始数字, 终止数字, 数字间隔)
# 打印0 - 5的值
for i in range(6):
    print(i)
# range()转列表,结果:[0, 1, 2, 3, 4, 5]
print(list(range(6)))

# 4.列表拼接
list1 = [1, 2]
list2 = [3, 4]
# 结果:[1, 2, 3, 4]
print(list1 + list2)

# 5.增加元素
languages = ["java", "c", "python"]
languages2 = ["C#", "python"]
# 插入末尾
languages.append("c#")
# 插入指定位置
languages.insert(1, "R")
# 在末尾整体并入另一个列表
languages.extend(languages2)
# 将一个列表整体作为一个元素添加到另一个列表中
languages.append(languages2)
# 6.删除元素, 列表.pop(位置), 不写位置默认删除最后一个
languages.pop(1)
# 删除元素, 列表.remove(待删元素),删除列表中第一个出现的该元素
languages.remove("python")
# 7.查找元素,列表中第一次出现该元素的位置,列表.index(待查元素)
print(languages.index("python"))
# 8.修改元素, 列表名[位置] = 新值
languages[1] = "C++"
# 9.列表复制 列表.copy()和列表[:] 两个方法
languages3 = languages.copy()
print(languages3)
languages4 = languages[:]
print(languages4)
print(languages)

# 10.列表排序, 列表.sort(),从小到大;列表.sort(reverse = True),从大到小
ls = [2, 5, 1, 3, 15, 4, 7, 3, 0, 2]
ls.sort()
print(ls)

# 使用sorted(列表)对列表进行临时排序,原列表保持不变,返回排序后的列表
ls_2 = sorted(ls, reverse=True)
print(ls_2)

# 列表翻转,列表.reverse()
ls.reverse()

# for循环对列表进行遍历
for i in ls:
    print(i)
