'''
组合密码
'''
import itertools
mylist = list(itertools.combinations([1,2,3,4,5], 3))
print(mylist)
print(len(mylist))

