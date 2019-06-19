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
进入与离开事件
<Enter>光标进入控件时触发
<Leave>光标离开控件时触发
<Button-1><Button-2><Button-3>
'''
def func(event):
    print(event.x,event.y)

label = tkinter.Label(win,text='good man',bg='red')

label.pack()
label1 = tkinter.Label(win,text='5108',bg='red')

label.pack()
label1.pack()

label.bind('<Enter>',func)
label1.bind('<Leave>',func)





win.mainloop()
