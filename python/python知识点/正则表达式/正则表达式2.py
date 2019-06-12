import re
'''
正则元字符
.              可以匹配除换行符以外的任意字符
'''
print(re.search('.', 'sunck is a good man 6'))
'''
[0123456789]   字符集合匹配方括号中所有所包含的任意字符
[sunck]        匹配s,u,n,c,k中任意一个字符
[a-z]          匹配任意小写字母
[A-Z]          匹配任意小写字母
[0-9]          匹配任意数字类似于[0123456789]
[0-9a-zA-Z]    匹配任意的数字和字母
[0-9a-zA-Z_]   匹配任意的数字,字母和下划线
[^sunck]       匹配除了sunck字母以外的所有字符^：脱字符，不匹配集合中的字符
[^0-9]         匹配所有的非数字字符
[\d]           匹配所有的数字效果同[0-9]
[\D]           匹配非数字字符,效果同[^0-9]
[\w]           匹配数字,字母和下划线效果同[0-9a-zA-Z_]
[\W]           匹配非数字,字母和下划线效果同[^0-9a-zA-Z_]
[\s]           匹配任意的空白符（空格，换行，回车，换页，制表）
[\S]           匹配任意非空白符效果同[^ \f\n\r\t]
'''
print(re.search('[0123456789]', 'sunck is a good man 6 sunck'))
print(re.search('[sunck]', 'sunck is a good man 6 sunck'))
print(re.findall('[\s]', 'sunck is a good man 6 sunck'))
'''
锚字符（边界字符）
^              行首匹配，和在[]里的^不是一个意思
$              行尾匹配
\A             匹配字符串开始。它和^的区别是\A只匹配整个字符串的开头即使在re.M模式下也不会匹配行首
\Z             匹配字符串结束,它它和$的区别是\Z只匹配整个字符串的开头即使在re.M模式下也不会匹配行尾
\b             匹配一个单词的边界，也就是值单词和空格间的位置
\B             匹配非单词边界
'''
#print(re.search('^sunck', 'sunck is a good man 6 sunck'))
#print(re.search('sunck$', 'sunck is a good man 6 sunck'))
#print(re.findall('\Asunck', 'sunck is a good man 6 sunck\nsunck is a nice man',re.M))
#print(re.findall('^sunck', 'sunck is a good man 6 sunck\nsunck is a nice man',re.M))
#print(re.findall('man$', 'sunck is a good man 6 sunck\nsunck is a nice man',re.M))
#print(re.findall('man\Z', 'sunck is a good man 6 sunck\nsunck is a nice man',re.M))
print(re.search(r'er\b', 'nerver'))
