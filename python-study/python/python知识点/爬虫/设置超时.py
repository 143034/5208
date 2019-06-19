import urllib.request

#如果网页长时间未响应系统判断超时无法爬取timeout
for i in range(1,10):
    try:
        response = urllib.request.urlopen('http://www.baidu.com',timeout=0.5)
        print(len(response.read().decode('utf-8')))
    except:
        print('请求超时,继续下一个爬取')