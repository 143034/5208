#post请求
import urllib.request
import urllib.parse
url = ''
data = {
    'username':'sunck',
    'passwd':'5108'
}
#打包发送的数据
postdata = urllib.parse.urlencode(data).encode('utf-8')
#请求体
req = urllib.request.Request(url, data=postdata)
#发起请求
response = urllib.request.urlopen(req)
print(response.data.decode('utf-8'))
