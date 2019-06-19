import tkinter
from tkinter import ttk
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('sunk')
#设置窗口大小和位置
win.geometry('400x400+200+20')
#进入消息循环


'''
Combobox:下拉控件
'''
#绑定变量
cv = tkinter.StringVar()


com = ttk.Combobox(win, textvariable=cv)

com.pack()
#设置下拉属性
com['value'] = ('黑龙江','吉林','辽宁')
#设置默认值
com.current(0)
def func(event):
    print(com.get())
    print(cv.get())
    print('sunk is a good man!')
com.bind('<<ComboboxSelected>>', func)


















win.mainloop()
