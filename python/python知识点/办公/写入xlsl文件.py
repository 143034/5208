'''
写入xlsl文件
'''
from collections import OrderedDict
from pyexcel_xls import save_data
def makeExcelFile(path, data):
    dic = OrderedDict()
    for sheetName, sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)
    save_data(path, dic)
path = r'C:\Users\Administrator\Desktop\文件工作区\workspace4\b.xls'
makeExcelFile(path,{'表1':[[1,2,3],[4,5,6],[7,8,9]],
            '表2':[[11,22,33],[44,55,66],[77,88,99]]})