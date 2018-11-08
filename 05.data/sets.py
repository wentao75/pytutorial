# 堆（Sets）是一个有不重复项组成的无序集合
# 这个数据结构的主要作用用于验证是否包含有指定的成员和消除重复条目
# 堆对象还支持如：并，交，差，对称差等操作
# 可以使用大括号或set()方法来产生堆对象，不要使用{}来产生空的堆对象
# {}会产生一个空的字典而不是堆对象

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
'orange' in basket
'crabgrass' in basket

a = set('abracadabra')
b = set('alacazam')
a
b
a - b
b - a
a | b
a & b
a ^ b

# 堆也支持队列导出式
a = {x for x in 'abracadabra' if x not in 'abc'}
a
