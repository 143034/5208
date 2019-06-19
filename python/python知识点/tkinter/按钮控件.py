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

'''
button控件
'''
#创建按钮command=函数名注意(不要括号)
button1 = tkinter.Button(win, text='sunk',command=func,
                        width=5,heigh=2)
#显示
button1.pack()
button2 = tkinter.Button(win, text='5108',command=lambda:print('5108'),
                        )
button2.pack()
button3 = tkinter.Button(win, text='quit',command=win.quit)
button3.pack()







win.mainloop()
