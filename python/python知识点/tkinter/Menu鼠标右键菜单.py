import tkinter
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('sunk')
#设置窗口大小和位置
win.geometry('400x400+200+20')
#进入消息循环


'''
Menu鼠标右键菜单
'''
def func():
    print('i am a good man!')
    
#菜单条
menubar = tkinter.Menu(win)


#创建一个菜单条
menu1 = tkinter.Menu(menubar, tearoff=False)
#给菜单选项添加内容
for item in ['python','c','c++','os','shell','php','java','汇编','退出']:
    menu1.add_command(label=item)
menubar.add_cascade(label='语言',menu=menu1)
def showMenu(event):
    menubar.post(event.x_root,event.y_root)
win.bind('<Button-3>',showMenu)
win.mainloop()
