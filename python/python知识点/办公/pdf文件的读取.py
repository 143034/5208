'''
pdf文件的读取
'''
import codecs
import sys
import importlib
importlib.reload(sys)
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
def readPDF(path, topath):
    f = open(path,'rb')
    #创建一个PDF文档分析器
    parser = PDFParser(f)
    pdfFile = PDFDocument()
    #链接
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    #提供初始化密码
    pdfFile.initialize('')
    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据
        manager = PDFResourceManager()
        #创建一个pdf对象
        laparams = LAParams()
        device = PDFPageAggregator(manager,laparams=laparams)
        interpreter = PDFPageInterpreter(manager, device)
        #每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(toPath,'a',encoding='utf8') as f:
                        str = x.get_text()
                        print(str)
                        f.write(str + '\n')





path = r'C:\Users\Administrator\Desktop\文件工作区\关于学生安全节约用电的通知.pdf'
toPath = r'C:\Users\Administrator\Desktop\文件工作区\a.txt'
readPDF(path,toPath)
