'''
字符串 h,n为数字
str1 + str2
str * h
str[h]
str[h:n]
str[:n]从头开始截取str[h:]从h-1到尾末
格式化输出(占位符):
print('%d',%变量)
%d %s %f(浮点数)%.3f三位小数
转意符:\
\n, \, \t(加四个空格)r(之后不用转意)
eval:
eval(str):
将str当成有效计算并返回计算结果
'''

str1 = 'hello'
str2 = ' world'
a = 10
print(str1 + str2)
print(str1 * 5)
print(str1[2])
print(str1[1:3])
print('l'in str1)
print("%d" %a)
print('%s\n%s' %(str1,str2))
print('i am \'a\' good\tman')
print(r"\[;")
print(r"https://www.bilibili.com/video/av19956343/?p=20")
print(eval('123+456'))
'''
闰年判断
闰年:能被四整除但不能被100整除 或能被400整除
'''
'''
date = int(input('请输入年份'))
if (date//4==0 and date//100!=0) or (date//400==0):
    print('yes', date)
else:
    print('no', date)
'''
'''
#00000101
#11111010
#10000110(-6)
print(~5)
'''

