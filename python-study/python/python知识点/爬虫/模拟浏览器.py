import  urllib.request
import random
url = 'http://www.baidu.com'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
#随机拿一个
#agent_str = random.choice(agentList)
#req = urllib.request.Request(url)
#req.add_header('User-Agent',agent_str)
#设置一个请求体
req = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(req)
data = response.read().decode('utf-8')
print(data)


'''
agentList = [
    '',
    '',
    ''
]
'''