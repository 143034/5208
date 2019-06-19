'''
分组:除了简单的判断是否匹配之外,正则表达式还有提取字符串功能，用()表示分组
'''
import re
str = '010-53247654'
m = re.match(r'(?P<first>\d{3})-(?P<last>\d{8})',str)
#给组取名?P<>
#使用序号获取对应组的信息group(0)表示原始字符串
print(m.group(0))
print(m.group(1))
print(m.group('first'))
#查看匹配的各组的情况
print(m.groups())
'''
编译:当我们使用正则表达式时，re模块会干两件事
1.编译正则表达式，如果正则表达式不合法会报错
2.用编译后正则表达式去匹配正则表达式
re.compile(pattern, flags)
pattern:要编译的表达式
'''
pat = r'(\d{3})-(\d{8})'
re.tele = re.compile(pat)
print(re.tele.match('010-53247654'))
print(re.tele.findall('010-53247654'))
