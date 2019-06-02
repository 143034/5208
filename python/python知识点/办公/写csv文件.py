'''
写csv文件
'''
import csv
def writeCsv(path, data):
    with open(path,'w',newline='') as f:
        writer = csv.writer(f)
        for rowData in data:
            print(rowData)
            writer.writerow(rowData)


path = r"C:\Users\Administrator\Desktop\文件工作区\工作簿1.csv"
writeCsv(path,[['1','22'],['2','44']])
