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
Frame:框架控件
可在屏幕上显示一个区域,多作为容器控件

'''
frm = tkinter.Frame(win)
frm.pack()
#left
frm_1 = tkinter.Frame(win#,frm_1)
tkinter.Label(frm_1, text="左上", bg='pink').pack(side=tkinter.TOP)
tkinter.Label(frm_1, text="左下", bg='blue').pack(side=tkinter.TOP)


frm_1.pack(side=tkinter.LEFT)
#right
frm_1 = tkinter.Frame(win#,frm_1)
tkinter.Label(frm_1, text="右上", bg='red').pack(side=tkinter.TOP)
tkinter.Label(frm_1, text="右下", bg='yellow').pack(side=tkinter.TOP)


frm_1.pack(side=tkinter.RIGHT)













win.mainloop()
