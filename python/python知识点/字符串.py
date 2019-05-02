'''
split(str='',num)num代表截取的元素个数num+1从前往后截
以str为分隔符截取字符串,将截取出的内容放入一个列表中.两个分隔符之间为一个元素
    str = 'i***am**a*boy'
    print(str.split('*'))
splitlines([keepends])默认keepends为false.true时保留换行符
    \r,\\r\n,\n
    依据每行截取
列表组字符串:join(seq)以一个特定字符串，将seq中的所有元素组合成一个字符串
    ''.join(list)
max(str),min(str)比较大小
替换内容:
    str.replace('要被替换的内容','替换的内容',count)默认全部替换
创建一个字符串映射表:
    t = str2.maketrans('old','new')o-n,l-e,d-w
    str1.translate(t)
判断字符串的开始
    str.startswith(str, start,end)
判断字符串的开始
    str.endwith(str, start,end)
编码格式:
    encode(encodeing='utf-8',errors='strict')
    str.encode()
解码:
    str.decode()
str.isalpha()
    如果字符串中至少有一个字符且所有字符都是字母返回true,否则为false
str.isalnum()
    如果字符串中至少有一个字符且所有字符都是字母或数字返回true,否则为false
str.isupper()
    如果字符串中至少有一个英文字符且所有英文字符都是大写英文字母返回true,否则为false
str.islower()
    如果字符串中至少有一个英文字符且所有英文字符都是小写写英文字母返回true,否则为false
str.istitle()
    标题化:单词首字母大写
    如果字符串是标题化的返回true
str.isdigit()
    如果字符串中只包含数字返回true,否则为false
str.isnumeric()
    如果字符串中只包含数字返回true,否则为false
str.isdecimal()
    字符串只包含十进制字符返回true,否则为false
str.isspace() \t,\r,\n都为空格符
    如果字符串中值包含空格返回true,否则为false
'''
str = 'i***am**a*boy'
print(str.split('*'))
#判断字符串中的单词个数:
str = str.split('*')
c = 0
for i in str:
    if len(i) > 0:
        c += 1
        print(i)
print(c)


