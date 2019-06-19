import urllib.request

urllib.request.urlretrieve('http://www.baidu.com',filename='file.html')

#清除缓存
urllib.request.urlcleanup()