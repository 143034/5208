'''
匹配多个字符
(xyz)      匹配小括号里的xyz（作为一个整体去匹配）
x?         匹配0个或者一个x
x*         匹配0个或者任意多个x(.*表示匹配0个或者任意多个字符(换行符除外))
x+         匹配至少一个x
x{n}       匹配确定的n个x(n是一个非负整数)
x{n,}      匹配至少n个x
x{n,m}     匹配至少n个最多m个x（注意n<=m）
x|y        匹配x或y

特殊
*?     +?       x?     最小匹配,通常都是尽可能多的匹配
'''
import re
#print(re.findall(r'(sunck)','sunck is a good man sunckman'))
#print(re.findall(r'o?','sunck is a good man sunckman'))
#print(re.findall(r'a?','aaaaba'))#非贪婪匹配
#print(re.findall(r'a*','aabaaa'))#贪婪匹配
#print(re.findall(r'.*','aaabaa'))
#print(re.findall(r'a+','aaabaa'))
#print(re.findall(r'a{3}','aaaabaaa'))
#print(re.findall(r'a{3,}','aaaabaaaaaaaa'))
#print(re.findall(r'a{3,6}','aaaabaaaaaaaa'))
print(re.findall(r'((s|S)unck)','sunck-Sunck'))
print(re.findall(r'sunck.*?man$','sunck is a good man!sunck is a nice man!sunck is a very good man'))
