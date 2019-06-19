import re
'''
字符串切割:
re.split()

re.finditer(pattern,string,flags)
功能:扫描字符串,返回的是一个迭代器与findall类似


字符串的替换和修改
re.sub(pattern,repl,string,count=0,flags=0)字符串类型
re.subn(pattern,repl,string,count=0,flags=0)元组类型并返回次数
repl:指定的用来替换的字符串
count:最多替换次数
功能：在目标字符串内衣正则表达式匹配字符串，在把他们替换成指定的字符串
可以正定替换的次数，不指定是匹配所有
'''
str1 = 'sunck is a good man!sunck is a nice man!sunck is a hardsome man'
#print(re.split(r' +',str1))
#d = re.finditer(r'(sunck)',str1)
#while True:
#    try:
#        l = next(d)
#        print(d)
#    except StopIteration as e:
#       break
#print(re.sub(r'(sunck)','nice', str1,count=2))
print(re.subn(r'(sunck)','nice', str1))
