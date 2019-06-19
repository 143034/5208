'''
set:(set是没有索引的)
    类似dict,是一组key的集合,不存储value
    本质:无序和无重复元素的集合,有重复自动过滤
    创建:
        s1 = set([1,2,3,4,5,5])
        s2 = set((1,2,3,3,2,1))
        s3 = set({1:'good',2:'ok'})
    添加:可以添加重复的,但是没有效果.
        1.add
            set的元素不能是列表和字典.
            元组不可变所以可以作为set的元素
            s4 = set([1,2,3,4,5])
            s4.add(num)
        2.update
            插入整个list,tuple,字符串,打碎插入
            s5 = set([1,2,3,4,5])
            s5.update([6,7,8])
            s5.update((6,7,8))
    删除:
        remove
            s6 = set([1,2,3,4,5])
            s6.remove(5)
    遍历:
        for i n set():
    交集:&
        s8 = set([1,2,3])
        s9 = set([2,3,4])
        a1 = s8 & s9
    并集:|同上
    set转list和元组:
        s3 = {1,2,3,4}
        l3 = list(s3)
        l4 = tuple(s3)
'''
s1 = set([1,2,3,4,5,5])
print(s1)
s5 = set([1,2,3,4,5])
s5.update([6,7,8])
print(s5)
