'''
两种if语句：
if-else
if-elif-else:if 和 elif只要有真则跳过后续的语句,都为假时执行else语句.每个el都是对上面表达式的否定
死循环:
while 1:
while-else语句:
当条件语句中的表达式为假时,执行else语句
for 变量 in 集合:
enumerate([]):枚举器.第一个值为元素的下标
break:跳出循环(while和for)
continue语句:
跳出当前循环中的剩余语句，然后进行下一次循环
turtle绘图模块:
导入库:import turtle
绘图窗口的原点(0,0)在屏幕正中央,默认海龟的方向是右边
1.运动命令
    forward(d)向前移动d长度
    backward(d)向后移动d命令
    right(d)向右转移d度
    left(d)向左转动d度
    goto(x,y)移动到坐标为x,y的位置
    speed(speed)笔画绘制的速度1-10
2.笔画控制命令
    up()笔画抬起，在移动的时候不会绘图
    down()画笔落下，移动会绘图
    setheading(d)改变海龟的朝向
    pensize(d)画笔尺寸
    pencolor(colorstr)改变画笔颜色
    reset()回复所有设置,清空窗口,重置turtle状态
    clear()清空窗口,不会重置turtle
    circle(r,steps)绘制圆形，r为半径，e为次数,次数越大越接近圆
    begin_fill()
    fillcolor(colorstr)
    end_fill()
    undo()撤销上一次命令
3.其他命令:
    done():程序继续执行
    undo()撤销上一次命令
    hideturtle()隐藏海龟
    showturtle()显示海龟
    screensize()屏幕大小

'''
'''
for i, m in enumerate(range(1,6)):
    print(i, m)
for i in range(5):
    if i == 3:
        continue
    print(i)
    print('*')
    print('&')
'''
import turtle
turtle.screensize(40,40)
turtle.speed(1)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.goto(-100,200)
turtle.up()
turtle.goto(100,100)
turtle.down()
turtle.pensize(10)
turtle.pencolor('red')
turtle.goto(200,100)
turtle.setheading(45)
turtle.begin_fill()
turtle.fillcolor('blue')
turtle.undo()
turtle.circle(100,steps=5)
turtle.end_fill()
#turtle.reset()
#turtle.clear()
turtle.done()

