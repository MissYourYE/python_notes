# -*- coding: utf-8 -*-


# 使用切片获取List的前3个元素
# L[0:3]代表从索引为0开始取，直到索引3为止，但是不包括索引3。即索引0、1、2
L = ['zs', 'ls', 'ww', 'zl', 'tom', 'jerry']
# ['zs', 'ls', 'ww']
print(L[0:3])
# 如果第一个索引是0，还可以省略
# ['zs', 'ls', 'ww']
print(L[:3])
# ['ls', 'ww']
print(L[1:3])
# 倒数切片
# ['tom', 'jerry']
print(L[-2:])
# 记住倒数第一个元素的索引是-1。
# ['tom']
print(L[-2:-1])
# 取前5个数
# ['zs', 'ls', 'ww', 'zl', 'tom']
print(L[:5])
# 取后5个数
# ['ls', 'ww', 'zl', 'tom', 'jerry']
print(L[-5:])
# 取前2-5个数
# ['ls', 'ww', 'zl', 'tom']
print(L[1:5])
# 前4个数每2个取一个
# ['zs', 'ww']
print(L[:4:2])
# 所有数每3个取一个
# ['zs', 'zl']
print(L[::3])
# 什么都不写,复制一个List
# ['zs', 'ls', 'ww', 'zl', 'tom', 'jerry']
print(L[:])
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
# ABC
print('ABCDEFG'[:3])
