# -*- coding: utf-8 -*-


# [1, 2, 3, 4]
print(sorted([1, 3, 2, 4]))

# sorted()函数是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# 例如按绝对值来排序
# [1, -2, -3, 4]
print(sorted([1, -3, -2, 4], key=abs))

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。


# 对字符串进行排序
# ['Credit', 'Zoo', 'about', 'bob']
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# 忽略大小写进行排序
# ['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 反向排序
# ['Zoo', 'Credit', 'bob', 'about']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
