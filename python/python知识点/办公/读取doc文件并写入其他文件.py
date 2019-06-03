'''
读取doc文件并写入其他文件
'''
import win32com
import win32com.client
def readWordToFile(path,topath):
    mw = win32com.client.Dispatch('Word.Application')
    doc = mw.Documents.Open(path)
    #保存到文件
    doc.SaveAs(topath,2)#2表示txt文件

    mw.Quit()
topath = r'C:\Users\Administrator\Desktop\文件工作区\b.txt'
path = r'C:\Users\Administrator\Desktop\文件工作区\5108.docx'
readWordToFile(path,topath)