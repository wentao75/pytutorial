# Tuples是标准序列型数据类型之一
# 元组包含许多用逗号分割的值
t = 12345, 54321, 'hello!'
t[0]
t
u = t, (1, 2, 3, 4, 5)
u

# 元组不支持赋值，它是不可变量
t[0] = 88888

# 元组能够包含可变对象
v = ([1, 2, 3], [3, 2, 1])
v

# 构造包含有0个或者1个项的元组时需要一些特殊的语法方式
empty = ()
singleton = 'hello',
len(empty)
len(singleton)
singleton


# 下面的表达式是元组包装（tuple packing），几个数值项包装为一个元组对象中
t = 12345, 54321, 'hello!'
# 那么将上面表达式反过来也是可以的，这被称作序列拆包（sequence unpacking）
# 拆包的等式左边需要有和右边数据结构中相同数量的变量
x, y, z = t
x
y
z
