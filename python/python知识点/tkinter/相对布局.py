import tkinter
from tkinter import ttk
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('sunk')
#设置窗口大小和位置
win.geometry('600x400+200+20')
#进入消息循环


'''
相对布局(窗体改变对控件有影响)
'''
label1 = tkinter.Label(win,text='good',bg='blue')
label2 = tkinter.Label(win,text='nice',bg='red')
label3 = tkinter.Label(win,text='cool',bg='pink')
#绝对布局
label1.pack(fill=tkinter.Y,side=tkinter.LEFT)
label2.pack(fill=tkinter.X,side=tkinter.TOP)
label3.pack()














win.mainloop()
