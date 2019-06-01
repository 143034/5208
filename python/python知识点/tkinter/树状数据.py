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
树状数据
'''
tree = ttk.Treeview(win)
tree.pack()
#添加一级树枝
treeF1 = tree.insert('',0,'中国',text='china',
                     values=('F1'))
treeF2 = tree.insert('',1,'美国',text='us',
                     values=('F2'))
treeF3 = tree.insert('',2,'英国',text='uk',
                     values=('F3'))
#添加二级树枝
treeF1_1 = tree.insert(treeF1,0,'黑龙江',text='HLJ',values=('F1_1'))
treeF1_2= tree.insert(treeF1,1,'吉林',text='JL',values=('F1_2'))
treeF1_3 = tree.insert(treeF1,2,'北京',text='BJ',values=('F1_3'))

treeF2_1 = tree.insert(treeF2,0,'1',text='HLJ',values=('F2_1'))
treeF2_2= tree.insert(treeF2,1,'2',text='JL',values=('F2_2'))
treeF2_3 = tree.insert(treeF2,2,'3',text='BJ',values=('F2_3'))
#三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,'哈尔冰',text='HRB',values=('F1_1'))

























win.mainloop()
