# -*- coding: utf-8 -*-
from functools import reduce


# map()函数接收两个参数，一个是函数名，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5])
# <map object at 0x10ac66390>
print(r)

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。
# [1, 4, 9, 16, 25]
print(list(r))

# 用map函数将list中的数字转成字符串
# ['1', '2', '3', '4', '5', '6']
print(list(map(str, [1, 2, 3, 4, 5, 6])))


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y


# 15
print(reduce(add, [1, 2, 3, 4, 5]))


# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y


# 13579
# print(reduce(fn, [1, 3, 5, 7, 9]))

# 把str转换为int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]

# 13579
# print(reduce(fn, map(char2num, '13579')))
