'''
写ppt
'''
import win32com
import win32com.client

def makePPT(path):
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    ppt.Visible = True
    pptFile = ppt.Presentations.Add()
    #创建页
    page1 = pptFile.Slides.Add(1,1)
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "sunck1"
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "sunck2"
    #括号第一个为页数,参数二为类型
    page2 = pptFile.Slides.Add(2, 1)
    t3 = page2.Shapes[0].TextFrame.TextRange
    t3.Text = "5108"
    t4 = page2.Shapes[1].TextFrame.TextRange
    t4.Text = "5208"
    page3 = pptFile.Slides.Add(3, 2)
    t5 = page3.Shapes[0].TextFrame.TextRange
    t5.Text = "51081"
    t6 = page3.Shapes[1].TextFrame.TextRange
    t6.Text = "52081"
    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()
path = r'C:\Users\Administrator\Desktop\文件工作区\workspace4\5108.ppt'
makePPT(path)
