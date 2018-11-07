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
