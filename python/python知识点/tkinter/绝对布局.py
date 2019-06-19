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
绝对布局(窗口变化对位置没有影响)
'''
label1 = tkinter.Label(win,text='good',bg='blue')
label2 = tkinter.Label(win,text='nice',bg='red')
label3 = tkinter.Label(win,text='cool',bg='pink')
#绝对布局
label1.place(x=10,y=20)
label2.place(x=50,y=40)
label3.place(x=100,y=100)














win.mainloop()
