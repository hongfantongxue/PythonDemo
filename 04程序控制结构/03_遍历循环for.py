"""
    author: shanghongfan
    Date: 2020/6/25 14:30
    Description: 
 """
"""
    主要形式:
            for 元素 in 可迭代对象:
                执行语句
"""
"""
    循环控住
    break 和 continue
"""

# for与else的配置
product_scores = [90, 78, 98, 75]
for score in product_scores:
    if score < 75:
        break
else:
    print("产品全部合格")
