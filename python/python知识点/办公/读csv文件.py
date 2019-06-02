'''
读csv文件
'''
import csv

def readCsv(path):
    infoList = []
    with open(path, 'r') as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            infoList.append(row)
            print(row)
    return infoList

path = r"C:\Users\Administrator\Desktop\文件工作区\工作簿1.csv"
info = readCsv(path)
for i in info:
    print(i)
