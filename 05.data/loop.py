# 需要对字典数据结构的数据进行循环，可以同时读取key和value
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 当在一个序列中循环时，位置序号和相应的值也可以同时通过enumerate()获取
for i, v in enumerate(['tie', 'tac', 'toe']):
    print(i, ':', v)
# 当同时循环两个或者多个序列，可以使用zip方法将入口打包
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

# 需要在一个序列中反向循环时，首先确定正向序列，然后使用reversed()方法即可
for i in reversed(range(1, 10, 2)):
    print(i)

# 如果需要按照一个排序循环，使用sorted()方法返回的排序队列，原始队列仍然保持未变化的顺序
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# 有时如果需要尝试在一个变化的队列上进行循环处理，比较简单和安全的方式是产生一个新的队列替换
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data
