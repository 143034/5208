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
鼠标点击事件
<Button-1><Button-2><Button-3>
'''
def func(event):
    print(event.x,event.y)
button1 = tkinter.Button(win,text='left button')
button2 = tkinter.Label(win,text='right button')
button3 = tkinter.Button(win,text='three')
button1.bind('<Button-1>', func)
button2.bind('<Double-Button-3>', func)
button3.bind('<Triple-Button-1>', func)
button1.pack()
button2.pack()
button3.pack()







win.mainloop()
