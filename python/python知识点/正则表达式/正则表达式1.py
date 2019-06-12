import re
'''
12345564asdafedfdgdrg
'''
'''
re.match(pattern, string, flags=0)
pattern:匹配的正则表达式
string:要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
re.I
忽略大小写
re.L
做本地化识别
re.M
多行匹配影响^和&
re.S
是.匹配包括换行符在内的所有字符
re.U
根据unciode字符集解析字符,影响\w \W \b \B
re.X
使我们以更灵活理解正则表达式
功能:尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，返回None


        #扫描字符串,返回从起始位置成功的匹配#
'''
#www.baidu.com
print(re.match('www','www.baidu.com').span())
print(re.match('www','wwW.baidu.com',flags=re.I))
print(re.match('www','baidu.wwwcom'))
'''
re.search函数
re.search(pattern, string, flags=0)
功能:扫描整个字符串,并返回第一个匹配成功的
'''
print(re.search('sunck', 'i am sunck, sunck1'))
'''
re.findall()
re.findall(pattern, string, flags=0)
功能:扫描整个字符串并返回列表
'''
print(re.findall('sunck', 'i am sunck, sunck1'))
