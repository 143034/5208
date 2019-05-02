'''
+ - * / **(幂运算) //(取整) =
+=, -=, *=, /=, %=, **=, //=
& (位与运算符) |(或运算符) ^(异或运算符:二进制两位想异时取1) ~(取反运算符)
<<(左移运算符) >>(右移运算符)
== != > < <= >=
and(逻辑与) or(逻辑或) not(逻辑非) in和not in(成员运算符)
is ,is not(身份运算符)
运算优先级：
**
~ *
/ % //
+ -
>> <<
&
^ |
<= ,< > >=
== !=
= %= += -= //=
is is not
in not in
not or and
短路原则:
表达式1 and 表达式2 and 表达式3 and 表达式4 and 表达式5
当第一个为假时不会执行后面的表达式
表达式1 or 表达式2 or 表达式3 or 表达式4 or 表达式5
当遇到真的表达式时不会执行后面的表达式
'''
'''
a=2
b=7
list = [1,3,5,7,9]
print(b**a)
print(b/a)
print(b//a)
print(a & b)
print(a | b)
print(a ^ b)
print(~b)
print(b<<2)
print(b>>2)
print(a>b and b>a)
print(a>b or b>a)
print(not a>b)
if b in list:
    print('*'*10)
'''
'''
a=0010,b=0111
a&b=0010,a|b=0111,a^b=0101,~b=-8
'''
'''
len(str) 计算长度
str.lover() 转换字符串大写字母为小写字母
str.upper() 转换小写字母为大写字母
str.swapcase() 大小写互换
str.capitalize() 首字母大写，其余小写
str.title() 每个单词的首字母大写
str.center(wudth, 'fillchar') 居中字符串
str.ljust(width[, fillchar]) 左对齐
str.rjust(width[, fillchar])右对齐
str.zfill(width) 前面补0
str.count(str[,start][,end]) 寻找个数start - end
str.find(str[,start][,end]) 检测是否含有目标字母 有的话显示第一个的位置没有则返回
-1
str.rfind()从右往左找
str.index(str ,start ,end)检测是否含有目标字母 有的话显示第一个的位置没有则报错
str.rindex()从右往左找，检测是否含有目标字母 有的话显示第一个的位置没有则报错
str.lstrip()截掉左侧字符串指定的字符， 默认为空格
str.rstrip()
str.strip()截掉左右开两侧的字符
ord(str)看aslla码对应的数字
chr(num)看对应的aslla码
'''

str = 'I am a boy'
print(('I AM A BOY!').lower())
print((('I AM A BOY!').lower()).upper())
print(str.swapcase())
print(str.capitalize())
print(str.title())
print(str.center(40,'*'))
print(str.ljust(40,"*"), "&")
#左对齐，用*填充，最后一位是&
print(str.rjust(40,"*"), "&")
#右对齐，用*填充，最后一位是&
print(str.zfill(40))
print(str.count('a'))
print(str.count('a',0 ,2))
print(str.find('a',0,8))
str1 = '*******   *   i am a boy haha       *******'
print(str1.lstrip())
print(str1.lstrip('*'))
print(str1.strip('*'))
