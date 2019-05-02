'''
元组:(一旦初始化不能被修改)
创建空元组
    tuple = ()
元组中的内容可以是多类型的
    tuple1 = (1,2,3,'good',True)
定义只有一个元素的元组:
    tuple2 = (1,)*加逗号
访问取值:
    元组名[下标]
修改元组:
    tuple2 = (1,2,3,4,[10,20,30])
    可修改元组中的列表值
删除元组:
    del 元组
元组的操作:
    列表相加 元组1+元组2
    元组重复 元组 * num
判断元素是否在列表里:
    print(元素 in 元组)
    在的话返回true 不在返回 false
元组的截取:同列表
    元组名[开始:结束]
二维元组:
    tuple = ((),(),())
元组方法:
    len(),max(),min()
列表转元祖:
    tuple(list)
遍历元组:
    for i in 元组:
'''
tuple1 = (1,2,3,'good',True)
print(tuple1)
tuple2 = (1,)
print(tuple2)
print(type(tuple2))
tuple2 = (1,2,3,4,[10,20,30])
tuple2[-1][0] = 100
print(tuple2)
print(tuple1[-1])
tuple = ((1,2),(3,4),(5,6))
print(tuple[1][1])
