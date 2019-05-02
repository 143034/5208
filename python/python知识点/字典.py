'''
字典:{key:''}
    使用键-值存储,极快的查找速度
key的特点:{'lilei':60}
    1.字典中key唯一
    2.key是不可变对象
    3.字符串.整数是不可变的,可以作为key
    4.list是可变的,不能做key
    5.字典的存储是无序的
    
元素的访问:
    获取: 字典名[key]
        dict = {'tom':70,'lilei':80}
        print(dict['tom'])
    添加和修改:
        字典名[key] = ''如果对应的键值存在,则修改相应的键值
    删除:
        dict.pop()
    遍历字典:
        dict.values():遍历值
        dict.items()
        for key in dict//dict.values():
            print(k, dict[key])
            dict.values():遍历值
    编号:
        enumerate(dict)
        for k,i in enumerate(dict):
    print(k,i)
    
'''
dict = {'tom':70,'lilei':80}
print(dict['tom'])
dict['hanmeimei'] = 90
print(dict)
for i in dict:
    print(i, dict[i])
for k,i in dict.items():
    print(k,i)
for k,i in enumerate(dict):
    print(k,i)
