import tkinter
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('sunk')
#设置窗口大小和位置
win.geometry('400x400+200+20')
#进入消息循环


'''
Spinbox:数值范围控件
increment:步长,默认为1
values 最好不要与from,to同时使用values=(0,2,4,6,8)
'''
#绑定变量
def update():#值改变执行相应的方法
    print(v.get())
v = tkinter.StringVar()
sp = tkinter.Spinbox(win,from_=0,to=100,increment=1,textvariable=v
                     ,command=update)
sp.pack()
#赋值
v.set(20)
print(v.get())






win.mainloop()
