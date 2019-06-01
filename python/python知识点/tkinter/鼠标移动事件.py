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
鼠标移动事件
<Button-1><Button-2><Button-3>
'''
def func(event):
    print(event.x,event.y)

label = tkinter.Label(win,text='good man')

label.pack()

label.bind('<B1-Motion>',func)





win.mainloop()
