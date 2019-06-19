'''
时间:
    表示形式:
    1.时间戳:
        以整形或浮点型表示时间的一个以秒为单位的时间戳个
        基础值:从1970-1-1开始算起
    2.元组:
        这个元组有8个整形内容
        (year,month,day,hours,minutes,seconds,weekday,julia day,flag(1或-1或0))
    3.格式化字符串
        
'''
'''
import time
#返回当前时间的时间戳,浮点数形式
c = time.time()
print(c)
#将时间戳转为utc时间元组
t = time.gmtime(c)
print(t)
#将时间戳转为本地时间元组
b = time.localtime(c)
print(b)
#元组转时间戳
m = time.mktime(b)
print(m)
#将时间元组转为字符串
s = time.asctime(b)
print(s)
#将时间戳转为字符串
p = time.ctime(c)
print(p)
#将时间元组转换成给定格式的字符串,参数二为时间元组,没有参数默认转当前时间
q = time.strftime('%Y-%m-%d %H:%M:%S', b)
print(q)
#将时间字符串转为时间元组
w = time.strptime(q, '%Y-%m-%d %H:%M:%S')
print(w)
#延时
#time.sleep(4)
#返回cpu执行时间
time.clock()
sum = 0
for i in range(100000000):
    sum += i
time.clock()
print(time.clock())
'''
'''
datetime模块:
    datetime    同时有时间和日期
    datedelta   主要用于计算时间的跨度
    tzinfo      时区相关
    time        只关注时间
    date        只关注日期
'''
'''
import datetime
#当前时间
d1 = datetime.datetime.now()
print(d1)
#指定时间
d2 = datetime.datetime(1999, 10, 1, 10 ,28, 25, 123456)
print(d2)
#将时间转为字符串
d3 = d1.strftime('%Y-%m-%d %X')
print(d3)
#将格式化字符喜欢转为datetime对象
d4 = datetime.datetime.strptime(d3, '%Y-%m-%d %X')
print(d4)
#时间间隔
d5 = datetime.datetime(1999, 10, 1, 10 ,28, 25, 123456)
d6 = datetime.datetime.now()
d7 =d6 - d5
print(d7)
print(d7.days)#天数
print(d7.seconds)#间隔天数除外的秒数
'''
'''
日历模块
'''
import calendar
#返回指定末年末月的日历
print(calendar.month(2017, 7))
#返回指定年的日历
print(calendar.calendar(2017))
#判断闰年
print(calendar.isleap(2000))
#返回某个月的weekday的第一天和这个月所有的天数
print(calendar.monthrange(2017, 6))
#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2017, 6))
