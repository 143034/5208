import tkinter
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('sunk')
#设置窗口大小和位置
win.geometry('400x400+200+20')
#进入消息循环


'''
Label:标签控件

'''
#win:父窗体,text:文本内容,bg:背景色,fg:字体颜色,font:字体,width:宽度,heigh:高度wraplength:指定txt文本多宽后换行
label = tkinter.Label(win,
                      text='sunk is a good man',
                      bg='pink',
                      fg='red',
                      font=('黑体',20),
                      width=20,
                      heigh=4,
                      #wraplength=100,
                      justify='left',#设置换行的对齐方式
                      anchor='center'#位置n,s,e,w,center,ne,se,sw,nw
                      )
#挂载到视图
label.pack()







win.mainloop()
