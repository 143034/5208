'''
堆栈:
    存储数据特点:先进后出，后进先出
队列:
     存储数据特点:先进先出
    
'''
'''
#模拟栈结构
stack = []
#压栈(向堆栈存东西)
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
#出栈（从栈里取数据）
res = stack.pop()
print(res)
print(stack)
'''
'''
import collections
#创建队列
queue = collections.deque()
print(queue)
#进队
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)
#出队
res = queue.popleft()
print(res)
print(queue)
'''

