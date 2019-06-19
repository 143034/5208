'''
urllib爬取网页
'''
import urllib.request
#向指定url发起请求,并返回服务器响应的数据
response = urllib.request.urlopen('http://www.baidu.com')
#读取文件的全部内容,会把读取到的数据给字符串变量
#data = response.read()
#读取一行
#data = response.readline()
#读取文件的全部内容,会把读取到的数据赋值给列表变量
data = response.readlines()
print(len(data))
print(data)
print(len(data))
#with open(r'./1.txt','wb') as f:
#    f.write(data)
'''
response属性
response.info()返回当前环境的有关信息
response.getcode()返回状态码
'''
