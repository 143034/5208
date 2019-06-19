import tkinter
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('sunk')
#设置窗口大小和位置
win.geometry('400x400+200+20')
#进入消息循环


'''
Radiobutton:单选框控件
'''
#绑定变量一样
def update():
    print(r.get())




r = tkinter.IntVar()
#r = tkinter.StringVar()




radio1 = tkinter.Radiobutton(win,text='one',value=1,variable=r,command=update)
radio1.pack()
radio2 = tkinter.Radiobutton(win,text='two',value=2,variable=r,command=update)
radio2.pack()











win.mainloop()
