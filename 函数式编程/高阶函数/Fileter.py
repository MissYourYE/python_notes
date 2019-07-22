# -*- coding: utf-8 -*-


# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 例如，在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1


# [1, 3, 5]
# print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()


a = filter(not_empty, ['a', None, 'b'])
# <filter object at 0x10d8ae550>
print(a)
# ['a', 'b']
print(list(a))


# 用filter求素数
# 首先构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
