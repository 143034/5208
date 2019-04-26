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
a=0010,b=0111
a&b=0010,a|b=0111,a^b=0101,~b=-8
'''
