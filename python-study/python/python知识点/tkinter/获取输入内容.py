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
def showInfo():
    print(entry.get())
entry = tkinter.Entry(win)
entry.pack()
button1 = tkinter.Button(win, text='sunk', command=showInfo)
button1.pack()



win.mainloop()
