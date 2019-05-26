import tkinter
def func():
    print('sunk is a good man!')
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('sunk')
#设置窗口大小和位置
win.geometry('400x400+200+20')
#进入消息循环



'''
unittest控件:输入控件,用于显示简单文本内容
'''
#绑定变量
e = tkinter.Variable()
#show='*'密纹显示
#entry = tkinter.Entry(win,show='*',textvariable=e)
entry = tkinter.Entry(win,textvariable=e)
entry.pack()
#e就代表输入框这个对象
#设置值
e.set('sunk is a good man')
#取值
print(e.get())
print(entry.get())

win.mainloop()
