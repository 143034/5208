'''
urllib爬取网页
'''
import urllib.request
#向指定url发起请求,并返回服务器响应的数据
response = urllib.request.urlopen('http://www.baidu.com')
#读取文件的全部内容,会把读取到的数据给字符串变量
data = response.read()
#读取一行
#data = response.readline()
#读取文件的全部内容,会把读取到的数据赋值给列表变量
#data = response.readlines()
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
'''
https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%87%AF%E5%93%A5%E5%AD%A6%E5%A0%82&rsv_pq=f2f0e47b00059109&rsv_t=94fesY1WlwVql%2F6EBLnFC7bjMLfDFekGDVcEKs3cZxb2jb7n1eM6zgrQw80&rqlang=cn&rsv_enter=1&rsv_sug3=15&rsv_sug1=13&rsv_sug7=101
'''
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%87%AF%E5%93%A5%E5%AD%A6%E5%A0%82&rsv_pq=f2f0e47b00059109&rsv_t=94fesY1WlwVql%2F6EBLnFC7bjMLfDFekGDVcEKs3cZxb2jb7n1eM6zgrQw80&rqlang=cn&rsv_enter=1&rsv_sug3=15&rsv_sug1=13&rsv_sug7=101'
#解码
new_url = urllib.request.unquote(url)
print(new_url)
#编码
new_url2 = urllib.request.quote(url)
print(new_url2)