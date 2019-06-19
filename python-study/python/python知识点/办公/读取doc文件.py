'''
读取doc文件
'''
import win32com
import win32com.client
def readWordFile(path):
    mw = win32com.client.Dispatch('Word.Application')
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    doc.Close()
    mw.Quit()

path = r'C:\Users\Administrator\Desktop\文件工作区\5108.docx'
readWordFile(path)