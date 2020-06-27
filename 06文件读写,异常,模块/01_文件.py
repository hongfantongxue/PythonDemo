"""
    author: shanghongfan
    Date: 2020/6/25 18:54
    Description: 
 """
"""
    文件打开通用格式:
    with open("文件路径", "打开模式", encoding = "gbk") as f:
        text = f.read()
        print(text)
    打开模式: r:只读模式,如果文件不存在,报错
             w:覆盖写模式,如果文件不存在,则创建;如果存在,则完全覆盖原文件
             x:创建写模式,如果文件不存在,则创建;如果文件存在,报错
             a:追加写模式,如果文件不存在,则创建;如果文件存在,则在原文件后追加内容
             b:二进制文件模式,需要配合使用如:"rb","wb","ab",该模式不需指定encoding
             t:文本文件模式,默认值,需要配合使用如:"rt","wt","at",一般省略,简写成如"r","w","a"
             +:与r,w,x,a配合使用,在原基础上增加读写功能,如r+,w+,a+
"""
with open("D:\\1.txt", "r") as f:
    text = f.read()
    print(text)

# f.readline(), 每次只读取一行
with open("D:\\1.txt", "r") as f:
    text_1 = f.readline()
    print(text_1)
    text_2 = f.readline()
    print(text_2)

# f.readlines(), 读入所有行,以每行为元素形成一个列表
with open("D:\\1.txt", "r") as f:
    text = f.readlines()
    print(text)

# f本身就是一个可迭代对象
with open("D:\\1.txt", "r") as f:
    for text in f:
        print(text)

# 二进制文件(图片)
with open("D:\\Black_Footed_Albatross_0002_55.jpg", "rb") as f:
    print(f.readlines())

"""
    文件的写入:
    
"""
with open("D:\\1.txt", "a") as f:
    f.write("qqq,www,eee\n")
    f.write("rrr,ttt,yyy\n")

# 将一个元素为字符串的列表整体写入文件,f.writelines()
ls = ["yyy\n", "xxx\n", "zzz\n"]
with open("D:\\1.txt", "a") as f:
    f.writelines(ls)

# 既读又写
with open("D:\\1.txt", "a+") as f:
    # a 默认指定在末尾
    # 移动指针
    f.seek(0,  0)
    text = f.readlines()
    print(text)
    f.writelines(ls)
