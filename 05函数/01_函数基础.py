"""
    author: shanghongfan
    Date: 2020/6/25 15:55
    Description: 
 """


# 阶乘抽取为函数
def factoria(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(factoria(5))


# 关键字传参的方式
def function(x, y, z):
    print(x, y, z)


function(y=4, z=0, x=4)


# 默认参数
def student(name, age=19):
    print(name, age)


student("张三")


# 可变长参数 *args
def foo(x, y, z, *args):
    print(x, y, z)
    print(args)


foo(1, 2, 3, 4, 5, 6)

# 实参打撒,打散的是列表,字符串,元组或集合
foo(1, 2, 3, *[4, 5, 6])


# 可变长参数 *kwargs, 多于的参数,以字典的形式打包传递给kwargs
def foo1(x, y, z, **kwargs):
    print(x, y, z)
    print(kwargs)


foo1(1, 2, 3, a=1, b=2)


