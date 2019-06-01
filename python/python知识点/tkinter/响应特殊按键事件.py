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
响应特殊按键事件
<Button-1><Button-2><Button-3>
<Shift_L>',<Shift_R>','<F5>','<Return>','<BackSpace>'
'''
def func(event):
    print('event.char=',event.char)
    print('event.keycode=',event.keycode)

label = tkinter.Label(win,text='good man',bg='red')
#设置焦点
label.focus_set()
label.pack()

label.bind('<Shift_L>',func)






win.mainloop()
