"""
    author: shanghongfan
    Date: 2020/6/26 17:52
    Description: 处理时间的标准库
 """
"""
    import time
    time.localtime() 本地时间 time.struct_time(tm_year=2020, tm_mon=6, tm_mday=26, tm_hour=17, tm_min=59, tm_sec=24, tm_wday=4, tm_yday=178, tm_isdst=0)
    time.gmtime() UTC世界统一时间
    time.ctime() 返回本地时间的字符串:Fri Jun 26 17:59:24 2020
    
    time.time() 返回自纪元以来的秒数, 记录sleep
    time.perf_counter() 随意选取一个时间点, 记录现在时间到该时间点的间隔秒数,记录sleep
    time.process_time() 随意选取一个时间点, 记录现在时间到该时间点的间隔秒数,不记录sleep
    时间格式化, %A表示周几
    local_time = time.localtime()
    print(time.strftime("%Y-%m-%d %A %H:%M:%S", local_time))
    休眠
    time.sleep()
    
    
"""
import time
print(time.localtime())
print(time.gmtime())
print(time.ctime())

print(time.time())
print(time.perf_counter())
print(time.process_time())

local_time = time.localtime()
print(time.strftime("%Y-%m-%d %A %H:%M:%S", local_time))