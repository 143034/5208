import tkinter
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title('sunk')
#设置窗口大小和位置
#win.geometry('400x400+200+20')
#进入消息循环


'''
Listbox控件
MULTIPLE:支持多选
'''
lb = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)

for item in ['good','nice','handsome','vg','vn','good1','nice1','handsome1','vg1','vn1,'
             'good2','nice2','handsome2','vg2','vn2']:
    lb.insert(tkinter.END,item)

#shift实现连选,ctrl连续单选
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
#额外给属性赋值
sc['command'] = lb.yview


win.mainloop()
