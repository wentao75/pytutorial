# 字典（dictionary）是另一个有用的数据类型
# 字典可以理解为一组 (key: value)组成的数据，并且key在字典中是唯一的。
# 使用{}可以创建一个空的字典对象；在大括号中使用逗号分割的key: value可以添加初始的数据

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
tel['jack']
del tel['sape']
tel['irv'] = 4127
tel
list(tel)
sorted(tel)
'guido' in tel
'jack' not in tel

# 可以使用dict()从key-value数据对序列中直接构建
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# dict Comprehensions也类似可用
{x: x**2 for x in (2, 4, 6)}

# 如果key是简单的字符串，也可以直接使用关键字参数的方式创建
dict(sape=4139, guido=4127, jack=4098)
