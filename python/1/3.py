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
'''
列表:
None值和0不是同一个概念，None是一个特殊值
列表里面存储的可以是不同类型的数据
list1 + list2
列表重复:
list * num
列表截取:
list[num:num]
二维列表:
list[[],[],[]]
列表操作方法:
append(加一个元素到列表)
extend(加多个值到列表末尾)括号内必须使用列表
insert(num,元素)在下标处添加一个元素，源数据向后顺延
pop()删除元素,不传值时默认删除最后一个元素，移除列表中指定下标中的元素,返回删除数据（重要）
remove() 删除所指定的列表中的元素
clear()清除所有数据
index(num,start,end)从列表中找到某个值的下标,寻找第一个
len(列表)长度
max(列表)取最大
min(列表)取最小
count()查看元素在列表中出现的次数
'''
'''
list = [[1,2,3], [4,5,6], [7,8,9]]
print(list[1][1])
list.extend([10,11,12])
print(list)
list.append(13)
print(list)
'''
list = [1,2,3,4,5]
list.insert(2, 10)
print(list)
list.remove(10)
print(list)
list.pop(3)
print(list)
print(list.pop(2))
print(list)
#list.clear()
#print(list)
print(list.index(2))

