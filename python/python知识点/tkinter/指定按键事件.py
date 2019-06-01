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
指定按键事件
'''
def func(event):
    print('event.char=',event.char)
    print('event.keycode=',event.keycode)

win.bind('a',func)






win.mainloop()
