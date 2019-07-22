# -*- coding: utf-8 -*-

# Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
# 迭代dict中的所有key
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
# a
# b
# c
for key in d:
    print(key)

# 迭代dict中的所有value
# 1
# 2
# 3
for value in d.values():
    print(value)

# 同时迭代key,value
# name: a age: 1
# name: b age: 2
# name: c age: 3
for k, v in d.items():
    print('name:', k, 'age:', v)

# python中字符串也是可以迭代的
# a
# b
# c
for ch in 'abc':
    print(ch)

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
# true
print(isinstance('abd', Iterable))
# true
print(isinstance([1, 2, 3], Iterable))
# false
print(isinstance(123, Iterable))

# 通过下标遍历
l = ['a', 'b', 'c', 'd']
# a
# b
# c
# d
for i, value in enumerate(l):
    print(l[i])
