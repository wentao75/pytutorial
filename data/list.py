# list 数组
# append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)
fruits.reverse()
fruits
fruits.append('grape')
fruits
fruits.sort()
fruits
fruits.sort(reverse=True)
fruits
fruits.pop()


# 堆栈 结构，后入先出 last-in，first-out
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack
stack.pop()
stack.pop()
stack


# 队列 结构，先入先出，first-in，first-out
from collections import deque
queue = deque(["Willy", "Kira", "..."])
queue.append("Tommy")
queue.append("Linda")
queue.popleft()
queue.popleft()
queue


# List Comprehensions，列表推导式
# 应用于列表形式的创建，传统代码创建一个列表：
# 第一种创建方式
squares = []
for x in range(10):
    squares.append(x**2)

squares


# 第二种创建方式
squares = list(map(lambda x: x**2, range(10)))
squares

# 第三种方式，列表推导式：
# 使用中括号[]，包含一个表达式，跟随for子句，可以有任意多个for或者if子句
squares = [x**2 for x in range(10)]
squares

# 多个for和if子句
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
combs

# 上面的表达式等同于下属循环
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

combs


# 其他的一些例子
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[x for x in vec if x >= 0]
[abs(x) for x in vec]
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
[(x, x**2) for x in range(6)]
# 下句是错误的使用方式，turple元祖需要用括号
# [x, x**2 for x in range(6)]

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]


from math import pi
[str(round(pi, i)) for i in range(1, 10)]


# 嵌套列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

[[row[i] for row in matrix] for i in range(4)]

# 可以尝试根据前面传统写法与列表推导式的对应来看看执行过程
# 这个表达式可以使用zip方法直接获得
list(zip(*matrix))
