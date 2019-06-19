'''
排列与组合
'''
import itertools
mylist = list(itertools.product('012345',repeat=4))
print(mylist)
print(len(mylist))

