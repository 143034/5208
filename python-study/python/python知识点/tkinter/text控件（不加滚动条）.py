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
text控件:文本控件,用于显示多行文本
'''
text = tkinter.Text(win, width=30, height=8)
text.pack()
str = '''Nong hao! Good afternoon.
It is a great honor for me to be here in Shanghai,
and to have this opportunity to speak with all of you.
I'd like to thank Fudan University's President Yang for his hospitality
and his gracious welcome.
I'd also like to thank our outstanding Ambassador,
Jon Huntsman, who exemplifies the deep
ties and respect between our nati ons.
I don't know what he said, but I hope it was good. (Laughter.)'''
text.insert(tkinter.INSERT,str)






win.mainloop()
