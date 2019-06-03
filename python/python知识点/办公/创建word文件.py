'''
创建word文件
'''
import win32com
import win32com.client
import os
def makeWordfile(fileName,name):
    word = win32com.client.Dispatch('Word.Application')
    #可见
    word.Visible = True
    doc = word.Documents.Add()
    #写内容
    r = doc.Range(0,0)
    r.InsertAfter('亲爱的' + name +'\n')
    r.InsertAfter('         我想你!' + '\n')
    doc.SaveAs(path)
    doc.Close()
    word.Quit()
names = ['张三','李四','王五']
for name in names:
    path = os.path.join(os.getcwd(),name)
    makeWordfile(path,name)

