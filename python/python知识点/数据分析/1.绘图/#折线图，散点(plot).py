#折线图，散点(plot)
import matplotlib.pylab as pyl

import numpy as npy

x = [1,2,3,4,5]
y = [5,5,8,9,8]
#plot(x,y,展现形式)
#折线图
#pyl.plot(x,y)

#展现
#散点图
#pyl.plot(x,y,'om')
#颜色
'''
颜色：
o 散点图
c 青色
r 红色
m 品红
g 绿色
b 蓝色
y 黄色
k 黑色
w 白色
'''
#展现
#pyl.show()
'''
线条:
#plot(x,y,展现形式)
- 直线
-- 虚线
-. -.
: 细小虚线


点的样式:(散点图)
s 方形
h 六角形
H 六角形
* 星形
+ 加号
x x形
d 菱形
D 菱形
p 五角行
'''
#pyl.plot(x,y,'-.')
#pyl.show()
#pyl.plot(x,y)
#pyl.title('show')
#pyl.xlabel('ages')
#pyl.ylabel('temp')
#pyl.xlim(0,10)
#pyl.ylim(0,10)
#x2 = [5,8,6,3,2,55]
#y2 = [1,8,6,3,9,33]
#pyl.plot(x2,y2)
#pyl.show()

'''
添加标题
pyl.title('show')
pyl.xlabel('ages')
pyl.ylabel('temp')


定义坐标范围
pyl,xlim(0,20)
pyl,ylim(0,25)


同区域绘制多条线段:
pyl.show()前绘制多个

'''
'''
data = npy.random.random_integers(1,20,10)#(最小值,最大值,个数)

data2 = npy.random.normal(5.0,2.0,10)#正态分布(均数,西格玛,个数)
a = range(10)
pyl.plot(a,data2)
pyl.show()
print(a)
'''
#直方图(hist)

#data3 = npy.random.normal(10.0,1.0,10000)


#pyl.hist(data3)


#pyl.show()

#data4 = npy.random.random_integers(1,25,1000)

#pyl.hist(data4)
#pyl.show()
#data4 = npy.random.random_integers(1,25,1000)
#sty = npy.arange(2,30,4)
#pyl.hist(data4,histtype = "stepfilled")
#pyl.show()


'''
直方图参数设置:
data4 = npy.random.random_integers(1,25,1000)

pyl.hist(data4)
设计宽度:
sty = npy.arange(2,17,4)

pyl.show()

'''




















